import sys
import json
from encodedecode import decode
from requestdata import log
from requestdata import sendRequest
import pprint

#### List data

# Define list function
def list():

# Get and check arg
  arg = ""
  try:
    arg = sys.argv[1]
    #print("type=" + arg)
  except:
    log("info: no type found in arguments")

# Prepare url
  url = "https://obriand.fr/api/v1/list.php"
  if arg:
    url += "?type="+arg

# Process request
  status, result = sendRequest("GET", url)
  if(status) :
    return result
  else:
    return "has failed"

# Main
r = str(list())
#.replace("\'", "\"")
print(r)
#json_object = json.loads(r)
#json_formatted_str = json.dumps(json_object, indent = 2)
#print(json_formatred_str)
