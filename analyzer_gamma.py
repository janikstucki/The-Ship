import requests
from concurrent.futures import ThreadPoolExecutor
import boto3

s3 = boto3.client(
    's3',
    endpoint_url='http://127.0.0.1:2016', 
    aws_access_key_id='theship',
    aws_secret_access_key='theship1234'
)

bucket_name = 'analyzer-gamma'

existing_buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]
if bucket_name not in existing_buckets:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' wurde erstellt!")
else:
    print(f"Bucket '{bucket_name}' existiert bereits.")
file_key = 'data.hex'

urls = [
    "http://10.255.255.254:2043/x/measure",
    "http://10.255.255.254:2043/y/measure",
    "http://10.255.255.254:2043/z/measure"
]

def measure(url):
    response = requests.post(url)
    return response.json()

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(measure, urls))

measurement_result = None
for r in results:
    if "measurement" in r:
        measurement_result = r["measurement"]
        break

if not measurement_result:
    raise RuntimeError("Keine Messung hat ein Ergebnis geliefert!")

print("Messung erfolgreich, Hex-Resultat:", measurement_result)

s3.put_object(Bucket=bucket_name, Key=file_key, Body=measurement_result.encode('utf-8'))
print(f"Ergebnis erfolgreich in S3 gespeichert: s3://{bucket_name}/{file_key}")
