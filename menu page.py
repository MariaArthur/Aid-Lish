from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
import random

root=Tk()

class App:
    def __init__(self, master):
        #master frame
        self.master = master
        #menu frames
        self.start_frame = Frame(master)
        self.login_frame = Frame(master)
        self.userlogin_frame = Frame(master)
        self.adminlogin_frame= Frame(master)
        self.register_frame = Frame(master)
        # user frames
        self.usermenu_frame =Frame(master)
        self.user_useracc_frame = Frame(master)
        self.user_useracc_changepass_frame = Frame(master)
        self.user_useracc_deleteacc_frame = Frame(master)
        self.usermenu_learning_frame = Frame(master)
        self.usermenu_quiz_frame = Frame(master)
        self.usermenu_quiz_credential_frame = Frame(master)
        self.usermenu_progress_frame = Frame(master)
        self.usermenu_WOTD_frame = Frame(master)
        self.usermenu_favlist_frame = Frame(master)
        #admin frames
        self.adminmenu_frame = Frame(master)
        self.admin_adminacc_frame =Frame(master)
        self.admin_adminacc_changepass_frame = Frame(master)
        self.admin_adminacc_del_acc_frame = Frame(master)
        self.admin_adminacc_addnew_frame = Frame(master)
        self.adminmenu_addnotes_frame = Frame(master)
        self.adminmenu_addWOTD_frame = Frame(master)
        self.adminmenu_checkprogress_frame = Frame(master)
        #----------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------------------
        #menu frame/ start frame
        self.title = Label(self.start_frame, text="Welcome to Aid-lish", font=(None,40))
        self.title.pack(pady=(50,100))

        self.login_button = Button(self.start_frame, text="Login", font=(None,20), command= self.show_login, padx=40, pady=10, fg="white", bg='black', width=25)
        self.login_button.pack(pady=(100,20))

        self.register_button = Button(self.start_frame, text="Register A New Account", font=(None,20), command= self.show_register, padx=40, pady=10, fg="white", bg='black', width=25)
        self.register_button.pack(pady=20)
        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #database
        register_conn =sqlite3.connect("database.sqlite")
        register_c=register_conn.cursor()
        register_c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, Quiz TEXT)")

        # register page frame
        self.registerpage_title=Label(self.register_frame, text="Registration", font=(None,40))
        self.registerpage_title.pack(pady=(50,80))
        self.reg_user_entry_label = Label(self.register_frame, text="Enter Your Username", font=(None,20))
        self.reg_user_entry_label.pack(pady=5)
        self.reg_user_entry = Entry(self.register_frame, width=100, borderwidth=10)
        self.reg_user_entry.pack(pady=20)

        self.reg_password_entry_label = Label(self.register_frame, text="Enter Your Password", font=(None,20))
        self.reg_password_entry_label.pack(pady=5)
        self.reg_password_entry = Entry(self.register_frame, width=100, borderwidth=10, show="*")
        self.reg_password_entry.pack(pady=20)

        #Register functions    

        # Write a function to create an new user.
        def reg_create_user():
            reg_username = self.reg_user_entry.get()
            reg_password = self.reg_password_entry.get()

            if reg_username == "" or reg_password == "":
                messagebox.showerror("Error", "Please enter your username and password!")
                return

            if reg_user_exists(reg_username):
                messagebox.showerror("Error", "Please choose another username!")
                self.reg_user_entry.delete(0, END)
                self.reg_password_entry.delete(0, END)
                return

            register_c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (reg_username, reg_password))
            register_conn.commit()
            register_conn.close()

            messagebox.showinfo("Notification", "Registration successful!")

            self.reg_user_entry.delete(0, END)
            self.reg_password_entry.delete(0, END)
            self.show_login()


        def reg_user_exists(reg_username):
            register_c.execute('SELECT * FROM users WHERE username = ?', (reg_username,))
            if register_c.fetchone():
                return True
            return False
        

        #register function button
        self.register_function_button=Button(self.register_frame, text="Create Account", font=(None,20), command= reg_create_user, padx=40, pady=10, fg="white", bg='black', width=25)
        self.register_function_button.pack(pady=10)
        
        #back button in register page
        self.registerback_button = Button(self.register_frame, text="Back", font=(None,20), command= self.show_start, padx=40, pady=10, fg="white", bg='black', width=25)
        self.registerback_button.pack(pady=10)
        #----------------------------------------------------------------------------------------------------------------



        #----------------------------------------------------------------------------------------------------------------
        #login page frame
        self.loginpage_title=Label(self.login_frame, text="Login As ?", font=(None,40) ) 
        self.loginpage_title.pack(pady=(50,100))

        self.userlogin_button= Button(self.login_frame, text="Student", font=(None,20) ,command= self.show_userlogin, padx=40, pady=15, fg="white", bg='black', width=25 )
        self.userlogin_button.pack(pady=20)

        self.adminlogin_button= Button(self.login_frame, text="Lecturer", font=(None,20) ,command= self.show_adminlogin, padx=40, pady=15, fg="white", bg='black', width=25 )
        self.adminlogin_button.pack(pady=20)

        #back button in login page
        self.adminlogin_back_button = Button(self.login_frame, text="Back", font=(None,20), command= self.show_start , padx=40, pady=15, fg="white", bg='black', width=25)
        self.adminlogin_back_button.pack(pady=20)
        #----------------------------------------------------------------------------------------------------------------
        
        #----------------------------------------------------------------------------------------------------------------
        #login as user frame
        self.login_user_entry_label = Label(self.userlogin_frame, text="Username", font=(None,20))
        self.login_user_entry_label.pack(pady= 20)
        self.login_user_entry = Entry(self.userlogin_frame, width=100, borderwidth=10)
        self.login_user_entry.pack(pady=20)

        self.userlogin_password_entry_label = Label(self.userlogin_frame, text="Password", font=(None,20))
        self.userlogin_password_entry_label.pack(pady=20)
        self.userlogin_password_entry = Entry(self.userlogin_frame, width=100, borderwidth=10,show="*")
        self.userlogin_password_entry.pack(pady=20)

        #Database
        userlogin_conn =sqlite3.connect("database.sqlite")
        userlogin_c = userlogin_conn.cursor()
        userlogin_c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, Quiz TEXT)")
        

        #Login functions as user
        def login_user():
            userlogin_username = self.login_user_entry.get()
            userlogin_password = self.userlogin_password_entry.get()

            if userlogin_username == "" or userlogin_password == "":
                messagebox.showerror("Error", "Please enter your username and password!")
                return

            if user_exists(userlogin_username):
                userlogin_c.execute('SELECT * FROM users WHERE username = ?', (userlogin_username,))
                userlogin_c.execute('SELECT password FROM users WHERE username = ?', (userlogin_username,))
                user_db_password = userlogin_c.fetchone()[0]

                if userlogin_password == user_db_password:
                    messagebox.showinfo("Notification", "Login successful!")
                    self.show_useracc()
                else:
                    messagebox.showerror("Error", "Please enter a valid password!")
                    return
            else:
                messagebox.showerror("Error", "Please enter a valid username and password!")
                return 
        
        def user_exists(userlogin_username):
            userlogin_username = self.login_user_entry.get()

            userlogin_c.execute('SELECT * FROM users WHERE username = ?', (userlogin_username,))
            return userlogin_c.fetchone() is not None 

        #user login function button
        self.userlogin_function_button=Button(self.userlogin_frame, text="Login", font=(None,20), command= login_user, padx=40, pady=10, fg="white", bg='black', width=25)
        self.userlogin_function_button.pack(pady=20)

        #back button in user login page
        self.userlogin_back_button = Button(self.userlogin_frame, text="Back", font=(None,20), command= self.show_login, padx=40, pady=10, fg="white", bg='black', width=25)
        self.userlogin_back_button.pack(pady=20)


        #----------------------------------------------------------------------------------------------------------------
        
        #----------------------------------------------------------------------------------------------------------------
        #login as admin frame
        self.login_admin_entry_label = Label(self.adminlogin_frame, text="Admin Username", font=(None,20))
        self.login_admin_entry_label.pack(pady=5)
        self.login_admin_entry = Entry(self.adminlogin_frame, width=100, borderwidth=10)
        self.login_admin_entry.pack(pady=20)

        self.admin_password_entry_label = Label(self.adminlogin_frame, text="Admin Password", font=(None,20))
        self.admin_password_entry_label.pack(pady=5)
        self.admin_password_entry = Entry(self.adminlogin_frame, width=100, borderwidth=10, show="*")
        self.admin_password_entry.pack(pady=20)

        #database
        adminlogin_conn = sqlite3.connect("database.sqlite")
        adminlogin_c = adminlogin_conn.cursor()
        # Create a table to store admin data.
        adminlogin_c.execute('CREATE TABLE IF NOT EXISTS admins(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)')

        def login_admin():
            adminlogin_username = self.login_admin_entry.get()
            adminlogin_password = self.admin_password_entry.get()

            print(f"Username: {adminlogin_username}")  # Debug statement
            print(f"Password: {adminlogin_password}")  # Debug statement
 
            if adminlogin_username == "" or adminlogin_password == "":
                messagebox.showerror("Error", "Please enter your username and password!")
                return

            if admin_login_exists(adminlogin_username):
                adminlogin_c.execute('SELECT * FROM admins WHERE username = ?', (adminlogin_username,))
                adminlogin_c.execute('SELECT password FROM admins WHERE username = ?', (adminlogin_username,))
                admin_db_password = adminlogin_c.fetchone()[0]

                print(f"Database Password: {admin_db_password}")  # Debug statement#(error here)

                if adminlogin_password == admin_db_password:
                    messagebox.showinfo("Notification", "Login successful!")
                    self.show_adminacc()
                else:
                    messagebox.showerror("Error", "Please enter a valid password!")
                    return
            else:
                messagebox.showerror("Error", "Please enter a valid username and password!")
                return 

        # Write a function to check if an admin exists.
        def admin_login_exists(adminlogin_username):
            adminlogin_c.execute('SELECT * FROM admins WHERE username = ?', (adminlogin_username,))
            return adminlogin_c.fetchone() is not None


        #admin login function button
        self.adminlogin_function_button=Button(self.adminlogin_frame, text="Login", font=(None,20), command= login_admin , padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminlogin_function_button.pack(pady=20)
        
        #back button in admin login page
        self.adminlogin_back_button = Button(self.adminlogin_frame, text="Back", font=(None,20), command= self.show_login , padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminlogin_back_button.pack(pady=20)
        #----------------------------------------------------------------------------------------------------------------
        
        #----------------------------------------------------------------------------------------------------------------
        #user authentication frame
        self.user_useracc_title = Label(self.user_useracc_frame, text="User Account Settings", font=(None,20))
        self.user_useracc_title.pack(pady=20)
        self.user_useracc_changepass = Button(self.user_useracc_frame, text="Change Password", font=(None,20),  command= self.show_user_useracc_changepass , padx=40, pady=10, fg="white", bg='black', width=25)
        self.user_useracc_changepass.pack(pady=20)
        self.user_useracc_del_acc = Button(self.user_useracc_frame, text="Delete Account", font=(None,20),  command= self.show_user_useracc_deleteacc, padx=40, pady=10, fg="white", bg='black', width=25)
        self.user_useracc_del_acc.pack(pady=20)
        self.user_useracc_next = Button(self.user_useracc_frame, text="Skip to Menu", font=(None,20),  command= self.show_usermenu , padx=40, pady=10, fg="white", bg='black', width=25)
        self.user_useracc_next.pack(pady=20)
        #----------------------------------------------------------------------------------------------------------------

        #Useracc Change Password frames
        self.user_useracc_changepass_label =Label(self.user_useracc_changepass_frame, text= "Change Password",font=(None,30))
        self.user_useracc_changepass_label.pack(pady=20)
        self.user_useracc_changepass_username_label = Label(self.user_useracc_changepass_frame,font=(None,20), text="Enter Username")
        self.user_useracc_changepass_username_label.pack(pady=5)
        self.user_useracc_changepass_username = Entry(self.user_useracc_changepass_frame, width=50, borderwidth=10)
        self.user_useracc_changepass_username.pack(pady=5)
        self.user_useracc_changepass_oldpass_label = Label(self.user_useracc_changepass_frame,font=(None,20), text="Enter Original Password")
        self.user_useracc_changepass_oldpass_label.pack(pady=5)
        self.user_useracc_changepass_oldpass = Entry(self.user_useracc_changepass_frame, width=50, borderwidth=10, show= "*")
        self.user_useracc_changepass_oldpass.pack(pady=5)
        self.user_useracc_changepass_newpass_label = Label(self.user_useracc_changepass_frame,font=(None,20), text="Enter New Password")
        self.user_useracc_changepass_newpass_label.pack(pady=5)
        self.user_useracc_changepass_newpass = Entry(self.user_useracc_changepass_frame, width=50, borderwidth=10,show="*")
        self.user_useracc_changepass_newpass.pack(pady=5)

        #database
        user_changepass_conn = sqlite3.connect('database.sqlite')
        user_cp_c = user_changepass_conn.cursor()
        # Create a table to store user data.
        user_cp_c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, Quiz TEXT)')

       
        #Functions
        def changepass_user_exists():
            user_changepass_username = self.user_useracc_changepass_username.get()
            user_cp_c.execute('SELECT * FROM users WHERE username = ?', [user_changepass_username,])
            return user_cp_c.fetchone() is not None
        
        def user_changepass():
            user_changepass_username = self.user_useracc_changepass_username.get()
            user_changepass_oldpass = self.user_useracc_changepass_oldpass.get()
            user_changepass_newpass = self.user_useracc_changepass_newpass.get()

            if user_changepass_username=="" or user_changepass_oldpass=="" or user_changepass_newpass=="":
                messagebox.showerror("Error", "Please enter your username and passwords!")
                return
            
            if changepass_user_exists():
                user_cp_c.execute('SELECT * FROM users WHERE username = ?', [user_changepass_username])
                user_cp_c.execute('SELECT password FROM users WHERE username = ?', (user_changepass_username,))
                db_oldpass = user_cp_c.fetchone()[0]

                if user_changepass_oldpass == db_oldpass:
                    user_cp_c.execute('UPDATE users SET password = ? WHERE username = ?', (user_changepass_newpass, user_changepass_username,))
                    user_changepass_conn.commit()
                    messagebox.showinfo('Notification', "Password changed successfully!")
                    self.show_useracc()
                else:
                    messagebox.showerror("Error", "Please enter a valid password!")
                    return
            else:
                messagebox.showerror("Error", "Please enter a valid username and password!")
                return 


            

        #User Changepass  function button
        self.user_changepass_function_button=Button(self.user_useracc_changepass_frame, text="Change Password", font=(None,20), command= user_changepass, padx=40, pady=10, fg="white", bg='black', width=25)
        self.user_changepass_function_button.pack(pady=20)
        
        #back button 
        self.user_changepass_back_button = Button(self.user_useracc_changepass_frame, text="Back", font=(None,20), command= self.show_useracc , padx=40, pady=10, fg="white", bg='black', width=25)
        self.user_changepass_back_button.pack(pady=20)

        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #User delete acc frame
        self.user_useracc_delacc_label =Label(self.user_useracc_deleteacc_frame, text= "Delete Account",font=(None,30))
        self.user_useracc_delacc_label.pack(pady=20)
        self.user_useracc_delacc_username_label = Label(self.user_useracc_deleteacc_frame,font=(None,20), text="Enter Username")
        self.user_useracc_delacc_username_label.pack(pady=10)
        self.user_useracc_delacc_username = Entry(self.user_useracc_deleteacc_frame, width=50, borderwidth=10)
        self.user_useracc_delacc_username.pack(pady=10)
        self.user_useracc_delacc_password_label = Label(self.user_useracc_deleteacc_frame,font=(None,20), text="Enter Password")
        self.user_useracc_delacc_password_label.pack(pady=10)
        self.user_useracc_delacc_password = Entry(self.user_useracc_deleteacc_frame, width=50, borderwidth=10, show= "*")
        self.user_useracc_delacc_password.pack(pady=10)

        #database
        user_deleteacc_conn = sqlite3.connect('database.sqlite')
        user_deleteacc_c = user_deleteacc_conn.cursor()
        # Create a table to store user data.
        user_deleteacc_c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, Quiz TEXT)')

        
        #function for delete account
        def user_delete_account():
            user_delacc_username = self.user_useracc_delacc_username.get()
            user_delacc_password = self.user_useracc_delacc_password.get()

            if user_delacc_username == "" or user_delacc_password == "":
                messagebox.showerror("Error", "Please enter your username and password!")
                return

            if user_exists(user_delacc_username):
                userlogin_c.execute('SELECT password FROM users WHERE username = ?', (user_delacc_username,))
                db_password = userlogin_c.fetchone()

                if db_password is not None and user_delacc_password == db_password[0]:
                    user_deleteacc_c.execute('DELETE from users WHERE username = ?', (user_delacc_username,))
                    user_deleteacc_conn.commit()
                    messagebox.showinfo("Notification", "Account Deleted!")
                    log_out(root)
                else:
                    messagebox.showerror("Error", "Please enter a valid password!")
                    return
            else:
                messagebox.showerror("Error", "Please enter a valid username and password!")
                return


        #user delete acc function button
        self.useracc_delacc_password_function_button=Button(self.user_useracc_deleteacc_frame, text="Delete", font=(None,20), command= user_delete_account, padx=40, pady=10, fg="white", bg='black', width=25)
        self.useracc_delacc_password_function_button.pack(pady=20)
        
        #back button 
        self.useracc_delacc_password_back_button = Button(self.user_useracc_deleteacc_frame, text="Back", font=(None,20), command= self.show_useracc , padx=40, pady=10, fg="white", bg='black', width=25)
        self.useracc_delacc_password_back_button.pack(pady=20)

        #----------------------------------------------------------------------------------------------------------------
        
        #----------------------------------------------------------------------------------------------------------------
        #user menu frame
        self.usermenu_title = Label(self.usermenu_frame, text="User Menu", font=(None,20))
        self.usermenu_title.pack(pady=20)
        self.usermenu_learning = Button(self.usermenu_frame, text="Learning", font=(None,20),  command= self.show_usermenu_learning , padx=40, pady=10, fg="white", bg='black', width=25)
        self.usermenu_learning.pack(pady=10)

        self.usermenu_quiz = Button(self.usermenu_frame, text="Quiz", font=(None,20),  command= self.show_usermenu_quiz , padx=40, pady=10, fg="white", bg='black', width=25)
        self.usermenu_quiz.pack(pady=10)

        self.usermenu_progress = Button(self.usermenu_frame, text="Your Progress", font=(None,20),  command= self.show_usermenu_progress , padx=40, pady=10, fg="white", bg='black', width=25)
        self.usermenu_progress.pack(pady=10)

        self.usermenu_WOTD = Button(self.usermenu_frame, text="Word of The Day", font=(None,20),  command= self.show_usermenu_WOTD , padx=40, pady=10, fg="white", bg='black', width=25)
        self.usermenu_WOTD.pack(pady=10)

        self.usermenu_favlist = Button(self.usermenu_frame, text="Favourite List", font=(None,20),  command= self.show_usermenu_favlist , padx=40, pady=10, fg="white", bg='black', width=25)
        self.usermenu_favlist.pack(pady=10)

        self.usermenu_logout = Button(self.usermenu_frame, text="Log Out & Exit", font=(None,20),  command=lambda: log_out(root) , padx=40, pady=10, fg="white", bg='black', width=25)
        self.usermenu_logout.pack(pady=10)
        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #User menu Learning Frame
        # Create a Treeview Frame
        learning_tree_frame = Frame(self.usermenu_learning_frame)
        learning_tree_frame.pack(pady=10)

        #Create a Treeview Scrollbar
        learning_tree_scroll = Scrollbar(learning_tree_frame)
        learning_tree_scroll.pack(side=RIGHT, fill=Y)

        # Create the Treeview
        learning_my_tree = ttk.Treeview(learning_tree_frame, yscrollcommand=learning_tree_scroll.set, selectmode="extended")
        learning_my_tree.pack()

        # Configure the Scrollbar
        learning_tree_scroll.config(command=learning_my_tree.yview)

        # Define Our Columns
        learning_my_tree['columns'] = ("Title", "Description", "Example")

        # Format Our Columns
        learning_my_tree.column("#0", width=0, stretch=NO)
        learning_my_tree.column("Title", anchor=W, width=140)
        learning_my_tree.column("Description", anchor=CENTER, width=500)
        learning_my_tree.column("Example", anchor=W, width=500)

        # Create Headings
        learning_my_tree.heading("#0", text="", anchor=W)
        learning_my_tree.heading("Title", text="Title", anchor=W)
        learning_my_tree.heading("Description", text="Description", anchor=CENTER)
        learning_my_tree.heading("Example", text="Example", anchor=W)

        # Create Striped Row Tags
        learning_my_tree.tag_configure('oddrow', background="white")
        learning_my_tree.tag_configure('evenrow', background="lightblue")


        # Back Button ( ADD command to sambung Ham's User Menu )
        learning_back_btn = Button(self.usermenu_learning_frame, text="Return to User Menu", command=self.show_usermenu , fg="white", bg='black', width=25)
        learning_back_btn.pack()

        # Database code
        # Connect to the database that exists
        conn_learning = sqlite3.connect('notes.db')

        # Create a cursor instance
        c_learning = conn_learning.cursor()

        # Create the table 
        # This should be deleted when buddy's database is added.
        c_learning.execute("""CREATE TABLE IF NOT EXISTS notes (
                title TEXT,
                description TEXT,
                example TEXT
                  )
                """)

        # Commit changes
        conn_learning.commit()

        # Close the connection
        conn_learning.close()

        # Query Database function
        def learning_query_database():
            # Connect to the database that exists
            conn_learning = sqlite3.connect('notes.db')

            # Create a cursor instance
            c_learning = conn_learning.cursor()

            c_learning.execute("SELECT * FROM notes")
            records = c_learning.fetchall()

            # Add data to the screen
            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    learning_my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
                else:
                    learning_my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))
                # increment counter
                count += 1

            # Commit changes
            conn_learning.commit()

            # Close the connection
            conn_learning.close()

        # Call the query_database function to load data on start
        learning_query_database()
        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        # User menu Quiz functions and add ons in frames
        # Database
        conn_quiz = sqlite3.connect('database.sqlite')

        # Create a cursor instance
        c_quiz= conn_quiz.cursor()

        # Create Table 
        # This should be deleted when Ben's database is added in.
        c_quiz.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, Quiz TEXT)")

        # Commit the changes
        conn_quiz.commit()

        # Close the connection
        conn_quiz.close()

        # List for the question and options
        self.usermenu_quiz_questions = []
        self.usermenu_quiz_options = []

        # # User menu Quiz Credential Frame
        # self.usermenu_quiz_credential_username_label = Label(self.usermenu_quiz_credential_frame, text="Username", font= ("Verdana",20))
        # self.usermenu_quiz_credential_username_label.pack()
        # self.usermenu_quiz_credential_username_entry = Entry(self.usermenu_quiz_credential_frame, font=("Verdana", 20), borderwidth=5)
        # self.usermenu_quiz_credential_username_entry.pack()

        # self.usermenu_quiz_submit_credential = Button(self.usermenu_quiz_credential_frame, text="Submit",fg="white" , bg="black", command= self.usermenu_quiz_credential_submit )
        # self.usermenu_quiz_submit_credential.pack()

        # User menu Quiz Frame
        self.usermenu_quiz_placehold = Frame(self.usermenu_quiz_frame, padx=10, pady=10, bg='#fff')
        self.usermenu_quiz_label = Label(self.usermenu_quiz_placehold, height=5, width=28, bg='#ddd', font=('Verdana', 20), wraplength=500)
        # Make the variables
        # StringVar() holds a string data where we can set text value and can retrieve it
        v1 = StringVar(self.usermenu_quiz_placehold)
        v2 = StringVar(self.usermenu_quiz_placehold)
        v3 = StringVar(self.usermenu_quiz_placehold)
        v4 = StringVar(self.usermenu_quiz_placehold)

        # Radiobutton to choose the answer
        option1 = Radiobutton(self.usermenu_quiz_placehold, bg='#fff', variable=v1, font=('Verdana', 20), command=lambda: usermenu_quiz_checkAnswer(option1))
        option2 = Radiobutton(self.usermenu_quiz_placehold, bg='#fff', variable=v2, font=('Verdana', 20), command=lambda: usermenu_quiz_checkAnswer(option2))
        option3 = Radiobutton(self.usermenu_quiz_placehold, bg='#fff', variable=v3, font=('Verdana', 20), command=lambda: usermenu_quiz_checkAnswer(option3))
        option4 = Radiobutton(self.usermenu_quiz_placehold, bg='#fff', variable=v4, font=('Verdana', 20), command=lambda: usermenu_quiz_checkAnswer(option4))

        # Button for the user to click next
        self.usermenu_quiz_next_btn = Button(self.usermenu_quiz_placehold, text='Next', font=('Verdana', 20), command=lambda: usermenu_quiz_displayNextQuestion(),fg="white", bg='black')
        self.usermenu_quiz_return_btn = Button(self.usermenu_quiz_placehold, text='Return to User Menu', font=('Verdana', 20), command = self.show_usermenu,fg="white", bg='black')
        

        # Display the frame, label, radiobuttons & button when the program run
        self.usermenu_quiz_placehold.pack()
        self.usermenu_quiz_label.grid(sticky='we', row=0, column=0)

        option1.grid(sticky='we', row=1, column=0)
        option2.grid(sticky='we', row=2, column=0)
        option3.grid(sticky='we', row=3, column=0)
        option4.grid(sticky='we', row=4, column=0)

        self.usermenu_quiz_next_btn.grid(row=5, column=0)

        self.usermenu_quiz_index = 0
        self.usermenu_quiz_correct = 0

        # Function to disable the button so user cannot choose a different answer once radiobutton is clicked
        def usermenu_quiz_disableButtons(state):
            option1['state'] = state
            option2['state'] = state
            option3['state'] = state
            option4['state'] = state

        # Function to check the selected answer
        def usermenu_quiz_checkAnswer(radio):   
            # options is the database
            # the 4th item is the correct answer
            # we will check the user-selected answer with the 4th item
            if radio['text'] == self.usermenu_quiz_options[self.usermenu_quiz_index][3]:
                self.usermenu_quiz_correct += 1

            self.usermenu_quiz_index += 1
            # set state=DISABLED to gray out the control and make it unresponsive so the user cannot click the radiobutton once the button is clicked
            usermenu_quiz_disableButtons('disable')
        
        # Restarts the quiz after the quiz has been attempeted by the use
        # def usermenu_quiz_restart():
        #     self.usermenu_quiz_index = 0
        #     self.usermenu_quiz_correct = 0
        #     usermenu_quiz_displayNextQuestion()

        # Function to display the next question
        def usermenu_quiz_displayNextQuestion():
            # Load questions and options from the text file
            # Get the directory path of the current script
            quiz_data_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the file path
            quiz_data_file_path = os.path.join(quiz_data_dir, "quiz_data.txt")
            if not self.usermenu_quiz_questions:
                with open(quiz_data_file_path, 'r') as file:
                    lines = file.readlines()

                    for i in range(0, len(lines), 2):
                        question = lines[i].strip()
                        options_list = lines[i + 1].strip().split('|')
                
                        # the questions and options from the text file is inserted into their respective list
                        self.usermenu_quiz_questions.append(question)
                        self.usermenu_quiz_options.append(options_list)

            # Stop displaying the Next Question            
            if self.usermenu_quiz_index == len(self.usermenu_quiz_options):
                percentage = (self.usermenu_quiz_correct / len(self.usermenu_quiz_options)) * 100

                self.usermenu_quiz_label['text'] = f"{self.usermenu_quiz_correct} / {len(self.usermenu_quiz_options)}\n" # Display how much they got correct over total questions
                student_score = f"{percentage:.0f}%" # make a student score variable to store the into data (.0f = so there is no decimal places)
                self.usermenu_quiz_label['text'] += student_score # Display the percentage 
        
                # Disable the radiobuttons
                usermenu_quiz_disableButtons('disable')
        
                # Update the quiz column in the database
                conn = sqlite3.connect('database.sqlite')
                c = conn.cursor()
                userlogin_username = self.login_user_entry.get()
                c.execute("UPDATE users SET Quiz = ? WHERE username = ?", (student_score, userlogin_username))
                messagebox.showinfo("Congratulations!!!!", "Thank you and congratulations for succussfully answering the quiz!!!")
                conn.commit()
                conn.close()
        
                # Change the text of the Next button to "Return to User Menu" ---------------------------------------------------------------------------------------------------------------------------------------------
                self.usermenu_quiz_next_btn.grid_forget()
                self.usermenu_quiz_return_btn.grid(row=5, column=0)

            else:
                # Continue to show the next question
                self.usermenu_quiz_label['text'] = self.usermenu_quiz_questions[self.usermenu_quiz_index]

                usermenu_quiz_disableButtons('normal')
        
                # opts is the index for options(database)
                opts = self.usermenu_quiz_options[self.usermenu_quiz_index]
                option1['text'] = opts[0]
                option2['text'] = opts[1]
                option3['text'] = opts[2]
                option4['text'] = opts[3]

                v1.set(opts[0])
                v2.set(opts[1])
                v3.set(opts[2])
                v4.set(opts[3])

        usermenu_quiz_displayNextQuestion() 
        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #User menu WOTD
        self.usermenu_WOTD_title = Label(self.usermenu_WOTD_frame, text="Word of The Day", font=(None,20))
        self.usermenu_WOTD_title.pack(pady=20)

        # Connect to database that exists
        usermenu_WOTD_conn = sqlite3.connect('wotd.db')

        # Create a cursor instance
        usermenu_WOTD_c = usermenu_WOTD_conn.cursor()

        usermenu_WOTD_c.execute("""CREATE TABLE if not exists wordoftheday (
            title text,
            description text,
            example text
            )
            """)

        # Commit changes
        usermenu_WOTD_conn.commit()

        # Close our connection
        usermenu_WOTD_conn.close()

        # Query Database
        def usermenu_WOTD_query_database():
            # Create a database or connect to one that exists
            usermenu_WOTD_conn = sqlite3.connect('wotd.db')

            # Create a cursor instance
            usermenu_WOTD_c = usermenu_WOTD_conn.cursor()

            usermenu_WOTD_c.execute("SELECT * FROM wordoftheday")
            records = usermenu_WOTD_c.fetchall()

            # Check if there are records in the list
            if records:

            # Randomize the order of tuples
                random.shuffle(records)

            # Create a text variable to store the records
                records_text = ""

            # Format the records as text # 
            
                record = records[0] # Prevent from displaying all the data, just one of the data
                record_text = "Word: " + record[0] + "\n\n"
                record_text += "Description: " + record[1] + "\n\n"
                record_text += "Example: " + record[2] + "\n\n\n"

                records_text += record_text
            

            # Create a label to display the records
                query_label = Label(self.usermenu_WOTD_frame, text=records_text)
                query_label.pack()

            else:
                print("No records found")


            # Commit changes
            usermenu_WOTD_conn.commit()

            # Close the connections
            usermenu_WOTD_conn.close()
        # Run to pull data from database on start
        usermenu_WOTD_query_database()

        # Back Button
        usermenu_WOTD_back_btn = Button(self.usermenu_WOTD_frame, text="Return to User Menu", command=self.show_usermenu,fg="white", bg='black')
        usermenu_WOTD_back_btn.pack()

        #----------------------------------------------------------------------------------------------------------------
        
        #----------------------------------------------------------------------------------------------------------------
        #User menu check progress
        #Connect to Database
        global check_user_progress   
        
        def check_user_progress():
            usermenu_progress_conn = sqlite3.connect('database.sqlite')
            usermenu_progress_c = usermenu_progress_conn.cursor()
            usermenu_progress_c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, Quiz TEXT)')
            userlogin_username = self.login_user_entry.get()
            usermenu_progress_c.execute("SELECT Quiz FROM users WHERE username = ?", (userlogin_username,))
            global result
            result = usermenu_progress_c.fetchone()[0]
            usermenu_progress_quiz_mark_label.config(text=f"Quiz Mark: {result}")
            print(result)

                

        # Labels
        usermenu_progress_progress_lbl = Label(self.usermenu_progress_frame, text="Your Progress", font=("Verdana", 40))
        usermenu_progress_progress_lbl.pack(pady=20)
        # Quiz Mark Label
        usermenu_progress_quiz_mark_label = Label(self.usermenu_progress_frame, text=("Quiz Mark:"), font=("Verdana", 20))
        usermenu_progress_quiz_mark_label.pack(pady=10)
        # Back Button
        usermenu_progress_back_btn = Button(self.usermenu_progress_frame, text="Return to user menu", fg="white", bg='black', command=self.show_usermenu)
        usermenu_progress_back_btn.pack(pady=10)            

        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #User menu Favlist
        usermenu_favlist_label = Label(self.usermenu_favlist_frame, text="Favourite Note", font=(NONE,40))
        usermenu_favlist_label.pack()


        # Database (Should be in admin feature not learning for user)
        # Connect to database that exists
        usermenu_favlist_conn = sqlite3.connect('notes.db')

        # Create a cursor instance
        usermenu_favlist_c = usermenu_favlist_conn.cursor()

        # Create Table (this is suppose to be in buddy's "admin add new notes feature")
        # This should be deleted when buddy's database is added in.
        usermenu_favlist_c.execute("""CREATE TABLE if not exists note (
            title text,
            description text,
            example text
            )
            """)

        # Database
        usermenu_favlist_conn2 = sqlite3.connect('database.sqlite')

        # Create a cursor instance
        usermenu_favlist_c2 = usermenu_favlist_conn2.cursor()

        # Create Table (this is supposed to be in Ben's feature)
        # This should be deleted when Ben's database is added in.
        usermenu_favlist_c2.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, Quiz TEXT)")

        # Commit the changes
        usermenu_favlist_conn2.commit()

        # Close the connection
        usermenu_favlist_conn2.close()

        # Query Database
        def usermenu_favlist_query_database():
            # Create a database or connect to one that exists
            usermenu_favlist_conn = sqlite3.connect('notes.db')
            
            # Create a cursor instance
            usermenu_favlist_c = usermenu_favlist_conn.cursor()
            
            usermenu_favlist_c.execute("SELECT * FROM notes")
            records = usermenu_favlist_c.fetchall()
            
            # Add our data to the screen
            count = 0
            
            for record in records:
                if count % 2 == 0:
                    usermenu_favlist_my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
                else:
                    usermenu_favlist_my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))
                # increment counter
                count += 1
            
            
            # Commit changes
            usermenu_favlist_conn.commit()
            
            # Close our connection
            usermenu_favlist_conn.close()

        def usermenu_favlist_search_database():
            # Clear the treeview
            usermenu_favlist_my_tree.delete(*usermenu_favlist_my_tree.get_children())

            # Create a database or connect to an existing one
            usermenu_favlist_conn = sqlite3.connect('notes.db')

            # Create a cursor instance
            usermenu_favlist_c = usermenu_favlist_conn.cursor()

            # Search the database for records matching the keyword
            keyword = usermenu_favlist_search_entry.get()
            usermenu_favlist_c.execute("SELECT * FROM notes WHERE title LIKE ? OR description LIKE ? OR example LIKE ?",
                    ('%{}%'.format(keyword), '%{}%'.format(keyword), '%{}%'.format(keyword)))
            records = usermenu_favlist_c.fetchall()

            # Add the matching records to the treeview
            count = 0
            for record in records:
                if count % 2 == 0:
                    usermenu_favlist_my_tree.insert(parent='', index='end', iid=count, text="",
                                values=(record[0], record[1], record[2]), tags=('evenrow',))
                else:
                    usermenu_favlist_my_tree.insert(parent='', index='end', iid=count, text="",
                                values=(record[0], record[1], record[2]), tags=('oddrow',))
                count += 1

            # Commit changes
            usermenu_favlist_conn.commit()

            # Close the connection
            usermenu_favlist_conn.close()

        # Create a reset function
        def  usermenu_favlist_reset_treeview():
            # Clear the search entry
            usermenu_favlist_search_entry.delete(0, END)

            # Clear the treeview
            usermenu_favlist_my_tree.delete(*usermenu_favlist_my_tree.get_children())

            # Query the database to display the initial data
            usermenu_favlist_query_database()

        #Widgets
        # Create a search entry widget
        usermenu_favlist_search_entry = Entry(self.usermenu_favlist_frame)
        usermenu_favlist_search_entry.pack()

        # Create a search button
        usermenu_favlist_search_button = Button(self.usermenu_favlist_frame, text="Search", command=usermenu_favlist_search_database, fg="white", bg="black")
        usermenu_favlist_search_button.pack(pady=5)

        # Create a reset button
        usermenu_favlist_reset_button = Button(self.usermenu_favlist_frame, text="Reset", command=usermenu_favlist_reset_treeview, fg="white", bg="black")
        usermenu_favlist_reset_button.pack(pady=5)

        # Add Some Style
        usermenu_favlist_style = ttk.Style()

        # Pick a Theme
        usermenu_favlist_style.theme_use('default')

        # Configure the Treeview Colors
        usermenu_favlist_style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=20,
                fieldbackground="#D3D3D3")

        # Create a Treeview Frame
        usermenu_favlist_tree_frame = Frame(self.usermenu_favlist_frame)
        usermenu_favlist_tree_frame.pack(pady=10)

        # Create a Treeview Scrollbar
        usermenu_favlist_tree_scroll = Scrollbar(usermenu_favlist_tree_frame)
        usermenu_favlist_tree_scroll.pack(side=RIGHT, fill=Y)

        # Create the Treeview
        usermenu_favlist_my_tree = ttk.Treeview(usermenu_favlist_tree_frame, yscrollcommand=usermenu_favlist_tree_scroll.set, selectmode="extended")
        usermenu_favlist_my_tree.pack()

        # Configure the Scrollbar
        usermenu_favlist_tree_scroll.config(command=usermenu_favlist_my_tree.yview)

        # Define Our Columns
        usermenu_favlist_my_tree['columns'] = ("Title", "Description", "Example")

        # Format Our Columns
        usermenu_favlist_my_tree.column("#0", width=0, stretch=NO)
        usermenu_favlist_my_tree.column("Title", anchor=W, width=140)
        usermenu_favlist_my_tree.column("Description", anchor=CENTER, width=500)
        usermenu_favlist_my_tree.column("Example", anchor=W, width=500)

        # Create Headings
        usermenu_favlist_my_tree.heading("#0", text="", anchor=W)
        usermenu_favlist_my_tree.heading("Title", text="Title", anchor=W)
        usermenu_favlist_my_tree.heading("Description", text="Description", anchor=CENTER)
        usermenu_favlist_my_tree.heading("Example", text="Example", anchor=W)

        # Create Striped Row Tags
        usermenu_favlist_my_tree.tag_configure('oddrow', background="white")
        usermenu_favlist_my_tree.tag_configure('evenrow', background="lightblue")

        # Create Add Note Feature

        def usermenu_favlist_student_note():
            
            # Get the input by user from entry widget and remove leading/trailing spaces 
            note = usermenu_favlist_Student_entry.get().strip()
            
            # Creating a label to display the input (note)
            # Add the note to the listbox if it's not empty
            while note != '':
                usermenu_favlist_my_listbox.insert(END, note)
                break
            else:
                messagebox.showerror("Error","Please input your notes!")
                return
            
            # Resets / clears the entry widget
            usermenu_favlist_Student_entry.delete(0, END)

        # Delete the selected note
        def delete():
            # Anchor is to let user to click the note and delete it
            usermenu_favlist_my_listbox.delete(ANCHOR)

        # Labels
        usermenu_favlist_Student_label = Label(self.usermenu_favlist_frame, text="Notes")
        usermenu_favlist_Student_label.pack()
        usermenu_favlist_Student_entry = Entry(self.usermenu_favlist_frame, width=150)
        usermenu_favlist_Student_entry.pack()
        usermenu_favlist_Student_btn = Button(self.usermenu_favlist_frame, text="Add Note", command=usermenu_favlist_student_note, fg="white", bg="black")
        usermenu_favlist_Student_btn.pack()
        # Delete Button
        usermenu_favlist_delete_btn = Button(self.usermenu_favlist_frame, text="Delete", command=delete, fg="white", bg="black")
        usermenu_favlist_delete_btn.pack()

        # Back Button
        usermenu_favlist_back_btn = Button(self.usermenu_favlist_frame, text="Return to User Menu", fg="white", bg="black", command= self.show_usermenu)
        usermenu_favlist_back_btn.pack()

        # Listbox
        usermenu_favlist_my_listbox = Listbox(self.usermenu_favlist_frame, width=150)
        usermenu_favlist_my_listbox.pack(pady=15)

       

        # Run to pull data from database on start
        usermenu_favlist_query_database()
        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #admin acc authentication frame
        self.admin_adminacc_title = Label(self.admin_adminacc_frame, text="Admin Account Settings", font=(None,20))
        self.admin_adminacc_title.pack(pady=20)
        self.admin_adminacc_changepass = Button(self.admin_adminacc_frame, text="Change Password", font=(None,20), command= self.show_admin_adminacc_changepass , padx=40, pady=10, fg="white", bg='black', width=25)
        self.admin_adminacc_changepass.pack(pady=20)
        self.admin_adminacc_del_acc = Button(self.admin_adminacc_frame, text="Delete Account", font=(None,20),  command= self.show_admin_adminacc_del_acc, padx=40, pady=10, fg="white", bg='black', width=25)
        self.admin_adminacc_del_acc.pack(pady=20)
        self.admin_adminacc_addnew = Button(self.admin_adminacc_frame, text="Add New Admin Account", font=(None,20),  command= self.show_admin_adminacc_addnew, padx=40, pady=10, fg="white", bg='black', width=25)
        self.admin_adminacc_addnew.pack(pady=20)
        self.admin_adminacc_next = Button(self.admin_adminacc_frame, text="Skip to Menu", font=(None,20),  command= self.show_adminmenu , padx=40, pady=10, fg="white", bg='black', width=25)
        self.admin_adminacc_next.pack(pady=20)
        #----------------------------------------------------------------------------------------------------------------
        #Admin acc Change password functions and frame
        self.admin_adminacc_changepass_label =Label(self.admin_adminacc_changepass_frame, text= "Change Password",font=(None,30))
        self.admin_adminacc_changepass_label.pack(pady=20)
        self.admin_adminacc_changepass_username_label = Label(self.admin_adminacc_changepass_frame,font=(None,20), text="Enter Username")
        self.admin_adminacc_changepass_username_label.pack(pady=5)
        self.admin_adminacc_changepass_username = Entry(self.admin_adminacc_changepass_frame, width=50, borderwidth=10)
        self.admin_adminacc_changepass_username.pack(pady=5)
        self.admin_adminacc_changepass_oldpass_label = Label(self.admin_adminacc_changepass_frame,font=(None,20), text="Enter Original Password")
        self.admin_adminacc_changepass_oldpass_label.pack(pady=5)
        self.admin_adminacc_changepass_oldpass = Entry(self.admin_adminacc_changepass_frame, width=50, borderwidth=10, show= "*")
        self.admin_adminacc_changepass_oldpass.pack(pady=5)
        self.admin_adminacc_changepass_newpass_label = Label(self.admin_adminacc_changepass_frame,font=(None,20), text="Enter New Password")
        self.admin_adminacc_changepass_newpass_label.pack(pady=5)
        self.admin_adminacc_changepass_newpass = Entry(self.admin_adminacc_changepass_frame, width=50, borderwidth=10,show="*")
        self.admin_adminacc_changepass_newpass.pack(pady=5)

        #database
        admin_changepass_conn = sqlite3.connect('database.sqlite')
        admin_cp_c = admin_changepass_conn.cursor()
        # Create a table to store user data.
        admin_cp_c.execute('CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)')

       
        #Functions
        def changepass_admin_exists():
            admin_changepass_username = self.admin_adminacc_changepass_username.get()
            admin_cp_c.execute('SELECT * FROM admins WHERE username = ?', [admin_changepass_username,])
            return admin_cp_c.fetchone() is not None
        
        def admin_changepass():
            admin_changepass_username = self.admin_adminacc_changepass_username.get()
            admin_changepass_oldpass = self.admin_adminacc_changepass_oldpass.get()
            admin_changepass_newpass = self.admin_adminacc_changepass_newpass.get()

            if admin_changepass_username=="" or admin_changepass_oldpass=="" or admin_changepass_newpass=="":
                messagebox.showerror("Error", "Please enter your username and passwords!")
                return
            
            if changepass_admin_exists():
                admin_cp_c.execute('SELECT * FROM admins WHERE username = ?', [admin_changepass_username])
                admin_cp_c.execute('SELECT password FROM admins WHERE username = ?', (admin_changepass_username,))
                db_oldpass = admin_cp_c.fetchone()[0]

                if  admin_changepass_oldpass == db_oldpass:
                    admin_cp_c.execute('UPDATE admins SET password = ? WHERE username = ?', (admin_changepass_newpass, admin_changepass_username,))
                    admin_changepass_conn.commit()
                    messagebox.showinfo('Notification', "Password changed successfully!")
                    self.show_adminacc()
                else:
                    messagebox.showerror("Error", "Please enter a valid password!")
                    return
            else:
                messagebox.showerror("Error", "Please enter a valid username and password!")
                return 
  

        #User Changepass  function button
        self.admin_changepass_function_button=Button(self.admin_adminacc_changepass_frame, text="Change Password", font=(None,20), command= admin_changepass, padx=40, pady=10, fg="white", bg='black', width=25)
        self.admin_changepass_function_button.pack(pady=20)
        
        #back button 
        self.admin_changepass_back_button = Button(self.admin_adminacc_changepass_frame, text="Back", font=(None,20), command= self.show_adminacc , padx=40, pady=10, fg="white", bg='black', width=25)
        self.admin_changepass_back_button.pack(pady=20)
        
        #----------------------------------------------------------------------------------------------------------------
        # Admin acc del acc Frame and functions
        self.admin_adminacc_delacc_label =Label(self.admin_adminacc_del_acc_frame, text= "Delete Account",font=(None,30))
        self.admin_adminacc_delacc_label.pack(pady=20)
        self.admin_adminacc_delacc_username_label = Label(self.admin_adminacc_del_acc_frame,font=(None,20), text="Enter Username")
        self.admin_adminacc_delacc_username_label.pack(pady=10)
        self.admin_adminacc_delacc_username = Entry(self.admin_adminacc_del_acc_frame, width=50, borderwidth=10)
        self.admin_adminacc_delacc_username.pack(pady=10)
        self.admin_adminacc_delacc_password_label = Label(self.admin_adminacc_del_acc_frame,font=(None,20), text="Enter Password")
        self.admin_adminacc_delacc_password_label.pack(pady=10)
        self.admin_adminacc_delacc_password = Entry(self.admin_adminacc_del_acc_frame, width=50, borderwidth=10, show= "*")
        self.admin_adminacc_delacc_password.pack(pady=10)

        #database
        admin_deleteacc_conn = sqlite3.connect('database.sqlite')
        admin_deleteacc_c = admin_deleteacc_conn.cursor()
        # Create a table to store user data.
        admin_deleteacc_c.execute('CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)')

        
        #function for delete account
        def admin_delete_account():
            admin_delacc_username = self.admin_adminacc_delacc_username.get()
            admin_delacc_password = self.admin_adminacc_delacc_password.get()

            if admin_delacc_username == "" or admin_delacc_password == "":
                messagebox.showerror("Error", "Please enter your username and password!")
                return

            if admin_del_exists(admin_delacc_username):
                admin_deleteacc_c.execute('SELECT password FROM admins WHERE username = ?', (admin_delacc_username,))
                db_password = admin_deleteacc_c.fetchone()

                if db_password is not None and admin_delacc_password == db_password[0]:
                    admin_deleteacc_c.execute('DELETE from admins WHERE username = ?', (admin_delacc_username,))
                    admin_deleteacc_conn.commit()
                    messagebox.showinfo("Notification", "Account Deleted!")
                    log_out(root)
                else:
                    messagebox.showerror("Error", "Please enter a valid password!")
                    return
            else:
                messagebox.showerror("Error", "Please enter a valid username and password!")
                return
            
        # Write a function to check if an admin exists.
        def admin_del_exists(admin_delacc_username):
            admin_deleteacc_c.execute('SELECT * FROM admins WHERE username = ?', (admin_delacc_username,))
            return admin_deleteacc_c.fetchone() is not None


        #user delete acc function button
        self.adminacc_delacc_password_function_button=Button(self.admin_adminacc_del_acc_frame, text="Delete", font=(None,20), command= admin_delete_account, padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminacc_delacc_password_function_button.pack(pady=20)
        
        #back button 
        self.adminacc_delacc_password_back_button = Button(self.admin_adminacc_del_acc_frame, text="Back", font=(None,20), command= self.show_adminacc , padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminacc_delacc_password_back_button.pack(pady=20)
        #----------------------------------------------------------------------------------------------------------------
        # Admin acc register new admins frames and functions
         #database
        admin_register_conn =sqlite3.connect("database.sqlite")
        admin_register_c=admin_register_conn.cursor()
        admin_register_c.execute("CREATE TABLE IF NOT EXISTS admins(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)")

        # register page frame
        self.admin_registerpage_title=Label(self.admin_adminacc_addnew_frame, text="Register New Admin", font=(None,40))
        self.admin_registerpage_title.pack(pady=(50,80))
        self.admin_reg_entry_label = Label(self.admin_adminacc_addnew_frame, text="Enter Username", font=(None,20))
        self.admin_reg_entry_label.pack(pady=10)
        self.admin_reg_entry = Entry(self.admin_adminacc_addnew_frame, width=100, borderwidth=10)
        self.admin_reg_entry.pack(pady=20)

        self.admin_reg_password_entry_label = Label(self.admin_adminacc_addnew_frame, text="Enter Password", font=(None,20))
        self.admin_reg_password_entry_label.pack(pady=10)
        self.admin_reg_password_entry = Entry(self.admin_adminacc_addnew_frame, width=100, borderwidth=10, show="*")
        self.admin_reg_password_entry.pack(pady=20)

        #Register functions
        # Write a function to create an new user.
        def reg_create_admin():
            admin_reg_username = self.admin_reg_entry.get()
            admin_reg_password = self.admin_reg_password_entry.get()

            if admin_reg_username == "" or admin_reg_password == "":
                messagebox.showerror("Error", "Please enter your username and password!")
                return

            if admin_exists(admin_reg_username):
                messagebox.showerror("Error", "Please choose another username!")
                self.admin_reg_entry.delete(0, END)
                self.admin_reg_password_entry.delete(0, END)
                return

            admin_register_c.execute('INSERT INTO admins (username, password) VALUES (?, ?)', (admin_reg_username, admin_reg_password))
            admin_register_conn.commit()
            admin_register_conn.close()

            messagebox.showinfo("Notification", "Registration successful!")
            self.show_adminacc()

            self.admin_reg_entry.delete(0, END)
            self.admin_reg_password_entry.delete(0, END)


        def admin_exists(admin_reg_username):
            admin_register_c.execute('SELECT * FROM admins WHERE username = ?', (admin_reg_username,))
            if admin_register_c.fetchone():
                return True
            return False


        #register function button
        self.register_admin_function_button=Button(self.admin_adminacc_addnew_frame, text="Creat Account", font=(None,20), command= reg_create_admin, padx=40, pady=10, fg="white", bg='black', width=25)
        self.register_admin_function_button.pack(pady=10)
        
        #back button in register page
        self.register_admin_back_button = Button(self.admin_adminacc_addnew_frame, text="Back", font=(None,20), command= self.show_adminacc, padx=40, pady=10, fg="white", bg='black', width=25)
        self.register_admin_back_button.pack(pady=10)

        #----------------------------------------------------------------------------------------------------------------
        

        #----------------------------------------------------------------------------------------------------------------

        #admin menu frame
        self.adminmenu_title = Label(self.adminmenu_frame, text="Admin Menu", font=(None,20))
        self.adminmenu_title.pack(pady=20)

        self.adminmenu_addnotes = Button(self.adminmenu_frame, text="Add New Notes", font=(None,20),  command= self.show_adminmenu_addnotes , padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminmenu_addnotes.pack(pady=10)

        self.adminmenu_checkprogress = Button(self.adminmenu_frame, text="Check Students Progress", font=(None,20),  command= self.show_adminmenu_checkprogress , padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminmenu_checkprogress.pack(pady=10)

        self.adminmenu_updateWOTD = Button(self.adminmenu_frame, text="Update Word of The Day", font=(None,20),  command= self.show_adminmenu_addWOTD , padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminmenu_updateWOTD.pack(pady=10)

        self.adminmenu_logout = Button(self.adminmenu_frame, text="Log Out & Exit", font=(None,20),  command=lambda: log_out(root) , padx=40, pady=10, fg="white", bg='black', width=25)
        self.adminmenu_logout.pack(pady=10)
        #----------------------------------------------------------------------------------------------------------------
        
        #----------------------------------------------------------------------------------------------------------------
        #Admin menu add new notes frame and functions
        # Database

        # Connection to database
        self.adminmenu_add_new_notes_conn = sqlite3.connect('notes.db')

        # create cursor
        add_new_notes_c = self.adminmenu_add_new_notes_conn.cursor()

        # Create table
        add_new_notes_c.execute("""CREATE TABLE if not exists notes (
                    title text,
                    description text,
                    example text)
                    """)
        
        self.adminmenu_add_new_notes_conn.commit()
        self.adminmenu_add_new_notes_conn.close()

        def add_new_notes_query_database():
            # Connection to database
            add_new_notes_conn = sqlite3.connect('notes.db')

            # create cursor
            add_new_notes_c = add_new_notes_conn.cursor()

            add_new_notes_c.execute("SELECT * FROM notes")
            notes = add_new_notes_c.fetchall()
            
            
            # add data to screeny
            global count
            count = 0

            for note in notes:
                if count % 2 == 0:
                    add_new_notes_my_tree.insert(parent='', index='end', iid=count, text='', values=(note[0], note[1], note[2]), tags=('evenrow',))
                else:
                    add_new_notes_my_tree.insert(parent='', index='end', iid=count, text='', values=(note[0], note[1], note[2]), tags=('oddrow',))
                # increment counter
                count += 1   
    
            
            # Commit changes
            add_new_notes_conn.commit()

            # Close connection
            add_new_notes_conn.close()

        # Add some style
        add_new_notes_style = ttk.Style()

        # Pick a theme
        add_new_notes_style.theme_use('default')

        # Configure the treeview colours
        add_new_notes_style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="D3D3D3")

        # Change the selected colours
        add_new_notes_style.map('Treeview',
                background=[('selected', "#347083")])

        # Create a Treeview Frame
        add_new_notes_tree_frame = Frame(self.adminmenu_addnotes_frame)
        add_new_notes_tree_frame.pack(pady=10)

        # Create a Treeview scrollbar
        add_new_notes_tree_scroll = Scrollbar(add_new_notes_tree_frame)
        add_new_notes_tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        add_new_notes_my_tree = ttk.Treeview(add_new_notes_tree_frame, yscrollcommand=add_new_notes_tree_scroll.set, selectmode="extended")
        add_new_notes_my_tree.pack()

        # Configure the Scrollbar
        add_new_notes_tree_scroll.config(command=add_new_notes_my_tree.yview)

        # Define columns
        add_new_notes_my_tree['columns'] = ("Title", "Description", "Example")

        # Format columns
        add_new_notes_my_tree.column('#0', width=0, stretch=NO)
        add_new_notes_my_tree.column("Title", anchor=CENTER, width=150)
        add_new_notes_my_tree.column("Description", anchor=CENTER, width=500)
        add_new_notes_my_tree.column("Example", anchor=CENTER, width=600)

        # create headings
        add_new_notes_my_tree.heading("#0", text="", anchor=W)
        add_new_notes_my_tree.heading("Title", text="Title", anchor=CENTER)
        add_new_notes_my_tree.heading("Description", text="Description", anchor=CENTER)
        add_new_notes_my_tree.heading("Example", text="Example", anchor=CENTER)

        # Create Striped Row Tags
        add_new_notes_my_tree.tag_configure('oddrow', background="white")
        add_new_notes_my_tree.tag_configure('evenrow', background="lightblue")

        # Add Note Entry Boxes
        add_new_notes_data_frame = LabelFrame(self.adminmenu_addnotes_frame, text="Notes")
        add_new_notes_data_frame.pack(fill="x", expand="yes", padx=20)

        add_new_notes_title_label = Label(add_new_notes_data_frame, text="Title")
        add_new_notes_title_label.grid(row=0, column=0, padx=10, pady=10)
        add_new_notes_title_entry = Entry(add_new_notes_data_frame)
        add_new_notes_title_entry.grid(row=0, column=1, padx=10, pady=10)

        add_new_notes_desc_label = Label(add_new_notes_data_frame, text="Description")
        add_new_notes_desc_label.grid(row=0, column=2, padx=10, pady=10)
        add_new_notes_desc_entry = Entry(add_new_notes_data_frame, width=40)
        add_new_notes_desc_entry.grid(row=0, column=3, padx=10, pady=10)

        add_new_notes_example_label = Label(add_new_notes_data_frame, text="Example")
        add_new_notes_example_label.grid(row=0, column=4, padx=10, pady=10)
        add_new_notes_example_entry = Entry(add_new_notes_data_frame, width=100)
        add_new_notes_example_entry.grid(row=0, column=5, padx=10, pady=10)

        def add_new_notes_clear_entries():
            add_new_notes_title_entry.delete(0, END)
            add_new_notes_desc_entry.delete(0, END)
            add_new_notes_example_entry.delete(0, END)

        # Delete selected notes
        def add_new_notes_delete_note():
            selected_item = add_new_notes_my_tree.selection()
            
            if not selected_item:
                messagebox.showerror("Error", "Please choose the note you wish to delete.")
                return

            
            item_id = add_new_notes_my_tree.item(selected_item)['values'][0]
            if item_id == "":
                messagebox.showerror("Error", "Please choose the note you wish to delete.")
                return
            else:
                add_new_notes_my_tree.delete(selected_item)

            # Connection to database
            add_new_notes_conn = sqlite3.connect('notes.db')

            # create cursor
            add_new_notes_c = add_new_notes_conn.cursor()

            # delete from database
            add_new_notes_c.execute("DELETE from notes WHERE title=?", (item_id,))

            # Commit changes
            add_new_notes_conn.commit()

            # Close connection
            add_new_notes_conn.close()

            # Clear entry boxes
            add_new_notes_clear_entries()

        # Select Notes
        def add_new_notes_select_notes(e):
            # Check if any item is selected
            selected = add_new_notes_my_tree.focus()
            if not selected:
                messagebox.showinfo("Info", "Please select a note.")
                return
            # Clear entry boxes
            add_new_notes_title_entry.delete(0, END)
            add_new_notes_desc_entry.delete(0, END)
            add_new_notes_example_entry.delete(0, END)

            # Grab notes values
            values = add_new_notes_my_tree.item(selected, 'values')

            # output to entry boxes
            add_new_notes_title_entry.insert(0, values[0])
            add_new_notes_desc_entry.insert(0, values[1])
            add_new_notes_example_entry.insert(0, values[2])

        # add new notes to db
        def add_new_notes_add_notes():
            # Connection to database
            add_new_notes_conn = sqlite3.connect('notes.db')
            
            # create cursor
            add_new_notes_c = add_new_notes_conn.cursor()

            # add new note
            title = add_new_notes_title_entry.get()
            description = add_new_notes_desc_entry.get()
            example = add_new_notes_example_entry.get()

            # Check if any of the required values are empty
            if title == "" or description == "" or example == "":
                messagebox.showerror("Error", "Please enter the required values.")
                add_new_notes_conn.close()  # Close connection
                return
            
            # Add new note
            add_new_notes_c.execute("INSERT INTO notes VALUES (:title, :description, :example)",
                                    {
                                        'title': title,
                                        'description': description,
                                        'example': example
                                    })
            # clear entries
            add_new_notes_clear_entries()


            # Commit changes
            add_new_notes_conn.commit()

            # Close connection
            add_new_notes_conn.close()
            
            # clear treeview table
            add_new_notes_my_tree.delete(*add_new_notes_my_tree.get_children())

            # run to pull data from database on start
            add_new_notes_query_database()

        # Search for specific notes in database
        def add_new_notes_search_database():
            # Get the search keyword from the entry widget
            keyword = add_new_notes_search_entry.get()

            # Clear the treeview
            add_new_notes_my_tree.delete(*add_new_notes_my_tree.get_children())

            # Create a database or connect to an existing one
            add_new_notes_conn = sqlite3.connect('notes.db')

            # Create a cursor instance
            c = add_new_notes_conn.cursor()

            # Search the database for records matching the keyword
            c.execute("SELECT * FROM notes WHERE title LIKE ? OR description LIKE ? OR example LIKE ?",
                    ('%{}%'.format(keyword), '%{}%'.format(keyword), '%{}%'.format(keyword)))
            records = c.fetchall()

            # Add the matching records to the treeview
            count = 0
            for record in records:
                if count % 2 == 0:
                    add_new_notes_my_tree.insert(parent='', index='end', iid=count, text="",
                                values=(record[0], record[1], record[2]), tags=('evenrow',))
                else:
                    add_new_notes_my_tree.insert(parent='', index='end', iid=count, text="",
                                values=(record[0], record[1], record[2]), tags=('oddrow',))
                count += 1

            # Commit changes
            add_new_notes_conn.commit()

            # Close the connection
            add_new_notes_conn.close()


        def add_new_notes_update_notes():
            # Get selected item from treeview
            selected_item = add_new_notes_my_tree.focus()
            if not selected_item:
                messagebox.showerror("Error", "Please select a note.")
                return

            # Get the ID of the selected item
            item_id = add_new_notes_my_tree.item(selected_item)['values'][0]

            # Check if any of the entry fields are empty
            if (not add_new_notes_title_entry.get()) or (not add_new_notes_desc_entry.get()) or (not add_new_notes_example_entry.get()):
                messagebox.showerror("Error", "Please enter all the required values.")
                return

            # Update the selected item in the treeview
            add_new_notes_my_tree.item(selected_item, values=(add_new_notes_title_entry.get(), add_new_notes_desc_entry.get(), add_new_notes_example_entry.get()))

            # Update the corresponding notes in the database
            # Connection to database
            add_new_notes_conn = sqlite3.connect('notes.db')

            # Create cursor
            c = add_new_notes_conn.cursor()

            # Update the notes
            c.execute("UPDATE notes SET title=?, description=?, example=? WHERE title=?",
                    (add_new_notes_title_entry.get(), add_new_notes_desc_entry.get(), add_new_notes_example_entry.get(), item_id))

            # Commit changes
            add_new_notes_conn.commit()

            # Close the connection
            add_new_notes_conn.close()

            # Clear entries
            add_new_notes_clear_entries()  

        add_new_notes_button_frame = LabelFrame(self.adminmenu_addnotes_frame, text="Commands")
        add_new_notes_button_frame.pack(fill="x", expand="yes", padx=20)

        add_new_notes_add_button = Button(add_new_notes_button_frame, text="Add Notes", command=add_new_notes_add_notes,fg="white", bg='black')
        add_new_notes_add_button.grid(row=0, column=0, padx=10, pady=10)

        add_new_notes_delete_button = Button(add_new_notes_button_frame, text="Delete Notes", command=add_new_notes_delete_note,fg="white", bg='black')
        add_new_notes_delete_button.grid(row=0, column=1, padx=10, pady=10)

        add_new_notes_update_button = Button(add_new_notes_button_frame, text="Update Notes", command=add_new_notes_update_notes,fg="white", bg='black')
        add_new_notes_update_button.grid(row=0, column=2, padx=10, pady=10)

        add_new_notes_clear_entry_button = Button(add_new_notes_button_frame, text="Clear", command=add_new_notes_clear_entries,fg="white", bg='black')
        add_new_notes_clear_entry_button.grid(row=0, column=3, padx=10, pady=10)

        add_new_notes_back_button = Button(add_new_notes_button_frame, text="Return to Admin Menu", command= self.show_adminmenu,fg="white", bg='black')
        add_new_notes_back_button.grid(row=0, column=4, padx=10, pady=10)

        # Create a search entry widget
        add_new_notes_search_entry = Entry(self.adminmenu_addnotes_frame)
        add_new_notes_search_entry.pack()

        # Create a search button
        add_new_notes_search_button = Button(self.adminmenu_addnotes_frame, text="Search", command=add_new_notes_search_database,fg="white", bg='black')
        add_new_notes_search_button.pack()

        # Bind the treeview     
        add_new_notes_my_tree.bind("<ButtonRelease-1>", add_new_notes_select_notes) 

        add_new_notes_query_database()
        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #Admin menu check progress 

        #Connection to the database
        adminmenu_progress_conn = sqlite3.connect("database.sqlite")

        #Create a cursor that calls connection
        adminmenu_progress_c = adminmenu_progress_conn.cursor()

        # Commit changes
        adminmenu_progress_conn.commit()

        # Close connection
        adminmenu_progress_conn.close()

        def adminmenu_progress_query_database():
            # Connection to database
            adminmenu_progress_conn = sqlite3.connect('database.sqlite')

            # create cursor
            adminmenu_progress_c = adminmenu_progress_conn.cursor()

            adminmenu_progress_c.execute("SELECT * FROM users")
            users = adminmenu_progress_c.fetchall()
            
            
            # add data to screeny
            global count
            count = 0

            for user in users:
                if count % 2 == 0:
                    adminmenu_progress_my_tree.insert(parent='', index='end', iid=count, text='', values=(user[0], user[1], user[3]), tags=('evenrow',))
                else:
                    adminmenu_progress_my_tree.insert(parent='', index='end', iid=count, text='', values=(user[0], user[1], user[3]), tags=('oddrow',))
                # increment counter
                count += 1   
            
                        
            # Commit changes
            adminmenu_progress_conn.commit()

            # Close connection
            adminmenu_progress_conn.close()

        # Add some style
        adminmenu_progress_style = ttk.Style()

        # Pick a theme
        adminmenu_progress_style.theme_use('default')

        # Configure the treeview colours
        adminmenu_progress_style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="D3D3D3")

        # Change the selected colours
        adminmenu_progress_style.map('Treeview',
                background=[('selected', "#347083")])

        # Create a Treeview Frame
        adminmenu_progress_tree_frame = Frame(self.adminmenu_checkprogress_frame)
        adminmenu_progress_tree_frame.pack(pady=10)

        # Create a Treeview scrollbar
        adminmenu_progress_tree_scroll = Scrollbar(adminmenu_progress_tree_frame)
        adminmenu_progress_tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        adminmenu_progress_my_tree = ttk.Treeview(adminmenu_progress_tree_frame, yscrollcommand=adminmenu_progress_tree_scroll.set, selectmode="extended")
        adminmenu_progress_my_tree.pack()

        # Configure the Scrollbar
        adminmenu_progress_tree_scroll.config(command=adminmenu_progress_my_tree.yview)

        # Define columns
        adminmenu_progress_my_tree['columns'] = ("ID", "Username", "Progress")

        # Format columns
        adminmenu_progress_my_tree.column('#0', width=0, stretch=NO)
        adminmenu_progress_my_tree.column("ID", anchor=CENTER, width=150)
        adminmenu_progress_my_tree.column("Username", anchor=CENTER, width=500)
        adminmenu_progress_my_tree.column("Progress", anchor=CENTER, width=600)

        # create headings
        adminmenu_progress_my_tree.heading("#0", text="", anchor=W)
        adminmenu_progress_my_tree.heading("ID", text="ID", anchor=CENTER)
        adminmenu_progress_my_tree.heading("Username", text="Username", anchor=CENTER)
        adminmenu_progress_my_tree.heading("Progress", text="Progress", anchor=CENTER)

        # Create Striped Row Tags
        adminmenu_progress_my_tree.tag_configure('oddrow', background="white")
        adminmenu_progress_my_tree.tag_configure('evenrow', background="lightblue")

        # Buttons
        adminmenu_progress_button_frame = LabelFrame(self.adminmenu_checkprogress_frame)
        adminmenu_progress_button_frame.pack( expand=TRUE, padx=20)
        
        adminmenu_progress_back_button = Button(adminmenu_progress_button_frame, text="Return to admin menu", command=self.show_adminmenu, fg="white", bg="black")
        adminmenu_progress_back_button.pack()

        # run to pull data from database on start
        adminmenu_progress_query_database()
        #----------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------------------
        #Admin menu update Word of The Day functions and frame
         #Connection to the database
        update_WOTD_conn = sqlite3.connect('wotd.db')

        #Create a cursor that calls connection
        update_WOTD_c = update_WOTD_conn.cursor()


        # Create table for word of the day 
        update_WOTD_c.execute("""CREATE TABLE IF NOT EXISTS wordoftheday (
                    name text,
                    meaning text,
                    example text
                    )""")         
        
        # Create Function to Delete Word
        def update_WOTD_delete():
            # Check if the entry field is empty
            if not update_WOTD_delete_box.get():
                messagebox.showerror("Error", "Please enter a word to delete.")
                return
            
            #Connection to the database
            update_WOTD_conn = sqlite3.connect('wotd.db')
            #Create a cursor that calls connection
            update_WOTD_c = update_WOTD_conn.cursor()

            # Delete a word
            update_WOTD_c.execute("DELETE from wordoftheday WHERE name=?", (update_WOTD_delete_box.get(),))

            update_WOTD_delete_box.delete(0, END)

            update_WOTD_conn.commit()

            update_WOTD_conn.close()

        # Create submit function for database
        def update_WOTD_submit():
            # Check if any of the entry fields are empty
            if (not update_WOTD_name.get()) or (not update_WOTD_meaning.get()) or (not update_WOTD_example.get()):
                messagebox.showerror("Error", "Please enter all the required values.")
                return
            #Connection to the database
            update_WOTD_conn = sqlite3.connect('wotd.db')
            #Create a cursor that calls connection
            update_WOTD_c = update_WOTD_conn.cursor()

            # Insert Into Table
            update_WOTD_c.execute("INSERT INTO wordoftheday VALUES (:name, :meaning, :example)",
                    {
                        'name': update_WOTD_name.get(),
                        'meaning': update_WOTD_meaning.get(),
                        'example': update_WOTD_example.get()    
                    })

            update_WOTD_conn.commit()

            update_WOTD_conn.close()

            # clear the text boxes
            update_WOTD_name.delete(0, END)
            update_WOTD_meaning.delete(0, END)
            update_WOTD_example.delete(0, END)

        # Create query function
        def  update_WOTD_query():
            #Connection to the database
            update_WOTD_conn = sqlite3.connect('wotd.db')
            #Create a cursor that calls connection
            update_WOTD_c =  update_WOTD_conn.cursor()  

            # Query the database
            update_WOTD_c.execute("SELECT *, oid FROM wordoftheday")
            words = update_WOTD_c.fetchall()
            

            # Loop Through Results
            print_words = ''
            for word in words:
                print_words += "Word: " + str(word[0]) + "    Meaning: " + str(word[1]) + "    Example: " + str(word[2]) + " " + "\n"

            update_WOTD_query_label = Label(self.adminmenu_addWOTD_frame, text=print_words)
            update_WOTD_query_label.grid(row=8, column=0, columnspan=2)

            update_WOTD_conn.commit()

            update_WOTD_conn.close()

        # Create labels for textboxes
        update_WOTD_name_label = Label(self.adminmenu_addWOTD_frame, text="Name of Word")
        update_WOTD_name_label.grid(row=0, column=0, pady=(10, 0))
        update_WOTD_meaning_label = Label(self.adminmenu_addWOTD_frame, text="Meaning of Word")
        update_WOTD_meaning_label.grid(row=1, column=0)
        update_WOTD_example_label = Label(self.adminmenu_addWOTD_frame, text="Example Sentence")
        update_WOTD_example_label.grid(row=2, column=0)
        update_WOTD_delete_box_label = Label(self.adminmenu_addWOTD_frame, text="Delete Word")
        update_WOTD_delete_box_label.grid(row=6, column=0, pady=5)

        # Create textboxes
        update_WOTD_name = Entry(self.adminmenu_addWOTD_frame, width=30)
        update_WOTD_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        update_WOTD_meaning = Entry(self.adminmenu_addWOTD_frame, width=30)
        update_WOTD_meaning.grid(row=1, column=1)
        update_WOTD_example = Entry(self.adminmenu_addWOTD_frame, width=30)
        update_WOTD_example.grid(row=2, column=1)
        update_WOTD_delete_box = Entry(self.adminmenu_addWOTD_frame, width=30)
        update_WOTD_delete_box.grid(row=6, column=1, padx=5)

        # Create Submit Button
        update_WOTD_submit_btn = Button(self.adminmenu_addWOTD_frame, text="Add New Word Of The Day", command=update_WOTD_submit,fg="white", bg='black')
        update_WOTD_submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create query button
        update_WOTD_query_btn = Button(self.adminmenu_addWOTD_frame, text="Show Word Of the Day", command=update_WOTD_query,fg="white", bg='black')
        update_WOTD_query_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

        # Create a delete button
        update_WOTD_delete_btn = Button(self.adminmenu_addWOTD_frame, text="Delete Word", command=update_WOTD_delete,fg="white", bg='black')
        update_WOTD_delete_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

        # Create a back button
        update_WOTD_back_btn = Button(self.adminmenu_addWOTD_frame, text="Return to Admin Menu", command=self.show_adminmenu,fg="white", bg='black')
        update_WOTD_back_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

        update_WOTD_conn.commit()

        update_WOTD_conn.close()
        #----------------------------------------------------------------------------------------------------------------
        




        self.show_start() # show the start frame initially

               
    def show_start(self):
        self.start_frame.pack()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        
    def show_register(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()  


    def show_useracc(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
    
    def show_user_useracc_changepass(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_user_useracc_deleteacc(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        
    def show_adminacc(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_login(self):
        self.start_frame.pack_forget()
        self.login_frame.pack()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        

    def show_userlogin(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
    
    def show_adminlogin(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        

    def show_user_useracc_changepass(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        

    def show_user_useracc_deleteacc(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()


    def show_usermenu(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_usermenu_learning(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        
           
    def show_usermenu_quiz_credential(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        
    # def usermenu_quiz_credential_submit(self):
    #     # Validate id and username
    #     username_entry = self.usermenu_quiz_credential_username_entry.get()
    
    #     if not username_entry:
    #         # Display an error message if the id or username is empty (user did not input anything)
    #         messagebox.showerror("Error", "Please enter your and username.")
    #         return
    
    #     # Connect to the database
    #     self.quiz_credential_conn = sqlite3.connect('database.sqlite')
    #     c = self.quiz_credential_conn.cursor()
    
    #     # Check if the user exists in the database 
    #     c.execute("SELECT * FROM users WHERE username = ?", (username_entry,))
    #     result = c.fetchone()

    #     if result is None:
    #         # Displays an error message if the user id or username does not exist in the database (checking whether the input is in the database)
    #         messagebox.showerror("Error", "Invalid ID or username.")
    #         self.quiz_credential_conn.close()
    #         username_entry.delete(0, END)
    #         return

    #     self.quiz_credential_conn.close()
                   
    #     # Hides the credential input frame and then shows the quiz frame
    #     self.show_usermenu_quiz()

    def show_usermenu_quiz(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_usermenu_progress(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
        check_user_progress()

    def show_usermenu_WOTD(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()


    def show_usermenu_favlist(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_admin_adminacc_changepass(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_admin_adminacc_del_acc(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_admin_adminacc_addnew(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_adminmenu(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()
       
    
    def show_adminmenu_addnotes(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_adminmenu_addWOTD(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack()
        self.adminmenu_checkprogress_frame.pack_forget()

    def show_adminmenu_checkprogress(self):
        self.start_frame.pack_forget()
        self.login_frame.pack_forget()
        self.userlogin_frame.pack_forget()
        self.adminlogin_frame.pack_forget()
        self.register_frame.pack_forget()
        self.usermenu_frame.pack_forget()
        self.user_useracc_frame.pack_forget()
        self.user_useracc_changepass_frame.pack_forget()
        self.user_useracc_deleteacc_frame.pack_forget()
        self.usermenu_learning_frame.pack_forget()
        self.usermenu_quiz_frame.pack_forget()
        self.usermenu_quiz_credential_frame.pack_forget()
        self.usermenu_progress_frame.pack_forget()
        self.usermenu_WOTD_frame.pack_forget()
        self.usermenu_favlist_frame.pack_forget()
        self.adminmenu_frame.pack_forget()
        self.admin_adminacc_frame.pack_forget()
        self.admin_adminacc_changepass_frame.pack_forget()
        self.admin_adminacc_del_acc_frame.pack_forget()
        self.admin_adminacc_addnew_frame.pack_forget()
        self.adminmenu_addnotes_frame.pack_forget()
        self.adminmenu_addWOTD_frame.pack_forget()
        self.adminmenu_checkprogress_frame.pack() 



def log_out(root):
    result = messagebox.askquestion("Logout", "Are you sure you want to logout?", icon='warning')
    if result == 'yes':
        root.destroy()  # Terminate the application window

def main():
    app = App(root)
    root.title("Aid-Lish")
    root.mainloop()


if __name__ =="__main__":
    main()
