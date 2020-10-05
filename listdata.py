
from requestdata import sendRequest

#### Main

status, result = sendRequest("https://obriand.fr/api/1/list.php")

if(status) :
	print("\n==> list data result = " + str(result))
else:
	print("\n==> list data has failed")
