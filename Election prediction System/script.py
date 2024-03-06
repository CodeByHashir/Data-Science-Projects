import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

start_page = 1
end_page = 266

csv_file_path = 'extracted_data.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Category', 'Number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

    for page_number in range(start_page, end_page + 1):
        url = f'https://www.geo.tv/election/NA-{page_number}'

        driver.get(url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'home_election_voter_left')))

        list_elements = driver.find_elements(By.CSS_SELECTOR, '.home_election_voter_left li')
        for li in list_elements:
            category = li.find_element(By.CSS_SELECTOR, '.home_election_voter_left_txt').text.strip()
            number = li.find_element(By.CSS_SELECTOR, '.home_election_voter_left_number').text.strip()
            writer.writerow({'Category': category, 'Number': number})
            print(f"{category}: {number}")

        print(f"Data has been extracted from page {page_number}")

driver.quit()
print(f"Data from all pages has been saved to {csv_file_path}")
