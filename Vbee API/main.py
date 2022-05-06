import requests

proxy = {
	"http":'http://45.119.83.40:3128',
	"https":'https://45.119.83.40:3128'
}

api = "https://v3.vbee.vn/api/v1/convert-tts"

text = "xin chao moi nguoi nhaaaaa"

params = {
	'input_text':text,
	'voice':'hn_female_ngochuyen_fast_news_48k-thg',
	'bit_rate':'128000'
	}
for i in range(30):
	c = requests.get(api, params=params, proxies=proxy)

	try:
		print(c.json()['link'])
	except:
		print("error")
