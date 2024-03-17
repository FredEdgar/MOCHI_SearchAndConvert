# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:19:49 2024

@author: Fred
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import configparser
import convert_mochi

# Charger les saisies précédentes de l'utilisateur à partir du fichier INI
config = configparser.ConfigParser()
config.read('inputs.ini')

# Créer une fenêtre principale
window = tk.Tk()

# Créer une variable pour stocker le chemin du répertoire
path_var = tk.StringVar()
if 'User' in config and 'LastDir' in config['User']:
    path_var.set(config['User']['LastDir'])

# Créer une variable pour stocker le type de fichier sélectionné
file_type_var = tk.StringVar()
file_type_var.set("JSON")  # Valeur par défaut
if 'User' in config and 'FileType' in config['User']:
    file_type_var.set(config['User']['FileType'])


# Définir le titre de la fenêtre
window.title("Mochi researcher and converter")

# Définir la taille de la fenêtre (800x200)
window_width = 800
window_height = 150
window.geometry(f"{window_width}x{window_height}")

# Centrer la fenêtre sur l'écran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Créer une entrée pour afficher le chemin du répertoire
path_entry = tk.Entry(window, textvariable=path_var, width=400)

# Ajouter l'entrée à la fenêtre
path_entry.pack()

# Créer un bouton pour sélectionner un répertoire
def select_directory():
    # Ouvrir une boîte de dialogue pour sélectionner un répertoire
    path = filedialog.askdirectory()
    # Mettre à jour la variable path_var avec le chemin sélectionné
    path_var.set(path)

button = tk.Button(window, text="Select the directory where the .mochi files are located", command=select_directory)
# Ajouter le bouton à la fenêtre
button.pack()

# Créer des boutons radio pour sélectionner le type de fichier
json_button = tk.Radiobutton(window, text="JSON", variable=file_type_var, value="JSON")
csv_button = tk.Radiobutton(window, text="CSV", variable=file_type_var, value="CSV")

# Ajouter les boutons radio à la fenêtre
json_button.pack()
csv_button.pack()

#Créer un bouton pour lancer le traitement
def search_and_convert():
    convert_mochi.analyze_directories_with_mochi_then_convert(path_var, file_type_var, "")
    messagebox.showinfo("Info", "Search and convert terminated")
    
launch_button = tk.Button(window, text="Search and convert", command=search_and_convert)
launch_button.pack()    
    
# Créer un bouton pour enregistrer les saisies de l'utilisateur
def save_entries():
    config['User'] = {'LastDir': path_var.get(), 'FileType': file_type_var.get()}
    with open('inputs.ini', 'w') as configfile:
        config.write(configfile)

save_button = tk.Button(window, text="Save entries", command=save_entries)

# Ajouter le bouton à la fenêtre
save_button.pack()

# Démarrer la boucle principale de l'interface graphique
window.mainloop()