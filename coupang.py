import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
URL = "https://www.coupang.com/np/categories/"


def getMaxPage(categoryNumber):
    result = requests.get(URL+categoryNumber, headers=HEADERS).text

    soup = BeautifulSoup(result, "html.parser")

    pagination = soup.find("div", {"class": "page-warpper"})

    links = pagination.find_all("a")
    links = links[1:-1]

    pages = []
    for link in links:
        pages.append(int(link.string))
    max_page = pages[-1]

    return max_page


def getArticles(max_page, categoryNumber):
    articles = []
    for page in range(max_page):
        print(f"{page+1} 완성")
        result = requests.get(
            f"{URL+categoryNumber}?listSize=60&page={page+1}", headers=HEADERS).text
        soup = BeautifulSoup(result, "html.parser")

        # 카테고리
        list_title = soup.find(
            "h3", {"class": "newcx-product-list-title"}).string.strip()
        list_title = list_title.replace(" ", "")
        # 제목
        titles = soup.find_all("div", {"class": "name"})
        names = []
        for title in titles:
            names.append(title.string[5:-1])
        # 가격
        price_value = soup.find_all("strong", {"class": "price-value"})
        prices = []
        for value in price_value:
            string = value.string

            prices.append(int(string.replace(",", "")))

        # 리뷰 수
        rating_total_count = soup.find_all(
            "span", {"class": "rating-total-count"})
        review_counts = []
        for total_count in rating_total_count:
            string = total_count.string
            review_counts.append(int(string[1:-1]))

        # 링크
        baby_product = soup.find_all(
            "li", {"class": "baby-product"})
        links = []
        for baby in baby_product:
            links.append("https://www.coupang.com" + baby.find("a")["href"])

        # 제품 번호
        baby_product = soup.find_all(
            "li", {"class": "baby-product"})
        ids = []
        for baby in baby_product:
            ids.append(int(baby.find("a")["data-item-id"]))

        # 정리
        for num in range(len(names)):
            articles.append(
                {"title": list_title, "id": ids[num], "name": names[num], "price": prices[num], "review_count": review_counts[num], "link": links[num]})
    return articles
