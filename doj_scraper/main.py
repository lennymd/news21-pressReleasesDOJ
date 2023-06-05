import time
from pathlib import Path

import scraper

LAST_PAGES_BY_YEAR = {
    2009: 23,
    2010: 25,
    2011: 30,
    2012: 27,
    2013: 26,
    2014: 28,
    2015: 33,
    2016: 30,
    2017: 27,
    2018: 30,
    2019: 27,
    2020: 28,
    2021: 27,
    2022: 29,
    2023: 13,
}


def main():
    # PART 1: Get the pages of press releases by year. Save their HTML to a file.
    for year, last_page in LAST_PAGES_BY_YEAR.items():
        page = last_page
        while page > -1:
            print(f"Getting page {page} for year {year}")
            raw_page = scraper.get_news_page_for_year(year, page)
            scraper.save_news_page_for_year(year, page, raw_page)
            time.sleep(2)
            page -= 1

    # PART 2: Go through news pages and get the metadata for each press release. Save that to a CSV.

    # PART 3: Go through the CSV and download the press releases.

    # PART 4: Go through each press release and get the text. Save text to a txt file and the path to the txt file to a CSV along with metadata.


main()
