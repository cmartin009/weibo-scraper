# weibo-scrapper for Windows
A Web scrapper specially designed for scrapping content returned by specific search term(s) on Weibo, in real-time.
 #### Dependencies
1. Selenium
2. PyMySQL
3. PhantomJS (optional) or ChromeDriver(Support for Phantom Js is obselete)
4. python-crontab (optional) for Linux or Mac and Task Scheduler for Windows

PhantomJS is an executable. Download link: (http://phantomjs.org/download.html)

Chromedriver is also an executable. Download link: (https://chromedriver.chromium.org/downloads)
It is already downloaded here for you 

 ## The Scrapper
 * No sign-in to Weibo is required.
* Scrape full content by expanding long posts that have been clipped by JavaScript.
* Parallel scraping with multi-threading.
* Designed to scrape content that contains TEXT ONLY. To scrape content that includes external links and media, remove or modify the filters under `scrape()` in `web_scraping.py`.
* Designed to use with a MySQL database.
* Designed to save only the meta-data that are useful for censorship verification purposes. To include additional meta-data, define selectors in `variables/element_selector.py`.
 #### How it works
1. Visits the target page with search term(s) of your choice. (http://s.weibo.com/weibo/YOUR_SEARCH_TERM_HERE&Refer=STopic_box)
2. Expand collapsible content.
3. Scrape all posts on target page.
4. Filter and save posts to database.
5. Repeat step 1 to 4 at time interval as defined in a cron job (optional).
 #### To run:
`python web_scraping.py [SEARCH TERM] [MYSQL TABLE NAME]` i.e python web_scraping.py 冠状病毒 武汉肺炎 武汉封城 weibo_tweets

 Multiple search terms are supported. Just make sure the last argument is the table name.
Beware of CAPTCHA if too many page requests are submitted at the same time.

### Scheduled Task for Windows OS
Good tutorial: https://datatofish.com/python-script-windows-scheduler/

1. Make sure your script works and all dependicies are in place for Windows 
2. Create .Bat script that will automatically run script from CMD (There is a sample .Bat file in repot that works web_scrape.bat)
3. Go to search bar and search for task scheduler and from there instructions are pretty straight forward
4. Filter and save posts to database.
5. I run my script for 12 hrs over night and in 15 minute intervals(Admin privaleges are required)
