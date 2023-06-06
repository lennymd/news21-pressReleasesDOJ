# import csv
# import urllib.parse as parse
from pathlib import Path

# import lxml
import requests

# from time import sleep


# from bs4 import BeautifulSoup

NEWS_URL = "https://www.justice.gov/news"
STORAGE_DIR = Path.cwd() / "storage"


def get_news_page_for_year(year: int, page: int):
    """Get the HTML for a page of press releases for a given year."""
    payload = {
        "items_per_page": 50,
        "f[0]": "type:press_release",
        "f[1]": f"field_pr_date:{str(year)}",
        "page": str(page),
    }
    response = requests.get(NEWS_URL, params=payload, timeout=10)
    return response.text


def save_news_page_for_year(year: int, page: int, raw_page: str):
    """Save the HTML for a page of press releases for a given year."""
    file_path = STORAGE_DIR / "news_pages" / f"{year}" / f"{year}_{page}.html"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch(exist_ok=True)
    with file_path.resolve().open("w") as f:
        f.write(raw_page)


# TODO check if file already has been downloaded before saving it.


# def get_news_pages_for_year(year: int, last_page: int):
#     payload = {
#         "items_per_page": 50,
#         "f[0]": "type:press_release",
#         "f[1]": f"field_pr_date:{str(year)}",
#         "page": "0",
#     }
#     page = last_page
#     while page > -1:
#         payload["page"] = str(page)
#         response = requests.get(NEWS_URL, params=payload, timeout=10)
#         print(response.url)
#         page -= 1


# for i in range(0, 254):
#     outfile = "indexPages/index_%03d.html" % i
#     path_to_outfile = Path(outfile)

#     if path_to_outfile.is_file():
#         print("We have gone through " + outfile + " already.")
#         pass

#     else:
#         # cycle through the different pages
#         payload["page"] = str(i)

#         # get the index page.
#         response = requests.get(baseurl, params=payload)
#         # print(response.url)
#         a = response.text
#         # Code was throwing an error (UnicodeEncodeError: 'ascii' codec can't encode character '\xf1' in position 5209: ordinal not in range(128))
#         # I fixed that error with: https://stackoverflow.com/questions/41663506/python-post-request-throws-unicodeencodeerror-ascii-codec-cant-encode-charac
#         a = a.encode("ascii", "ignore").decode("utf-8")

#         # get rid of html encoding.
#         a = parse.unquote(a)

#         # keep a copy of the page.
#         out = open(outfile, "w")
#         out.write(a)
#         out.close()
#         # print("page \'" + outfile +"\' has been saved for later")

#         try:
#             # create the bs4 object
#             page_of_interest = BeautifulSoup(a, "lxml")

#             # All the title divs
#             titles = page_of_interest.find_all(
#                 "div", class_="views-field views-field-title"
#             )
#             # print(len(titles))
#             # print(str(len(titles))+" titles have been found in " + outfile)
#             for t in range(0, len(titles)):
#                 title = titles[t]
#                 turl = title.find("a").attrs["href"]
#                 tstring = title.find("a").string
#                 tdate = (
#                     title.find_previous("h3")
#                     .find("span", class_="date-display-single")
#                     .attrs["content"]
#                 )
#                 out_url_list.append([t, str(tstring), str(turl), str(tdate)])
#                 # print(str(t+1) + " title(s) processed")
#                 # sleep(0.5)
#         except Exception as e:
#             print(e)
#         print("Finished going through '" + outfile + "'")
#         sleep(3)

# with open("out_url_list.csv", "r+") as my_csv:
#     csvWriter = csv.writer(my_csv, delimiter=",")
#     csvWriter.writerows(out_url_list)
