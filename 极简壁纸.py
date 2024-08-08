import json

import requests
import execjs

class JiJian():
    def __init__(self):
        self.headers = {
            "referer": "https://bz.zzzmh.cn/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        self.url = "https://api.zzzmh.cn/bz/v3/getData"
        self.js = execjs.compile(open('极简壁纸.js', encoding='utf-8').read())
    def get_data(self):
        data = {"size":24,"current":11,"sort":0,"category":0,"resolution":0,"color":0,"categoryId":0,"ratio":0}
        response = requests.post(self.url,headers = self.headers,json=data)
        return response.json()
    def pares_data(self,response):
        res = self.js.call(' _0x1e5a5f',response['result'])
        ai = json.loads(res)
        # print(res)
        for i in ai['list']:
            res = requests.get('https://api.zzzmh.cn/bz/v3/getUrl/' + i['i']+ '29', headers=self.headers, allow_redirects=False)
            self.save_data(res.headers['location'],i['i'])

    def save_data(self, img_url, name):
        with open('壁纸/' + name + '.jpg', 'wb')as f:
            result = requests.get(img_url, headers=self.headers)
            f.write(result.content)
            print('正在下载{}'.format(name))
    def main(self):
        res = self.get_data()
        self.pares_data(res)

if __name__ == '__main__':
    jj = JiJian()
    jj.main()