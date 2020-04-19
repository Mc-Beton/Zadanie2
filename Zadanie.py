lista = {
    "piekarni": ["chleb", "bułki", "pączek"],
    "warzywniaka": ["marchew", "seler", "rukole", "jabłko"]
}
print("Lista zakupów")
z=0
for a,b in lista.items():
    a=a.capitalize()
    b=[c.capitalize() for c in b]
    print(f"Idę do {a} i kupuję tam następujące rzeczy: {b}.")
    y=len(b)
    print(y)
    z=z+y
print(f"W sumie kupuję {z} produktów.")