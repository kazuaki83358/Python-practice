from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
import time

# Step 1: Setup Chrome options (run headlessly)
options = Options()
options.add_argument("--headless")  # Run without opening Chrome window
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Step 2: Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.ipuranklist.com/ranklist/btech?batch=24&insti=180&sem=4&branch=CSE"
driver.get(url)

# Step 3: Wait for table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.ng-star-inserted"))
)

# Step 4: Get the rendered HTML
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Step 5: Extract data
rows = soup.find_all("tr", class_="ng-star-inserted")
data = []

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 5:
        roll_number = cols[0].text.strip()
        name = cols[1].text.strip()
        marks = cols[2].text.strip()
        sgpa = cols[3].text.strip()
        rank = cols[4].text.strip()
        data.append([roll_number, name, marks, sgpa, rank])

# Step 6: Save to CSV
with open("ranklist.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Roll Number", "Name", "Marks", "SGPA", "Rank"])
    writer.writerows(data)

driver.quit()
print("✅ Data saved to ranklist.csv (headless mode)")
