from tkinter import *

#create window object
app = Tk()

#part 
part_text = StringVar()
part_label = Label(app, text="Part Name", font=('bold,14'), pady=20)
part_label.grid(row=0,column=0)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)

app.title('Part Manager')
app.geometry('700x350')

#start program
app.mainloop()
