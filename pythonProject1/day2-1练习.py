'''题目一：字符串反转

编写一个函数 reverse_string(s)，接收一个字符串 s，返回该字符串的反转形式。

示例：

```
输入: "hello"
输出: "olleh"

输入: "Python"
输出: "nohtyP"
```
'''
import string
def reverse_string(s):
   return s[::-1]


string1 = 'Hello'

print(reverse_string(string1))

'''题目二：统计字符出现次数

编写一个函数 count_char(s, ch)，统计字符串 s 中指定字符 ch 出现的次数（区分大小写）。如果 ch 不在字符串中，返回 0。

示例：

```
输入: s = "hello world", ch = "o"
输出: 2

输入: s = "Python", ch = "p"
输出: 0  (因为大小写不匹配)
```
'''
def count_char(s,ch):
   x=0;
   for i in range(len(s)):
      if(s[i]==ch):
         x+=1
   return x
str="hjskdhkv sjakjlka"
ch = 'K'
print(count_char(str,ch))

'''
题目三：判断回文字符串

回文字符串是指正读和反读都一样的字符串，例如 "radar" 或 "level"。编写一个函数 is_palindrome(s)，判断输入的字符串是否为回文。忽略空格和标点符号，并且不区分大小写（只考虑字母和数字，忽略其他字符）。如果字符串是回文返回 True，否则返回 False。

示例：

```
输入: "A man, a plan, a canal: Panama"
输出: True

输入: "race a car"
输出: False'''
def is_palindromes(s):
   new_s = ""
   for c in s:
      if c.isalnum():
         new_s = new_s + c
   str = new_s[::-1]
   for i in range(len(new_s)):
      if(new_s[i] != str[i]):
         return False
   return True
string_1 =  "A man, a plan, a canal: Panam"
str = string_1.lower()
print(is_palindromes(str))