import pandas as pd

url_content = 'https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv'
url_salaries = 'https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv'
sf = pd.read_csv(url_content)
sf_salaries = pd.read_csv(url_salaries)
print(sf_salaries)
