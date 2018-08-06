#encoding=utf-8
import re
import requests

request_data = {
    'iid': '37343461246',
    'device_id': '34883460132',
    'os_api': '18',
    'app_name': 'aweme',
    'channel': 'App Store',
    'idfa': 'E52A57DE-3C38-438D-8BFC-9ABD53FAAB86',
    'device_platform': 'iphone',
    'build_number': '19007',
    'vid':'5C9DA5A7-2838-4C78-A370-589081FCFA45',
    'openudid': 'ee596af8c6e9bf15902b3cd6e3d8d1feeb9a7a66',
    'device_type': 'iPhone9,1',
    'app_version': '1.9.0',
    'version_code': '1.9.0',
    'os_version': '11.4',
    'screen_width': '750',
    'aid': '1128',
    'ac': 'WIFI',
    'count': '6',
    'user_id': '67640189377',
    'ts': '1531211578'
}
def http_request(url):
    result = requests.get(url, params = request_data)
    print result.json()

http_request('https://api.amemv.com/aweme/v1/feed/')