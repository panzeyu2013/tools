import requests
import time
from requests.auth import HTTPBasicAuth

def download(url,file_path):
    r = requests.get(url,auth=HTTPBasicAuth("id","keys"))
    with open(file_path, 'wb') as f:
        f.write(r.content)
        f.close()
    
if __name__ == "__main__":
    url_base = "url"
    file_path_base = "file_path"
    for i in range(1,10):
        print(i)
        url = url_base + str(i) + ".webm"
        file_path = file_path_base + str(i) + ".webm"
        
        try:
            download(url,file_path)
        except:
            time.sleep(1)
            continue

