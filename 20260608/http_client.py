import time
import json
import logging
import requests
from functools import wraps

# ==========================================
# 1. 统一日志配置（告别 print，拥抱专业日志）
# ==========================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ==========================================
# 2. 重试装饰器（网络波动自动重试）
# ==========================================
def retry(max_retries=2, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    logger.warning(f"⚠️ 第 {attempt + 1} 次请求失败: {e}")
                    if attempt < max_retries:
                        time.sleep(delay)
                    else:
                        raise

        return wrapper

    return decorator


# ==========================================
# 3. 核心：企业级 API 客户端封装
# ==========================================
class ApiClient:
    """
    企业级 HTTP 请求工具类
    功能：Session保持、统一日志、自动重试、异常处理
    """

    def __init__(self, base_url, timeout=10):
        """
        初始化客户端
        :param base_url: 接口的基础域名（如 https://restapi.amap.com）
        :param timeout: 全局超时时间（秒）
        """
        self.base_url = base_url
        self.timeout = timeout
        # 核心：使用 Session 自动保持 Cookie/Token 状态
        self.session = requests.Session()
        # 设置默认的请求头
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "AutoTest-Client/1.0"
        })

    @retry(max_retries=2, delay=2)
    def _request(self, method, endpoint, **kwargs):
        """
        底层统一请求方法（包含日志、异常处理、重试）
        """
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)

        # 记录请求日志
        logger.info(f"🚀 发起请求: [{method}] {url}")
        if 'params' in kwargs:
            logger.info(f"📋 查询参数: {kwargs['params']}")
        if 'json' in kwargs:
            logger.info(f"📦 请求体: {json.dumps(kwargs['json'], ensure_ascii=False)}")

        try:
            # 发送请求
            response = self.session.request(method, url, **kwargs)

            # 记录响应日志
            logger.info(f"📥 收到响应: 状态码={response.status_code} | 耗时={response.elapsed.total_seconds():.2f}s")

            # 如果状态码不是 2xx，主动抛出异常触发重试
            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            logger.error(f"❌ 请求超时: {url}")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"❌ 连接失败: {url}")
            raise
        except requests.exceptions.HTTPError as e:
            logger.error(f"❌ HTTP错误: {e}")
            raise
        except Exception as e:
            logger.error(f"❌ 未知异常: {e}")
            raise

    # ==========================================
    # 4. 封装常用 HTTP 方法（让调用更优雅）
    # ==========================================
    def get(self, endpoint, **kwargs):
        """发送 GET 请求"""
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """发送 POST 请求"""
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """发送 PUT 请求"""
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        """发送 DELETE 请求"""
        return self._request("DELETE", endpoint, **kwargs)

    def update_token(self, token):
        """
        更新全局 Token（用于接口关联）
        """
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        logger.info(f"🔑 Token 已更新: {token[:10]}...")