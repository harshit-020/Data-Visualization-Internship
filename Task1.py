#--------------------------------------StudentDataRecord-------------------------------------------------------------------------------------
record=["stdid","stdname","Standard","Age","Hindi","English","Maths","Science","Computer","Total"]
record1=[101,"Ashish Kumar","10th",15,67,89,87,89,90,422]
record2=[102,"Abhishek Kumar","10th",14,85,45,48,90,45,313]
record3=[103,"Aman","10th",15,23,56,78,78,67,302]
record4=[104,"Rahul","10th",14,45,67,45,45,56,258]
record5=[105,"Ruby","10th",13,89,67,89,93,65,403]
record6=[106,"Suman","10th",13,90,46,67,67,67,337]
record7=[107,"Saurabh","10th",15,23,23,34,45,34,159]
record8=[108,"Sumit","10th",14,56,45,67,78,90,336]
record9=[109,"Kamlesh","10th",15,45,56,78,99,67,345]
record10=[110,"Rohan","10th",15,34,12,24,45,56,171]
Data_Record=[record,record1,record2,record3,record4,record5,record6,record7,record8,record9,record10]
Duplicate_Data_Record=[record,record1,record2,record3,record4,record5,record6,record7,record8,record9,record10]
print(Data_Record)

#-----------------------------------------------------Display the name of students whose marks in english is greater than 50--------------------------------------------

print("Following students have their marks greater than 50 in english")

index=record.index("English")
for element in range (1,len(Data_Record)):
    if Data_Record[element][index] > 50:
        print( Data_Record[element][1],Data_Record[element][index])

#------------------------------------------------------Display student name and age of top 4 scorer of maths-------------------------------------------------------

print("These students are the top 4 scorers in Maths")
index = record.index("Maths")
top_scorer = []

for i in range(4):
    max_index = 1  # Reset max_index to the start of the list for each iteration
    max_value = Data_Record[1][index]  # Reset max_value for comparison
    for element in range(1, len(Data_Record)):
        if Data_Record[element][index] > max_value:
            max_value = Data_Record[element][index]
            max_index = element
    
    top_scorer.append(Data_Record[max_index])
    Data_Record.pop(max_index)

# Optionally print out the names and scores
for scorer in top_scorer:   
    print("Name:",scorer[1] ,"Age:",scorer[3], " Marks:",scorer[index])

#---------------------------------------------Display name, id, age of student who are bottom three scorer in computer-------------------------------------------------

print("These students are bottom 3 scorers in computer")
index = record.index("Computer")
bottom_scorer = []

for i in range(3):
    min_index = 1  # Reset min_index to the start of the list for each iteration
    min_value = Duplicate_Data_Record[1][index]  # Reset mim_value for comparison
    for element in range(1, len(Duplicate_Data_Record)):
        if Duplicate_Data_Record[element][index] < min_value:
            min_value = Duplicate_Data_Record[element][index]
            min_index = element
    
    bottom_scorer.append(Duplicate_Data_Record[min_index])
    Duplicate_Data_Record.pop(min_index)

# Optionally print out the names, id, age and scores
for scorer in bottom_scorer:   
    print("Name:",scorer[1] ,"ID:",scorer[0], "Age:",scorer[3], "Marks:",scorer[index])


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------