html_document = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk Sayfa</title>
</head>
<body>
    <h1 id = "header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <img src="fred.jpg" alt="">
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_document, 'html.parser')
result = soup.prettify()
# result = soup.title
# result = soup.title.name (.string)
# result = soup.head
# result = soup.body
# result = soup.find_all("h1")

print(result)