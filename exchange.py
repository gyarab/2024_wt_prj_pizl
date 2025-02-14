import httpx 


print("online prevodnik neceho idk")

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025')

##print(r.text)

in_array = r.text.split("\n")

for line in in_array:
    if "|EUR|" in line:
        print(line)




castka = input("zadej castku v czk: ")

result = int(castka) * 25
print(f"to je v EUR: {result}")
