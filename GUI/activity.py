import tkinter as tk

def button1_action():
    # Function for Button 1 action
    text = entry1.get()
    textbox.insert(tk.END, f"Button 1 clicked. Entry 1 value: {text}\n")

def button2_action():
    # Function for Button 2 action
    text = entry2.get()
    textbox.insert(tk.END, f"Button 2 clicked. Entry 2 value: {text}\n")

# Create the main window
window = tk.Tk()
window.title("Entry and Buttons Example")

# Create the three entries
label1 = tk.Label(window, text="Entry 1:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Entry 2:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Create the textbox to display the button actions
textbox = tk.Text(window)
textbox.pack()

# Create the buttons
button1 = tk.Button(window, text="START", command=button1_action)
button1.pack()



# Run the main event loop
window.mainloop()
