import chardet
with open("article.csv", 'rt', encoding='utf-8') as f:
    file_data = f.readline()
print(chardet.detect(file_data.encode()))

