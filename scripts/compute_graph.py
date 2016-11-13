import sys
import numpy as np
COUNTRY_NAME_DIR = "data/countries.csv"
ROW_DATA_DIR_1 = "data/dataset1.csv"
ROW_DATA_DIR_2 = "data/dataset2.csv"
OUTPUT_DIR = "data/clean_data.csv"

CATEGORIES = ["source_code", "source_name", "source_income", "destination_code", "destination_name", "firm", "firm_type", "total_cost_200", "total_cost_500"]
CATEGORY_NUM = [2, 3, 5, 8, 9, 14, 15, 25, 32]
class Country:

    def __init__(self, country_id, country_name):
        self.id = country_id
        self.name = country_name
        self.income_group = ""
        self.links = {}
        self.costs = {}

    #Add links in the form (destination, total_cost_200, total_cost_500)
    def addLink(self, country_to, total_cost_200, total_cost_500, firm_name):
        if not country_to in self.links:
            self.links[country_to] = []
        self.links[country_to].append((total_cost_200, total_cost_500, firm_name))

    #Returns the links with the least cost based on the amount to send
    def calculateCost(self, cost_200, cost_500, amount):
        return (5./300. * cost_500 - 2./300. * cost_200) * amount + (-10./3. * cost_500 + 10./3. * cost_200)

    def getMinLink(self, send_amount, country_dest):
      min_cost = sys.maxsize
      min_firm = ""
      for pair in self.links[country_dest]:
          try:
              cost_200 = float(pair[0])
              cost_500 = float(pair[1])
              firm = pair[2]
          except ValueError:
              continue
          newCost = self.calculateCost(cost_200,cost_500,send_amount)
          if newCost < min_cost:
          	min_cost = newCost
          	min_firm = firm
      self.costs[country_dest] = min_cost
      return min_firm

def find_index(category):
    return CATEGORY_NUM[CATEGORIES.index(category)]

def generate(amount, countries):
        # creates a list of all the data and costs to be passed to pathfinder
    connections = []
    for country in countries:
        for country_dest in countries[country].links:
            firm = countries[country].getMinLink(amount, country_dest)
            row = [country, country_dest, -np.log(1-countries[country].costs[country_dest]/amount), firm]
            connections.append(row)
    return connections

def analyze():
    countries = {}
    with open(COUNTRY_NAME_DIR, 'r') as rin:
        lines = rin.readlines()
        header = lines[2].split(',')
        for i in range(3, len(lines)):
            country_cur = lines[i].split(',')
            countries[country_cur[0]] = Country(country_cur[0], country_cur[1])

    with open(ROW_DATA_DIR_1, 'r') as rin:
        with open(OUTPUT_DIR, 'w') as rout:
            lines = rin.readlines()
            header = lines[0].split(',')
            for row in range(1, len(lines)):
                data_split = lines[row].split(',')
                try:
                	cost_200 = float(data_split[find_index("total_cost_200")])
                	cost_500 = float(data_split[find_index("total_cost_500")])
                except ValueError:
                	continue
                countries[data_split[find_index("source_code")]].addLink(data_split[find_index("destination_code")], data_split[find_index("total_cost_200")], data_split[find_index("total_cost_500")],data_split[find_index("firm")])
    return countries
