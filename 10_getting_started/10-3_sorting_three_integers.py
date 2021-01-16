# -*- coding: UTF-8 -*-

# 入力
a = int(input())
b = int(input())
c = int(input())
# 整列
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
# 出力
print(a, b, c)