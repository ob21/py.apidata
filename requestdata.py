import requests
import json
from datetime import datetime

#### Send request fonction
def sendRequest(method, url, parameters={}):
	status = False
	result = json.dumps({})
	# Set auth object
	auth={}
	# Set proxies
	proxies = {
	  "http": "http://p-goodway.rd.francetelecom.fr:3128",
	  "https": "https://p-goodway.rd.francetelecom.fr:3128",
	}
	# Create a session
	session = requests.Session()
	# Get the current hour to build the token
	hour = datetime.now().strftime("%H")
	token = "go"+hour
	# Get params
	parameters["token"] = "go"+hour
	auth["token"] = "go"+hour
	# Print the request url
	print(url)
	# Print the request parameters
	print(str(parameters))
	# Try to perform the request
	try:
	    print("On essaie sans proxy")
	    if(method=="GET"):
	     res = session.get(url, params=parameters)
	    else:
	     res = session.post(url, data=parameters, params=auth)
	except requests.exceptions.ConnectionError as e:
	    print("Ca ne passe pas donc on utilise un proxy")
	    if(method=="GET"):
	     res = session.get(url, params=parameters, proxies=proxies)
	    else:
	     res = session.post(url, data=parameters, params=auth, proxies=proxies)
	except requests.exceptions.RequestException as e:
	    print("Ca ne marche pas même avec un proxy, verifier la connexion internet")
	    raise SystemExit(e)
	# Print the url
	print(res.url)
	# Print the status code response
	print(res.status_code)
	# Print the response
	if res:
	    print('Response OK')
	    print("res="+res.text)
	    status = True
	    json_result = res.json()
	    result = json_result
	    print("La reponse en JSON est : \n" + str(json_result))
	    request_result = json_result["result"]
	    #print("Le tableau est : \n" + str(request_result))
	    #print("Le premier element est : \n" + str(request_result[0]))
	else:
	    print('Response Failed')
	return status, result

