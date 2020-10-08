import sys
from requestdata import sendRequest

#### Main

# Get and check arg
arg = ""
try:
  arg = sys.argv[1]
  try:
    int(arg)
    print("id=" + arg)
  except ValueError:
    print("warning: id '" + arg + "' is not an integer")
except:
  print("warning: no id found in arguments")

# Process get request
status, result = sendRequest("GET", "https://obriand.fr/api/v1/get.php?id=" + arg)

if(status) :
	print("\n==> get data result = " + str(result))
else:
	print("\n==> get data has failed")
