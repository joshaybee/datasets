import csv
import io
import os
import time
import markovify
import tweepy
import private

# Twitter Markov Bot


# read the CSV in
def generate_fortune_cookie():
    fortunes = []
    path = os.path.join('data', 'fortunecookies.csv')
    with io.open(path, "rt", encoding='utf-8') as f:

        reader = csv.reader(f)
        for row in reader:
            fortunes.append(row)
    fortunes = fortunes[1:]  # remove header
    fortunes = [item for sublist in fortunes for item in sublist]  # flatten
    fortunes_string = (" ").join(str(x) for x in fortunes)  # convert to string
    text_model = markovify.Text(fortunes_string)  # Build the model.

    fortune = text_model.make_short_sentence(120)

    hashtag = ' #fortunecookie'

    tweet = fortune + hashtag
    print(tweet)
    return tweet


def send_to_twitter(tweet):
    auth = tweepy.OAuthHandler(private.CONSUMER_KEY,
                               private.CONSUMER_SECRET)  # (CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(private.ACCESS_TOKEN,
                          private.ACCESS_SECRET)  # (ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api.update_status(tweet)
