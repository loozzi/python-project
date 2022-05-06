import requests
from threading import Thread

class JoinGroup(Thread):
    def __init__(self, cookie, id_group):
        super(JoinGroup, self).__init__()
        self.cookie = cookie
        self.id_group = id_group

        self.headers = {
            'authority': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie':self.cookie
        }

    def run(self):
        self.join_group()

    def get_fbdtsg(self):
        res = requests.get("https://mbasic.facebook.com/profile.php", headers=self.headers)
        res.encoding = res.apparent_encoding
        try:
            dtsg = res.text.split('"fb_dtsg" value="')[1].split('"')[0]
        except:
            dtsg = ""

        return dtsg

    def join_group(self):
        url_join = "https://mbasic.facebook.com/a/group/join/?group_id={0}&gfid=AQD0pkx0BCFeKaoOBS0&refid=18".format(self.id_group)
        data_post = {
            "fb_dtsg": self.get_fbdtsg(),
            "jazoest": "21908"
        }
        requests.post(url_join, headers=self.headers, data=data_post)
        return "+1"


JoinGroup(
    "fr=0ROwoFOqR4dPQXLbN.AWWTxS8ujV6CrFeIFyFUhEMAzJQ.BidHIC.H8.AAA.0.0.BidHI8.AWXlh2aA748; sb=aWN0Yob2_iWIFh2O-qjU6Y3w; wd=960x326; datr=aWN0Yr5idv49bVtxw2j419nO; locale=vi_VN; c_user=100080805979509; xs=23%3AojExVQyDiwS69g%3A2%3A1651798585%3A-1%3A-1",
    "595654371402075"
).start()
# group id: 595654371402075
