import requests

url = "http://10.255.255.254:2030/send"

data = {"src": "Core Station", 
        "msg": "0aCKiMfP2dnLzc+IkIqI0fbEivaI2cXf2MnP9oiQivaI6cXYz4r53svew8XE9oiG9sSK9ojOz9new8TL3sPFxPaIkIr2iOvQ39jLivney97DxcT2iIb2xIr2iM7L3sv2iJCK9ojsxdjZycLfxM3Zzsvez8SKgu3Y39raz4qbk5iEm5yShJuam4ScnIP2iIb2xIr2iN7Z9oiQivaIn5qfkpKfmJz2iPbE1/bEiIagiojZw83Ey97f2M+IkIqIyZ/PnsubnJ2emJOdmJ2bmc7Ik8yfncyanZjLzJ2Zn5qSm86YnsuTyJ2dz5KenM/Ins+ZnJqfzszLzJjJmZ3PiKDXoA=="}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())