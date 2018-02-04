import os
import string
import csv
from collections import defaultdict
from collections import Counter

filenumbers = ['2']
for datasets in filenumbers:
    pollingCSV = os.path.join ('..', 'Resources','election_data_'+ datasets +'.csv')
    newpollingtxt = os.path.join ('..', 'Resources','final_election_data_'+ datasets +'.txt')
    voter_ID = []
    county = []
    votetotal = []
    candidate = []
    candidatelist = []
    uniquecandidate = []
    winner = []
    with open(pollingCSV, 'r') as csvFile:
        csvReader = csv.reader (csvFile, delimiter=",")
        next (csvReader, None)
        for row in csvReader:
           voter_ID.append(row[0])
           county.append(row[1])
           candidate.append(row[2])
        print ("Election Results", file=open("newpollingtext","a"))
        print ("-"*80,file=open("newpollingtext","a"))
        print ("Election Results")
        print ("-"*80)
        votetotal = len(voter_ID)
        print ("Total Votes: "+ str(votetotal),file=open("newpollingtext","a"))
        print ("-"*80,file=open("newpollingtext","a"))
        print ("Total Votes: "+ str(votetotal))
        print ("-"*80)
        uniquecandidate = Counter(candidate)
        for key, value in uniquecandidate.items():
            candidatelist= (key,'{0:.2f}%'.format(value/votetotal*100),("(" + str(value) + ")"))
            print (candidatelist,file=open("newpollingtext","a"))
            print (candidatelist)
        print ("-"*80,file=open("newpollingtext","a"))
        print ("-"*80)
        winner = uniquecandidate.most_common(1)
        print ("Winner:" + str(winner),file=open("newpollingtext","a"))   
        print ("Winner: "+ str(winner))