import requests
from bs4 import BeautifulSoup

def sestav_statistiku_slov(text):
    """
    Procedura přijme text od uživatele a vrátí seznam slov s počtem výskytů slov v procentech.

    Parametry:
        text (str): Vstupní text od uživatele.

    Návratová hodnota:
        list: Seznam tuple obsahujících slovo a jeho výskyt v procentech.
    """
    # Rozdělení textu na slova
    slova = text.split()

    # Počítání výskytů jednotlivých slov
    pocet_slov = len(slova)
    slovnik_vyskytu = {}
    for slovo in slova:
        slovnik_vyskytu[slovo] = slovnik_vyskytu.get(slovo, 0) + 1

    # Vytvoření seznamu tuple obsahujících slovo a jeho výskyt v procentech
    statistika_slov = [(slovo, (vyskyt / pocet_slov) * 100) for slovo, vyskyt in slovnik_vyskytu.items()]

    print("Statistika slov:")
    for slovo, vyskyt in statistika_slov:
        print(f"{slovo}: {vyskyt:.2f}%")

    return statistika_slov

def vypis_statistiky_textu(text1, text2):
    """
    Procedura přijme dva texty, zavolá proceduru sestav_statistiku_slov pro každý z textů a vypíše informace o jejich shodnosti.

    Parametry:
        text1 (str): První text.
        text2 (str): Druhý text.
    """
    # Získání statistik slov pro oba texty
    statistika_text1 = sestav_statistiku_slov(text1)
    statistika_text2 = sestav_statistiku_slov(text2)

    # Výpočet shodnosti textů
    pocet_shodnych_slov = sum(1 for slovo, _ in statistika_text1 if slovo in [slovo2 for slovo2, _ in statistika_text2])
    shodnost_textu1 = (pocet_shodnych_slov / len(statistika_text1)) * 100
    shodnost_textu2 = (pocet_shodnych_slov / len(statistika_text2)) * 100

    # Výpis informací o shodnosti textů
    print("Informace o shodnosti textů:")
    print(f"Počet shodných slov v textu 1: {pocet_shodnych_slov}")
    print(f"Shodnost textu 1 s textem 2: {shodnost_textu1:.2f}%")
    print(f"Shodnost textu 2 s textem 1: {shodnost_textu2:.2f}%")


def vypis_shodnost_textu(text1, text2):
    """
    Procedura přijme dva texty, zavolá proceduru sestav_statistiku_slov pro každý z textů a vypíše informace o jejich shodnosti.

    Parametry:
        text1 (str): První text.
        text2 (str): Druhý text.
    """
    # Získání statistik slov pro oba texty
    statistika_text1 = sestav_statistiku_slov(text1)
    statistika_text2 = sestav_statistiku_slov(text2)

    # Výpočet shodnosti textů
    pocet_shodnych_slov = sum(1 for slovo, _ in statistika_text1 if slovo in [slovo2 for slovo2, _ in statistika_text2])
    shodnost_textu1 = (pocet_shodnych_slov / len(statistika_text1)) * 100
    shodnost_textu2 = (pocet_shodnych_slov / len(statistika_text2)) * 100

    # Výpis informací o shodnosti textů
    print("Informace o shodnosti textů:")
    print(f"Počet shodných slov v textu 1: {pocet_shodnych_slov}")
    print(f"Shodnost textu 1 s textem 2: {shodnost_textu1:.2f}%")
    print(f"Shodnost textu 2 s textem 1: {shodnost_textu2:.2f}%")

# Příklad použití procedury vypis_shodnost_textu
# text1 = input("Zadejte první text: ")
# text2 = input("Zadejte druhý text: ")

# URL adresa stránky s textem 1
url = "https://cs.wikisource.org/wiki/Havran_(p%C5%99eklad_%C5%A0embera)"

# Získání obsahu stránky
response = requests.get(url)
html_content = response.text

# Analyzování HTML obsahu pomocí BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Hledání konkrétní části stránky s tagem div a třídou entrytext
entry_text_div = soup.find('div', class_='poem')

# Získání textu uvnitř tohoto divu
text1 = entry_text_div.get_text(separator='\n')

if text1:
    print(text1)


# URL adresa stránky s textem 2
url = "https://www.odaha.com/edgar-allan-poe/basne/havran-preklad-jaroslav-vrchlicky"

# Získání obsahu stránky
response = requests.get(url)
html_content = response.text

# Analyzování HTML obsahu pomocí BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Hledání konkrétní části stránky s tagem div a třídou entrytext
entry_text_div = soup.find('div', class_='entrytext')

# Získání textu uvnitř tohoto divu
text2 = entry_text_div.get_text(separator='\n')
    
if text2:
    print(text2)
    
vypis_shodnost_textu(text1, text2)