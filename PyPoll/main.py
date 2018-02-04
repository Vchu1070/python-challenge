import os
import string
import csv
from collections import defaultdict
from collections import Counter

filenumbers = ['1']
for datasets in filenumbers:
    pollingCSV = os.path.join ('..', 'Resources','election_data_'+ datasets +'.csv')
    newpollingCSV = os.path.join ('..', 'Resources','final_election_data_'+ datasets +'txt')
    voter_ID = []
    county = []
    candidate = []
    pctcandidate = []
    candidatevotes = []
    winner = []
    with open(pollingCSV, 'r') as csvFile:
        csvReader = csv.reader (csvFile, delimiter=",")
        next (csvReader, None)
        for row in csvReader:
           voter_ID.append(row[0])
           county.append(row[1])
           candidate.append(row[2])
        print ("Election Results")
        print ("-"*80)
        for v in voter_ID:
              votetotal=len(voter_ID)
        print ("Total Votes: "+ str(votetotal))
        print ("-"*80)
        uniquecandidate=Counter(candidate)
        #print (uniquecandidate)
        for key, value in uniquecandidate.items():
            print (key,'{0:.2f}%'.format(value/votetotal*100),("(" + str(value) + ")"))
        print ("-"*80)
        winner = uniquecandidate.most_common(1)
        print ("Winner:" + str(winner))
        #cleaned_csv = zip ()
    #with open(output_file, 'w') as datafile:
        #csvWriter=csv.writer(datafile)
        #writer.writerow()
        #writer.writerows(cleaned_csv)
