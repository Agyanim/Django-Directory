import customtkinter as ctk

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Frames')
app.geometry('500x600')

main_container = ctk.CTkFrame(app, width=500 , height=550, border_width=1, border_color='grey', corner_radius=5 )
main_container.pack(fill='both', expand= True)

#Display area
name_label = ctk.CTkLabel(main_container,text='Display:').pack(pady=10)
#Input field
name_field = ctk.CTkEntry(main_container)
name_field.pack(pady=10)

#button

submit_button = ctk.CTkButton(main_container,text='Submit')
submit_button.pack(pady=20)


app.mainloop()

