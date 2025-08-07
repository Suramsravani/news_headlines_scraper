# Project: News Headlines Scraper
This project is a Python program that automatically visits a news website (like BBC News), looks at the webpage code,
finds the top news headlines, and saves them into a text file on your computer.

How it works:

*   Fetch the webpage: The program uses the requests library to download the HTML content (the webpage code) from the news site.
*   Read the webpage content: It uses BeautifulSoup to read and understand the HTML structure of the page.
*   Find headlines: The program searches for headlines inside specific HTML tags (like h2 heading) These tags usually contain the news headlines.
*   Save headlines: It collects all those headlines and writes them line by line into a file called headlines.txt.


Tools Used:

*   Python programming language: The primary language used for writing the scraper.
*   Requests library: This library facilitates the process of fetching the webpage data, enabling the program to access and retrieve the necessary information from the target website.
*   BeautifulSoup library: This library is instrumental in parsing and extracting specific data, such as headlines, from the HTML structure of the webpage.
*   Text file: The selected method for storing the extracted headlines in an organized, readable format.

Outcome:

*   A straightforward, reusable method for collecting the latest news headlines and saving them in a text file.
*   Acquisition of fundamental programming skills through hands-on experience with web scraping.
