import csv

with open('table_in.cvs') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    with open('email_es_nev.cvs', 'a') as newfile:
        newfile.write('Email,'+'Name' + '\n')
    for row in csvreader:
        print(row)
        with open('email_es_nev.cvs', 'a') as newfile:
            newfile.write(row[1]+',' + row[0] + '\n')

