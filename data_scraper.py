import urllib
from BeautifulSoup import *
import pandas as pd
import time


url = 'http://prnews.mn/nomination/100'   #url to be scraped

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
main = soup('div',{"class":"main container"})
sources = main[0].findAll('span',{"class":"link-nomin"})
likes = main[0].findAll('a',{"class":"vote-plus"})
dislikes = main[0].findAll('a',{"class":"vote-minus"})

data = []
#for each profile, scrape the number of likes, dislikes and the image url with the profile
for source,like,dislike in zip(sources,likes,dislikes):
	temp_dic = {}
	temp_dic["link"]=source.findAll('img')[0]["src"]
	temp_dic["like"]=int(like.findAll('span')[0].text)
	temp_dic["dislike"]=int(dislike.findAll('span')[0].text)
	data.append(temp_dic)


data_df = pd.DataFrame(data)
file_name = "data.csv"    #file name
data_df.to_csv(file_name, index=False)
