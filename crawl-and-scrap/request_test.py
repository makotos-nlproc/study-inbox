import requests
import sys


if len(sys.argv) > 1:
    # この長さが引数の個数か、単に文字列の長さか確認する
    response_obj  = requests.get(sys.argv)
    
else:
    print('no url')
