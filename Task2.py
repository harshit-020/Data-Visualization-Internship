# --------------------------------Converting the data into list of dictionaries-------------------------------------------
records = [
    {"stdid": 101, "stdname": "Ashish Kumar", "Standard": "10th", "Age": 15, "Hindi": 67, "English": 89, "Maths": 87, "Science": 89, "Computer": 90, "Total": 422},
    {"stdid": 102, "stdname": "Abhishek Kumar", "Standard": "10th", "Age": 14, "Hindi": 85, "English": 45, "Maths": 48, "Science": 90, "Computer": 45, "Total": 313},
    {"stdid": 103, "stdname": "Aman", "Standard": "10th", "Age": 15, "Hindi": 23, "English": 56, "Maths": 78, "Science": 78, "Computer": 67, "Total": 302},
    {"stdid": 104, "stdname": "Rahul", "Standard": "10th", "Age": 14, "Hindi": 45, "English": 67, "Maths": 45, "Science": 45, "Computer": 56, "Total": 258},
    {"stdid": 105, "stdname": "Ruby", "Standard": "10th", "Age": 13, "Hindi": 89, "English": 67, "Maths": 89, "Science": 93, "Computer": 65, "Total": 403},
    {"stdid": 106, "stdname": "Suman", "Standard": "10th", "Age": 13, "Hindi": 90, "English": 46, "Maths": 67, "Science": 67, "Computer": 67, "Total": 337},
    {"stdid": 107, "stdname": "Saurabh", "Standard": "10th", "Age": 15, "Hindi": 23, "English": 23, "Maths": 34, "Science": 45, "Computer": 34, "Total": 159},
    {"stdid": 108, "stdname": "Sumit", "Standard": "10th", "Age": 14, "Hindi": 56, "English": 45, "Maths": 67, "Science": 78, "Computer": 90, "Total": 336},
    {"stdid": 109, "stdname": "Kamlesh", "Standard": "10th", "Age": 15, "Hindi": 45, "English": 56, "Maths": 78, "Science": 99, "Computer": 67, "Total": 345},
    {"stdid": 110, "stdname": "Rohan", "Standard": "10th", "Age": 15, "Hindi": 34, "English": 12, "Maths": 24, "Science": 45, "Computer": 56, "Total": 171},
]

# ----------------------Display the name of students whose marks in English are greater than 50---------------------------------
print("Following students have their marks greater than 50 in English")
for record in records:
    if record["English"] > 50:
        print(record["stdname"], record["English"])

# ------------------------------Display student name and age of top 4 scorers in Maths----------------------------------------------
print("\nThese students are the top 4 scorers in Maths")
top_scorers = sorted(records, key=lambda x: x["Maths"], reverse=True)[:4]
for scorer in top_scorers:
    print("Name:", scorer["stdname"], "Age:", scorer["Age"], "Marks:", scorer["Maths"])

# -----------------------------Display name, id, age of students who are bottom 3 scorers in Computer------------------------------------
print("\nThese students are the bottom 3 scorers in Computer")
bottom_scorers = sorted(records, key=lambda x: x["Computer"])[:3]
for scorer in bottom_scorers:
    print("Name:", scorer["stdname"], "ID:", scorer["stdid"], "Age:", scorer["Age"], "Marks:", scorer["Computer"])
