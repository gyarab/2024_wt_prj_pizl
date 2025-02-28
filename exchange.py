import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025"
r = httpx.get(url)

# print(r.text)

lines = r.text.split("\n")

row = ""
for line in lines:
    if "|EUR|" in line:
        row = line
        
# print(row)

row_arr = row.split("|")

kurz_str = row_arr[-1]
kurz_str = kurz_str.replace(",", ".")

kurz = float(kurz_str)
# print(kurz)

while(1):
    mode = input("Zadej mód převodu: 1 = CZK na EUR, 2 = EUR na CZK\n")
    
    if mode == '1':
        currency = "CZK"
        break
    
    elif mode == '2':
        currency = "EUR"
        break
    else:
        print("Nepovolená hodnota, prosím zadejte jinou.")
        mode = 0
        

while(1):
    value_str = input("Zadej hodnotu " + currency + " pro převedení: \n")
    
    try:
        value = float(value_str)
        break
    except:
        print("Nepovolená hodnota, prosím zadejte jinou.")
        value = 0    


while(1):
           
    
    if mode == '1':
        result = value / kurz
        print(f"Výsledek je {result} EUR")
        break
    elif mode == '2':
        result = value * kurz
        print(f"Výsledek je {result} CZK")
        break
    else:
        print("Nepovolená hodnota, prosím zadejte jinou.")
        value = 0
        break