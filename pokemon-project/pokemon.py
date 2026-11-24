import requests
def get_pokemon(name):
    response=requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status_code==200:
        data=response.json()
        return data
    elif response.status_code==404:
        return None
    return None

def get_types(name):
    data=get_pokemon(name)
    if not data:
        return None
    
    return [entry["type"]["name"] for entry in data["types"]]
     
        
pokemon=get_pokemon("pikachuuuu")
types=get_types('pikachu')
print(types)