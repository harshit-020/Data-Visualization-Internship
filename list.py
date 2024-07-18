record = ["stdid", "stdname", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]
record1 = [101, "Ashish Kumar Kumar", "10th", 15, 67, 89, 87, 89, 90, 422]
record2 = [102, "Abhishek Kumar", "10th", 14, 85, 45, 48, 90, 45, 313]
record3 = [103, "Aman", "10th", 15, 23, 56, 78, 78, 67, 302]
record4 = [104, "Rahul", "10th", 14, 45, 67, 45, 45, 56, 258]
Data_Record = [record, record1, record2, record3, record4]

print(Data_Record)

print("Following students have their marks greater than 50 in English")

index = record.index("English")
for element in range(1, len(Data_Record)):
    if Data_Record[element][index] > 50:
        print(Data_Record[element][1], Data_Record[element][index])

print("Following students are the 4 top scorers in Maths")

index = record.index("Maths")
scores = [(Data_Record[element][1], Data_Record[element][index]) for element in range(1, len(Data_Record))]
scores.sort(key=lambda x: x[1], reverse=True)

top_4_scorers = scores[:4]
for scorer in top_4_scorers:
    print(scorer[0], scorer[1])
