####################################################################################
#                                                                                  #
# PROJECT OF RENDERING DYNAMIC PAGES AND SAVING DATA INTO JSON FILES               #
#                                                                                  #
####################################################################################


import customtkinter as ctk
import os
import json


user = {
    'fname':'Gideon Okai',
    'lname':'Boateng',
    'email': 'agyanim@gmail.com',
    'age':30,
    'Profession':'Network Administrator'
    
    }

sub_dir = 'Test'
file = 'profile.json'
file_path = os.path.join(sub_dir,file)


ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

#set up main app window
app = ctk.CTk()
app.title('Dynamic Pages')
app.geometry('600x800') #main windwo size

#configure layout (rows and columns)

app.columnconfigure(0, weight=0)
app.columnconfigure(1,weight= 1, minsize = 400)
app.rowconfigure(0,weight=1, minsize=500)

# side bar 
side_bar = ctk.CTkFrame(app, width=150, height=500, border_width=1, border_color='grey')
side_bar.grid(row = 0 , column = 0, sticky = 'nsew', pady = 5, padx=5)

#main content area
main_content_area = ctk.CTkFrame(app, width=400,height = 600 ,border_width=1, border_color='grey')
main_content_area.grid(row = 0, column = 1, sticky = 'nsew',pady = 5, padx=5)

#set up pages for dashboard,profile and settings (Frames)
dashboard_layout = ctk.CTkFrame(main_content_area, width=150, height=500,border_width=1, border_color='grey',corner_radius=5)
profile_layout = ctk.CTkFrame(main_content_area, width=150, height=500,border_width=1, border_color='grey',corner_radius=5)
settings_layout = ctk.CTkFrame(main_content_area, width=150, height=500,border_width=1, border_color='grey',corner_radius=5)
home_layout = ctk.CTkFrame(main_content_area, width=150, height=500,border_width=1, border_color='grey',corner_radius=5)
home_layout.pack(fill = 'both', expand = True)


#widgets and layers for pages
#Home page
#layout configuration
home_layout.columnconfigure(0,weight=1)
home_layout.rowconfigure(1,weight=1)


#layout for header (page title)
title_layout = ctk.CTkFrame(home_layout, border_width=1,border_color='grey')
title_layout.grid(row = 0, column = 0, sticky = 'nsew',padx = 5,pady=5)
home_label = ctk.CTkLabel(title_layout, text = 'Home',font=('',20)).pack(pady = 10, padx=10)

#layer of Home content
content_layout = ctk.CTkFrame(home_layout,width=500, height=600)
content_layout.grid(row = 1, column = 0, sticky = 'nsew', pady = 2 , padx = 5)
content_label = ctk.CTkLabel(content_layout,text='Welcome To The Page of Dynamic Pages',text_color='#d3c4d1',font=('',20))
content_label.pack(pady=10, padx=10, fill='both', expand = True)

#profile page
#configurations for prfile layout
profile_layout.columnconfigure(0,weight=1)
profile_layout.rowconfigure(1,weight=1)

#layout and widgets
#profile header
profile_header_layout = ctk.CTkFrame(profile_layout, border_width=1, border_color='grey')
profile_header_layout.grid(row = 0, column =0, sticky = 'nsew',padx = 5, pady = 5)
profile_header_label = ctk.CTkLabel(profile_header_layout, text = 'Profile',font = ('',20))
profile_header_label.pack(pady = 10, )



#################################### Profile Page Starts Here ##################################################
#profile content

profile_content_layout = ctk.CTkFrame(profile_layout)
profile_content_layout.grid(row = 1, column = 0, sticky = 'nsew',pady = 2, padx = 5)



#content columns
#column 1
col_1 = ctk.CTkFrame(profile_content_layout,)
col_1.grid(row = 0, column = 1,padx=5, pady = 20, sticky = 'nsew')
#column 2
col_2 = ctk.CTkFrame(profile_content_layout,)
col_2.grid(row = 0, column = 2, pady = 20, sticky = 'nsew')
#column 3
col_3 = ctk.CTkFrame(profile_content_layout,)
col_3.grid(row = 0, column = 3, pady = 20,padx=5, sticky = 'nsew')
#column 4
col_4 = ctk.CTkFrame(profile_content_layout,)
col_4.grid(row = 0, column = 4, pady = 20, sticky = 'nsew')

for i in range(1,5):
    profile_content_layout.columnconfigure(i,weight=0)

profile_content_layout.columnconfigure(0, weight=0)
profile_content_layout.columnconfigure(2, weight=1)


#conlumn configuration
col_2.columnconfigure(0,weight=0)

#id
id_header_label = ctk.CTkLabel(col_1,text='ID: ')
id_header_label.grid(row= 0, column = 0, padx = 5,sticky = 'w')
id_name_label = ctk.CTkLabel(col_2,text=f'1')
id_name_label.grid(row= 0, column = 1, padx = 5, sticky = 'w')
#Nmae
name_header_label = ctk.CTkLabel(col_1,text='Name: ')
name_header_label.grid(row= 1, column = 0, padx = 5,sticky = 'w')
name_label = ctk.CTkLabel(col_2,text=f'{user['fname']} {user['lname']}')
name_label.grid(row= 1, column = 1, padx = 5, sticky = 'w')


#Emain
email_header_label = ctk.CTkLabel(col_1,text='Email: ')
email_header_label.grid(row= 2, column = 0, padx = 5,sticky = 'w')
email_name_label = ctk.CTkLabel(col_2,text=f'{user['email']}')
email_name_label.grid(row= 2, column = 1,padx = 5,sticky = 'w')

#Age
age_header_label = ctk.CTkLabel(col_1,text='Age: ')
age_header_label.grid(row= 3, column = 0, padx = 5 ,sticky = 'w')
age_name_label = ctk.CTkLabel(col_2,text=f'{user['age']}')
age_name_label.grid(row= 3, column = 1, padx = 5 , sticky = 'w')

#Profession
profession_header_label = ctk.CTkLabel(col_3,text='Profession: ')
profession_header_label.grid(row= 0, column = 0, padx = 5,sticky = 'w' )
profession_name_label = ctk.CTkLabel(col_4,text=f'{user['Profession']}')
profession_name_label.grid(row= 0, column = 0, padx = 5 , sticky = 'w')
#Bio
bio_header_label = ctk.CTkLabel(col_3,text='Biography: ')
bio_header_label.grid(row= 1, column = 0, padx = 5,sticky = 'w' )

bio_name_label = ctk.CTkLabel(col_4,text=f'{user['Profession']}')
bio_name_label.grid(row= 1, column = 0, padx = 5 , sticky = 'w')


# Profile Form 
#layout
form_layout = ctk.CTkFrame(profile_content_layout)
form_layout.grid(row = 1, column = 2, sticky = 'nsew',padx=5)


#form header
form_header_label = ctk.CTkLabel(form_layout, text='Create Profile').pack(pady = 10)

#id
id_entry = ctk.CTkEntry(form_layout,placeholder_text="Id")
id_entry.pack(pady =5)
#first name
fname_entry = ctk.CTkEntry(form_layout,placeholder_text="Enter First Name")
fname_entry.pack()

#last name
lname_entry = ctk.CTkEntry(form_layout,placeholder_text="Enter Last Name")
lname_entry.pack(pady = 10)
#Email
email_entry = ctk.CTkEntry(form_layout,placeholder_text="example.gmail.com")
email_entry.pack()
#age
age_entry = ctk.CTkEntry(form_layout,placeholder_text="Age")
age_entry.pack(pady =10)

#Profession
professtion_entry = ctk.CTkEntry(form_layout,placeholder_text='profession')
professtion_entry.pack()

#Biography
bio_text = ctk.CTkTextbox(form_layout)
bio_text.pack(pady = 10)

profileList = []

def submitHandler():
    formData = {
    'id':id_entry.get().strip(),
    'fname':fname_entry.get().strip().title(),
    'lname':lname_entry.get().strip().title(),
    'email': email_entry.get().strip(),
    'age':  age_entry.get().strip(),
    'profession':professtion_entry.get().strip().title(),
    'bio':bio_text.get('1.0','end').strip()
    }
    #Displaying data on the form
    id_name_label.configure(text=f'{formData['id']}')
    name_label.configure(text=f'{formData["fname"]} {formData['lname']}')
    email_name_label.configure(text=f'{formData["email"]}')
    age_name_label.configure(text=f'{formData["age"]}')
    profession_name_label.configure(text=f'{formData["profession"]}')
    bio_name_label.configure(text=f'{formData["bio"]}')


    #saveing data to json file
    profileList.append(formData)
    with open(file_path,'w') as f:
        json.dump(profileList,f,indent=4)

    print(formData)

    #clearing text fields
    id_entry.delete(0,'end')


#Submit Button
submit_button = ctk.CTkButton(form_layout,text='Submit',command = submitHandler)
submit_button.pack()
delete_button = ctk.CTkButton(form_layout,text='Delete',command = {},fg_color='red')
delete_button.pack(pady = 10)




#####################################  Profile Ends Here############################################
#settings page
settings_label = ctk.CTkLabel(settings_layout, text = 'Settings').pack(pady = 10,padx=10)

#dashboard page
dashboard_label = ctk.CTkLabel(dashboard_layout, text = 'Dashboard').pack(pady = 10,padx=10)

def displayPage(page):
    for widget in main_content_area.winfo_children():# this line loops throught all the children layout of the main_area layout
        widget.pack_forget() #This line of code hides the layout that matches the loop
    page.pack(fill = 'both',expand = True)

#Widgets for side bar
side_bar_laybel = ctk.CTkLabel(side_bar, text = 'Menu').pack(pady = 20)
#profile
#profile
home_button = ctk.CTkButton(side_bar,text = 'Home', command = lambda:displayPage(home_layout) )
home_button.pack(pady = 5, padx = 5)

profile_button = ctk.CTkButton(side_bar,text = 'Profile', command = lambda:displayPage(profile_layout) )
profile_button.pack(pady = 5, padx = 5)

#settings
settings_button = ctk.CTkButton(side_bar, text = 'Settings',command = lambda:displayPage(settings_layout))
settings_button.pack(pady = 5, padx = 5)

#dashboard
dashboard_button = ctk.CTkButton(side_bar, text = 'Dashboard',command = lambda:displayPage(dashboard_layout))
dashboard_button.pack(pady = 5, padx = 5)



app.mainloop() #this keeps the app UI active and running 
