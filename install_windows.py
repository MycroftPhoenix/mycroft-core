import os
import subprocess
import sys

# Fonction pour exécuter une commande
def run_command(command):
    subprocess.check_call(command, shell=True)

def install():
    # Récupérer le chemin absolu du répertoire du script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Récupérer le chemin absolu du répertoire mycroft-core
    mycroft_dir = os.path.join(script_dir, "..")
    
    # Votre logique d'installation pour Windows
    # Assurez-vous de placer les fichiers dans le répertoire mycroft-core
    
    # Fonction pour installer les dépendances Python à partir du fichier requirements.txt
    run_command('pip install -r requirements/requirementswindows.txt')
    run_command('pip install -r requirements/extra-audiobackend.txt')
    run_command('pip install -r requirements/tests.txt')


    print("Installation de Mycroft sur Windows terminée.")
if __name__ == "__main__":
    install()
