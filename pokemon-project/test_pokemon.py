from pokemon import get_pokemon,get_types
import pytest 
@pytest.mark.parametrize(
        "name,expected",
        [
            ("pikachu",["electric"]),
            ("bulbasaur",["grass","poison"]),
            ("charmander",["fire"]),
            ("squirtle", ["water"]),
            ("gengar", ["ghost", "poison"])
            
        ]
)
def test_get_types(name,expected):
    assert get_types(name)==expected

def test_get_pokemon():
    pokemon=get_pokemon('pikachu')
    assert pokemon is not None
    assert pokemon['name']=='pikachu'



def test_invalid_pokemon():
    pokemon=get_pokemon('jhbfhe')
    assert pokemon is None
