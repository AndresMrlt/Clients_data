import pprint

clients_data = {'Damián': {'Address': 'Viamonte 45', 'Rent': 14500, 'Rental expire date': '30/8/2021', 'Phone number': '15-0000-0000'},
          'Javier': {'Address': 'Avenida Santa Fe 2092', 'Rent': 15500, 'Rental expire date': '31/1/2022', 'Phone number': '15-1111-1111'},
          'Erica': {'Address': 'Monteagudo 403', 'Rent': 8500, 'Rental expire date': '30/11/2020', 'Phone number': '15-2222-2222'}}

def dev_y_act(dictio):
     name = input("Enter the name of a client to see their information (to close the program press Enter): ")
     print("\n")
     while name != '':
         if name in dictio.keys():
             pprint.pprint(dictio[name])
             print("\n")
             name = input("Enter the name of another client to see their information (to close the program press Enter): ")
             print("\n")
         else:
             print("The name you entered is not in the data base. Enter their data below to add it to the system: ")
             address = input("What's the address? ")
             rent = int(input("How much do they pay for rent?: "))
             expDate = input("When does their rental expire?: ")
             phone = input("What's their phone number?: ")
             print("\n")
             dictio[name] = {'Address': address, 'Rent': rent, 'Rental expire date': expDate, 'Phone number': phone}
             print("The new client's data was added to the data base.")
             nombre = input("Enter the name of another client to see their information (to close the program press Enter): ")
             print("\n")
         

dev_y_act(clients_data)
