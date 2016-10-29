import json, requests

def getKarma(username):
    url = "https://www.reddit.com/user/" + username + "/about/.json"
    res = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
    data = res.json()
    if res.status_code == 404:
        return -1
    return data['data']['link_karma']

karma = getKarma("Pradeet")
print(karma)
