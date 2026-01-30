from datetime import date

# data
NAME = "Kari"
EXPERIENCE_YEARS = 1.3
show_age_info = True
is_eu_cv = True
today = date.today().strftime("%B %d, %Y")

# additional info
AGE = 29
add_age_info = show_age_info and not is_eu_cv
age_info = f"I'm {AGE} years old. " if add_age_info else ""


# day activity
def calculate_daily_activity(cv_sent, engagement_cv, subject, engagement_learn):
    total_hours = engagement_cv + engagement_learn
    return {
        "date": today,
        "total_hours": total_hours,
        "day_cv_activity": {
            "subject": cv_sent,
            "engagement_hour": engagement_cv
        },
        "day_learn_activity": {
            "subject": subject,
            "engagement_hour": engagement_learn
        }
    }


day_plan = calculate_daily_activity(10, 1, "Python", 2)
day_fact = calculate_daily_activity(1, 1, "Python", 2)


# function to create engagement message based on total_hours
def generate_fact_engagement_message(day_fact: dict) -> str:
    cv_activity = day_fact["day_cv_activity"]["subject"]
    learn_hours = day_fact["day_learn_activity"]["engagement_hour"]
    subject = day_fact["day_learn_activity"]["subject"]

    if cv_activity > 0 and learn_hours > 0:
        return f"sent CVs and studied {subject} for {learn_hours} hours!"
    elif cv_activity > 0:
        return f"focused on sending CVs."
    elif learn_hours > 0:
        return f"studied {subject} for {learn_hours} hours."
    else:
        return f"procrastinated..."


# messages
greeting = "Hey there!"
header = f"{greeting.upper()} My name is {NAME}! :)"
subheader = f"{age_info}I work as a Manual QA Engineer with {EXPERIENCE_YEARS} years of experience in GameDev.\nHow did my {today} go?"
body = f"I {generate_fact_engagement_message(day_fact)}"
farewell = "Tschüssi, bis bald!"

# message
message = f"""{header}
{subheader}
{body}
{farewell}
"""

# print
print(message)