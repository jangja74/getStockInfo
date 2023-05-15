# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
from bs4 import BeautifulSoup

#PER 정보 조회
def get_per(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")
    print(soup.text)
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)

print("[000660: ", get_per("000660"), "]")
print(get_per("005930"))
