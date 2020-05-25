import json
def capital(capitals):
    arr = []
    for i in json.loads(json.dumps(capitals)):
        try:
            place = i["state"]
        except:
            place = i["country"]
        out = "The capital of " + place + " is " + i["capital"]
        arr.append(out)
    return arr

state_capitals = [{"state": 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital": "Madrid"}]
print (capital(state_capitals))
