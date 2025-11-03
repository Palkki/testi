
while True:
    try:
          Morjes = int(input("Anna kokonaisluku: "))
    except ValueError:
         print(f"Tuo ei näytä kokonaisluvulta!\n")
    else:
         print(f"Annoit luvun {Morjes}")
         break

