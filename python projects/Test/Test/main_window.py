from turtle import onclick
import customtkinter as ctk

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')


#create main application window
app = ctk.CTk()
app.geometry('300x500') #set the size of the window (width x height)
app.title('Main Window') #set window title
display_label = ctk.CTkLabel(app, text='Display')
display_label.pack(side='top', padx = 20) # loads the label into the window

#display text functon
def displayText():
    text = display_input.get().title()
    #set display with text from the inputfiled
    display_label.configure(text= f'hi {text}')
    #clear the input value after assigning it to the disply filed
    display_input.delete(0,'end')       
display_input = ctk.CTkEntry(app, placeholder_text='Enter something')
display_input.pack(side='top', fill='x', pady = 20)

#get text from display input entry

submint_button = ctk.CTkButton(app, text='Enter', command=displayText)
submint_button.pack(side = 'top',pady= 10,fill='x')




app.mainloop()