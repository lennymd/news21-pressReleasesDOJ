# Scrape DOJ Press releases to identify hate crime cases.

## 2018 Strategy

In 2018, the strategy was loosely to:

1. Scrape all the pages of the press release site, saving the HTML for each page listing press releases.
2. Go through these saved HTML files and scrape the info for each press release on the page.
3. Go through each press release page and scrape the info for each press release.

We did this to keep a backup of the pages the press releases were linked to in case they changed or were removed at a later date.

## 2023 Refactor Strategy

I want to follow the same idea, but I want to avoid having to scrape the same press releases over and over. One way I see of doing this is to scrape by year, and then scrape the press releases for each year. This way, we can keep a record of the press releases for each year, and we can scrape the press releases for each year as needed.
