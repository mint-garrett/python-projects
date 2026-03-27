#poke api use
### simplified pokedex. imput pokemon's name, and you will get the nat dex#, color, types, and the first english pokedex description

##imports
import requests
import time


#setting up blank string for pokemon name
name = ""
pokemon = input(name)


## notification if there is wifi
try:
    info = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")

except:
    print("There is no wifi Garrett....")
    

time.sleep(.5)  
print("Pokemon Info Loading....")
json_info = info.json()
time.sleep(2)

#color of pokemon
color = (json_info["color"]["name"])
#national dex #
id_number = json_info.get("id")

#types
type_info = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
type_json_info = type_info.json()
type_list = type_json_info["types"]
type1 = type_list[0]["type"]["name"]
if len(type_list) > 1:
    type2 = type_json_info["types"][1]["type"]["name"]
else:
    type2= "None"


#previous evolution
pre_evo = json_info.get("evolves_from_species")
if pre_evo == None:
    previous_mon = "This is a basic Pokemon!"
else:
    previous_mon = pre_evo["name"]

## trying to find english description
flavor_entries = json_info.get("flavor_text_entries", [])
english_entries = [
    entry1["flavor_text"]
    for entry1 in flavor_entries
    if entry1["language"]["name"] == "en"
]

if english_entries:
    general_flavor = english_entries[0]
else:
    general_flavor = "No English Pokedex entry"

##basic info
print(f"{pokemon}, national dex number {id_number}, is {color}.")

##types
print(f"{pokemon} is a {type1} type and {type2} type")

##evolution
print(f"{pokemon} evolves from: {previous_mon}")
print("---------------")

##dex info
print(f"A pokedex entry: {general_flavor}")

print("---------------")


