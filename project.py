from tkinter import *

root = Tk()
root.title("Voting System (CRUD)")


students:list = []
index:list = []

for i in range(0,len(index)):
    students[i] == index[i]
    for j in range(0,len(index)-i-1):
        if index[j]> index[j+1]:
            temp = index[j]
            index[j] = index[j+1]
            index[j+1] = temp
            
            temp = students[j]
            students[j] = students[j+1]
            students[j+1] = temp


Label(root, text="Current Students:").pack(pady=5)
listbox = Listbox(root, width=50, height=10)
listbox.pack(pady=5)

Label(root, text="Enter Student Name:").pack(pady=5)

def add_student():
    name = student_name.get().strip().lower() 
    if name: 

        exists = False
        for student in students:
            if student["name"] == name:
                exists = True
                break
        if not exists:
            students.append({"name": name, "votes": 0}) 
            student_name.delete(0, END)
            refresh_list() 
        else:
            message_label.config(text=f"Student '{name}' already exists!")
    else:
        message_label.config(text="Please enter a name!")


        
            
student_name = Entry(root, width=50, borderwidth=5)
student_name.pack(pady=5)
Button(root, text="Add Student", command=add_student, fg="green").pack(pady=2)

def refresh_list():
    listbox.delete(0, END)
    for student in students:
        listbox.insert(END, f"{student['name']} - Votes: {student['votes']}")






def add_vote():
    selected = listbox.curselection()  
    if selected:
        index = selected[0]
        students[index]["votes"] += 1 
        refresh_list()
    else:
        message_label.config(text="Select a student first!")

Button(root, text="Add Vote", command=add_vote, fg="blue").pack(pady=2)


def delete_student():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        removed_name = students[index]["name"]
        students.pop(index)
        refresh_list()
        message_label.config(text=f"Deleted: {removed_name}")
    else:
        message_label.config(text="Select a student to delete!")
        
Button(root, text="Delete Student", command=delete_student, fg="red").pack(pady=2)       
message_label = Label(root, text="", fg="gray")
message_label.pack(pady=5)






root.mainloop()


