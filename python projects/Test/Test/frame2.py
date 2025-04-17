from copyreg import dispatch_table
import customtkinter as ctk

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Two Forms')
#rows and columns configuraton
app.grid_columnconfigure(0,weight=0) #keeps first column fixed
app.grid_columnconfigure(1,weight=1, minsize=500)#keeps column 2 expandable and the minimum width to 500
app.grid_rowconfigure(0, weight=1, minsize=600)#keeps row 0 expandable and the minimum hieght to 600

#left side bar layout
left_bar = ctk.CTkFrame(app, width=200, height= 500)
left_bar.grid(row=0,column=0 ,sticky = 'nsew')

#main content layout
right_bar = ctk.CTkFrame(app,width=500, height=500,border_width=1, border_color='grey')
right_bar.grid(row=0,column = 1, sticky = 'nsew')

#search filed
search_field = ctk.CTkEntry(left_bar)
search_field.pack(pady=20, padx=10)

#display area
display_label = ctk.CTkLabel(right_bar, text='Display')
display_label.pack(pady=250)

#display function
def displayMessage():
    message = search_field.get()
    display_label.configure(text=f'⚙️ {message}')
    search_field.delete(0,'end')


#Submit button
submit_button = ctk.CTkButton(left_bar, text='Submint', command=displayMessage)
submit_button.pack( padx=10) 

app.mainloop()