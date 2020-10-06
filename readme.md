![Test Image 1](Assets/main.png)
Hi guys,
In this video will be creating an email app with python's tkinter module

Before we dive into the code,let me demostrate this.As you can see the program is a standalone executable file where we just need to open it up.

By default the sender's credential are configured in code so all the user needs to focus on is the receiver's email,subject and message.

So let me go ahead and try to send an email to devngecu@gmail.com.The subject ,message and then press the send button.

The application prompts a message box saying message sent successfully to the email that i entered.

So to prove this ill need to open my email on my browser.

As you can see it surely delivered the email.

The best way to unearth errors is creating one yourself,so what if a user doesn't input a valid email or doesnt fill any subject or message.

Well the application detects this and breaks the sending cycle.

Also as soon as the message is sent the application,records the details in its database.For the user to access the sending history,all he/she needs is to click on the sent button.

He/she has the option of viewing all the emails,or search for a particular receipient's email or subject.

This also applies for the drafts,where the user can save a draft and review it late as it is also stored ont the application's databe.

So,without wasting anytime lets get started.

-----------------------

We will start off with creating the user interface which is the frontend so inside our empty directory:
```
touch frontend.py
```
But first we need to also create a virtual environment to enclose our project's dependencies within. So
```
virtualenv -p /usr/bin/python3 venv
```
Dont forget to activate the environment.
```
source venv/bin/activate
```
Then inside our frontend script import all packages from the tkinter module
````
from tkinter import *
````
we then define the main_window from the Tk() package
````
main_window = Tk()
````
our app will need a title so:
```
main_window.title (" DevNgecu Email Sender")
```
and then finally the mainloop to keep the window open through out unless otherwise
```
main_window.mainloop()
```
so lets check out the results:
![Test Image 1](Assets/main_window.png)

----------------------------------
Next step is working on the background image.For that i'll create a directory by the name "Assets" and paste my background image in there

When working with media elements such as photos in tkinter we require the help of external modules to implement such use.

For this task we need to install a module called Pillow also called PIL:
```
pip3 install Pillow
```
in our script we require 2 packages from pillow,which are "Image" and "ImageTk":
```
from PIL import Image,ImageTk
```

the first package,image comes in handy to open up our picture from the directory:
```
image = Image.open('Assets/original2.png')

```
And the second one intergrates it to be compatible for the tkinter workspace.
```
photo_image = ImageTk.PhotoImage(image)
```
ill not dwell much on this,i'll have the link in the description.

Next we need to foster the compatible tkinter image to the actual window as a widget.There is no better way than a label since it accepts image as it propperties:
```
background_image = Label(main_window, image = photo_image)

```
Since the photo resolution is equivalent to the screen,we just need to pack it:
```
background_image.pack()
```
-----------------------------

next widget to work on is the compose fame:

ill attach it to the main window with a red touch colour and place it relative to the its master 
```
compose_frame = Frame(main_window,bg="#D72017")
compose_frame.place(relx=.199,rely=.13,relwidth=.775,relheight=.86)
```
inside the compose frame are the three labels:
### 1. To Label
```
to_var = StringVar()
to_label = Label( compose_frame, textvariable=to_var, bg="#D72017",fg="white",font = ('courier', 30,))
to_var.set("To:")
to_label.place(relx=.0,rely=0.03,relwidth=.18,relheight=.075)
```
### 2. Subject Label

```
var = StringVar()
subject_label = Label( compose_frame, textvariable=var, bg="#D72017",fg="white",font = ('courier', 30,) )
var.set("Subject:")
subject_label.place(relx=.0,rely=0.15,relwidth=.18,relheight=.075)
```
### 3. Compose Label

```
var = StringVar()
compose_label = Label( compose_frame, textvariable=var, bg="#D72017",fg="white",font = ('courier', 30,) )
var.set("Message:")
compose_label.place(relx=.0,rely=0.32,relwidth=.18,relheight=.075)
```

Beside each of these three we require 2 input fields and a textfield

### Email Adress Input Field Widget
starting of is the receipient's email input field,which in tkinter's language is an entry widget

```
email_value=StringVar()
to_email_address_input_field = Entry(compose_frame,textvariable=email_value,bg="#737373",fg="white",font = ('courier', 30, 'bold'))
to_email_address_input_field.place(relx=.197,rely=0.03,relwidth=.78,relheight=.075)
```
### Subject Input Field Widget
```
subject_value=StringVar()
subject_input_field = Entry(compose_frame,textvariable=subject_value,bg="#737373",fg="white",font = ('courier', 30, 'bold'))
subject_input_field.place(relx=.197,rely=0.15,relwidth=.78,relheight=.075)
```
### Message TextField Widget
```
message_text_field = Text(compose_frame,fg="white",relief=FLAT,bg="#444444",font = ('courier', 20, 'bold'))
message_text_field.place(relx=.197,rely=.32,relwidth=.78,relheight=.55)
```

Also inside the compose frame we have the two buttons:
### Save Button
```
save_btn = Button(compose_frame,text="Save ♥", relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
save_btn.place(relx=.55,rely=.90,relwidth=.18,relheight=.075)
```

### Send Button
```
send_btn = Button(compose_frame,text="Send \u2713 ",compose_field.get("1.0",END)),relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
send_btn.place(relx=.797,rely=.90,relwidth=.18,relheight=.075)
```
Now for the other buttons:

### Sent Button
```
sent_btn = Button(main_window,text="Sent",fg="white",font = ('courier', 30, 'bold') )
sent_btn.place(relx=.01,rely=.595,relwidth=.18,relheight=.075)
```
### Draft Button
```
draft_btn = Button(main_window,text="Drafts",relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
draft_btn.place(relx=.01,rely=.8,relwidth=.18,relheight=.075)
```
-----------------------------
With that we are through with the user interphase of our main window.Next is to focus on the two sub windows that are triggered when the user clicks on the draft or sent button:
For this we need to define the function:
```
def sent_window_f():
    sent_window = Toplevel(main_window)
```
now,we need to call it once the button is pressed so will use lambda functio:
```
sent_btn = Button(main_window,text="Sent",command=lambda:sent_window_f(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )

```
Also for the other button:
```
def draft_window_f():
    draft_window = Toplevel(main_window)
```
```
draft_btn = Button(main_window,text="Drafts",command=lambda:draft_window_f(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
```
Lets run the script to find how much we have covered:

Lets now build up the draft and sent windows:

```
def sent_window_f():
    sent_window = Toplevel(main_window)
    sent_window.title ("Sent Emails")
    sent_window.geometry("700x200+350+200")
    sent_window.resizable(0,0)
    # this wil create a label widget 
    # this wil create a label widget 
    l1 = Label(sent_window, text = "To:") 
    l1.grid(row = 0, column = 1, sticky = W, pady = 2) 


    l2 = Label(sent_window, text = "Message") 
    l2.grid(row = 0, column = 4, sticky = W, pady = 2) 


    to_text=StringVar()
    subject_text = StringVar()
    message_text=StringVar() 

    e1 = Entry(sent_window,textvariable=to_text)
    e2 = Entry(sent_window,textvariable=subject_text) 

    # this will arrange entry widgets 
    e1.grid(row = 0, column = 1, pady = 1,columnspan=3) 
    e2.grid(row = 0, column = 5, pady = 1) 

    view_all_btn = Button(sent_window,text="View All",width=12)
    view_all_btn.grid(row=2,column=5)    
    
    search_btn = Button(sent_window,text="Search",width=12)
    search_btn.grid(row=3,column=5)
   
    close_sent = Button(sent_window,text="Close",width=12)
    close_sent.grid(row=4,column=5)  
    
    listbox1=Listbox(sent_window,height=8,width=60)
    listbox1.grid(row=2,column=0,rowspan=10,columnspan=5)      
```
```
def draft_window_f():
    draft_window = Toplevel(main_window)
    draft_window.title ("Draft Emails")
    draft_window.geometry("700x200+750+200")
    draft_window.resizable(0,0)
    
    
    # this wil create a label widget 
    l1 = Label(draft_window, text = "To:") 
    l1.grid(row = 0, column = 1, sticky = W, pady = 2) 


    l2 = Label(draft_window, text = "Message") 
    l2.grid(row = 0, column = 4, sticky = W, pady = 2) 



    to_text=StringVar()
    subject_text = StringVar()
    message_text=StringVar() 

 
    e1 = Entry(draft_window,textvariable=to_text)
    e2 = Entry(draft_window,textvariable=subject_text) 

    # this will arrange entry widgets 
    e1.grid(row = 0, column = 1, pady = 1,columnspan=3) 
    e2.grid(row = 0, column = 5, pady = 1) 


    listbox1=Listbox(draft_window,height=8,width=60)
    listbox1.grid(row=2,column=0,rowspan=10,columnspan=5)    

    view_all_btn = Button(draft_window,text="View All",width=12)
    view_all_btn.grid(row=2,column=5)
        
    search_btn = Button(draft_window,text="Search",width=12)
    search_btn.grid(row=3,column=5)

  
    close_btn = Button(draft_window,text="Close",width=12)
    close_btn.grid(row=4,column=5)
```
next is the functionality of this buttons:
```
    view_all_btn = Button(draft_window,text="View All",width=12,command=lambda :view_command_draft(listbox1))
    view_all_btn.grid(row=2,column=5)
        
    search_btn = Button(draft_window,text="Search",width=12,command=lambda : search_command_draft(listbox1,to_text,subject_text,message_text))
    search_btn.grid(row=3,column=5)

  
    close_btn = Button(draft_window,text="Close",command=lambda : close_draft_window(draft_window),width=12)
    close_btn.grid(row=4,column=5) 
```
```
    view_all_btn = Button(sent_window,text="View All",command=lambda : view_all_email(listbox1),width=12)
    view_all_btn.grid(row=2,column=5)    
    
    search_btn = Button(sent_window,command=lambda : search_email(listbox1,to_text,subject_text,message_text) ,text="Search",width=12)
    search_btn.grid(row=3,column=5)
   
    close_sent = Button(sent_window,text="Close",command=lambda : close_sent_window(sent_window),width=12)
    close_sent.grid(row=4,column=5)  
```
now lets define the functions to call:

```
#draft functions    
def view_command_draft(l):
    l.delete(0,END)
    for row in backend_draft.view():
        if row:
            l.insert(END,row)
        else:
            l.insert(END,"No such data")

def search_command_draft(l,to_text,subject_text,message_text):
    l.delete(0,END)
    
    if to_text.get() not in backend_draft.search(to_text.get(),subject_text.get(),message_text.get()) :
        messagebox.showinfo("Search Result", "No such data") 

    
    for row in backend_draft.search(to_text.get(),subject_text.get(),message_text.get()):
        l.insert(END,row)
        

def save_to_draft(email,subject,compose):
   backend_draft.insert(email,subject,compose,datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
   print("saved {} {} {},".format(email,subject,compose))
    
def close_draft_window(window):
    window.destroy() 
    

#email functions
def view_all_email(l):
    l.delete(0,END)
    for row in backend_email.view():
       l.insert(END,row)

def search_email(l,to_text,subject_text,message_text):
    l.delete(0,END)

    if to_text.get() not in backend_email.search(to_text.get(),subject_text.get(),message_text.get()) :
        messagebox.showinfo("Search Result", "No such data") 
        
    for row in backend_email.search(to_text.get(),subject_text.get(),message_text.get()):
        
        l.insert(END,row) 
        if "no such data" in row:
            l.delete(0,0)
def close_sent_window(window):
    window.destroy()
```
