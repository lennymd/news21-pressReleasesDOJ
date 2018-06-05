# Data Diary: DoJ press releases

Going through the press releases scraped from the DoJ's website. 

## June 5, 2018

I forgot everything I had done before to get the data I'm looking at, so I'm going to start this diary there. 

Sarah and I initially talked about scraping DoJ press releases related to hate crimes (found [here](https://www.justice.gov/crt/press-releases)). But we moved to scraping the general [news website](https://www.justice.gov/news) for press releases to get all of the ones since the Hate Crimes committee started around 2009. 

We split the scraping process in two parts: the urls of the press releases, and the text of the press releases.

I worked using some pseudocode written by Sarah ([scrape_doj_urls.py](https://gist.github.com/sarahcnyt/cd771c5c012e26f9df77821811087458)) to scrape the URLs in the first step.

My scraper is found at `scripts/scrape_doj_url.py` and was last run April 14, 2018.

In scraping the DoJ press releases, we went through 254 pages numbered from 0 to 253 and have press releases from as far back as January 5, 2009 up until and including April 13, 2018.There are three csv files with the urls and I need to figure which one is the correct one to refer to going forward. We have: `out_url_list_withID.csv`,`out_url_list2.csv`, and `out_url_list_original.csv`. I remember adding in an id column to keep track of the press release number because the original ID saved was the position of the press release on the page. We were looking at 50 items per page so the ID kept cycling from 0 to 49. If need be, we can run the script again using the saved index pages.

From the 254 pages we got 12694 press releases. But the csv files have different lengths. Running `wc -l out_url_list*` returned the following line counts.:
* 63 out_url_list2.csv
*	14421 out_url_list_original.csv
* 14421 out_url_list_withID.csv

I need to verify if there are duplicates or missed cases because we do have the added releaseID going from 1 to 12694 but 14421 lines in the out_url_list csv files. It is safe to say that the `out_url_list2.csv` was a code test of some sort and will be deleted once I'm sure of everything.

After I scraped all the urls, I wrote a script that would scrape the text in the same style that we scraped the URLs. That scraper is at `scipts/scrape_pressRelease.py`.

Something different about this scraping was that I create outputs. First, I saved the page the press release was on in case the page online disappeared. Second, I scraped the text from each release into its own text file. Lastly I scraped some metadata associated with the press release into a csv file. The metadata fields were located after the text and are: Topic, Components, and Press Release Number. 

Not everybody filled out the topic field, but the component field had all the groups that the release impacted/was associated with. The Press Release Number was the concatenation of the last two year numbers (18 in the case of 2018, 09 in the case of 2009) with the number of the release in the respective year using a hyphen. the Press Release Number 18-484 corresponds to the 484th press release of 2018. They are not released sequentially and some numbers are skipped, so this could be the identification number in the CMS. 

I ran the script in several takes and generated 7 different `out_pr_list.csv` files that I later combined into the `main_out_pr_list.csv` file. There were 12694 scraped releases but the input file still had 14421 lines according to sublime. 

*Maybe there are some empty lines somewhere in the middle?*
I just checked the `out_url_list_withID.csv` and found no empty lines in the middle. The file has 14421 lines but 12694 press releases. I'm not sure what the other 1727 lines are.

