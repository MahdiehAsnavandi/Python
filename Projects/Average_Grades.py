import csv
# For the average
from statistics import mean 
from collections import OrderedDict
def calculate_averages(file_name):
    with open(file_name , "r") as f:
        reader = csv.reader(f)
        person_average = OrderedDict()
        for row in reader:
            average_list = []        
            name = row[0]
            for grade in row[1:]:
                average_list.append(int(grade))
            averages = mean(average_list)
            person_average[name] = averages     
    with open("source.py" , "w" , newline = "") as l:
        writer = csv.writer(l)
        for name , grade in person_average.items():
            writer.writerow([name, grade])
   
    
calculate_averages("All_grades.csv")    


def calculate_sorted_averages(file_name):
    with open(file_name , "r") as f:
        reader = csv.reader(f)
        people_averages = []   
        for row in reader:
            average_list = []
            name = row[0]
            for grade in row[1:]:
                average_list.append(int(grade))
                average = mean(average_list)
            people_averages.append([name , average])
        for p in range(len(people_averages)):
            for i in range( p +1 , len(people_averages) ):
                if people_averages[p][1] > people_averages[i][1]:
                    people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]
                elif people_averages[p][1] == people_averages[i][1]:
                    if people_averages[p][0] > people_averages[i][0]:
                        people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]

    with open("source.py" , "a" , newline= "") as r:
        writer = csv.writer(r)
        for k in people_averages:
            writer.writerow(k)


calculate_sorted_averages("All_grades.csv")



    


def calculate_three_best(file_name):
    with open(file_name , "r") as f:
        reader = csv.reader(f)
        people_averages = []   
        for row in reader:
            average_list = []
            name = row[0]
            for grade in row[1:]:
                average_list.append(int(grade))
                average = mean(average_list)
            people_averages.append([name , average])
        for p in range(len(people_averages)):
            for i in range( p +1 , len(people_averages) ):
                if people_averages[p][1] < people_averages[i][1]:
                    people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]
                elif people_averages[p][1] == people_averages[i][1]:
                    if people_averages[p][0] > people_averages[i][0]:
                        people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]


    with open("source.py" , "a" , newline= "") as  m:
        writer = csv.writer(m)
        count = 0
        for v in people_averages:
                if count < 3:
                    writer.writerow(v)
                    count = count + 1
       
calculate_three_best("All_grades.csv")    

    

def calculate_three_worst(file_name):
    with open(file_name , "r") as f:
        reader = csv.reader(f)
        people_averages = []  
        for row in reader:
            average_list = []
            name = row[0]
            for grade in row[1:]:
                average_list.append(int(grade))
                average = mean(average_list)
            people_averages.append([name , average])
        for p in range(len(people_averages)):
            for i in range( p +1 , len(people_averages) ):
                if people_averages[p][1] > people_averages[i][1]:
                    people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]
                elif people_averages[p][1] == people_averages[i][1]:
                    if people_averages[p][0] > people_averages[i][0]:
                        people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]
            

    with open ("source.py" , "a" , newline= "") as n:
        writer = csv.writer(n)
        for person in people_averages[:3]:
            writer.writerow([person[1]]) 

    
calculate_three_worst("All_grades.csv")    


def calculate_average_of_averages(file_name):
    with open(file_name , "r") as f:
        reader = csv.reader(f)
        people_averages = []  
        for row in reader:
            average_list = []
            name = row[0]
            for grade in row[1:]:
                average_list.append(int(grade))
                average = mean(average_list)
            people_averages.append([name , average])
        for p in range(len(people_averages)):
            for i in range( p +1 , len(people_averages) ):
                if people_averages[p][1] > people_averages[i][1]:
                    people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]
                elif people_averages[p][1] == people_averages[i][1]:
                    if people_averages[p][0] > people_averages[i][0]:
                        people_averages[p] , people_averages[i]  = people_averages[i] , people_averages[p]


    with open ("source.py" , "a" , newline= "") as d:
        writer = csv.writer(d)
        average_grades = []
        for person in people_averages:
            average_grades.append(person[1])
        a = mean(average_grades)
        writer.writerow([a])         



calculate_average_of_averages("All_grades.csv")    