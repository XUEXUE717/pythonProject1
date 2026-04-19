"""数据统计与分析

"""
def analyze_scores(**kwargs):
    """接收学生姓名和分数，并返回一个包含最高分，最低分，平均分"""
    max_scores = max(kwargs)
    min_scores = min(kwargs)
