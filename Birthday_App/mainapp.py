from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
import json

# Constants
MAIN_BACKGROUND_COLOR = "#FFF3E2"
MAIN_TEXT_COLOR = "#ffffff"
SECONDARY_TEXT_COLOR = "#E74646"
BUTTON_COLOR = "#FA9884"

# Variables used in the creation of the add form
name_entry_label = None
name_entry = None
email_entry_label = None
email_entry = None
birthday_entry = None
add_entry_button = None
go_to_home_button = None

# Variables used in the home forms
app_title = None
add_button = None
remove_button = None
show_button = None

# Variable used in the remove entry form
remove_entry_button = None

# Variable used in the display birthday list
listbox = None


def go_to_home():
    canvas.grid(row=0, column=1, rowspan=5)
    # ==============================================================
    # CREATING THE LOGO AND THE BUTTONS
    # ==============================================================
    global app_title, add_button, remove_button, show_button
    if type(app_title) == type(Label()):
        app_title.destroy()

    app_title = Label(text="BIRTHDAY APP",
                      bg=MAIN_BACKGROUND_COLOR,
                      fg=SECONDARY_TEXT_COLOR,
                      font=("Helvetica", 16, "bold"),
                      )
    app_title.grid(row=0, column=0, pady=(20, 0))

    # Creating the add the person button
    add_button = Button(text="ADD PERSON",
                        bg=BUTTON_COLOR,
                        fg=MAIN_TEXT_COLOR,
                        width=30,
                        pady=5,
                        command=show_add_person_form)
    add_button.grid(row=1, column=0, pady=10)

    # Creating the remove the person button
    remove_button = Button(text="REMOVE PERSON",
                           bg=BUTTON_COLOR,
                           fg=MAIN_TEXT_COLOR,
                           width=30,
                           pady=5,
                           command=remove_entry_form)
    remove_button.grid(row=2, column=0, pady=10)

    # Creating the show the birthday list button
    show_button = Button(text="SHOW THE LIST",
                         bg=BUTTON_COLOR,
                         fg=MAIN_TEXT_COLOR,
                         width=30,
                         pady=5,
                         command=show_birthday_list)
    show_button.grid(row=3, column=0, pady=10)


def destroy_home_buttons():

    if type(add_button) == type(Button()):
        add_button.destroy()
    if type(remove_button) == type(Button()):
        remove_button.destroy()
    if type(show_button) == type(Button()):
        show_button.destroy()


# ============================================================
# FUNCTION WHICH IS USED TO DISPLAY THE ENTRY FORM USED TO ADD THE PERSON
# ============================================================
def show_add_person_form():

    destroy_home_buttons()
    # importing all the variable
    global name_entry, name_entry_label, email_entry, email_entry_label, birthday_entry, add_entry_button, go_to_home_button

    # Changing the text of app title
    app_title.config(text="ADD PERSON TO THE LIST", font=("Helvetica", 10, "bold"))
    app_title.grid(pady=(0, 0))


    # NAME ENTRY
    name_entry_label = Label(text="ENTER THE NAME OF THE PERSON", width=34, fg=MAIN_TEXT_COLOR, bg=BUTTON_COLOR)
    name_entry_label.grid(row=1, column=0, pady=10)
    name_entry = ttk.Entry(width=40)
    name_entry.grid(row=2, column=0, ipady=5)
    name_entry.focus()

    # EMAIL ENTRY
    email_entry_label = Label(text="ENTER THE EMAIL OF THE PERSON", width=34, fg=MAIN_TEXT_COLOR, bg=BUTTON_COLOR)
    email_entry_label.grid(row=3, column=0, pady=10)
    email_entry = ttk.Entry(width=40)
    email_entry.grid(row=4, column=0, ipady=5)

    # BIRTHDAY DATE ENTRY
    birthday_entry = Calendar(bordercolor="RED",
                              background=SECONDARY_TEXT_COLOR,
                              headersbackground=BUTTON_COLOR,
                              headersforeground=MAIN_TEXT_COLOR,
                              selectbackground=SECONDARY_TEXT_COLOR,
                              weekendforeground=MAIN_TEXT_COLOR,
                              weekendbackground=BUTTON_COLOR,
                              othermonthforeground=MAIN_TEXT_COLOR,
                              othermonthbackground=SECONDARY_TEXT_COLOR,
                              othermonthwebackground="#FF3C4D",
                              othermonthweforeground=MAIN_TEXT_COLOR
                              )
    birthday_entry.grid(row=5, column=0, pady=5)

    # ADD ENTRY BUTTON
    add_entry_button = Button(text="ADD ENTRY", bg=BUTTON_COLOR,
                              fg=MAIN_TEXT_COLOR, width=35, pady=5, command=add_entry_functionality)
    add_entry_button.grid(row=6, column=0, pady=5)

    # ADD GO TO HOME BUTTON
    go_to_home_button = Button(text="GO TO HOME", bg=BUTTON_COLOR,
                               fg=MAIN_TEXT_COLOR, width=35, pady=5, command=destroy_add_form)
    go_to_home_button.grid(row=7, column=0, pady=5)

    # spanning the image to six rows
    canvas.grid(row=0, column=1, rowspan=8)


# -------------------------------------
# FUNCTION TO ADD THE ENTRY
# -------------------------------------
def add_entry_functionality():
    birthday_date = birthday_entry.get_date().split("/")
    birthday_day = birthday_date[1]
    birthday_month = birthday_date[0]

    birthday_data = {
        f"{(birthday_day, birthday_month)}": {
            "name": name_entry.get(),
            "email": email_entry.get(),
            "birthday_day": birthday_day,
            "birthday_month": birthday_month,
            "birthday_year": birthday_date[2]
        }
    }

    if name_entry.get() == "" or email_entry.get() == "":
        messagebox.showerror(title="ERROR", message="PLEASE ENTER THE VALID DETAILS")
    else:

        try:
            with open("./DATA/birthday_data.json", "r") as birthday_data_file:
                data = json.load(birthday_data_file)

        except FileNotFoundError:
            data = birthday_data
            with open("./DATA/birthday_data.json", "w") as birthday_data_file:
                json.dump(data, birthday_data_file, indent=4)
                messagebox.showinfo(title="CONFIRMATION MESSAGE", message="PERSON WITH FOLLOWING DETAILS WILL BE ADDED\n\n"
                                                                          f"NAME : {name_entry.get()}\n"
                                                                          f"EMAIL : {email_entry.get()}\n"
                                                                          f"BIRTHDAY : {birthday_entry.get_date()}\n")

        else:
            data.update(birthday_data)
            with open("./DATA/birthday_data.json", "w") as birthday_data_file:
                json.dump(data, birthday_data_file, indent=4)
                messagebox.showinfo(title="CONFIRMATION MESSAGE",
                                    message="PERSON WITH FOLLOWING DETAILS WILL BE ADDED\n\n"
                                    f"NAME : {name_entry.get()}\n"
                                    f"EMAIL : {email_entry.get()}\n"
                                    f"BIRTHDAY : {birthday_entry.get_date()}\n")

        finally:
            name_entry.delete(0, END)
            email_entry.delete(0, END)
            name_entry.focus()


def destroy_add_form():

    if type(name_entry_label) == type(Label()):
        name_entry_label.destroy()
    if type(name_entry) == type(ttk.Entry()):
        name_entry.destroy()
    if type(email_entry_label) == type(Label()):
        email_entry_label.destroy()
    if type(email_entry) == type(ttk.Entry()):
        email_entry.destroy()
    if type(birthday_entry) == type(Calendar()):
        birthday_entry.destroy()
    if type(add_entry_button) == type(Button()):
        add_entry_button.destroy()
    if type(go_to_home_button) == type(Button()):
        go_to_home_button.destroy()

    go_to_home()


# ===============================================================
# FUNCTION WHICH IS USED TO DISPLAY THE FORM USED TO REMOVE ENTRY
# ===============================================================
def remove_entry_form():
    global name_entry_label, name_entry, birthday_entry, remove_entry_button, go_to_home_button
    # Changing the text of app title
    destroy_home_buttons()
    app_title.config(text="REMOVE PERSON FROM THE LIST", font=("Helvetica", 10, "bold"))
    app_title.grid(row=0, column=0, pady=(0, 0))

    # NAME ENTRY
    name_entry_label = Label(text="ENTER THE NAME OF THE PERSON", width=34, fg=MAIN_TEXT_COLOR, bg=BUTTON_COLOR)
    name_entry_label.grid(row=1, column=0, pady=10)
    name_entry = ttk.Entry(width=40)
    name_entry.grid(row=2, column=0, ipady=5)
    name_entry.focus()

    # BIRTHDAY DATE ENTRY
    birthday_entry = Calendar(bordercolor="RED",
                              background=SECONDARY_TEXT_COLOR,
                              headersbackground=BUTTON_COLOR,
                              headersforeground=MAIN_TEXT_COLOR,
                              selectbackground=SECONDARY_TEXT_COLOR,
                              weekendforeground=MAIN_TEXT_COLOR,
                              weekendbackground=BUTTON_COLOR,
                              othermonthforeground=MAIN_TEXT_COLOR,
                              othermonthbackground=SECONDARY_TEXT_COLOR,
                              othermonthwebackground="#FF3C4D",
                              othermonthweforeground=MAIN_TEXT_COLOR
                              )
    birthday_entry.grid(row=3, column=0, pady=5)

    # REMOVE ENTRY BUTTON
    remove_entry_button = Button(text="REMOVE ENTRY", bg=BUTTON_COLOR,
                              fg=MAIN_TEXT_COLOR, width=35, pady=5, command=remove_entry_functionality)
    remove_entry_button.grid(row=4, column=0, pady=5)

    # ADD GO TO HOME BUTTON
    go_to_home_button = Button(text="GO TO HOME", bg=BUTTON_COLOR,
                               fg=MAIN_TEXT_COLOR, width=35, pady=5, command=destroy_remove_form)
    go_to_home_button.grid(row=5, column=0, pady=5)


def remove_entry_functionality():
    birthday_in_lst_format = birthday_entry.get_date().split("/")
    birthday_tuple = f"{(birthday_in_lst_format[1], birthday_in_lst_format[0])}"
    # ERROR HANDLING
    try:
        with open("./DATA/birthday_data.json", "r") as birthday_data_file:
            data = json.load(birthday_data_file)

    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="Birthday List doesn't exist\n"
                                                    "Please create a birthday list\n")
    else:
        # Checking if the name and birthday matches
        if birthday_tuple in data:
            if data[birthday_tuple]["name"].lower() == name_entry.get().lower():
                if name_entry.get() != "":
                    data.pop(birthday_tuple)
                    with open("./DATA/birthday_data.json", "w") as birthday_data_file:
                        json.dump(data, birthday_data_file, indent=4)
                        messagebox.showinfo(title="CONFIRMATION MESSAGE", message="THE PERSON WITH FOLLOWING DETAILS HAVE BEEN REMOVED\n\n"
                                                                                  f"NAME : {name_entry.get()}\n"
                                                                                  f"BIRTHDAY : {birthday_entry.get_date()}")
                        name_entry.delete(0, END)
                else:
                    messagebox.showerror("Enter the name of the person")
            else:
                messagebox.showerror(title="", message="The name doesnot match with the given birthday")
        else:
            messagebox.showerror(title="ERROR", message="The person doesn't exist in the birthday list\n"
                                                        "If the person exist then please check the name and birthday")
            print(str(birthday_tuple), data)


def destroy_remove_form():
    if type(name_entry_label) == type(Label()):
        name_entry_label.destroy()
    if type(name_entry) == type(ttk.Entry()):
        name_entry.destroy()
    if type(birthday_entry) == type(Calendar()):
        birthday_entry.destroy()
    if type(remove_entry_button) == type(Button()):
        remove_entry_button.destroy()
    if type(go_to_home_button) == type(Button()):
        go_to_home_button.destroy()

    go_to_home()


# =================================================================
# FUNCTION WHICH IS USED TO SHOW THE BIRTHDAY LIST
# ===============================================================
def show_birthday_list():
    global app_title, listbox, go_to_home_button
    destroy_home_buttons()
    app_title.config(text="BIRTHDAY LIST")
    with open("./DATA/birthday_data.json") as birthday_data_file:
        data = json.load(birthday_data_file)

    listbox = Listbox(width=40, bg=BUTTON_COLOR, fg="white", height=20)
    for person_key in data:
        person = data[person_key]
        listbox.insert(0, f"\n")
        listbox.insert(1, f"  Name : {person['name']}")
        listbox.insert(2, f"  Email : {person['email']}")
        listbox.insert(3, f'  Birthday : {person["birthday_day"]}/{person["birthday_month"]}/{person["birthday_year"]}')
        listbox.insert(4, "\n")

    listbox.grid(row=1, column=0)

    # ADD GO TO HOME BUTTON
    go_to_home_button = Button(text="GO TO HOME", bg=BUTTON_COLOR,
                               fg=MAIN_TEXT_COLOR, width=35, pady=5, command=destroy_birthday_list)
    go_to_home_button.grid(row=5, column=0, pady=5)

def destroy_birthday_list():
    if type(listbox) == type(Listbox()):
        listbox.destroy()
    if type(go_to_home_button) == type(Button()):
        go_to_home_button.destroy()
    go_to_home()

# ==============================================================
# CREATING AND INITIALIZING THE WINDOW
# ==============================================================
window = Tk()
window.minsize(width=800, height=500)
window.maxsize(width=800, height=500)
window.title("Birthday Manager App")
window.config(bg=MAIN_BACKGROUND_COLOR, padx=50, pady=30)

# ==============================================================
# CREATING THE HAPPY BIRTHDAY SECTION ON THE RIGHT SIDE
# ==============================================================
canvas = Canvas(width=400,
                        height=400,
                        bg=MAIN_BACKGROUND_COLOR,
                        highlightthickness=0,)
canvas.grid(row=0, column=1, rowspan=5, padx=(50, 0))

# Creating the canvas image ( HAPPY BIRTHDAY IMAGE )
birthday_image = PhotoImage(file="./happy_birthday.png")
canvas.create_image(200, 200, image=birthday_image)

go_to_home()

window.mainloop()
