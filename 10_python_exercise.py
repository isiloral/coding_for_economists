#Exercise 3
#The task is to count the nuber of times each country won a tender in the ted-sample.csv

#Task1: Find the index position of the column "WIN_COUNTRY_CODE"
#Hint: grab the headers and assign them to a variable. Then, iterate through headers using enumerate.
f = open("data/raw/european_commission/ted-sample.csv", "r")
headers = f.readline().strip().split(",") 
f.close()

for index, value in enumerate(headers):
  print(index, value)

#WIN_COUNTRY_CODE at index 61

#Task2: Instantiate an empty list called data
data = []

#Task 3: use the context manager open() and
#3.1: iterate through the rows (each line) of the csv file and 
#3.2: append the each row to the data list using (in the loop body) data.append(list(line.split(","))) 


#Hint: Use the .split() method on the line to automatically create a list, passing the appropriate argument to split().
with open('data/raw/european_commission/ted-sample.csv') as f:
  for line in f:
    data.append(list(line.split(",")))

print(data[0])

#Task 4: Iterate through the data list and count the number of times each country won a tender.
data = data[1:] #Get rid of headers, dont need them
#or data.pop(0)

#output should look like: d= {"country1": N1 ...} (lidt of lists)
#Hint: Use a dictionary to store the count of each country.
d = {} 
for row in data:
  country = row[61] #careful: some tenders are won by several countries
  countries = country.split('---') #returns a list of winning countries
  for winning_country in countries:
    if not winning_country in d:
      d[winning_country] = 0
    d[winning_country += 1

print(d)
