#data
name = "Kari"
experience_years = 1.3
is_active = True
show_age_info = True
is_eu_cv = True

#additional info
age = 29
add_age_info = show_age_info == True and not is_eu_cv
age_info = (
    f"I'm {age} years old. "
    if add_age_info
    else ""
)

#messages
greeting = "Hey there!"
status_text = "And now I'm"
python_engagement = (
    "happy to share that I’m learning Python and applying for jobs. \nHow did my day go today?"
    if is_active
    else "procrastinating instead of learning Python and applying for jobs."
)
farewell = "Tschüssi, bis bald!"

#construct message
header = f"{greeting.upper()} My name is {name}! :)"
subheader = f"{age_info}I work as a Manual QA Engineer with {experience_years} years of experience in GameDev."
body = f"{status_text} {python_engagement}"

#list
total_hours_plan = 0
day_plan = [
    ["26.01.2026", total_hours_plan],
    {"CV_sent": 10, "engagement_hour": 1, "satisfaction": True},
    {"subject": "Python", "engagement_hour": 2, "satisfaction": True}
]
for item in day_plan:
    if isinstance(item, dict) and "engagement_hour" in item:
        if isinstance(item["engagement_hour"], (int, float)):
            total_hours_plan += item["engagement_hour"]

total_hours_fact = 0
day_fact = [["26.01.2026"],]
activity1_fact = {"CV_sent": 0, "engagement_hour": 0, "satisfaction": False}
activity2_fact = {"subject": "Python", "engagement_hour": 1.2, "satisfaction": True}
day_fact.extend([activity1_fact, activity2_fact])
for item in day_fact:
    if isinstance(item, dict) and "engagement_hour" in item:
        if isinstance(item["engagement_hour"], (int, float)):
            total_hours_fact += item["engagement_hour"]
day_fact[0].append(total_hours_fact)
print(day_fact)
print(day_plan)

#message
message = f"""
{header}
{subheader}
{body}
{farewell}
"""

#print
print(message)