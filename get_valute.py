import requests
from bs4 import BeautifulSoup


def valyuta_kurslari():
    URL = "https://cbu.uz/oz/"
    page = requests.get(URL)
    kurslar = ""
    soup = BeautifulSoup(page.content, "html.parser")

    job_elements = soup.find_all("div", class_="exchange__item_value")
    for job_element in job_elements:
        value = job_element.text.strip()
        if "USD" in value:
            kurslar += f"{value} UZS\n\n"
        if "EUR" in value:
            kurslar += f"{value} UZS\n\n"
        if "RUB" in value:
            kurslar += f"{value} UZS\n\n"
        
    return kurslar

valyuta_kurslari()