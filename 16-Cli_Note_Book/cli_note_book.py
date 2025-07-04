import json

NOTE_PATH = "notes.json"

def get_note_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    



print(type(get_note_book(NOTE_PATH)))