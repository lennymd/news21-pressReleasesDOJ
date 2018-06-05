'''
 Good tutorial on bs4 for WH press briefings - similar to what we are doing
 http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/
 I'm using lxml, but using bs4 with 'lxml' option is pretty much the same.
 
 this is just pseudo-code. It won't work as is. 

'''

#from bs4 import BeautifulSoup
from lxml import etree
import requests
import urllib.parse.unquote as unquote


#parameters to start up the query. 

baseurl = "https://www.justice.gov/news"
payload = {"items_per_page":50,
          "f[0]":"type:press_release",
          "page": "0"}


parser = etree.HTMLParser(remove_blank_text=True)
out_url_list = []


for i in range(0, 253):
    
    # create a file name to save the index page.
    outfile = "doj_index/page_%03d.html" % i
    
    ''' In a real program, you'd check to see 
        if you have already downloaded it, so 
        you don't go back to the site again.
    '''
    
    payload["page"]=str(i)
    
    #get the index page.
    r = requests.get(baseurl, params=payload)
    html = r.text
    #get rid of html encoding.
    html = unquote(html)
      
    #keep a copy of the page.
    out = open(outfile, 'w')
    out.write(html)
    out.close()
  
    try:
        etree.fromstring(html, parser)
        
        ''' This creates a tree for the html. You need to search the tree
            for all of the items you want. 
            The easiest way in my view was to look for the titles of the press releases,
            then look up to find the date, and down to find the url. 
        
            I use xpath, which I find easier to test with chrome scraper.
                    
           //div[@class="views-field views-field-title"] for the title
           
           if that is selected, then 
           ./preceding::h3/span/@content is the date it UTM format.
           .//a/@href  is the relative url to the actual press release.
        
           basic idea of lxml xpath is this: 
            
          titles = tree.xpath('//div[@class="views-field views-field-title"]')
          (xpath always returns a list, even when it doesn't make sense. This time it does.)
        
          for t in titles:
              get the text of all children to get the title, then strip it of extra characters.
                    
              tstring = t.xpath("string()")  -- this turns all children into one string. I'm not sure if it's a list.
              
              The date is UTM format in an attribute called @content in the preceding h3 
              tdate = t.xpath( ./preceding::h3/span/@content")[0]
                       
              turl = the_title.xpath('.//a/@href')[0]
              
              Now add it to a list of urls you want to download.
              out_url_list.append([i, tstring, turl, tdate])
    
      
      '''
            
    except:
        pass
        # or write out the error then pass.
  
  
 #Consider importing time and then putting a random sleep or 1 second sleep here to make sure it doesn't go too fast.
   
 