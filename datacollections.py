#list stores amultiple of data types
#xtics
# mutable 
#index
varName= []
studentName =["sandra","patricia","phiona","anitah"] #string
studentMarks=[80,56,78,90]#integers
data =['Julian',50,'Hoima']#mixed data types
#acces the whole list
print(studentName,type(studentName))

#accessing list items 
#indexes
print(studentName[0])#fist item
print(studentName[1])#second item
print(studentName[2])#third item
print(studentName[3])#fourt item

#for negative index
print(studentName[-4])#fist item
print(studentName[-3])#second item
print(studentName[-2])#third item
print(studentName[-1])#fourt item

#adding misshell to the student list
#at the end
studentName.append('Mishell')
print(studentName)

#at a particular position
studentName.insert(2,'Faith')
print(studentName)


#QUESTIONS AND ANSWERS
#print patricia to anitah
studentName.remove('sandra')
print(studentName)


#add masha at the fourth position
studentName.insert(3,'Masha')
print(studentName)

#update the name phiona Aladina 
name=["patricia","Faith","Anitah","phiona"]
index=name.index('phiona')
name[index] = "phiona Aladina"
print(name)

#display the length of the student list
student=["patricia","Faith","Anitah","phiona Aladina"]
lenght=[len(student) for student in student]
print(lenght)

#print all the students name having updated using a four loop
studentName= ["patricia","Faith","Anitah","phiona Aladina"]
for name in studentName:
    print(studentName)

#calculate the total marks for the student marks variable and the answer is 304
studentMarks=[80,56,78,90]
totalMarks = sum(studentMarks)
print("Total marks:", totalMarks)