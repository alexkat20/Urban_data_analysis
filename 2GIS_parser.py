import time
import geopandas as gpd
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from geopy.geocoders import ArcGIS


def geocode_buildings(address):

    geolocator = ArcGIS(user_agent="Tester")  # Указываем название приложения (так нужно, да)

    try:
        location = geolocator.geocode("Калининград " + address, timeout=10)  # Создаем переменную, которая состоит из нужного нам адреса
        return (location.latitude, location.longitude)
    except:
        return (None, None)


class WebDriver:
    location_data = {}

    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.options.headless = False
        self.options.page_load_strategy = 'none'

        chrome_path = ChromeDriverManager().install()
        chrome_service = Service(chrome_path)

        self.driver = Chrome(options=self.options, service=chrome_service)
        self.driver.implicitly_wait(10)

    def get_number_of_places(self, url):

        self.driver.get(url)

        services = pd.DataFrame({"Name": [], "address": [], "latitude": [], "longitude": []})

        i = 1
        while True:  # <=== change this number based on your requirement
            time.sleep(1)
            try:
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
                    (By.XPATH, f'(//div[contains(@class,"search-business-snippet-view__address")])[{i}]')))
                # load the reviews
                self.driver.find_element(By.XPATH,
                                         f'(//div[contains(@class,"search-business-snippet-view__address")])[{i}]'). \
                    location_once_scrolled_into_view

                review = self.driver.find_element(By.XPATH,
                                                  f'(//div[contains(@class,"search-business-snippet-view__address")])[{i}]')
                name = self.driver.find_element(By.XPATH,
                                                  f'(//div[contains(@class,"search-business-snippet-view__title")])[{i}]').text

                # wait for loading the reviews

                address = review.text
                latitude, longitude = geocode_buildings(address)
                services.loc[len(services)] = {"Name": name, "address": address, "latitude": latitude, "longitude": longitude}

                # get the reviewsCount
                print(name, address)
                i += 1
            except:
                break

        return services


links = []

print("Enter all the links you need to parser. When you finish enter 0")
link = input()

while link != '0':
    links.append(link)
    link = input()

print(links)

file_name = input("Enter the name of the file you want to sava your data in: ")

print(file_name)

for l in links:

    x = WebDriver()
    services = x.get_number_of_places(l)
    print(services)

services.to_csv(file_name + ".csv")

gdf = gpd.GeoDataFrame(services, geometry=gpd.points_from_xy(services.longitude, services.latitude))

gdf.to_file(f"{file_name}.geojson", driver="GeoJSON")
