import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# google transtlate api içn bir tercüman

translator = Translator()

def get_university_data(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        university_data = []
        
        ul_tag = soup.find("ul", {'id': 'myUl'})
        li_tags = ul_tag.find_all("li", class_="unilist")
        
        for li_tag in li_tags:
            data_id = li_tag.find("a", href=True)["data-id"]
            uni_name_tr = li_tag.find("h3", class_="baslik").text.strip()
            uni_name_en = translator.translate(uni_name_tr, src="tr", dest="en").text
            university_data.append({
                "id": data_id,
                "name_tr": uni_name_tr,
                "name_en": uni_name_en
            })
        return university_data

def save_to_txt(data):
    with open("university_data.txt", "w", encoding="utf-8") as file:
        file.write("ID, Name(EN), Name(TR)\n")
        for entry in data:
            file.write(f"{entry["id"]}, {entry["name_en"]}, {entry["name_tr"]}\n")
    
url = "https://yokatlas.yok.gov.tr/universite.php"

print(f"University data for {url}:")
university_data = get_university_data(url)

for entry in university_data:
    print(f"ID: {entry["id"]}, University en name: {entry["name_en"]}, University tr name: {entry["name_tr"]}")

save_to_txt(university_data)