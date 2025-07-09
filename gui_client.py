# Autor: Claudia Leins
# Erstellungsdatum: 2025-07-09
# Beschreibung: 
# GUI-Anwendung für den SmartTaskBot mit CRUD-Funktionalität.
# Ermöglicht das Anzeigen, Hinzufügen, Bearbeiten, 
# Löschen und Markieren von Aufgaben (To-Dos) über eine REST-API.
#-----------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:5000/api/tasks"

class SmartTaskBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartTaskBot")
        
        tk.Label(root, text="SmartTaskBot Aufgabenliste", font=("Arial", 16)).pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=40, font=("Arial", 11))
        self.task_listbox.pack(pady=5)
        self.task_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.task_label = tk.Label(root, text="Neue oder bearbeitete Aufgabe:", font=("Arial", 12))
        self.task_label.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Aufgabe hinzufügen", command=self.add_task)
        self.add_button.pack(pady=2)

        self.edit_button = tk.Button(root, text="Ausgewählte Aufgabe bearbeiten", command=self.edit_task)
        self.edit_button.pack(pady=2)

        self.clear_button = tk.Button(root, text="Auswahl aufheben", command=self.clear_selection)
        self.clear_button.pack(pady=2)

        self.complete_button = tk.Button(root, text="Als erledigt markieren", command=self.complete_task)
        self.complete_button.pack(pady=2)

        self.delete_button = tk.Button(root, text="Löschen", command=self.delete_task)
        self.delete_button.pack(pady=2)

        self.tasks = []
        self.selected_task_id = None
        self.selected_index = None

        self.refresh_tasks()


    def refresh_tasks(self):
        response = requests.get(API_URL)
        if response.status_code == 200:
            self.tasks = response.json()
            self.task_listbox.delete(0, tk.END)
            for task in self.tasks:
                done = "✅" if task["done"] else "❌"
                self.task_listbox.insert(tk.END, f'{task["id"]}: {task["title"]} {done}')
        else:
            messagebox.showerror("Fehler", "Aufgaben konnten nicht geladen werden")

    def add_task(self):
        title = self.entry.get()
        if not title:
            messagebox.showwarning("Hinweis", "Bitte gib einen Titel ein")
            return
        response = requests.post(API_URL, json={"title": title})
        if response.status_code == 201:
            self.entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showerror("Fehler", "Aufgabe konnte nicht hinzugefügt werden")

    def on_select(self, event):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if self.selected_task_id == task["id"]:
                # Auswahl wieder entfernen, wenn dieselbe Aufgabe erneut angeklickt wird
                self.clear_selection()
            else:
                self.selected_task_id = task["id"]
                self.selected_index = index
                self.entry.delete(0, tk.END)
                self.entry.insert(0, task["title"])
                self.add_button.config(state=tk.DISABLED)
        else:
            self.clear_selection()

    def clear_selection(self):
        self.task_listbox.selection_clear(0, tk.END)
        self.entry.delete(0, tk.END)
        self.selected_task_id = None
        self.selected_index = None
        self.add_button.config(state=tk.NORMAL)

    def edit_task(self):
        if self.selected_task_id is None:
            messagebox.showinfo("Hinweis", "Bitte zuerst eine Aufgabe auswählen")
            return
        new_title = self.entry.get()
        if not new_title:
            messagebox.showwarning("Hinweis", "Titel darf nicht leer sein")
            return
        response = requests.put(f"{API_URL}/{self.selected_task_id}", json={"title": new_title})
        if response.status_code == 200:
            self.clear_selection()
            self.refresh_tasks()
        else:
            messagebox.showerror("Fehler", "Bearbeiten fehlgeschlagen")

    def complete_task(self):
        if self.selected_task_id is None:
            messagebox.showinfo("Hinweis", "Bitte zuerst eine Aufgabe auswählen")
            return

       
        response = requests.patch(f"{API_URL}/{self.selected_task_id}", json={"done": True})
        if response.status_code == 200:
            self.refresh_tasks()
        else:
            try:
                error_msg = response.json().get('error', response.text)
            except Exception:
                error_msg = response.text
            messagebox.showerror("Fehler", f"Status konnte nicht aktualisiert werden.\nServerantwort: {error_msg}")


    def delete_task(self):
        if self.selected_task_id is None:
            messagebox.showinfo("Hinweis", "Bitte zuerst eine Aufgabe auswählen")
            return
        response = requests.delete(f"{API_URL}/{self.selected_task_id}")
        if response.status_code == 200:
            self.clear_selection()
            self.refresh_tasks()
        else:
            messagebox.showerror("Fehler", "Löschen fehlgeschlagen")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartTaskBotGUI(root)
    root.mainloop()
