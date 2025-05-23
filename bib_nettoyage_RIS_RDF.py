import re
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Variables globales pour les statistiques
count_subject_tags = 0
count_abstract_tags = 0
count_kw_lines = 0
count_ab_lines = 0

def remove_text_between_tags(file_path, output_folder):
    global count_subject_tags, count_abstract_tags

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Compter les balises avant suppression
    count_subject_tags += len(re.findall(r'<DC:subject>.*?</dc:subject>', content, flags=re.DOTALL | re.IGNORECASE))
    count_abstract_tags += len(re.findall(r'<dcterms:abstract>.*?</dcterms:abstract>', content, flags=re.DOTALL | re.IGNORECASE))

    # Supprimer les balises
    content = re.sub(r'<DC:subject>.*?</dc:subject>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<dcterms:abstract>.*?</dcterms:abstract>', '', content, flags=re.DOTALL | re.IGNORECASE)

    base = os.path.basename(file_path)
    date_str = datetime.now().strftime("%Y%m%d")
    new_file_path = os.path.join(output_folder, f"{os.path.splitext(base)[0]}_{date_str}.rdf")

    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def remove_lines_from_ris(file_path, output_folder):
    global count_kw_lines, count_ab_lines

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('KW  -'):
            count_kw_lines += 1
            i += 1
            continue
        elif line.startswith('AB  -'):
            count_ab_lines += 1
            i += 1
            while i < len(lines) and not re.match(r'^[A-Z]{2}  -', lines[i]):
                i += 1
            continue
        else:
            filtered_lines.append(line)
            i += 1

    base = os.path.basename(file_path)
    date_str = datetime.now().strftime("%Y%m%d")
    new_file_path = os.path.join(output_folder, f"{os.path.splitext(base)[0]}_{date_str}.ris")

    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)

def process_files():
    output_folder = 'fichiers nettoyes'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir('.'):
        if file_name.endswith('.rdf'):
            remove_text_between_tags(file_name, output_folder)
        elif file_name.endswith('.ris'):
            remove_lines_from_ris(file_name, output_folder)

def on_yes():
    process_files()
    messagebox.showinfo(
        "Terminé",
        f"Le traitement est terminé.\n\n"
        f"Balises supprimées :\n"
        f" - <DC:subject> : {count_subject_tags}\n"
        f" - <dcterms:abstract> : {count_abstract_tags}\n\n"
        f"Lignes supprimées :\n"
        f" - KW  - : {count_kw_lines}\n"
        f" - AB  - : {count_ab_lines}"
    )

def on_close():
    root.destroy()

def create_gui():
    global root
    root = tk.Tk()
    root.title("Nettoyeur de fichiers")

    label = tk.Label(
        root,
        text="Avez-vous placé les fichiers .rdf et .ris\n dans le dossier courant ?",
        font=("Arial", 14, "bold")
    )
    label.pack(pady=20)

    yes_button = tk.Button(root, text="Oui", command=on_yes, font=("Arial", 12))
    yes_button.pack(pady=10)

    close_button = tk.Button(root, text="Quitter", command=on_close, font=("Arial", 12))
    close_button.pack(pady=10)

    root.mainloop()

create_gui()
