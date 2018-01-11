import urllib.request
import csv
from bs4 import BeautifulSoup
from pandas import DataFrame
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# print(soup.prettify())

tags = soup.findAll('div', attrs={'class':'tit3'})
tags_range = soup.findAll('td', attrs={'class':'range ac'})

# print(tags)
# print(tags_range)
# print(tags_sum)

result = []
if(tags):
    for tags_list in tags:
        list = tags_list.text
        movie_name = list
        result.append([1]+[movie_name]+[2])

# print(ranking)

movie_table = DataFrame(result, columns = ('순위','영화명','변동폭'))
movie_table.to_csv("movie.csv",encoding="cp949",mode='w',index=False)

print("End")