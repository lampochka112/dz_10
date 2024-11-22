import requests
from bs4 import BeautifulSoup


def main():
    url = "https://ww.52shuku.vip/yanqing/hx4r_2828.html"
    response = requests.get(url)
    print(response.status_code)

    soup = BeautifulSoup(response, 'html.parser')
    part = soup.find("div", class_="text-container")
    with open("page.txt", 'a', encoding ='UTF-8') as file:
        file.write(part.text)


if __name__ == "__main":
    main()
