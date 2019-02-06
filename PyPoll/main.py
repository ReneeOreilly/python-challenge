import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
totaldata = {}
Totalvotes = 0
#opening the csv and passing the header
with open(csvpath, newline="") as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
  #creating dictionary to count for each unique key  
    for row in csvreader:
      if(str(row[2]) in totaldata):
          totaldata[row[2]] = totaldata[row[2]] + 1
      else:
          totaldata[row[2]] = 1
        #calculations
    total = sum(totaldata.values())
    key_max = max(totaldata.keys(), key=(lambda k: totaldata[k]))
    #print to verify
    print(totaldata)
    print(str(sum(totaldata.values())))   
    print("Election Results")
    print("------------------------")
    print("Total Votes: " + str(total))
    print("------------------------")
    #loop through each Key
    for cand in totaldata.keys():
        #print(cand + " " + str(totaldata[cand]))
        p = '{0:.3f}'.format(totaldata[cand] / total * 100)
        print(cand + ":"+ " " + str(p) + "%" + " " + str(totaldata[cand]))
    print("-----------------------")
    print("Winner: " + key_max)
    print("-----------------------")
#creating outfile
    outfile = open('resultsPYPoll.txt', 'w')
    ResultsString = "Election Results" + "\n"
    ResultsString += "------------------------" + "\n"
    ResultsString += "Total Votes: " + str(total) + "\n"
    ResultsString += "------------------------" + "\n"  
    for cand in totaldata.keys():
        #print(cand + " " + str(totaldata[cand]))
      p = '{0:.3f}'.format(totaldata[cand] / total * 100)
      ResultsString += cand + ":"+ " " + str(p) + "%" + " " + str(totaldata[cand]) + "\n"
    ResultsString += "------------------------" + "\n"  
    ResultsString += "Winner: " + key_max + "\n"
    ResultsString += "------------------------" + "\n"
    outfile.write(ResultsString)
    outfile.close