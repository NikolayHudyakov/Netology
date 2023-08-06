"""
<a class="serp-item__title" data-qa="serp-item__title" target="_blank" href="https://spb.hh.ru/vacancy/80002041?from=vacancy_search_list&amp;query=python">
    Старший программист-разработчик (Python/Django) / Senior back-end developer
</a>
"""
"""
<span class="bloko-tag__section bloko-tag__section_text" data-qa="bloko-tag__text">
    Python
</span>
"""
"""
<span data-qa="vacancy-salary-compensation-type-net" class="bloko-header-section-2 bloko-header-section-2_lite">
    от 
    <!-- -->
        200&nbsp;000
    <!-- --> 
    до 
    <!-- -->
    300&nbsp;000
    <!-- --> 
    <!-- -->
    ₽
    <span class="vacancy-salary-compensation-type">
        <!-- -->
        на руки
    </span>
</span>
"""
"""
<a data-qa="vacancy-view-link-location" class="bloko-link bloko-link_kind-tertiary bloko-link_disable-visited" target="_blank" href="/search/vacancy/map?vacancy_id=80002041&amp;hhtmFrom=vacancy">
    <span data-qa="vacancy-view-raw-address">
        Москва, 
        <span class="metro-station">
            <span class="bloko-metro-pin" style="background-color: rgb(79, 176, 79);">
            </span>
            Павелецкая
        </span>, 
        <span class="metro-station">
            <span class="bloko-metro-pin" style="background-color: rgb(145, 81, 51);">
            </span>
            Павелецкая
        </span>, 
        1-й Кожевнический переулок, 6с1
    </span>
</a>
"""
"""
<span data-qa="bloko-header-2" class="bloko-header-section-2 bloko-header-section-2_lite">
    <span>
        CATAPULTO.RU
    </span>
</span>
"""

import json
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import fake_headers


headers_gen = fake_headers.Headers(browser='firefox', os='win')
headers = headers_gen.generate()

response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers)
html_data = response.text

soup = BeautifulSoup(html_data, 'lxml')
span_tag = soup.find_all('a', class_='serp-item__title')

vacancies = {}


for item in span_tag:
    response1 = requests.get(item['href'], headers=headers)
    html_data1 = response1.text
    vacancy = {}
    soup1 = BeautifulSoup(html_data1, 'lxml')
    span_tag1 = soup1.find_all('span', class_='bloko-tag__section bloko-tag__section_text')
    for item1 in span_tag1:
        a = item1.text.find('Django')
        if item1.text.find('Django') != -1 or item1.text.find('Flask') != -1:
            vacancy['href'] = item['href']

            span_tag2 = soup1.find_all('span', class_='bloko-header-section-2 bloko-header-section-2_lite')
            vacancy['salary'] = span_tag2[0].text
            vacancy['company_name'] = span_tag2[1].text

            span_tag3 = soup1.find('a', class_='bloko-link bloko-link_kind-tertiary bloko-link_disable-visited')
            if span_tag3 is not None:
                vacancy['city'] = span_tag3.text
                vacancies[item.text] = vacancy
                break

with open('vacancies.json', "w") as f:
    json.dump(vacancies, f)

pprint(vacancies)