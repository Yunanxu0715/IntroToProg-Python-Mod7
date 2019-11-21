# Title    Assignment 7
**Dev:** *Yunan XU*
**Date** *11.20.2019*

## Introduction
In this Assignment, I first created a binary file called binaryInformation.dat. This binary file ends with dat instead of txt.

I want to add people’s name and email address as information inside this binary file.

Since this file was empty at the beginning, I enter the email address and name into a list and use both append binary and pickle.dump to add my first row into the file.

In this assignment, I want all my email addresses form to end with .com. Therefore, I raise a customer error. I define the Email error inside my script with “E-mail address doesn’t end with .com” as print out if the error exists.

In order to insert more valid data that I want, I use try-except command. I was trying to input more data as the same procedure above instead of there are some error. Errors may be the invalid email address or may be some built-in python error.

After adding data into the binary file, I want to read binary file. Therefore, I use “rb” to read binary file. Then, I use pickle.load to extract data and finally print them out.

## Code
```
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
```


## Result of code
![Result of code1](https://github.com/Yunanxu0715/IntroToProg-Python-Mod7/blob/master/Screen%20Shot%202019-11-21%20at%2011.48.19%20AM.png)


![Result of code2](https://github.com/Yunanxu0715/IntroToProg-Python-Mod7/blob/master/Screen%20Shot%202019-11-21%20at%2011.49.27%20AM.png)

![Result of code2](https://github.com/Yunanxu0715/IntroToProg-Python-Mod7/blob/master/Screen%20Shot%202019-11-21%20at%2011.51.21%20AM.png)






