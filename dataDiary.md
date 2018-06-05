# Data Diary: DoJ press releases

Going through the press releases scraped from the DoJ's website. 

## June 5, 2018

I forgot everything I had done before to get the data I'm looking at, so I'm going to start this diary there. 

Sarah and I initially talked about scraping DoJ press releases related to hate crimes (found [here](https://www.justice.gov/crt/press-releases)). But we moved to scraping the general [news website](https://www.justice.gov/news) for press releases to get all of the ones since the Hate Crimes committee started around 2009. 

We split the scraping process in two parts: the urls of the press releases, and the text of the press releases.

I worked using some pseudocode written by Sarah ([scrape_doj_urls.py](https://gist.github.com/sarahcnyt/cd771c5c012e26f9df77821811087458)) to scrape the URLs in the first step.

My scraper is found at `scripts/scrape_doj_url.py` and was first run April 14, 2018.

In scraping the DoJ press releases, we went through 255 pages and have press releases from as far back as January 5, 2009 up until and including April 13, 2018. In the initial scraping we got 14421 press releases. There are three csv files with the urls and I need to figure which one is the correct one to refer to going forward. We have: `out_url_list_withID.csv`,`out_url_list2.csv`, and `out_url_list_original.csv`. I remember adding 
