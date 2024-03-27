import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Aksaray"

response = requests.get(url) # Web sayfamızı çekiyoruz

html_icerigi = response.content # Web sayfamızın içeriğini alıyoruz.

print(html_icerigi)

# # soup = BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

# # # print(soup.prettify())

# # print(soup.find_all("span"))

# import requests
# from bs4 import BeautifulSoup

# url = "https://realpython.github.io/fake-jobs/"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
# # print(soup.prettify())
# # print(soup.find_all("a"))

# job_elements = soup.find_all("div", class_="column is-half")
# # print(job_elements)

# # for job_element in job_elements:
# #     print("*************************")
# #     title_element = job_element.find("h2", class_="title")
# #     company_element = job_element.find("h3", class_="company")
# #     location_element = job_element.find("p", class_="location")
# #     print(title_element, company_element, location_element)
# #     print("*************************")

# for job_element in job_elements:
#     print("*************************")
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip(), company_element.text.strip(), location_element.text.strip(),sep=" - ")
#     print("*************************")