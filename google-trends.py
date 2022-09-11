from pytrends.request import TrendReq
from pytrends.dailydata import get_daily_data
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["bitcoin"]
df = get_daily_data('bitcoin',
                 start_year=2015,
                 start_mon=1,
                 stop_year=2022,
                 stop_mon=9,
                 geo='')
df.reset_index(inplace=True)
df.to_csv('daily_bitcoin.csv')
df["date"] = pd.to_datetime(df["date"])
df["week"] = df["date"].dt.isocalendar().week
df["year"] = df["date"].dt.isocalendar().year
df_week = df.groupby(["week","year"]).agg({"bitcoin":sum}).sort_values(['year','week'])
df_week.to_csv('weekly_bitcoin.csv')