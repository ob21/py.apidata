
from requestdata import sendRequest

#### Main

status, result = sendRequest("https://obriand.fr/api/1/create.php")

if(status) :
	print("\n==> create data result = " + str(result))
else:
	print("\n==> create data has failed")
