import httpx

def get_exchange_rate():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
    response = httpx.get(url)
    
    lines = response.text.split("\n")
    for line in lines:
        if "|EUR|" in line:
            return float(line.split("|")[-1].replace(",", "."))
    
    raise ValueError("Nepodařilo se načíst kurz EUR.")

def convert_currency(amount, rate, mode):
    if mode == "CZ":
        return amount / rate 
    elif mode == "EUR":
        return amount * rate  
    else:
        raise ValueError("Neplatný režim převodu.")

def main():
    try:
        rate = get_exchange_rate()
        print(f"Aktuální kurz EUR/CZK: {rate}")
        
        while True:
            mode = input("Zadej režim převodu (CZ pro CZK->EUR, EUR pro EUR->CZK, Q pro konec): ").strip().upper()
            if mode == "Q":
                break
            
            if mode not in ["CZ", "EUR"]:
                print("Neplatný režim. Zadej CZ nebo EUR.")
                continue
            
            try:
                amount = float(input("Zadej částku: ").replace(",", "."))
                converted = convert_currency(amount, rate, mode)
                print(f"Převedená částka: {converted:.2f} {'EUR' if mode == 'CZ' else 'CZK'}")
            except ValueError:
                print("Neplatná částka. Zkus to znovu.")
    
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    main()