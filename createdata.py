import sys
from requestdata import sendRequest

#### Main

# Get and check args
arg1 = ""
try:
  arg1 = sys.argv[1]
  print("type=" + arg1)
except:
  print("warning: no type found in arguments")

arg2 = ""
try:
  arg2 = sys.argv[2]
  print("value=" + arg2)
except:
  print("warning: no value found in arguments")

p = {}
p["type"] = arg1
p["value"] = arg2

status, result = sendRequest("POST", "https://obriand.fr/api/v1/create.php", p)

if(status) :
	print("\n==> create data result = " + str(result))
else:
	print("\n==> create data has failed")
