# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 02:23:20 2017

@author: Tayyab Rashid

We will be building an application which will have some function for a high school
the function will be adding new student and assign an unique id number to them
We will also inheritate Teacher class from Student Class. 
"""

class Student:
    StudentList=[]
    Num_of_Students=0
    def __init__(self, first, second, Origin):
        self.first=first #First name
        self.second=second #Second name or surname
        self.Origin=Origin #Domestic or foreig student
        self.email=first+"."+second+"@Highschool.com"#Email adress is created 
        Student.Num_of_Students+=1
        Student.StudentList.append("{} {}".format(self.first, self.second)) 
    
    @property #This is a getter we get fullname as an attribute
    def fullname(self): #Regular methods take instane as the first argument
        return "{} {}".format(self.first, self.second)

    @fullname.setter #This we use to pass whole name to change first and second
    def fullname(self,name):
        first, second=name.split(' ')
        self.first=first
        self.second=second
        
    @fullname.deleter #This one we use to delete a name del dev_1.fullname
    def fullname(self):
        print("Delete name!")
        self.first=None
        self.second=None

class Teacher(Student):#inheritated from Student
    def __init__(self, first, second, Origin, Students=None):
        super().__init__(first, second, Origin)
        if Students is None:
            self.Students=[]
        else:
            self.Students=Students
    def add_std(self, std):
        if std not in self.Students:
            self.Students.append(std)
    
    def remove_std(self, std):
        if std not in self.Students:
            self.Students.remove(std)
    def print_std(self):
        for std in self.Students:
            print("-->", std.fullname)
        
        
        