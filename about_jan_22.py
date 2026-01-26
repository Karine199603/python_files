name = "Kari"
age = 29
exp = 1.3
learning_python = True

#What on earth am I doing right now?
engagement = (
    "happy to share that I’m learning Python"
    if learning_python
    else "procrastinating instead of learning Python"
)

#print info
print(f"\nHey there, my name is {name}! :)")
print(
    f"I'm {age} years old.",
    f"I work as a Manual QA Engineer with {exp} years of experience in GameDev."
)
print(f"And now I'm {engagement}!")
print(f"Tschüssi, bis bald!")