import json
from pprint import pprint

with open('data.json') as file:
    data = json.load(file)

AllShops = []
AllColleges = {}


def shortName(s):

    # split the string into a list
    l = s.split()
    new = ""

    # traverse in the list
    for i in range(len(l)):
        s = l[i]

        # adds the capital first character
        new += (s[0].upper())

    # l[-1] gives last item of list l. We
    # use title to print first character in
    # capital.
    # new += l.title()

    return new


jsondata = {
    "intents": [{
        "tag": "greeting",
        "patterns": [
            "Hi",
            "Hey",
            "How are you",
            "Is anyone there?",
            "Hello"
        ],
        "responses":[
            "Hey",
            "Hello",
            "Hi there",
            "Hi there, how can I help?"
        ]
    }]
}


for d in range(len(data)):
    if data[d]["model"] == "nearapp.college":
        feilds = data[d]['fields']
        # subData = {}
        AllColleges[data[d]["pk"]] = [feilds["name"], feilds["location"]]
        # feilds["pk"] = data[d]["pk"]
        # AllColleges.append(subData)

for d in range(len(data)):
    if data[d]["model"] == "nearapp.shop":
        feilds = data[d]['fields']
        feilds["pk"] = data[d]["pk"]
        feilds["college"] = AllColleges[feilds["college"]][0]
        AllShops.append(feilds)
        # AllShops.append(data[d])
        # print(pprint(data[d]))


def getNearByShops(college, Type):
    lst = {}
    for i in AllShops:
        if i["college"] == college and i["Type"] == Type and len(lst) <= 3:

            lst[i["distance"]] = [i["ShopName"], i["pk"]]
    # print(lst)
    output = {}
    anchor = []
    for key in sorted(lst):

        output[key] = lst[key]
        # print("%s: %s" % (key, ))
    # print(output)
    outLst = []
    for key, value in output.items():
        a = f"<a href='/shop/{output[key][1]}' >{output[key][0]} ({key}KM)</a>"
        outLst.append(a)

    return outLst


def getBestShops(college, Type):
    lst = {}
    for i in AllShops:
        if i["college"] == college and i["Type"] == Type and len(lst) <= 3:

            lst[i["rating"]] = [i["ShopName"], i["pk"]]
    # print(lst)
    output = {}
    anchor = []
    for key in sorted(lst, reverse=True):

        output[key] = lst[key]
        # print("%s: %s" % (key, ))
    # print(output)
    outLst = []
    for key, value in output.items():
        a = f"<a href='/shop/{output[key][1]}' >{output[key][0]} ({key} Star)</a>"
        outLst.append(a)
    # print(outLst)
    return outLst


# getBestShops(
#     'Mukesh Patel School of Technology Management & Engineering',  'gym')


# print(pprint(AllShops))
# print(pprint(AllColleges))

for i in AllShops:
    anchorsNear = " ".join(getNearByShops(i['college'], i['Type']))
    anchorsBest = " ".join(getBestShops(i['college'], i['Type']))
    entNear = {
        "tag": f"near by {i['college']} {shortName(i['college'])}",
        "patterns": [
            f"{i['Type']} near {i['college']} {shortName(i['college'])}"

        ],
        "responses": [
            f"{anchorsNear}"
        ]
    }
    entBest = {
        "tag": f"best {i['college']} {shortName(i['college'])}",
        "patterns": [
            f"Best {i['Type']} {i['college']} {shortName(i['college'])}"

        ],
        "responses": [
            f"{anchorsBest}"
        ]
    }
    jsondata["intents"].append(entNear)
    jsondata["intents"].append(entBest)
    # print(ent)

# pprint(jsondata)

with open("databot.json", 'w') as file:
    json.dump(jsondata, file)
