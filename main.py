import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from import_everything import *
from mailsender_functions import *


# Define your settings
class Settings:
    def __init__(self, znamka="", cenaMin=100, cenaMax=9999999, letnikMin=0, letnikMax=2090,
                 kmMin=0, kmMax=250000, kwMin=66, kwMax=999, EQ1=1000000000, EQ2=1000000000,
                 EQ3=1000000000, EQ4=100000000, EQ5=1000000000, EQ6=1000000000, EQ7=1110100120,
                 EQ8=101000000, EQ9=1000000020, KAT=1010000000, paketgarancije=0, zaloga=10, bencin=0):
        self.znamka = znamka
        self.cenaMin = cenaMin
        self.cenaMax = cenaMax
        self.letnikMin = letnikMin
        self.letnikMax = letnikMax
        self.kmMin = kmMin
        self.kmMax = kmMax
        self.kwMin = kwMin
        self.kwMax = kwMax
        self.EQ1 = EQ1
        self.EQ2 = EQ2
        self.EQ3 = EQ3
        self.EQ4 = EQ4
        self.EQ5 = EQ5
        self.EQ6 = EQ6
        self.EQ7 = EQ7
        self.EQ8 = EQ8
        self.EQ9 = EQ9
        self.KAT = KAT
        self.paketgarancije = paketgarancije
        self.zaloga = zaloga
        self.bencin = bencin #bencin = 201, diesel = 202, vse = 0

# Function to be called when a new item is added to the JSON file
def on_new_item_added(new_item):
    print(f"New item added: {new_item}")
    #send_mail("casperkadivec@gmail.com ", "testsubject", "testmessage\n"+new_item)


# Create an instance of the Settings class with default values
budget = 5000
allSettings = [
    Settings(znamka="audi", cenaMax=budget, letnikMin=2008, bencin=202),
    Settings(znamka="honda", cenaMax=budget, letnikMin=2004),
    Settings(znamka="volkswagen", cenaMax=budget, letnikMin=2008, bencin=202)
]

for settings in allSettings:
    # Construct the URL using the settings object
    url = "https://www.avto.net/Ads/results.asp?"
    url += "&".join([f"{key}={value}" for key, value in settings.__dict__.items()])

    # Set up Chrome WebDriver
    options = Options()
    driver = webdriver.Chrome(options=options)

    # Open the URL in the browser
    driver.get(url)

    # Extract href attribute from all links with class "stretched-link"
    links = driver.find_elements(By.CSS_SELECTOR, "a.stretched-link")
    links_array = [link.get_attribute("href") for link in links]

    # Save links array to a JSON file, calling the on_new_item_added function if a new item is added
    json_file_path = 'extracted_links.json'

    try:
        with open(json_file_path, 'r') as file:
            existing_links = json.load(file)
    except FileNotFoundError:
        existing_links = []

    # Check for duplicates and append non-duplicates to the existing links
    for link in links_array:
        if link not in existing_links:
            existing_links.append(link)
            on_new_item_added(link)

    # Save the updated links array to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(existing_links, file, indent=2)

    # Close the browser window
    driver.quit()
quit_everything()