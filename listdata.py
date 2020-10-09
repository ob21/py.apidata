import sys
from requestdata import sendRequest

#### List data

# Define list function
def list():

# Get and check arg
  arg = ""
  try:
    arg = sys.argv[1]
    #print("type=" + arg)
  except:
    print("info: no type found in arguments")

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
print("\n==> list data result = " + str(list()))
