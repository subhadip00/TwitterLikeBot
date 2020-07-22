import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("7r9iZrJU27hZzjiE6KLz2YNZm", 
    "8nWfFeTGrXLApObXmPzlKIG09RhqFpzGsUDSTkDpRRvk1YwNU7")
auth.set_access_token("868720664915492865-5MAPecqUKwmDgTz8trE4AZrnFobOR34", 
    "ExtVFgyLev8zyIVykyXBDDB4M0s1F89rIrDMqLGfC4sEq")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(tweet.id,tweet.author.name)
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)