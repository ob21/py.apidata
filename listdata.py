import sys
from requestdata import sendRequest

#### Main

# Get and check arg
arg = ""
try:
  arg = sys.argv[1]
  print("type=" + arg)
except:
  print("info: no type found in arguments")

# Prepare url
url = "https://obriand.fr/api/v1/list.php"
if arg:
  url += "?type="+arg

# Process request

status, result = sendRequest("GET", url)

if(status) :
	print("\n==> list data result = " + str(result))
else:
	print("\n==> list data has failed")
