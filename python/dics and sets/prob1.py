hindi_to_english = {
    "pustak": "Book",
    "seb": "Apple",
    "kutta": "Dog",
    "billi": "Cat",
    "pani": "Water",
    "aag": "Fire",
    "ghar": "House",
    "school": "School",
    "dost": "Friend",
    "suraj": "Sun"
}


value = input("Enter the value you want to translate it !")

transletedValue = hindi_to_english.get(value)

if(transletedValue):
    print(transletedValue)
else:
    print(f"not found the translation of {value}")