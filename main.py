from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password ="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = Email_entry.get()
    password = password_entry.get()
    new_data= {
        website:{
            "email" : email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading of old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            is_ok = messagebox.askokcancel(title=website, message=f"Thease are the details entered: \nEmail: {email} "
                                                                  f"\nPassword:{password}|n Is is ok to save?")

            if is_ok:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website}|{email}|{password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- Find Password ------------------------------- #

def find_password():
    website =  website_entry.get()
    try :
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manger")
windows.config(padx = 50,pady = 50)


canvas = Canvas(width= 200,height=200)
logo_img= PhotoImage(file ="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column = 1 , row =0 )


#labels
website_label = Label(text="Website:")
website_label.grid(column =0, row =1)

email_label = Label(text ="Email/Username:")
email_label.grid(column =0, row = 2)

Password_label = Label(text="Password:")
Password_label.grid(column= 0, row = 3)

#Entry

website_entry = Entry(width=17)
website_entry.grid(column =1, row =1)
website_entry.focus()


Email_entry = Entry(width=35)
Email_entry.grid(column =1  , row =2,columnspan = 2)
Email_entry.focus()
Email_entry.insert(0,"tarunmishra12122002@gmail.com")



password_entry = Entry(width=17)
password_entry.grid(row =3,column =1)

#Buttons

generate_password_button = Button(text ="Generate Password",command=generate_password)
generate_password_button.grid(column = 2, row = 3)

Search_button = Button(text="Search",width=14,command=find_password)
Search_button.grid(column =2, row =1)

Add_button = Button(text="Add", width=30,command=save)
Add_button.grid(column = 1, row = 4,columnspan = 2)





windows.mainloop()