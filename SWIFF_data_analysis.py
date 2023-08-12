import csv

with open("/Users/EMWork/Downloads/Grid_view.csv", mode='r') as file:
    csvFile = csv.reader(file)
    countries = []
    for line in csvFile:
        countries.append(line[1])

new_countries = []
for i in range(len(countries)):
    if countries[i] not in new_countries:
        new_countries.append(countries[i])

country_stats = []

for country in new_countries:
    total_of_submissions = 0
    for i in range(len(countries)):
        if countries[i] == country:
            total_of_submissions += 1
    country_stats.append(total_of_submissions)

with open('SWIFF_data_analysis.txt', 'w') as f:
    for i in range(len(new_countries)):
        f.write(new_countries[i] + ": " + str(country_stats[i]) + "\n")