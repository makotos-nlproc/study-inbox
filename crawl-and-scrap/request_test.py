import requests
import sys
import pprint

if len(sys.argv) > 1 and 'http' in sys.argv[1]:
    response_obj  = requests.get(sys.argv[1])
    content_type = response_obj.headers.get('content-type')

    if 'text/html' in content_type:
        log_list = [type(response_obj),
                    content_type,
                    response_obj.status_code,
                    response_obj.encoding,
                    response_obj.text[:6]]
        pprint.pprint(log_list)
    elif 'json' in content_type:
        print(response_obj.json())
    else:
        print('no expecting content type')
else:
    print('no url')
