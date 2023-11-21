from bs4 import BeautifulSoup

# ローカルのHTMLファイルのパスを指定
html_file_path = 'index.html'

# HTMLファイルを読み込みます
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html_content, 'html.parser')

# 例: タイトルタグのテキストを取得して表示
title_tag = soup.title
if title_tag:
    print(f'Title: {title_tag.text}')
else:
    print('Title tag not found.')

# 他の要素を取得したり、必要な情報を抽出するためにBeautiful Soupの機能を使用できます
# 例: すべてのリンクを取得して表示
for Div in soup.find_all('div',class_=''):
    print(f'Div: {Div.get("class")} - Text: {Div.text}')