import sys
from sys import exit
import re

# 1 point = 1/72 inch
# 1 inch = 25.4 mm
def pointToMillimetre(val):
    res = float(val) / 72 * 25.4
    return str(res)

# ファイル名取得（引数が間違っていたらエラー）
def getFilename(argsArray):
    argslen = len(argsArray)
    if argslen == 2:
        return argsArray[1]
    else:
        print('Command <Filename>')
        exit()

# 引数のファイル名取得
readFilename = getFilename(sys.argv)
serchString = b'%%HiResBoundingBox: '

f = open(readFilename, 'rb')

datalist = f.read()

# serchString と　次の'%%' の位置を取得 
start = datalist.find(serchString)
end = datalist.find(b'%%',datalist.find(serchString)+len(serchString))
if start<0:
    print('Failed to determine the size.')
    exit()

# スタート位置に移動
f.seek(start)
# エンドまで切り抜き（テキストに変換）
data = f.read(end-start).decode()
# 改行削除
data = data.rstrip()

print(data)
dataArray = data.split(' ')

print("天地：" + pointToMillimetre(dataArray[4]))
print("左右：" + pointToMillimetre(dataArray[3]))

f.close()

# Masatoshi MORITA 2021.08.29
# 新聞EPSのサイズを表示するプログラム