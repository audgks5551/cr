from coupang import getMaxPage, getArticles
from save import save_to_file

categoryNumber = ["186764", "187069", "213201"]
articles = []
for number in categoryNumber:
    max_page = getMaxPage(number)
    articles += getArticles(max_page, number)
save_to_file(articles)
