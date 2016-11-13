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

    #Add links in the form (destination, fixed_cost, slope)
    def addLink(self, country_to, fixed_cost, slope):
        if country_to is not in self.links:
            self.links[country_to] = []
        self.links[country_to].append((fixed_cost, slope))

    #Returns the links with the least cost based on the amount to send
    def getMinLink(self, send_amount, country_dest):
        minTrip = (sys.maxsize, sys.maxsize, sys.maxsize)
        for cost in country_dest:
            fixed_cost = self.links[country_dest][cost][0]
            slope = self.links[country_dest][cost][1]
            percent_cost = (fixed_cost + slope * send_amount)/(send_amount)



    def toJSON(self):


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
                countries[data_split[CATEGORIES.index("source_code")]].addLink(data_split[CATEGORIES.index("destination_code")],


