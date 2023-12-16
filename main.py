class Note:
    def _init_(self, title, content, creation_date):
        self.title = title
        self.content = content
        self.creation_date = creation_date

import json

class NoteManager:
    def _init_(self, file_path):
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        with open(self.file_path, 'r') as file:
            self.notes = json.load(file)

    def save_notes(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.notes, file)

    def add_note(self, note):
        self.notes.append(note)

    def edit_note(self, note_index, new_title, new_content):
        self.notes[note_index].title = new_title
        self.notes[note_index].content = new_content

    def delete_note(self, note_index):
        del self.notes[note_index]


if __name__ == "__main__":
    file_path = "notes.json"
    manager = NoteManager()
    manager.load_notes()

    note1 = Note("Заголовок 1", "Содержимое 1", "16-12-2023")
    manager.add_note(note1)

    for i, note in enumerate(manager.notes):
        print(f"Заметка {i + 1}: {note.title}")

    manager.edit_note(0, "Новый заголовок", "Новое содержимое")

    manager.delete_note(0)

    manager.save_notes()
