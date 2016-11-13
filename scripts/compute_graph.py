import sys

COUNTRY_NAME_DIR = "../data/countries.csv"
ROW_DATA_DIR_1 = "../data/dataset1.csv"
ROW_DATA_DIR_2 = "../data/dataset2.csv"
OUTPUT_DIR = "../data/clean_data.csv"

CATEGORIES = ["source_code", "source_name", "source_income", "destination_code", "destination_name", "firm", "firm_type", "total_cost_200", "total_cost_500"]
CATEGORY_NUM = [2, 3, 5, 8, 9, 14, 15, 25, 32]
class Country:

    def __init__(self, country_id):
        self.id = country_id
        self.income_group = ""
        self.links = {}
        self.costs = {}

    #Add links in the form (destination, total_cost_200, total_cost_500)
    def addLink(self, country_to, total_cost_200, total_cost_500):
        if not country_to in self.links:
            self.links[country_to] = []
        self.links[country_to].append((total_cost_200, total_cost_500))

    #Returns the links with the least cost based on the amount to send
    def calculateCost(cost_200, cost_500, amount):
        return (5/300 * cost_500 - 2/300 * cost_200) * amount + (-10/3 * cost_500 + 10/3 * cost_200)

    def getMinLink(self, send_amount, country_dest):
        for country in self.links:
            min_cost = sys.maxsize
            for pair in self.links[country]:
                try:
                    cost_200 = float(pair[0])
                    cost_500 = float(pair[1])
                except ValueError:
                    continue
                min_cost = min(min_cost, Country.calculateCost(cost_200, cost_500, send_amount))
            self.costs[country] = min_cost

def find_index(category):
    return CATEGORY_NUM[CATEGORIES.index(category)]

if __name__=="__main__":
    countries = {}
    with open(COUNTRY_NAME_DIR, 'r') as rin:
        lines = rin.readlines()
        header = lines[2].split(',')
        for i in range(3, len(lines)):
            country_cur = lines[i].split(',')
            countries[country_cur[0]] = Country(country_cur[0])

    with open(ROW_DATA_DIR_1, 'r') as rin:
        with open(OUTPUT_DIR, 'w') as rout:
            lines = rin.readlines()
            header = lines[0].split(',')
            for row in range(1, len(lines)):
                data_split = lines[row].split(',')
                countries[data_split[find_index("source_code")]].addLink(data_split[find_index("destination_code")], data_split[find_index("total_cost_200")], data_split[find_index("total_cost_500")])

    for country in countries:
        for country_dest in countries[country].links:
            countries[country].getMinLink(10000., country_dest)

    for country in countries:
        print(country, end=" ")
        print(countries[country].costs)

