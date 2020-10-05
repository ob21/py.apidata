
from requestdata import sendRequest

#### Main

type = "note"
value = "test"

status, result = sendRequest("https://obriand.fr/api/v1/create.php?type="+type+"&value="+value)

if(status) :
	print("\n==> create data result = " + str(result))
else:
	print("\n==> create data has failed")
