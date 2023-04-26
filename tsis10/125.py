import csv

data = [['John Doe', '12345'], 
        ['Jane Doe', '120304'],
        ['hhaa', '298398'],
        ['ijdije', '928392'],
        ['bhsash', '826310']]
#create csv file
with open('contacts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)