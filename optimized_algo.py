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
                dict['name'], dict['price'], dict['profit'] = row['name'], int(float(row['price'])*100), float(row['price']) * float(row['profit']) / 100
                list.append(dict)
        return list

# Retourner la liste de combinaisons d'actions la plus profitable
def get_best_combination_optimized(invest_amount, list):
    costs, profits = [], []
    stock = len(list)
    best_combination = []
    invest = invest_amount * 100
    for element in list:
        costs.append(element['price'])
        profits.append(element['profit'])
    matrix = [[0 for x in range(invest + 1)] for x in range(len(list) + 1)]
    for stock in range(1, len(list) + 1):
        for amount in range(1, invest + 1):
            if costs[stock-1] <= amount:
                matrix[stock][amount] = max(profits[stock-1] + matrix[stock-1][amount-costs[stock-1]], matrix[stock-1][amount])
            else:
                matrix[stock][amount] = matrix[stock-1][amount]
    while invest >= 0 and stock >= 0:
        if matrix[stock][invest] == matrix[stock-1][invest-costs[stock-1]] + profits[stock-1]:
            best_combination.append(list[stock-1])
            invest -= costs[stock-1]
        stock -= 1
    return best_combination

stocks_list = get_list_from_csv_file('dataset.csv')
best_combinations = get_best_combination_optimized(500, stocks_list)

final_profit, final_cost = [], []
for comb in best_combinations:
    final_profit.append(comb['profit'])
    final_cost.append(comb['price']/100)
    print(comb['name'])
print("cost: " + str(sum(final_cost)) + '\n'
      "profit: " + str(round(sum(final_profit), 2)))
