def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
        
        
#Usage
print(http_status(200))  #output : ok
print(http_status(404))  #output : not found
print(http_status(500))  #output : internal server error
print(http_status(403))  #output : unknown status
            