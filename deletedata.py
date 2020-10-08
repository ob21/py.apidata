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

# Process delete request
status, result = sendRequest("GET", "https://obriand.fr/api/v1/delete.php?id=" + arg)

if(status) :
	print("\n==> delete data result = " + str(result))
else:
	print("\n==> delete data has failed")
