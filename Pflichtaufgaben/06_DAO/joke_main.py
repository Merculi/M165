from dao_joke import DaoJoke
from joke import Joke


dao_joke = DaoJoke("mongodb://localhost:27017/")

joke = Joke(
    "Warum benutzen Programmierer dunkle Themes? Weil Licht Bugs anzieht.",
    ["programmieren", "it"],
    "Fabio",
)

joke_id = dao_joke.insert(joke)
print(f"Joke gespeichert mit ID: {joke_id}")

it_jokes = dao_joke.get_category("it")

for joke in it_jokes:
    print(joke.text)

dao_joke.delete(joke_id)
