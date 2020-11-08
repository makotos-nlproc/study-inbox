import sys
import requests

url = sys.argv[1]
req_obj = requests.get(url)
print(f'encoding: {req_obj.encoding}',file=sys.stderr)
print(req_obj.text)