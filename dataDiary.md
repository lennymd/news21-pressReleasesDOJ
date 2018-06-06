# Data Diary: DoJ press releases

Going through the press releases scraped from the DoJ's website. I'm doing this to understand who has been prosecuting hate crimes in the DoJ and who has been prosecuted for committing hate crimes. I hope to get names of prosecutors, information about cases, districts where prosecutions have happened, information about the people prosecuted for hate crimes, the frequency of hate crime laws that have been prosecuted over the years. 

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

Moving on to the scraped press releases, there is the metadata I talked about earlier that is in a csv file. The titles for the press releases are stored in the original url list scraped in the first part of the process and the text of the press releases are stored in the individual text files. I need to update the ID column of the url list because that one starts with 1 and in every other reference we start with 0. This ID is meant to be the unique identifier for the releases over the different files. 

Looking at the scraper for the press releases, I also notice that the input file is a variation of the `out_url_list_withID.csv` file which makes me understand better what all the files mean.

To summarize:
`scrape_url/out_url_list2.csv`: irrelevant. will be deleted.
`scrape_url/out_url_list_original.csv`: a clean copy of the URL list without added columns or headers. output of the `scrape_doj_url.py` file with added `_original` ending.
`scrape_url/out_url_list_withID.csv`: version of URL list with added ID column and headers.
`scrape_pressRelease/out_url_list_withID.csv`: a copy of `scrape_url/out_url_list_withID.csv`. not necessary in this folder. Will be deleted.
`scrape_pressRelease/out_url_list_withoutHeader.csv`:used as input for the `scrape_pressRelease.py` file. A copy of `scrape_pressRelease/out_url_list_withID.csv` but without the header line because I didn't know how to really deal with it before (I'm sure I can do it better now.). May get deleted if I fix up the scripts before publishing.
`scrape_pressRelease/out_pr_list.csv`: empty file. will get deleted.
`scrape_pressRelease/out_pr_list1.csv`: contains the metadata for the press releases numbered 0 to 998 inclusive.
`scrape_pressRelease/out_pr_list2.csv`: contains the metadata for the press releases numbered 999 to 2000 inclusive.
`scrape_pressRelease/out_pr_list3.csv`: contains the metadata for the press releases numbered 2001 to 7350 inclusive.
`scrape_pressRelease/out_pr_list4.csv`: contains the metadata for the press releases numbered 7351 to 7979 inclusive.
`scrape_pressRelease/out_pr_list5.csv`: contains the metadata for the press releases numbered 7980 to 9999 inclusive.
`scrape_pressRelease/out_pr_list6.csv`: contains the metadata for the press releases numbered 8300 to 9999 inclusive.
`scrape_pressRelease/out_pr_list7.csv`: contains the metadata for the press releases numbered 10000 to 12693 inclusive.


STOP. That overlap between `out_pr_list5.csv` and `out_pr_list6.csv` bothers me. I checked with the `main_our_pr_list.csv` file and there doesn't seem to be a duplicate anywhere in that range. Back to the files:

`scrape_pressRelease/main_out_pr_list.csv`: contains all the metadata for the press releases numbered 0 to 12693 inclusive. It was a compilation of the numbered `out_pr_list.csv` files. 

The other files are: 
* `scrape_url/indexPages/` which contains a saved copy of each page of press releases that we scraped.
* `scrape_pressRelease/pressReleases/` which contains a saved copy of each web version of the press release.

The above two files are meant for emergencies (if no internet or we want to scrape more or they take down the press release).

* `scrape_pressRelease/pressReleases_txt/` contains all the body text for each press release.  Sometimes a None was appended to the end of the file when there was an extra return or paragraph tag in the html. Still haven't figured out how to delete them, but I don't think I have to worry too much about that for now.


## June 06, 2018

After I had scraped the text from the press releases, I uploaded them to [overviewdocs](https://www.overviewdocs.com/) and today am beginning work on tagging and sifting through them. My goal is to get all the press releases related to hate and bias-motivated crimes so that I can then extract the people involved in them (victims, perpetrators, and prosecutors).

The first thing I tried was the Entities view which went through all 12694 press releases and identified entities, how often they appeared (counts) and in how many docs they appeared (docs). I used the default settings which searched for Companies, Cities, Countries, Political Boundaries, Numbers and then removed English: Google Book words, and Numbers.  This wasn't that helpful becaused I have to go through the entity list and exclude all the other things I don't care about to try and get the entities that look like names. 

Next thing I tried was to search for "hate crimes" (without quotes) throughout the press releases. I got 125 press releases that had that phrase in them. Now I'm going through each one and checking if it fits into one of the following categories: 
indictment, guilty plea, sentencing, conviction, or charge to try and get a breakdown of what each release is talking about. 

To identify the guilty pleas I used the search terms "pleaded guilty","guilty" on the set of press releases in the "hate crime" group I had previously found. 39 of the 125 press releases are about guilty pleas.

To identify releases related to sentencing, I used the search term "sentenced" on the group of 125 press releases related to hate crimes. 32 of the 125 press releases are about sentencings.

To identify releases related to indictments, I used the search terms "indicted" and "indictment" on the group of 125 releases. 26 of the 125 press releases are about indictments.

I created a new category of "arrest" types since some releases had to do with arrests. After I finish tagging the 125 releases, I'll go through USAO's [Justice 101](https://www.justice.gov/usao/justice-101) to make sure the categories are tagged properly. 

After a quick break I decided to cycle through the entire corpus of releases and tag/review the tags. At the end I have the following set of tags oof the 125 releases:

* arrest: 2 releases dealt with arrests.
* case: 1 release was about the initial court appearance of John W. Ng of Albuquerque, N.M.
* civil rights division: 1 release was about the Civil Rights Division's work in 2013.
* unc chapel hill: 1 release was a statement about chapel Hill
* zimmerman: 1 release was an announcement by the Justice Department regarding the insufficient evidence to pursue federal civil rights charges against George Zimmerman.
* meeting: 1 release was about A.G. Lynch's first official visit to North Carolina for a meeting with civil rights leaders and individals combatting human trafficking.
* lynch: 1 release that relates to the same event describe in the "meeting" tag. 
* church fires: 1 release was a statement from Melanie Newman regarding church fires currently under investigation.
* restitution: 1 release was about a restitution order of 840,000 dollars by US District Judge Carlton Reeves of the Southern District of Mississippi.
* resignation: 1 release was US Attorney Benjaming Wagner's resignation. 
* hate crime statistics: 1 release was about the release of the 2015 hate crime statistics
* charged: 6 releases were about individuals and groups being charged
* conviction: 10 releases were about convictions of committing federal hate crimes. 
* guilty plea: 39 releases were about guilty pleas to different federal hate crime 
* indictment: 26 releases were about individuals and groups being indicted.
* sentencing: 32 releases were about sentencings.


After searching for all releases with "hate crime" in the release, I went through and looked for other terms. Phrases I used that returned releases to add to the corpus were: "bias motivated", "Matthew Shepard and James Byrd", "racially motivated".

In going through the tagging with the term "racially motivated", `pressReleases_txt/release_02561.txt` is interesting because it talks about a case that has ended up as a guilty plea and is not listed as a hate crime but has the racial motivation. Need to check with Sarah if this counts for what we're tagging. **Do we count racially motivated crimes as part of the hate crimes? I'm asking this because hate crimes are under the broader umbrella of civil rights crimes.** 

 "gender identity", "religiously motivated"

I tried searching with the phrases "sexual identity", "sexual identity motivated", "religion motivated", "sexual orientation motivated", "bias incident", "hate incident", "bias crime", "bias motivated incident".

