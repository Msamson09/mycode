#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



for farm in farms[0]["agriculture"]:
    print(farm)


farm_name = input("Which farm would you like to take a look at?\n")

for farm in farms:
    if farm_name in farm["name"]:
        print(f"{farm['agriculture']}")

for farm in farms:
    if farm_name in farm["name"]:
       if  
