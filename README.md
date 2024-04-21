Sure, here's a README file for your code:

---

# YellowPages UAE Scraper

This script is designed to scrape restaurant data from the YellowPages UAE website and save it to a CSV file. The script collects the restaurant's name, address, city, postal code, phone number, mobile number, business page URL, and logo image URL.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library
- Pandas library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

## Usage

1. Update the `total` variable to the total number of pages you want to scrape. Each page contains multiple restaurant entries.
2. Run the script:

    ```bash
    python yellowpages_scraper.py
    ```

3. The scraped data will be saved in a file named `data.csv`.

## Code Structure

### Functions

- **getName(item: BeautifulSoup)**
    - Extracts the restaurant name from the BeautifulSoup item.
    
- **getAddress(item: BeautifulSoup)**
    - Extracts the restaurant address from the BeautifulSoup item.

- **getPostalCode(item: BeautifulSoup)**
    - Extracts the restaurant postal code from the BeautifulSoup item.

- **getCity(item: BeautifulSoup)**
    - Extracts the restaurant city from the BeautifulSoup item.

- **getPhone(item: BeautifulSoup)**
    - Extracts the restaurant phone number from the BeautifulSoup item.

- **getMobile(item: BeautifulSoup)**
    - Extracts the restaurant mobile number from the BeautifulSoup item.

- **getBusinessPage(item: BeautifulSoup)**
    - Extracts the restaurant business page URL from the BeautifulSoup item.

- **getLogo(item: BeautifulSoup)**
    - Extracts the restaurant logo image URL from the BeautifulSoup item.

### Main Script

1. Iterates through each page of the YellowPages UAE restaurant listings.
2. Sends a GET request to the page URL.
3. Parses the HTML content using BeautifulSoup.
4. Finds all restaurant entries on the page.
5. Extracts the required data using the defined functions.
6. Appends the data to a list.
7. Creates a Pandas DataFrame from the data.
8. Saves the DataFrame to a CSV file named `data.csv`.

## Error Handling

The script includes error handling to manage HTTP errors, bad requests, and other exceptions that may occur during the scraping process.

---
