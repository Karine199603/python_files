#data
name = "Kari"
experience_years = 1.3
is_learning_python = True
tell_age_info = True
cv_market_EU = True

#additional info
age = 29
additional_age_info = tell_age_info == True and not cv_market_EU
age_info = (
    f"I'm {age} years old. "
    if additional_age_info
    else ""
)

#messages
greeting = "Hey there!"
status_text = "And now I'm"
python_engagement = (
    "happy to share that I’m learning Python"
    if is_learning_python
    else "procrastinating instead of learning Python"
)
farewell = "Tschüssi, bis bald!"

#construct message
header = f"{greeting.upper()} My name is {name}! :)"
subheader = f"{age_info}I work as a Manual QA Engineer with {experience_years} years of experience in GameDev."
body = f"{status_text} {python_engagement}"

#message
message = f"""
{header}
{subheader}
{body}
{farewell}
"""

#print
print(message)