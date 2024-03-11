import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Aksaray"

response = requests.get(url) # Web sayfamızı çekiyoruz

html_icerigi = response.content # Web sayfamızın içeriğini alıyoruz

# print(html_icerigi)

soup = BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için Beautifulsoup 

# print(soup.prettify())

print(soup.find_all("img"))
