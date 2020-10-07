
from requestdata import sendRequest

#### Main

p = {}
p["type"] = "note"
p["value"] = "{toto=\"true\"}"

status, result = sendRequest("POST", "https://obriand.fr/api/v1/create.php", p)

if(status) :
	print("\n==> create data result = " + str(result))
else:
	print("\n==> create data has failed")
