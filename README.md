# VTU-Result-Scrape-Analysis
Python Project to scrape VTU results off the website and analyze it using matplotlib

# What is this project about?
> In this project I scrape the VTU semester results from the VTU website using the request and bs4(BeautifulSoup) modules. 

>The results are extracted for a group of students using a range of USNs.

> The scraped data is stored in a csv file (res_scrape.csv) wherein each row pertains to the result information of one student.

> Making use of matplotlib module, basic data structures and arithmetic operations I have performed some basic result analysis.

>The result analysis in re_analysis.py is done for one student whose USN is entered by the user. The details of that student are searched and pulled from the csv file and even reports an error message if the record does not exist.

>The user can perform different types of analysis based on the options provided in the main menu

> This project is platform independent and only requires Python 3 and an IDE.

>Additionally for scraping data from the VTU website an active internet connection is required.

>I would also recommend making use of MS-Excel for working with .csv files
 

# Instructions to use
## Steps to follow
* Open vtu_scrape.py and Enter the range of USN (VTU only) whose results you re required to analyse.
* If you wish you can rename the csv file into which the scraped data will be dumped ("res_dump.csv" by default).
* Open re_analysis.py and enter the usn whose result analysis you wish to perform
* Choose any of the options from among the ones in the main menu.
* Choose the Exit option from the menu when you wish to terminate. 
