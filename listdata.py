
from requestdata import sendRequest

#### Main

status, result = sendRequest("GET", "https://obriand.fr/api/v1/list.php")

if(status) :
	print("\n==> list data result = " + str(result))
else:
	print("\n==> list data has failed")
