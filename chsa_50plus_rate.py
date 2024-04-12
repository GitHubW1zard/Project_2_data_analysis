import matplotlib.pyplot as plt

x1 = []
y1 = []

def chsa_rent_50plus_rate():
    with open("BC_census_2016_data.txt", 'r') as f_ref:
        for line in f_ref:
            line_elements = line.split(',')
            shelt_rent_30plus_rate = float(line_elements[5])
            if shelt_rent_30plus_rate >= 50:
                y1.append(shelt_rent_30plus_rate)
                x1.append(line_elements[0])

chsa_rent_50plus_rate()

plt.bar(x1, y1)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Community Health Service Areas')
plt.ylabel('Percentage of Renters')
plt.title('Community Health Service Areas Where More Than 50% of Renters are Spending 30% or More of Their Monthly Income on Rent')

plt.show()