

from apiclient.discovery import build
from apiclient.errors import HttpError
import tweepy
import datetime

CK="APIkey"
CS="APIkeysecret"
AT="Accesstoken"
AS="Accesstokensecret"

DEVELOPER_KEY = 'youtubeAPI'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

wd = datetime.date.today().weekday()

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY
    )

a = youtube.videos().list(
  part='id,snippet',
  chart='mostPopular',
  maxResults=wd+1,
  regionCode="JP",
).execute()

a

for sr in a.get("items", []):
  A="http://www.youtube.com/watch?v="+sr['id']
  #print(sr['snippet']['title'])
  #print(sr['snippet']['publishedAt'])
  #print(A)

api.update_status("本日の急上昇"+str(wd+1)+"番目の動画\n"+A)