from datetime import datetime

# Získání aktuálního času
aktualni_cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Zápis do souboru
with open("pokus.txt", "a") as soubor:
    soubor.write(f"{aktualni_cas}\n")

print("Aktuální čas byl zapsán do souboru pokus.txt")
