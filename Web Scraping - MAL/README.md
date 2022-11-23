# Web Scraping MyAnimeList
---
This project is all about scraping data from the website of MyAnimeList. The purpose of this project is to get an understanding on how web scraping works by gathering data from a website that I mostly check into. In addition, this is created in preparation for working with the acquired data in other future projects.

### How It's Made
---

| Libraries | Descriptions | 
| --------- | ------------ |
| os | one of the built-in functions in Python. Used for extracting information from the local system. |
| re | one of the built-in functions in Python. Used to perform regex over text data to navigate and locate required data |
| json | one of the built-in functions in Python. Used to store the gathered data from the webpages into a .json format. |
| time | one of the built-in functions in Python. Utilized the .sleep() function to put lag between visits of webpages; avoiding a timeout from the web server. |
| requests | one of the built-in functions in Python. Used to gather the html content of a webpage. |
| BeautifulSoup | a library that is used to navigate a webpage. Paired with *requests* to acquire the html page. |

#### Process
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To obtain anime data from the MyAnimeList website, knowing how the website works and navigating it is a good start. In addition, a general understanding of web scraping is needed such as its general purpose, how to create one, and the legality of the concept as well. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Before delving into the navigation process of MyAnimeList website, I started looking into the concept of web scraping. Web Scraping, from my understanding, is a process where it extracts the html content of a website. It sounds pretty simple yet illegal as it sounds like you're gathering property from another person's or organization's work. Looking into the legality of Web Scraping was my next goal.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As I read through various articles and Reddit posts about Web Scraping, there are two things to note: one is that it is totally fine to scrape data over the internet so long as the data is publicly available, and two, that some websites provide a *robot.txt* file that shows what the website permits when it comes to scraping their data. Knowing these, checking through the website's *robots.txt* file would provide us information on what data is legally available to scrape from their website and the other limitation to take note of would be the difficulty to scrape their website.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now, tackling the idea on how to create one is quite easy given that there are a lot of tutorials about making one. Following through various of them would suffice in understanding the basic concepts of Web Scraping. There are a lot of tools that you can use to create a web scraper; *Selenium* that is created to be used as an automation testing tool for webpages can be used to scrape data, and the combination of *BeautifulSoup* and *requests* from Python libraries is one of the highly used tools to scrape data.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With those in mind, creating the web scraper is pretty simple enough. First thing that I did was to understand how MyAnimeList works. The main homepage isn't as important to gather the anime data that I need but there are other links in there that sends me to a webpage where I can get them. The *Category* webpage shows various available genres that clicking one of them would lead you to a collection of anime pages that correlates with the genre. When looking at one of the webpages, I noticed that there is a GET method in the anime webpage's URL. Modifying the number indicated in the URL led me to another webpage containing another anime. With that, there are two options for me to go through on how to get the anime data: navigating through the *Category* page or modifying the URL and I went with the URL one as it was less tedious compared to navigating through the *Category* page. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Knowing that, I started working on building the web scraper. I divided the work of this project into three sections: creating a connection from my script to the webpages, scraping the information of the html content, and loading the information to a file. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The first thing that I did was to create a connection to the website. This was done using the *requests* library and attaching the URL of the webpage to it. Afterwards, I proceeded with testing out the connection if I was able to gather the webpages' contents using the *BeautifulSoup* library. Took a few tries to actually get into the content of the things that I want to get. The next step was to identify what content should I get based from the webpage's information. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifying the content that I should scrape from the webpage was based on the different headings and sections from the webpage. These features are: Title of the Anime, Rating, no. of people who rated it, the synopsis, and the contents that is under, "Information". I didn't gather the other remaining information from the webpage because I didn't want to end up storing large amounts of data on my potato pc. Probably in the future, I'd be updating the scripts to gather the remaining info from the webpages.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The last step of the scraping script was to create the loading process of the data to a file. Since I don't know any ways to store it on a cloud without the need of paying for the services, I decided to store it on a .json file for ease and familiarity of dealing with such files. Other than saving the file, I created different functions to automate the process of gathering and loading the data by creating checkpoints and backups to the files. 

### Improvements
---

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After running the script for a few months to gather data and modify the codes to implement other things I've learned in the background, there are still features that needs to be added or improved on. 

1. Automating the script to run indefinitely and working with real-time updates of the webpage every season (or whenever there are new reviews or updated the ratings) would be one of the next features to be implemented on this project.
2. Modifying the script to accept data that I wasn't able to gather (due to restricted space and just having a potato pc)

