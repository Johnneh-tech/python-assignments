from datetime import datetime

full_name = "John Doe"
age = 20
department = "Computer Science"
school = "ABC University"
level = "200 Level"
state = "Lagos"
favorite_color = "Blue"
favorite_food = "Rice"

birth_year = datetime.now().year - age

print("========== STUDENT INFORMATION ==========")
print(f"Full Name: {full_name}")
print(f"Age: {age}")
print(f"Department: {department}")
print(f"School: {school}")
print(f"Level: {level}")
print(f"State: {state}")
print(f"Favourite Color: {favorite_color}")
print(f"Favourite Food: {favorite_food}")
print(f"Birth Year: {birth_year}")