import requests
import bs4
import pandas as pd

getpage=requests.get("https://weather.com/en-IN/weather/today/l/28.64,77.34?par=google&temp=c")
getpage.raise_for_status()

soup = bs4.BeautifulSoup(getpage.content,"html.parser")

location=soup.find(class_="CurrentConditions--location--1Ayv3")
curr_time=soup.find(class_="CurrentConditions--timestamp--1SWy5")
curr_cond=soup.select("main#MainContent div.CurrentConditions--primary--3xWnK > span")
curr_desc=soup.select("main#MainContent div.CurrentConditions--primary--3xWnK > div")
aqi_text=soup.find(class_="AirQuality--AirQualityCard--Ipx5M").get_text()
aqi_remark=list(aqi_text)
print(location.get_text() + "\n")
print("Weather Report : " + "Temperature is " + curr_cond[0].text.strip() +  ", Weather is " + curr_desc[0].text.strip() )
print("Air Quality Index (AQI): " + ''.join(aqi_remark[0:3]) )
print( curr_time.get_text() )

print("\n"+"*"*20 + "\n Overall Briefing for Today ")
period=[]
today=soup.find_all(class_="Ellipsis--ellipsis--lfjoB")
for i in range(0,4):
    period.append(today[i].get_text())

temp=[]
morning=soup.select('main#MainContent div:nth-child(2) > section > div > ul > li:nth-child(1) > a > div.Column--temp--2v_go > span')
afternoon=soup.select('main#MainContent div:nth-child(2) > section > div > ul > li:nth-child(2) > a > div.Column--temp--2v_go > span')
evening=soup.select('main#MainContent div:nth-child(2) > section > div > ul > li.Column--column--2bRa6.Column--active--FeXwd > a > div.Column--temp--2v_go > span')
night=soup.select('main#MainContent div:nth-child(2) > section > div > ul > li:nth-child(4) > a > div.Column--temp--2v_go > span')
temp.append(morning[0].text.strip())
temp.append(afternoon[0].text.strip())
temp.append(evening[0].text.strip())
temp.append(night[0].text.strip())

weather_chart=pd.DataFrame({"DAY PERIOD ":period,"TEMPERATURE":temp})
print(weather_chart)
