import matplotlib.pyplot as plt

y2 = []
x2 = []

def income_to_rent_ratio():
    with open("BC_census_2016_data.txt", 'r') as f_ref:
        for line in f_ref:
            line_elements = line.split(',')
            subsidy_rate = float(line_elements[4]) / 100 
            monthly_rent = float(line_elements[7]) - (float(line_elements[7]) * subsidy_rate) # Monthly rent after adjusted subsidy rate
            monthly_income = float(line_elements[11]) / 12
            rent_income_ratio = monthly_rent / monthly_income * 100
            shelt_rent_30plus_rate = float(line_elements[5])
            if shelt_rent_30plus_rate >= 50:            
               y2.append(round(rent_income_ratio, 2))
               x2.append(line_elements[0])

income_to_rent_ratio()

plt.bar(x2, y2)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Community Health Service Areas')
plt.ylabel('Median Monthly Income to Rent Ratio')
plt.title('Percentages of Median Monthly Incomes Spent on Rent In The Areas Where More Than 50% of Renters are Spending 30% or More of Their Monthly Income on Rent')

plt.show()