"""
1) put( ):- It is used to send a put request to a variable. It is usually used to update or
completely change the resources of a specific URL.

2) delete( ):- Delete is used to delete the specific resource, specified by URL.

3) head( ):- The head method returns a header for a specific resource

4) post( ):- Post requests take with it the data to the server to update it with.

5) patch( ):- The patch is used to send patch requests. It is used to apply partial
modifications to a resource. It carries with it the instructions for the modification.

"""


import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
