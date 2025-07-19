#assignment : 5
# task-1
students={
"rohit": 95,
"vansh": 85,
"names": 90,
"john": 80,
"baby": 70,
"alex": 50,
}
name = input("Enter student name: ")
if name in students:
    print(f"student { name }'s marks:{students[name]}")
else:
    print("student name is not found")

# task-2
numbers=list(range(1,11))
first_five=numbers[:5]
reversed_five=first_five[::-1]
print(numbers)
print(first_five)
print(reversed_five)































