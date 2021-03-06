import urllib.request

from  bs4 import  BeautifulSoup
from pandas import DataFrame

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tags = soup.find_all('div',attrs={"class":"tit3"},)
change = soup.find_all('td',attrs={"class":"range ac"})

result = []
for tag in tags:
    tr_tag = list(tag.strings)
    movie_name=tr_tag[1]
    result.append([movie_name])

number = []
for movie_number in change:
    movie_number = list(movie_number)
    movie_change = movie_number[0]
    number.append([movie_change])

movie_list = []
for i in range(len(result)):
    movie_list.append([i+1]+result[i]+number[i])

movie_table = DataFrame(movie_list, columns=('순위','영화명','변동폭'))
movie_table.to_csv("movie1.csv",encoding='cp949',mode='w',index=False)