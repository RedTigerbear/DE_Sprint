import urllib.request as req
from bs4 import BeautifulSoup
import json
import time

data = {
    "data":[]
}

#получаем код страницы с поиском вакансий
for page in range(1, 3):
    url = "https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&search_field=name&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=100&page=" + str(page)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'}
    resp = req.Request(url=url, headers=headers)
    with req.urlopen(resp) as response:
        page_html = response.read()
    soap = BeautifulSoup(page_html, "lxml")

    #получаем со страницы список url отдельных вакансий
    tags_vac_url = soap.find_all(class_="serp-item__title")
    
    #проходим в цикле по этим url, чтобы получить информацию по каждой из вакансий
    for iter in tags_vac_url:
        time.sleep(2)

        vac_url = iter.attrs["href"][0:30]
        resp_vac = req.Request(url=vac_url, headers=headers)
        with req.urlopen(resp_vac) as response:
            vac_html = response.read()
        soap_vac = BeautifulSoup(vac_html, "lxml")
        
        #получаем нужные нам значения
        tag_name = soap_vac.find(attrs={"data-qa":"vacancy-title"}).text
        tag_exp = soap_vac.find(attrs={"data-qa":"vacancy-experience"}).text
        tag_salary = soap_vac.find(attrs={"data-qa":"vacancy-salary"}).text.replace('\xa0', ' ').partition(".")[0]
        if soap_vac.find(attrs={"data-qa":"vacancy-view-location"}) is None:
            tag_region = soap_vac.find(attrs={"data-qa":"vacancy-view-raw-address"}).text.partition(",")[0]
        else:
            tag_region = soap_vac.find(attrs={"data-qa":"vacancy-view-location"}).text
        
        #сохраняем данные в список
        data["data"].append({'title':tag_name, 'work experience':tag_exp, 'salary':tag_salary, 'region':tag_region})
        #сохраняем список в json и в файл
        with open("data.json", "a", encoding='cp1251') as f:
            json.dump(data, f, ensure_ascii=False)