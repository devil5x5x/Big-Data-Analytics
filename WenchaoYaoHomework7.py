#Wencchao Yao Homework 7
import pandas as pd
# Part A

customer = {'name': 'Orwell', 'address':'4 Church St', 'age':'46'}
address = customer['address']
print(address)
customer['birthday'] = '25 June'
customer['name'] = 'Orwell,George'
print(customer)
new_customer = {}
new_customer[1] = customer
new_customer[2] = {'name': 'Cicero', 'address': '11 Carmine St', 'age': '63'}
print(new_customer)

# Part B

phonebook = {
            'Euclid': {'number':'212.479.2851'}
            , 'Pythagoras': {'number':'212.479.4653'}
            , 'Avicenna': {'number':'212.892.1234'}
            , 'Descartes': {'number':'917.372.1650'}
            }
m = 0
for name in phonebook:
    if name == 'Newton':
        number = phonebook.get(name)
        print(number)
    else:
        m += 1
if m == len(phonebook):
    print('Name not found')
    phonebook['Newton'] = {'number':'917.364.1727'}
phonebook['Avicenna'] = {'number':'212.472.1037'}
phonebook.pop('Descartes')

for name in phonebook:
    number = phonebook[name].get('number')
    print(name + number)  
for name, number in phonebook.items():
    if number['number'] == '212.479.4653':
        print(name)

#Part C

new_phonebook = pd.DataFrame(phonebook)
new_phonebook = new_phonebook.transpose()
print(new_phonebook)







