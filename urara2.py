import csv
mydict=[{'branch':'coe','cgpa':'9.0','name':'nikhil','year':'2'},
        {'branch': 'it', 'cgpa': '9.7', 'name': 'archana', 'year': '6'},
        {'branch': 'se', 'cgpa': '7.0', 'name': 'nick', 'year': '2'}]
csvfields=['name','branch','year','cgpa']
filename="univ2.csv"
with open(filename,"w")as fp:
    dictwriter=csv.DictWriter(fp,fieldnames=csvfields)
    dictwriter.writeheader()
    dictwriter.writerows(mydict)
    print("\ndict data written to csv file")

