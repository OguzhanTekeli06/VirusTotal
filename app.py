import requests
import json
import time

api_key = "adb34e2491e6eb3fbe5c1d142e9f749015af3afcb07071864696c0b53fa0dab6"
url = "https://www.virustotal.com/vtapi/v2/url/report"

with open('apis.txt', 'r') as f:
	apikeys = [line.rstrip('\n') for line in open('apis.txt')]

with open('urls.txt', 'r') as f:
	urls = [line.rstrip('\n') for line in open('urls.txt')]

# print(apikeys)
# print(urls)

def process_response(response_json, site):
    if 'positives' in response_json:
        positives = response_json['positives']
        total = response_json['total']
        scan_date = response_json['scan_date']
        scans = response_json['scans']
        
        with open('vt_results.txt', 'a') as vt:
            vt.write(f"URL: {site}\n")
            vt.write(f"Positives: {positives}/{total}\n")
            vt.write(f"Scan Date: {scan_date}\n")
            vt.write("Detailed Results:\n")
            
            for scanner, result in scans.items():
                vt.write(f"  Scanner: {scanner}\n")
                vt.write(f"    Detected: {result['detected']}\n")
                vt.write(f"    Result: {result['result']}\n")
                if 'detail' in result:
                    vt.write(f"    Detail: {result['detail']}\n")
            vt.write("\n")
    else:
        with open('vt_results.txt', 'a') as vt:
            vt.write(f"URL: {site} - URL NOT FOUND\n")

for apis in apikeys:
    for i in range(0,4):
        for site in urls:
            params = {'apikey': api_key, 'resource': site}
            response = requests.get(url, params=params)
            response_json = response.json()
            print(json.dumps(response_json, indent=4))
            process_response(response_json, site)
            time.sleep(15)





