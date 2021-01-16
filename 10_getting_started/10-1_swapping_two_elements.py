# -*- coding: UTF-8 -*-

# 入力
a = int(input())
b = int(input())
# Swap1
tmp = a
a = b
b = tmp
# 出力1
print('a:', str(a))
print('b:', str(b))
# Swap2
a, b = b, a
# 出力2
print('a:', str(a))
print('b:', str(b))

'''------------------------------------
Pythonでの関数実装はできない。
この場合は数値(ミュータブル)の参照渡しになる。
返値でswapしたものを返すことが最も近い。
------------------------------------'''