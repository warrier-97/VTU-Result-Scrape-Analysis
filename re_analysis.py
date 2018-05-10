# -*- coding: utf-8 -*-
"""
Created on Tue May  8 19:01:24 2018

@author: ADITYA
"""

import csv,re
from matplotlib import pyplot as plt
from matplotlib import style

code,subs,perc,int_marks,ext_marks,tot,cred=list(),list(),list(),list(),list(),list(),list()
grade,grade_pts,pf=list(),list(),list()

def fill_cred():
    for i in code:
        if re.match('15CS5[1-9]',i):
            cred.append(4)
        elif re.match('15CS5[1-9][1-9]',i):
            cred.append(3)
        else:
            cred.append(2)
            
def fill_grade():
    global tot,grade,grade_pts
    for i in tot:
        if i>=90:
            grade.append('S+')
            grade_pts.append(10)
        elif i>=80 and i<90:
            grade.append('S')
            grade_pts.append(9)
        elif i>=70 and i<80:
            grade.append('A')
            grade_pts.append(8)
        elif i>=60 and i<70:
            grade.append('B')
            grade_pts.append(7)
        elif i>=50 and i<60:
            grade.append('C')
            grade_pts.append(6)
        elif i>=40 and i<50:
            grade.append('D')
            grade_pts.append(5)
        elif i>=30 and i<40:
            grade.append('E')
            grade_pts.append(4)
        else:
            grade.append('F')
            grade_pts.append(0)
                

def search(usn):
    flag=0
    file = open("res_dump.csv","r") 
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0].strip() == usn:
            flag=1
            return row
    if flag==0:
        print("\nINVALID USN")
        return -1

def remove_commas(x):
    c=0
    for i in x:
        if i=='':
            c+=1
    actual_len=len(x)-c
    x=x[0:actual_len]
    return x

def fill(x):
    global code,subs,perc,int_marks,ext_marks,tot
    i=2
    while i<len(x):
        subs.append(x[i+1])
        code.append(x[i])
        per=(int(x[i+4])/100)*100
        perc.append(per)
        int_marks.append(int(x[i+2]))
        ext_marks.append(int(x[i+3]))
        tot.append(int(x[i+4]))
        pf.append(x[i+5])
        i+=6
    fill_grade()
    fill_cred()
    
def print_details(x):
    global code,subs,perc,int_marks,ext_marks,tot
    print("Name: "+x[1]+"\nUSN: "+x[0]+"\n\n")
    i=2
    while i<len(x):
        print("Subject Code:",x[i],"\nSubject name:",x[i+1])
        print("Internal Marks =",x[i+2],"\nExternal Marks =",x[i+3],"\nTotal Marks =",x[i+4])
        print("Result = ",x[i+5])
        print("\n\n")
        i+=6

def plot_tot():
    global code,subs,perc
    i=0
    while i<len(code):
        print("\nSubject Code:",code[i],"\nSubject name:",subs[i],"\nPercentage = ",perc[i],"%\n\n")
        i+=1

    style.use('ggplot')
    plt.figure(figsize=(10,5), dpi=100)
    plt.bar(code, perc, align='center')

    plt.title('Result analysis')
    plt.ylabel('Percentage')
    plt.ylim(0,100)
    plt.xlabel('Subject')
    
    plt.show()           

def sub(sub_code):
    global code,subs,int_marks,ext_marks,tot
    flag=0
    for i in range(len(code)):
        if code[i] == sub_code:
            print("\nSubject Code:",code[i],"\nSubject name:",subs[i],"\nInternal marks = ",int_marks[i],"\nExternal marks = ",ext_marks[i],"\nTotal marks = ",tot[i],"\nResult = ",pf[i],"\nGrade = ",grade[i],"\nGrade Points = ",grade_pts[i],"\n\n")
            flag=1
            plt.figure(figsize=(10,10), dpi=100)
            plt.subplot2grid((2,2),(0,0))
            plt.pie([int_marks[i],(20-int_marks[i])],
                    labels=['Internal','Unscored'],
                    colors=['yellowgreen', 'lightcoral'],
                    explode=(0.1,0),
                    autopct='%1.1f%%', shadow=True,
                    startangle=140
                    )
            plt.title("Internal Assesment")
            
            plt.subplot2grid((2, 2), (0, 1))
            plt.pie([ext_marks[i],(80-ext_marks[i])],
                    labels=['External','Unscored'],
                    colors=['yellowgreen', 'lightcoral'],
                    explode=(0.1,0),
                    autopct='%1.1f%%', shadow=True,
                    startangle=140
                    )
            plt.title("External Assesment")
            
            plt.subplot2grid((2, 2), (1, 0))
            plt.pie([int_marks[i],ext_marks[i],(100-(int_marks[i]+ext_marks[i]))],
                    labels=['Internal','External','Unscored'],
                    colors=['yellowgreen', 'lightcoral', 'lightskyblue'],
                    explode=(0,0.1,0),
                    autopct='%1.1f%%', shadow=True,
                    startangle=140
                    )
            plt.title('Subject Analysis\n'+code[i]+" : "+subs[i])            
            plt.show()

            break
        else:
            continue
    if flag==0:
        print("\nInvalid Subject code")
        
def internals():
    global int_marks,code,subs
    for i in range(len(int_marks)):
        print("\nSubject Code:",code[i],"\nSubject name:",subs[i],"\nInternal marks = ",int_marks[i],"\n\n")
        
    style.use('ggplot')
    plt.figure(figsize=(10,5), dpi=100)
    plt.bar(code,int_marks, align='center')

    plt.title('Internal Assesment')
    plt.ylabel('Marks')
    plt.ylim(0,20)
    plt.xlabel('Subject')
    
    plt.show()      

def externals():
    global ext_marks,code,subs
    for i in range(len(int_marks)):
        print("\nSubject Code:",code[i],"\nSubject name:",subs[i],"\nExternal marks = ",ext_marks[i],"\n\n")
        
    style.use('ggplot')
    plt.figure(figsize=(10,5), dpi=100)
    plt.bar(code,ext_marks, align='center')

    plt.title('External Assesment')
    plt.ylabel('Marks')
    plt.ylim(0,80)
    plt.xlabel('Subject')
    
    plt.show()           
    
                    
def sgpa():
    global cred,grade_pts
    x=[a*b for a,b in zip(grade_pts,cred)]
    sgpa=sum(x) / 26
    print("S.G.P.A = ",sgpa)
    
def main():

    usn=input("Enter USN of student : ")
    usn=usn.upper()
    data=search(usn)
    
    if data==-1:
        pass
    else:
        data=remove_commas(data)
        fill(data)
        while(1):
            print("\n\n**** MAIN MENU **** \n \n\t1-->Check Results \n\t2-->Internal Marks \n\t3-->External marks \n\t4-->Total result analysis \n\t5-->Subject analysis \n\t6-->SGPA \n\t7-->Exit")
            ch=int(input("Enter your choice :"))
            
            if ch == 1:
               print_details(data)
            elif ch == 2:
                internals()
            elif ch == 3:
                externals()
                
            elif ch == 4:
                plot_tot()
            elif ch == 5:
                sub_code=input("Enter subject code : ")
                sub_code=sub_code.upper()
                sub(sub_code)
            elif ch == 6:
                sgpa()
            elif ch == 7:
                break
            else:
                print("\n Invalid option \n Please Try again")
            
       
if __name__ == "__main__":
    main()    
