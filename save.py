import csv


def save_to_file(articles):
    file = open("article.csv", mode="w", encoding='utf8')
    writer = csv.writer(file)
    writer.writerow(["title", "id", "name", "price", "review_count", "link"])
    for article in articles:
        writer.writerow(list(article.values()))
    return
