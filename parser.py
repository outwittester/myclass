import json

f = open("data.json", "r")
data = json.load(f)

orderType = "orderType"
dueToday = "dueToday"
email = "email"
shippingAddress = "shippingAddress"
arr = [orderType, dueToday, email, shippingAddress]
result = {}
for key in arr:
    result[key] = set()


def helper(data):
    if type(data) == str:
        return

    if type(data) == dict:
        for (k, v) in data.items():
            if k in arr:
                if k == shippingAddress:
                    result[k].add(','.join(v.values()))
                elif type(v) == list:
                    for e in v:
                        result[k].add(e)
                else:
                    result[k].add(v)
            else:
                helper(v)

    if type(data) == list:
        for e in data:
            helper(e)


f.close()
helper(data)
print(result)
