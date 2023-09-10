import tweepy
import datetime
import config

#J'initialise Tweepy avec mes identifiants API Twitter
auth = tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

#Je test la connexion à l'API
try:
    api.verify_credentials()
    print("ok")
except :
    print("erreur de connexion")

# Je défini la date de début de la saison NBA
date_debut_saison = datetime.date(2023, 10, 24)

# Calcule du nombre de jours restants jusqu'à la date de début de la saison
today = datetime.date.today()
jours_restants = (date_debut_saison - today).days

# Création du texte du tweet

if jours_restants <=0 :
    print(f"NBA Season started {-1 * jours_restants} ago ! Have fun this year ! THUNDER UP !! ")
else : 
   print(f"Today is {today}, NBA 2023-2024 Season will start in {jours_restants} days!")

# On poste le tweet
#api.update_status(texte_tweet)

print("Tweet posté avec succès !")