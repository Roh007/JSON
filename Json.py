#importing json 
import json

#input for json to fetch particular key value pair. 
n=input("Enter json no : ")

#Opening and reading json file.
f = open('Downloads/in.json','r')

#loading json file.
data = json.load(f)

#parsing key value pair by giving input.
for i in data:
    #print(i)
    if(i == n):
        print(data[i])

#closing file.
f.close()