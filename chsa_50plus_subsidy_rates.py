import matplotlib.pyplot as plt

x5 = []
y5 = []

def subsidy_rates_across_chsa():
    with open("BC_census_2016_data.txt", 'r') as f_ref:
        for line in f_ref:
            line_elements = line.split(',')
            shelt_rent_30plus_rate = float(line_elements[5])
            subsidy_rate = float(line_elements[4])
            if shelt_rent_30plus_rate >= 50:
                y5.append(subsidy_rate)
                x5.append(line_elements[0])

subsidy_rates_across_chsa()

plt.bar(x5, y5)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Community Health Service Areas')
plt.ylabel('Subsidy Rates')
plt.title('Subsidy Rates In The Areas Where More Than 50% of Renters are Spending 30% or More of Their Monthly Income on Rent')

plt.show()