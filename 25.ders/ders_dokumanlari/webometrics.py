import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

def get_university_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        university_data = []

        rows = soup.select("table.sticky-enabled tbody tr")
        for row in rows:
            rank = row.select_one("td:nth-of-type(2) center").text.strip()
            university_name = row.select_one("td:nth-of-type(3) a").text.strip()
            turkish_translation = translator.translate(university_name, src="en", dest="tr").text

            university_data.append({
                "rank": rank,
                "university_name": university_name,
                "name_tr": turkish_translation
            })
        return university_data

def save_to_txt(data):
    with open("webometrics.txt", "w", encoding="utf-8")as file:
        file.write("rank, university_name, name_tr\n")
        for entry in data:
            file.write(f"{entry["rank"]}, {entry["university_name"]}, {entry["name_tr"]}\n")

urls = [
    "https://www.webometrics.info/en/Asia/turkey?sort=asc&order=World%20Rank",
    "https://www.webometrics.info/en/Asia/turkey?page=1&sort=asc&order=World%20Rank",
    "https://www.webometrics.info/en/Asia/turkey?page=2&sort=asc&order=World%20Rank"
]

all_university_data = []

for url in urls:
    print(f"University data for {url}:")
    uni_datas = get_university_data(url)
    all_university_data.extend(uni_datas)
    print("\n")

print(all_university_data)
save_to_txt(all_university_data)