import requests

oauthurl = "http://10.255.255.254:2039/configure_oauth"

data = {"client_secret": "JhcFmalXgrUWJ66VPzrprWxWvWhkLI37",
        "authorize_url": "http://10.255.255.254:8080/realms/Laser/protocol/openid-connect/auth",
        "token_url": "http://10.255.255.254:8080/realms/Laser/protocol/openid-connect/token"
        }



response = requests.post(oauthurl, json=data)

print(response.status_code)
print(response.json())