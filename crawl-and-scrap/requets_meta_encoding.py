import sys
import re
import requests


url = sys.argv[1]
req_obj = requests.get(url)

scanned_text = req_obj.content[:1024].decode('ascii', erros='replace')

match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

if match:
    req_obj.encoding = match.group(1)
else:
    req_obj.encoding = 'utf-8'

print(f'encoding: {req_obj.encoding}', file=sys.stderr)
print(req_obj.text)