import matplotlib.pyplot as plt

x3 = []
y3 = []
pha_dict = {}

def median_subsidy_rate_pha(): 
    with open("BC_census_2016_data.txt", 'r') as f_ref:
        for line in f_ref:
            line_elements = line.strip().split(',')
            pha_name = line_elements[2]
            pha_subsidy_rate = float(line_elements[4])
            if pha_name in pha_dict:
                pha_dict[pha_name].append(pha_subsidy_rate)
            else:
                pha_dict[pha_name] = [pha_subsidy_rate]
            if pha_name not in x3:
             x3.append(pha_name)   
        for pha_name in pha_dict:
            sortedList = sorted(pha_dict[pha_name])
            listLen = len(pha_dict[pha_name])
            index = (listLen - 1) // 2
            if (listLen % 2):  # If number is odd, then (listLen % 2) evaluates to True(1) 
                pha_dict[pha_name] = (sortedList[index]) # If len of numbers is odd, take the index of the middle one
            else:
                pha_dict[pha_name] = round(((sortedList[index] + sortedList[index + 1])/2.0), 2) # If len of numbers is even, take the middle value of two nums in the middle
            y3.append(pha_dict[pha_name])

median_subsidy_rate_pha()

plt.bar(x3, y3)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Provincial Health Authority')
plt.ylabel('Median Subsidy Rate')
plt.title('Median Subsidy Rates Across Five PHA')

plt.show()