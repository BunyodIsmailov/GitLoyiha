






# pip install requests
# pip install requests-toolbelt
import time
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


time.sleep(5)
try:
	multipart_data = MultipartEncoder(fields={"scanerStatus": "true","file": ("filename.jpg",open("D:/printchi/printchiapp/kalit_suzlar.jpg", 'rb'),"image/jpeg")})
	r = requests.put(url="https://api.printchi.uz/scaner/set/3/",headers={"Content-Type": multipart_data.content_type,},data=multipart_data,)
	print(r.status_code)
	time.sleep(5)
except:
	print("Error on PUT Scanner data!")





