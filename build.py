"""
https://www.npmjs.com/package/html-styles
"""
from bs4 import BeautifulSoup
import requests
from HtmlStyles import html_styles
import tinycss2

tags = html_styles

# download file
page = requests.get("https://raw.githubusercontent.com/marionebl/html-styles/master/index.json")
data = page.json()


with open("HtmlStyles/html_styles.py", "w+", encoding="utf8") as built:
    built.write(
        f"""\"\"\"
List of HTML default tag styles.
\"\"\"

html_styles = {data}"""
    )
