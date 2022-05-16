






# pip install requests
# pip install requests-toolbelt

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

try:
	multipart_data = MultipartEncoder(
	    fields={
	        "scanerStatus": "true",
	        "file": (
	            "filename.jpg",
	            open("D:/printchi/printchiapp/kalit_suzlar.jpg", 'rb'),
	            "image/jpeg"
	        )
	    }
	)

	requests.put(
	    url="https://api.printchi.uz/scaner/set/3/",
	    headers={
	        "Content-Type": multipart_data.content_type,
	    },
	    data=multipart_data,
	)
except:
	print("Error on PUT Scanner data!")





