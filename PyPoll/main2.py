
#from collections import defaultdict
from collections import Counter
import os
import csv

print (csv)

filenumbers = ['1','2']
for datasets in filenumbers:
    pollingCSV=os.path.join ('..', 'Resources','election_data_'+ datasets +'.csv')
    newpollingCSV=os.path.join ('..', 'Resources','final_election_data_'+ datasets +'.csv')
    with open(pollingCSV, 'r') as f_in, open(newpollingCSV, 'w') as f_out:
        d_reader = csv.Dictreader(f_in)
        fieldnames = ['VoterID', 'Candidate', 'Candidatepct', 'candidatevotes', 'Winner']