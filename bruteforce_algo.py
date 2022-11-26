
import itertools
import csv

# Retourner une liste de dictionnaires à partir de la lecture d'un fichier csv
def get_list_from_csv_file(file):
    with open(file) as f:
        list = []
        reader = csv.DictReader(f)
        for row in reader:
            if float(row['price']) <= 0:
                pass
            else:
                dict = {}
                dict['name'], dict['price'], dict['profit'] = row['name'], int(float(row['price'])), float(row['price']) * float(row['profit']) / 100
                list.append(dict)
        return list

# Retourner le coût d'une combinaison donnée (somme des prix de toutes les actions de la combinaison)
def get_cost_for_a_combination(combination):
    costs = []
    for element in combination:
        costs.append(element['price'])
    return sum(costs)

# Retourner le profit d'une combinaison donnée (somme des profits de toutes les actions de la combinaison)
def get_profit_for_a_combination(combination):
    profits = []
    for element in combination:
        profits.append(float(element['price']) * float(element['profit']/100))
    return sum(profits)

# Retourner la combinaison d'actions la plus profitable après avoir itéré sur l'ensemble des combinaisons
def get_best_combination(list):
    best_combination = ""
    profit = 0
    for element in range(len(list)):
        for combination in itertools.combinations(list, element):
            combination_cost = get_cost_for_a_combination(combination)
            if combination_cost <= 500:
                combination_profit = get_profit_for_a_combination(combination)
                if combination_profit > profit:
                    profit = combination_profit
                    best_combination = combination
    return best_combination

stocks_list = get_list_from_csv_file('test.csv')
best_combinations = get_best_combination(stocks_list)
