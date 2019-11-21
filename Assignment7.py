#-----------------
#Yunan XU
#Assignment 7
#11.20.2019

#First create a binary file
Email1="hjy@yahoo.com"
Name="hyj"
fstlist=[Email1,Name]

import pickle
file=open("binaryInformation.dat","ab")
pickle.dump(fstlist,file)
file.close()

#Define some error function
class EmailError(Exception):
    def _str_(self):
        return "Email address is not end with .com"




#ADD data into the binary file and test some error
try:
    Inputname=input("Enter name : ")
    Inputemail=input("Enter email here:")
    InputList=[Inputname,Inputemail]
    if Inputname.isnumeric():
        raise Exception(" Do not use number in the name")
    elif Inputemail.endswith(".com")==False:
        raise EmailError()

except Exception as e:
       print("There was a non specific error")
       print("Built-In Python error info:")
       import pickle
       #Add new data above into the binary information file
file = open("binaryInformation.dat", "ab")
pickle.dump(InputList, file)
file.close()
    #Extract data from the binary information file
import pickle
objfile=open("binaryInformation.dat","rb")
filedata=pickle.load(objfile)
objfile.close()
print(filedata)
