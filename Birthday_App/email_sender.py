import smtplib
import datetime
import json
import random

EMAIL = "YOUR-EMAIL"
PASSWORD = "YOUR-EMAIL-PASSWORD"

today_date = datetime.datetime.now()
current_month = today_date.month
current_day = today_date.day
key = f"{(str(current_day), str(current_month))}"

letter_template_path = f"./LETTER_TEMPLATES/letter_template_{random.randint(1,5)}.txt"

# =================================================
# CHECKING IF TODAY IS SOMEONE'S BIRTHDAY
# =================================================
with open("./DATA/birthday_data.json", "r") as birthday_data_file:
    try:
        data = json.load(birthday_data_file)
    except json.decoder.JSONDecodeError:
        print("The data file is empty")
    else:
        if key in data:
            birthday_person = data[key]
            RECEIVERS_EMAIL = birthday_person["email"]

            # DESIGNING THE LETTER TEMPLATE
            with open(letter_template_path) as letter_template:
                final_letter_template = letter_template.read().replace("[Name]", birthday_person["name"]).replace("[Your Name]", "Sahabaj")

            # SENDING THE BIRTHDAY MESSAGE TO THE RECEIVERS_EMAIL
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=RECEIVERS_EMAIL, msg=f"Subject:Happy Birthday\n\n{final_letter_template}")
