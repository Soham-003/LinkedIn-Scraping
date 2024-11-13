import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    """Setup the Selenium WebDriver."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Maximize browser window for better view
    return driver

def login_to_linkedin(driver, email, password):
    """Log in to LinkedIn."""
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys(email)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)  # Press Enter to login

    time.sleep(3)

def search_linkedin(driver, first_name, last_name):
  """Search for people on LinkedIn by name and scroll down to capture all visible results."""
  search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
  search_box.send_keys(f'{first_name} {last_name}')
  search_box.send_keys(Keys.RETURN)

  # Scroll down to capture all visible results
  last_height = driver.execute_script("return document.body.scrollHeight")
  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
  # Adjust delay as needed
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
      break
    last_height = new_height


def get_user_data(driver):
  """Scrape user data from all visible LinkedIn search results."""
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  people = soup.find_all('li', class_='search-result__occluded-item')  # Adjust based on actual class names

  users = []
  for person in people:
    name = person.find('span', class_='name').text.strip() if person.find('span', class_='name') else "N/A"
    job_title = person.find('p', class_='subline-level-1').text.strip() if person.find('p', class_='subline-level-1') else "N/A"
    location = person.find('p', class_='subline-level-2').text.strip() if person.find('p', class_='subline-level-2') else "N/A"
    profile_url = person.find('a', href=True)['href'] if person.find('a', href=True) else "N/A"

    # Print extracted data for debugging
    print(f"Name: {name}")
    print(f"Job Title: {job_title}")
    print(f"Location: {location}")
    print(f"Profile URL: {profile_url}")
    print("-" * 30)

    users.append({
        'Name': name,
        'Job Title': job_title,
        'Location': location,
        'Profile URL': profile_url
    })

  return users

def save_to_csv(data, filename='linkedin_users.csv'):
    """Save the scraped data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    logging.info(f"Data saved to {filename}")

def main():
    """Main function to execute the script."""
    # User LinkedIn credentials
    email = input("Enter LinkedIn email: ")
    password = input("Enter LinkedIn password: ")

    # Get user names for search
    first_name = input("Enter the user's first name: ")
    last_name = input("Enter the user's last name: ")

    # Set up Selenium WebDriver
    driver = setup_driver()

    try:
        # Log in to LinkedIn
        login_to_linkedin(driver, email, password)

        # Perform LinkedIn search
        search_linkedin(driver, first_name, last_name)

        # Scrape user data
        users = get_user_data(driver)

        # Save the data to a CSV file
        save_to_csv(users)
    except NoSuchElementException as e:
        logging.error(f"Element not found: {e}")
    except TimeoutException as e:
        logging.error(f"Timeout error: {e}")
    except WebDriverException as e:
        logging.error(f"WebDriver error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == '__main__':
    main()