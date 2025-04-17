

import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")



ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.geometry('450x600')
app.title('Practice Grid System')

#username
userName_label = ctk.CTkLabel(app, text='Name').grid(row=0,column=0, padx=5)
userName_field = ctk.CTkEntry(app)
userName_field.grid(row=0,column=1,columnspan=3,padx=5,)

#Email
email_label = ctk.CTkLabel(app, text='Email').grid(row=1,column=0, padx=5 ,pady=10)
email_field = ctk.CTkEntry(app)
email_field.grid(row=1,column=1,pady=10,columnspan=2 ,padx=5)


#message
message_label = ctk.CTkLabel(app,text='Message:').grid(row=2,column=0, pady=5,padx=10,sticky='n')
message_field = ctk.CTkTextbox(app, width=160,height=140)
message_field.grid(row=2,column=1, padx=10,pady=5)

#Display Message label
display_label = ctk.CTkLabel(app,text='')
display_label.grid(row=4,column = 1,pady=10)

#Funtion to display message into display field
def getDetails():
    name = userName_field.get().title()
    email = email_field.get()
    message = message_field.get('1.0','end')
    display_label.configure(text=f'Name: {name}\nEmail: {email}\nMessage:{message}')

    #clear fields
    userName_field.delete(0,'end')
    email_field.delete(0,'end')
    message_field.delete('1.0','end')

#Button
submit_button = ctk.CTkButton(app,text='submit',command=getDetails)
submit_button.grid(row=3,column=1,columnspan=2,pady=10,padx=5,sticky='')




app.mainloop()