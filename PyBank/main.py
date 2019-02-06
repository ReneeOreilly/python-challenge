import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
Table = []
new_val = {}
newchan = 0
nextchan = 0
lastmon = 0
maxval = 0
maxdate = " "
minval = 100000000
mindate = " " 
change = []
#opening the csv and passing the header
with open(csvpath, newline="") as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   # print(f"Header: {csv_header}")
   #looping through the monthly profit/loses to get change 
   #assessing values for the min and max values
    for row in csvreader:
      new_val[row[0]] = int(row[1])
      newchan = int(row[1]) - lastmon
      lastmon = int(row[1])
      if newchan > maxval:
        maxval = newchan
        maxdate = row[0]

      if newchan < minval:
        minval = newchan
        mindate = row[0]

      change.append(newchan)
      finalval = change[1:]

      #printing to verify
    print("Financial Analysis")
    print("-----------------------")
    print("Total Months: " + str(len(new_val)))
    print("Total: $" + str(sum(new_val.values())))
    print("Average: $" + str(round(sum(finalval)/len(finalval),2)))
    print("Largest Increase: " + str(maxdate) + " $" + str(maxval))
    print("Largest Decrease: " + str(mindate) + " $" + str(minval))

 #creating the output file
outfile = open("results.txt", 'w')

resultString = "Financial Analysis" + "\n"
resultString += "Total Months: " + str(len(new_val)) +"\n"
resultString += "Total: $" + str(sum(new_val.values())) + "\n"
resultString += "Average: $" + str(round(sum(finalval)/len(finalval),2)) + "\n"
resultString += "Largest Increase: " + str(maxdate) + " $" + str(maxval) + "\n"
resultString += "Largest Decrease: " + str(mindate) + " $" + str(minval) + "\n"
outfile.write(resultString)
outfile.close