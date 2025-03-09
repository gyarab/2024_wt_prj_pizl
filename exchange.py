import httpx

def ziskej_kurz():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/denni_kurz.txt"
    try:
        response = httpx.get(url)
        
        if response.status_code != 200:
            return None
        
        data = response.text.split("\n")
        
        for radek in data:
            if "|EUR|" in radek:
                casti = radek.split("|")
                if len(casti) >= 5:
                    kurz = casti[-1].replace(",", ".")
                    return float(kurz)
        
        return None
    except Exception:
        return None

def prepocitej_castku(castka, kurz, smer):
    if smer == "CZK->EUR":
        return castka / kurz, "EUR"
    else:
        return castka * kurz, "CZK"

def ziskej_vstup(text, moznosti=None):
    while True:
        vstup = input(text).strip()
        if moznosti and vstup not in moznosti:
            print("Neplatná volba, zkuste znovu.")
        else:
            return vstup

def main():
    kurz = ziskej_kurz()
    if kurz is None:
        return
    print(f"Aktuální kurz EUR/CZK: {kurz:.2f}")
    
    smer = ziskej_vstup("Vyberte převod (1 = CZK na EUR, 2 = EUR na CZK): ", ["1", "2"])
    
    if smer == "1":
        mena = "CZK"
        smer_text = "CZK->EUR"
    else:
        mena = "EUR"
        smer_text = "EUR->CZK"
    
    while True:
        try:
            castka = float(input(f"Zadejte částku v {mena}: "))
            break
        except ValueError:
            print("Neplatná hodnota, zkuste znovu.")
    
    vysledek, cilova_mena = prepocitej_castku(castka, kurz, smer_text)
    print(f"Výsledek: {vysledek:.2f} {cilova_mena}")

if __name__ == "__main__":
    main()
