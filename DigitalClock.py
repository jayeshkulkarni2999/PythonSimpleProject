from tkinter import *
from time import strftime

# Initialize Tkinter window
root = Tk()
root.title("Digital Clock")
root.configure(bg="black")  # Set background to black
root.geometry("600x300")  # Adjust window size

# Load custom digital font (Ensure it's installed or available)
FONT_LARGE = ("DS-Digital", 120)  # Time font
FONT_MEDIUM = ("DS-Digital", 40)   # Date & AM/PM font
FONT_SMALLER = ("DS-Digital", 20)  # Time font
FONT_SMALL = ("DS-Digital", 25)    # Weekday font

# Function to update time
def update_time():
    current_time = strftime('%I:%M')  # 12-hour format
    current_sec = strftime('%S')  # seconds
    am_pm = strftime('%p')  # AM/PM
    full_date = strftime('%B %d %Y')  # Month Day Year
    weekday = strftime('%A')  # Weekday name

    # Update labels
    time_label.config(text=current_time)
    am_pm_label.config(text=am_pm)
    date_label.config(text=full_date)
    weekday_label.config(text=weekday)
    second_label.config(text=current_sec)

    # Refresh every second
    root.after(1000, update_time)



# AM/PM display
am_pm_label = Label(root, font=FONT_SMALL, bg="black", fg="lime")
am_pm_label.place(x=425, y=40)  # Position in top-

# Time display
time_label = Label(root, font=FONT_LARGE, bg="black", fg="lime")
time_label.place(x=75, y=20)

second_label = Label(root,font=FONT_SMALL,bg="black", fg="lime")
second_label.place(x=425, y= 120)

# Date display
date_label = Label(root, font=FONT_SMALLER, bg="black", fg="lime")
date_label.place(x=75, y=170)

# Weekday display
weekday_label = Label(root, font=FONT_SMALLER, bg="black", fg="lime")
weekday_label.place(x=350, y=170)

# Start clock update
update_time()

# Run application
root.mainloop()
