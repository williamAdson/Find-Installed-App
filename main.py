from tkinter import *
import winapps

# Attach output
def app():
    for item in winapps.search_installed(e.get()):
        name.set(item.name)
        version.set(item.version)
        Install_date.set(item.install_date)
        publisher.set(item.publisher)
        uninstall_string.set(item.uninstall_string)

# tkinter objects
root = Tk()
root.title('Windows App Finder')
root.configure(bg='light green')

# tkinter variables
name = StringVar()
version = StringVar()
Install_date = StringVar()
publisher = StringVar()
uninstall_string = StringVar()

# create labels each variable
Label(root, text="Enter Application Name: ").grid(row=0, sticky=W)
Label(root, text="Name: ").grid(row=2, sticky=W)
Label(root, text="Version: ").grid(row=3, sticky=W)
Label(root, text="Install Date: ").grid(row=4, sticky=W)
Label(root, text="Publisher: ").grid(row=5, sticky=W)
Label(root, text="Uninstall String: ").grid(row=6, sticky=W)

# create labels for inputs
Label(root, text="", textvariable=name).grid(row=2, column=1, sticky=W)
Label(root, text="", textvariable=version).grid(row=3, column=1, sticky=W)
Label(root, text="", textvariable=Install_date).grid(row=4, column=1, sticky=W)
Label(root, text="", textvariable=publisher).grid(row=5, column=1, sticky=W)
Label(root, text="", textvariable=uninstall_string).grid(row=6, column=1, sticky=W)

# 
e = Entry(root, width=30)
e.grid(row=0, column=1)

# create a button using the widget
btn = Button(root, text="Show", command=app, bg='Red')
btn.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

root.mainloop()