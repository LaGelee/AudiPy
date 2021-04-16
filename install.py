import os

def header():
    print("    ___             ___ ____       ")
    print("   /   | __  ______/ (_) __ \__  __")
    print("  / /| |/ / / / __  / / /_/ / / / /")
    print(" / ___ / /_/ / /_/ / / ____/ /_/ / ")
    print("/_/  |_\__,_/\__,_/_/_/    \__, /  ")
    print("                          /____/   ")


header()
reponse = ""
while 1:
    reponse = str(input("Voulez vous installer les modules nécessaires (y/n)? "))
    if reponse == "y" or reponse == "n":
        break

if reponse == "y":
    try:
        os.system('pip install termcolor')
        os.system("pip install colorama")
        os.system("pip install PyAudio")
    except:
        os.system("pip install pipwin")
        os.system("pipwin install pyaudio")
    finally:
        print("[*] Les modules devraient être installer correctement ")
        input("Appuyez sur la touche ENTREE pour continuer...")
else:
    input("Appuyez sur la touche ENTREE pour continuer...")