# Elden Ring lore 


I built this website inspired by Elden Ring game. 
I wrote python script https://github.com/Anivaries/eldenlorecrawler to crawl Elden Ring wikipedia and convert it's content to json which i loaded in database.
Basically split that data into most important names, places, events etc. in the game world and made those as foreign keys for all the small items that can be found
in the game. Those items have names and description for which those names are related to foreign keys and it's description is shown in modal form for each item.

Used PostgreSQL to store all data and it's hosted on Heroku. 

I have plans to expand this project with other FromSoftware games 


https://eldenlore.herokuapp.com/
