import requests
import json
from datetime import datetime
from encodedecode import decode

#### Log function
logs = ""
def log(msg):
  #print(msg)
  return

#### Decode json function
def decodeJson(json):
  for element in json["result"]:
    element["value"] = decode(element["value"])
  return json

#### Send request function
def sendRequest(method, url, parameters={}):
	status = False
	result = json.dumps({})
	# Init auth object
	auth={}
	# Init data object
	data = dict(parameters)
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
	# Log the request url
	log(url)
	# Log the request parameters
	log("parameters=" + str(parameters))
	# Log the request data
	log("data=" + str(data))
	# Try to perform the request
	try:
	    log("On essaie sans proxy")
	    if(method=="GET"):
	     res = session.get(url, params=parameters)
	    else:
	     res = session.post(url, data=data, params=auth)
	except requests.exceptions.ConnectionError as e:
	    log("La requête ne passe pas donc on utilise un proxy")
	    if(method=="GET"):
	     res = session.get(url, params=parameters, proxies=proxies)
	    else:
	     res = session.post(url, data=data, params=auth, proxies=proxies)
	except requests.exceptions.RequestException as e:
	    log("Ca ne marche pas même avec un proxy, verifier la connexion internet")
	    raise SystemExit(e)
	# Log the url
	log(res.url)
	# Log the status code response
	log(res.status_code)
	# Log the response
	if res:
	    log('Response OK')
	    log("res="+res.text)
	    status = True
	    try:
	      json_result = res.json()
	    except:
	      json_result = {}
	      json_result["error"] = "Response is not a JSON"
	    try:
	      decodeJson(json_result)
	    except:
	      log("Fail to decode value attribute in JSON response")
	    result = json_result
	    log("La reponse en JSON est : \n" + str(json_result))
	    try:
	      request_result = json_result["result"]
	    except KeyError:
	      request_result = json_result["error"]
	    #print("Le tableau est : \n" + str(request_result))
	    #print("Le premier element est : \n" + str(request_result[0]))
	else:
	    log('Response Failed')
	print(logs)
	return status, result

