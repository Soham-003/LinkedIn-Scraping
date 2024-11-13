# LinkedIn Data Scraper
This project retrieves LinkedIn user data based on a person's first and last name using two methods:

LinkedIn API (Script 1): Fetches data via LinkedIn's official API.
Web Scraping (Script 2): Uses Selenium and BeautifulSoup to scrape LinkedIn search results.

# Technologies Used
Python 3.x
Requests, Selenium, BeautifulSoup, Pandas
ChromeDriver for Selenium

# Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/linkedin-data-scraper.git
cd linkedin-data-scraper

2. Install Required Libraries
bash
Copy code
pip install -r requirements.txt

3. Download ChromeDriver
Download the appropriate ChromeDriver from here and move it to your project folder.

4. Obtain LinkedIn API Access Token
Get your LinkedIn API access token from LinkedIn Developer and replace the token in Script 1.

# Usage
1. Run Script 1 (LinkedIn API)
bash
Copy code
python linkedin_api_script.py
Enter first and last name to fetch data from the LinkedIn API.
Output: linkedin_users.csv (or .json / .txt).

2. Run Script 2 (Web Scraping)
bash
Copy code
python linkedin_scraping_script.py
Enter first and last name to scrape LinkedIn search results.
Output: linkedin_users.csv (or .json / .txt).
File Outputs
CSV: linkedin_users.csv
JSON: scraped_data.json
TXT: linkedin_users.txt

# Notes
API Token: Replace the ACCESS_TOKEN in Script 1 with your token.
Web Scraping: Ensure ChromeDriver is properly set up for Selenium.
