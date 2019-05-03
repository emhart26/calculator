<<<<<<< HEAD
#


# LALALALALALALA
=======
# we are on the test branch
>>>>>>> test
Active Ingredient Price List(Cents per Gram)
price_per_gram = {
    "fluoxetine": 240,
    "methimazole": 280,
    "pregabalin": 2548,
    "tadalafil": 9113,
    "nifedipine": 300,
    "omeprazole": 100,
    "testosterone": 100,
    "boric acid": 40
}

cost_per_type = {
    'capsule': 0.4,
    'transdermal': 1.75,
    'ointment': 0.6,
    'treat': 1.1,
    'suspension': .02,
    'solution': .02,
    'lozenge': 1.15,
    'suppository': 1.15
}

input_data = {
    'ingredients': [{
        'name': 'pregabalin',
        'amount': 2.324
    }, ],
    'compound_type': [{
        'form': 'capsule',
        'quantity': 28
    }, ]
}

def calc_price(input_data):
    total = 0
for ingredient in input_data['ingredients']:
    ing_cost = float(price_per_gram[ingredient['name']]) * float(ingredient['amount'])
total += ing_cost / 100
for dosage_form in input_data['compound_type']:
    time_cost = float(cost_per_type[dosage_form['form']]) * float(dosage_form['quantity'])
total += time_cost
return total

our_cost = calc_price(input_data) + 10

def final_price():
    if our_cost < 20:
    return 28.97
elif our_cost >= 20 and our_cost < 32:
    return 32.76
else :
    return our_cost

print(round(final_price(), 2))