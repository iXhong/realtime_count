import os
import requests
from dotenv import load_dotenv

load_dotenv()

# I stored the token in the .env
cookie = {
    'mars_token': os.getenv("MARS_TOKEN")
}

headers = {
    'referer': 'https://online.njtech.edu.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


# return the realtime online number
def online_num():

    url = "https://online.njtech.edu.cn/api/v1/user/profile/count"

    r = requests.get(url=url, cookies=cookie, headers=headers)

    if r.status_code == 200:
        data = r.json()
        user_count = data['data']['onlineCount']

        return user_count

    else:
        print("Failed to get")
        return None

