from random import randint
import requests as rq

def check_connection():
    try:
        r = rq.get(f'http://ip-api.com/')
        status_code = r.status_code
        print(status_code)
        return status_code
    except Exception as e:
        print(f'error: {e}')


def get_info(ip, cfg=None, log=False):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting,query"
    try:
        r = rq.get(url)
        r.raise_for_status()
        data = r.json()
        if data.get("status") == "fail":
            raise Exception(f'failed to get info of {ip}')


        query_info = {
            "query" : "ip",
            "status": "status",
            "country": "country",
            "countryCode": "country_code",
            "region": "region",
            "regionName": "region_name",
            "city": "city",
            "zip": "zip",
            "lat": "latitude",
            "lon": "longitude",
            "timezone": "timezone",
            "isp": "isp",
            "org": "org",
            "as": "as",
            "mobile": "mobile",
            "proxy": "proxy",
            "hosting": "hosting"
            }

        ip_info = {}
        for api_field, display_name in query_info.items():
            if data[api_field]:
                value = data[api_field]
            else:
                value = 'None'
            ip_info[display_name] = value

        return ip_info

    except rq.exceptions.JSONDecodeError as e:
        print(f'error during json decoding: {e}')
    except rq.exceptions.RequestException as e:
        print(f'error getting data: {e}')
    except Exception as e:
        print(f'unexpected error: {e}')



if __name__ == '__main__':
    random_ip = '.'.join(str(randint(1,255)) for i in range(4))
    check_connection()
    ip_info = get_info(random_ip)
    print(ip_info)