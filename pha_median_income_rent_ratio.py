import matplotlib.pyplot as plt

y4 = []
x4 = []
pha_dict = {}

def income_to_rent_ratio_median():
    with open("BC_census_2016_data.txt", 'r') as f_ref:
        for line in f_ref:
            line_elements = line.split(',')
            pha_name = line_elements[2]
            subsidy_rate = float(line_elements[4]) / 100 
            monthly_rent = float(line_elements[7]) - (float(line_elements[7]) * subsidy_rate)
            monthly_income = float(line_elements[11]) / 12
            rent_income_ratio = round((monthly_rent / monthly_income * 100), 2)
            if pha_name in pha_dict:
                pha_dict[pha_name].append(rent_income_ratio)
            else:
                pha_dict[pha_name] = [rent_income_ratio]
            if pha_name not in x4:
             x4.append(pha_name)
        for pha_name in pha_dict:
            sortedList = sorted(pha_dict[pha_name])
            listLen = len(pha_dict[pha_name])
            index = (listLen - 1) // 2
            if (listLen % 2):
                pha_dict[pha_name] = (sortedList[index])
            else:
                pha_dict[pha_name] = round(((sortedList[index] + sortedList[index + 1])/2.0), 2)
            y4.append(pha_dict[pha_name])

income_to_rent_ratio_median()

plt.bar(x4, y4)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Provincial Health Authority')
plt.ylabel('Median Monthly Income to Rent Ratio')
plt.title('Percentages of Median Monthly Incomes Spent on Rent Across Five PHA')

plt.show()