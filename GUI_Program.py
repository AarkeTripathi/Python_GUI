''' Mandatory line for any gui coding'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
win=tk.Tk()
win.title('GUI')


'''Creating menubar'''
def func():
    print('menu button pressed')


main_menu=tk.Menu(win)
#main_menu.add_command(label='Save', command=func)             #add_command method adds a command named saved to the menubar
#main_menu.add_command(label='Save As', command=func)
#main_menu.add_command(label='Copy', command=func)
#main_menu.add_command(label='Paste', command=func)


#assigning a menubar to the main menubar
file_menubar=tk.Menu(main_menu, tearoff=0)                    #setting tearoff to 0 disables the file menubar from tearing off, i.e., from coming off as new window. Any other value of tearoff will do the opposite. It can also be set to Tru or False.
file_menubar.add_command(label='New', command=func)
file_menubar.add_separator()                    #adds a seperating line between two commands
file_menubar.add_command(label='Open', command=func)
file_menubar.add_separator()
file_menubar.add_command(label='Save', command=func)
file_menubar.add_command(label='Save As', command=func)

edit_menubar=tk.Menu(main_menu, tearoff=0)
edit_menubar.add_command(label='Undo', command=func)
edit_menubar.add_command(label='Redo', command=func)


#adding menubars to the main menu 
main_menu.add_cascade(label='File', menu=file_menubar)        #add_cascade method adds the file menubar to the main menubar
main_menu.add_cascade(label='Edit', menu=edit_menubar)



win.config(menu=main_menu)    # config method assigns menubar to win




'''_______________Main________________'''

#creating file in which to enter this data
fileout=open(r'C:\Users\AARKE\Documents\file.txt','a+')
fileout.seek(0)
empty_check=fileout.read()
fileout.seek(fileout.tell()-1)
if len(empty_check)==0:
    fileout.write('Name , Age , Gender , Profession , E-mail_id , Physical Disability\n')
else:
    pass

#creating tabs and pages so that window can contain more than one pages
nb=ttk.Notebook(win)        #Notebook class creates notebook in window in which pages will be created
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1, text='ONE')    #text variable is the name of the tab through which page 1 can be accessed
nb.add(page2, text='TWO')
nb.pack(expand=True, fill='both')   #expand=true decides that pages on nb will cover whole screen, and fill=both decides that page will cover the screen both, horizontally and vertically. fill can also be set to 'none','x' and 'y' depending on need





'''Creating Page 1 widgets'''





#creating labelframe which will contain all labels, entryboxes and buttons
label_frame=ttk.LabelFrame(page1, text='Enter your details below')
label_frame.grid(row=0, column=0, padx=100, pady=40)

#creating labels
user_var=['name','email','age','country','state','city','gender','profession']
labels=[f'Enter your {i} :' for i in user_var]
for k in range(len(labels)):
    variable=user_var[k]+'_label'
    variable=ttk.Label(label_frame, text=labels[k], foreground='Blue', font=('Helvetica', 10, 'bold'))
    variable.grid_configure(row=k, column=0, sticky=tk.W, padx=0, pady=0)

#creating entryboxes
dict1={i:tk.StringVar() for i in user_var if (i!='profession' and i!='gender')}
count=0
for j in dict1:
    variable2=j+'_entrybox'
    variable2=ttk.Entry(label_frame, width=16, textvariable = dict1[j])
    variable2.grid_configure(row=count, column=1, padx=0, pady=0)
    count+=1

#creating combobx
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(label_frame, width=14, textvariable = gender_var, state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.grid(row=6, column=1)

#creating radio button
userprofession=tk.StringVar()
radio_button1=ttk.Radiobutton(label_frame, text='Student', value='Student', variable = userprofession)
radio_button1.grid(row=7, column=1)
radio_button2=ttk.Radiobutton(label_frame, text='Teacher', value='Teacher', variable = userprofession)
radio_button2.grid(row=7, column=2, sticky=tk.W)

#creating check button
handicap_var=tk.IntVar()
check_button=ttk.Checkbutton(label_frame, text='I am handicap', variable = handicap_var)
check_button.grid(row=8, columnspan=5, sticky=tk.W)

#defining fuction that submit button will perform
def action():
    username=dict1['name'].get()
    if username=='':
        mbox.showerror('Incomplete details!','Please fill your name')
        return None
    useremail_id=dict1['email'].get()
    if useremail_id=='':
        mbox.showerror('Incomplete details!','Please fill your email')
        return None
    elif '@' not in useremail_id:
        mbox.showerror('Invalid input!','Please enter valid email address')
        return None
    userage=dict1['age'].get()
    if userage=='':
        mbox.showerror('Incomplete details!','Please fill your age')
        return None
    usercountry=dict1['country'].get()
    if usercountry=='':
        mbox.showerror('Incomplete details!','Please fill your residential country')
        return None
    userstate=dict1['state'].get()
    if userstate=='':
        mbox.showerror('Incomplete details!',f'Please fill your residential state in {usercountry}')
        return None
    usercity=dict1['city'].get()
    if usercity=='':
        mbox.showerror('Incomplete details!',f'Please fill your residential city in {userstate}, {usercountry}')
        return None
    usergender=gender_var.get()
    if usergender=='':
        mbox.showerror('Incomplete details!','Please select your gender')
        return None
    usertype=userprofession.get()
    if usertype=='':
        mbox.showerror('Incomplete details!','Please select your profession')
        return None
    userability=handicap_var.get()
    try:
        userage=int(userage)
    except ValueError:
        mbox.showerror('Invalid input!','Please enter only digits for age')
    else:
        if userage>80:
            mbox.showerror('Invalid input!','Age must be 80 or less')
        elif userage<18:
            mbox.showwarning('18+ only!!!','You are below 18. Enter at your own risk!')
            win2=tk.Tk()
            win2.title('GUI2')


            main_menu=tk.Menu(win2)
            #main_menu.add_command(label='Save', command=func)             #add_command method adds a command named saved to the menubar
            #main_menu.add_command(label='Save As', command=func)
            #main_menu.add_command(label='Copy', command=func)
            #main_menu.add_command(label='Paste', command=func)


            #assigning a menubar to the main menubar
            file_menubar=tk.Menu(main_menu, tearoff=0)                    #setting tearoff to 0 disables the file menubar from tearing off, i.e., from coming off as new window. Any other value of tearoff will do the opposite. It can also be set to Tru or False.
            file_menubar.add_command(label='New', command=func)
            file_menubar.add_separator()                    #adds a seperating line between two commands
            file_menubar.add_command(label='Open', command=func)
            file_menubar.add_separator()
            file_menubar.add_command(label='Save', command=func)
            file_menubar.add_command(label='Save As', command=func)

            edit_menubar=tk.Menu(main_menu, tearoff=0)
            edit_menubar.add_command(label='Undo', command=func)
            edit_menubar.add_command(label='Redo', command=func)


            #adding menubars to the main menu 
            main_menu.add_cascade(label='File', menu=file_menubar)        #add_cascade method adds the file menubar to the main menubar
            main_menu.add_cascade(label='Edit', menu=edit_menubar)



            win2.config(menu=main_menu)    # config method assigns menubar to win


            label_frame2=ttk.LabelFrame(win2)
            label_frame2.grid(row=0, column=0, padx=200, pady=100)

            entrance_var=tk.StringVar()
            ent_confirm=ttk.Radiobutton(label_frame2, text='I agree to enter at my own risk', value='a', variable=entrance_var)
            ent_confirm.grid(row=0, column=0, sticky=tk.W)
            ent_denial=ttk.Radiobutton(label_frame2, text='I do not agree to enter at my own risk', value='b', variable=entrance_var)
            ent_denial.grid(row=1, column=0)

            def action2():
                userrisk=entrance_var.get()
                print(userrisk)
                if userrisk=='a':
                    print(f'{username} is {userage} years old, with email id {useremail_id} and {username}\'s gender is {usergender}.By profession {username} is {usertype}')
                    if userability==1:
                        userdisability = 'Yes'
                        print('{username} is handicap')
                    else:
                        userdisability = 'No'
                        print('{username} is not handicap')

                    fileout.write(f'{username} , {userage} , {usergender} , {usertype} , {useremail_id} , {userdisability}, {usercountry}, {userstate}, {usercity}\n')
                    fileout.flush()

                    mbox.showinfo('Submit successful!', 'Your details have been successfully submitted.')

                else:
                    mbox.showinfo('Entrance Denied!', 'Sorry you can\'t enter the site.')
                    return None

            #creating button
            submit_button=ttk.Button(win2, text='Submit', command=action2)
            submit_button.grid(row=1, column=0, sticky=tk.W, padx=200)

            win2.mainloop()
            
        else:
            print(f'{username} is {userage} years old, with email id {useremail_id} and {username}\'s gender is {usergender}.By profession {username} is {usertype}')
            if userability==1:
                userdisability = 'Yes'
                print('{username} is handicap')
            else:
                userdisability = 'No'
                print('{username} is not handicap')

            fileout.write(f'{username} , {userage} , {usergender} , {usertype} , {useremail_id} , {userdisability}, {usercountry}, {userstate}, {usercity}\n')
            fileout.flush()

            mbox.showinfo('Submit successful!', 'Your details have been successfully submitted.')
               



#applying common padding to all widgets in the label_frame
for child in label_frame.winfo_children():    #given function returns the list of widgets inside label frame, on which for loop is then applied
    child.grid_configure(padx=4, pady=5)

#creating button
submit_button=ttk.Button(page1, text='Submit', command=action)
submit_button.grid(row=1, column=0, sticky=tk.W, padx=200)


#_________________________________________________________________________________________________________________________________________________________________________________________



'''If user is below 18 years of age'''

        

#________________________________________________________________________________________________________________________________________________________________________________________        



'''Creating Page 2 widgets'''


name_label2=ttk.Label(page2, text="Thank You for cooperating with us!", foreground='Blue', font=('Helvetica', 15, 'bold'))
name_label2.pack(pady=200)




win.mainloop()


        

        
