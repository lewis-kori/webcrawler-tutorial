from selenium.webdriver import Chrome
import pandas as pd

webdriver = "path_to_your_driver"

driver = Chrome(webdriver)

pages = 11

total = []
for page in range(1,pages):
    
    url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"

    driver.get(url)
    
    quotes = driver.find_elements_by_class_name("quote")
    for quote in quotes:
        quote_text = quote.find_element_by_class_name('text').text[1:-2]
        author = quote.find_element_by_class_name('author').text
        new = ((quote_text,author))
        total.append(new)

driver.close()
df = pd.DataFrame(total,columns=['quote','author'])
df.to_csv('quoted.csv')
