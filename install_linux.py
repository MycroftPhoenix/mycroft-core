import os
import shutil

def install():
    # Récupérer le chemin absolu du répertoire du script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Récupérer le chemin absolu du répertoire mycroft-core
    mycroft_dir = os.path.join(script_dir, "..")
    
    # Votre logique d'installation pour Linux
    # Assurez-vous de placer les fichiers dans le répertoire mycroft-core
    
    print("Installation de Mycroft sur Linux terminée.")

if __name__ == "__main__":
    install_linux()
