from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile

from PIL import Image,ImageTk
import backend_draft
import backend_email
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib




main_window = Tk()
main_window.title (" DevNgecu Email Sender")




#Send email function
def send_email(receiver_email,subject,message):
    if "@" and ".com" not in receiver_email:
        messagebox.showinfo("showinfo", "Invalid email") 
        return FALSE
    if (len(subject)==0) or (len(message)==1):
        messagebox.showinfo("Error","Please fill all entries")
        return FALSE
    else:
        print("length of receiver is",len(receiver_email),len(subject),len(message))
        # create message object instance
        msg = MIMEMultipart()
        
        print("receiver",receiver_email)
        
        # setup the parameters of the message
        password = "fromKenyaToTheWorld254"
        msg['From'] = "ngecu16@gmail.com"
        msg['To'] = receiver_email
        msg['Subject'] = subject
        

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
         
        
    
        
        #create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        
        
        # send the message via the server.
        server.sendmail(msg['From'], receiver_email.split(','), msg.as_string())
        
        server.quit()

        print ("successfully sent email to %s:" % (msg['To']))
        messagebox.showinfo("showinfo", "Message successfully sent to {}".format(msg['To'])) 
        
        
        backend_email.insert(msg['To'],msg['Subject'],message,datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))


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
               
#functions to call other windows
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


    

    view_all_btn = Button(sent_window,text="View All",command=lambda : view_all_email(listbox1),width=12)
    view_all_btn.grid(row=2,column=5)    
    
    search_btn = Button(sent_window,command=lambda : search_email(listbox1,to_text,subject_text,message_text) ,text="Search",width=12)
    search_btn.grid(row=3,column=5)
   

    
    close_sent = Button(sent_window,text="Close",command=lambda : close_sent_window(sent_window),width=12)
    close_sent.grid(row=4,column=5)  
    
    
    listbox1=Listbox(sent_window,height=8,width=60)
    listbox1.grid(row=2,column=0,rowspan=10,columnspan=5)    
    
                
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

    view_all_btn = Button(draft_window,text="View All",width=12,command=lambda :view_command_draft(listbox1))
    view_all_btn.grid(row=2,column=5)
        
    search_btn = Button(draft_window,text="Search",width=12,command=lambda : search_command_draft(listbox1,to_text,subject_text,message_text))
    search_btn.grid(row=3,column=5)

  
    close_btn = Button(draft_window,text="Close",command=lambda : close_draft_window(draft_window),width=12)
    close_btn.grid(row=4,column=5)  
    
    
#background image
image = Image.open('Assets/original2.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(main_window, image = photo_image)
label.pack()

#bouter uttons



compose_var = StringVar()
compose_label = Label(main_window,textvariable=compose_var,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
compose_var.set("✍Compose")
compose_label.place(relx=.01,rely=.4,relwidth=.18,relheight=.075)

# attachment_btn = Button(main_window,text="Attachment",command=lambda:UploadAction(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
# attachment_btn.place(relx=.01,rely=.4,relwidth=.18,relheight=.075)


sent_btn = Button(main_window,text="Sent",command=lambda:sent_window_f(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
sent_btn.place(relx=.01,rely=.595,relwidth=.18,relheight=.075)

draft_btn = Button(main_window,text="Drafts",command=lambda:draft_window_f(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
draft_btn.place(relx=.01,rely=.8,relwidth=.18,relheight=.075)

#main_frame
compose_frame = Frame(main_window,bg="#D72017")
compose_frame.place(relx=.199,rely=.13,relwidth=.775,relheight=.86)

#content inside compose frame

to_var = StringVar()
to_label = Label( compose_frame, textvariable=to_var, bg="#D72017",fg="white",font = ('courier', 30,))
to_var.set("To:")
to_label.place(relx=.0,rely=0.03,relwidth=.18,relheight=.075)

email_value=StringVar()
to_email_address_input_field = Entry(compose_frame,textvariable=email_value,bg="#737373",fg="white",font = ('courier', 30, 'bold'))
to_email_address_input_field.place(relx=.197,rely=0.03,relwidth=.78,relheight=.075)


var = StringVar()
subject_label = Label( compose_frame, textvariable=var, bg="#D72017",fg="white",font = ('courier', 30,) )
var.set("Subject:")
subject_label.place(relx=.0,rely=0.15,relwidth=.18,relheight=.075)

subject_value=StringVar()
subject_input_field = Entry(compose_frame,textvariable=subject_value,bg="#737373",fg="white",font = ('courier', 30, 'bold'))
subject_input_field.place(relx=.197,rely=0.15,relwidth=.78,relheight=.075)

var = StringVar()
compose_label = Label( compose_frame, textvariable=var, bg="#D72017",fg="white",font = ('courier', 30,) )
var.set("Message:")
compose_label.place(relx=.0,rely=0.32,relwidth=.18,relheight=.075)

compose_field = Text(compose_frame,fg="white",relief=FLAT,bg="#444444",font = ('courier', 20, 'bold'))
compose_field.place(relx=.197,rely=.32,relwidth=.78,relheight=.55)


save_btn = Button(compose_frame,text="Save ♥",command=lambda : save_to_draft(email_value.get(),subject_value.get(),compose_field.get("1.0",END)), relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
save_btn.place(relx=.55,rely=.90,relwidth=.18,relheight=.075)


send_btn = Button(compose_frame,text="Send \u2713 ",command=lambda :send_email(email_value.get(),subject_value.get(),compose_field.get("1.0",END)),relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
send_btn.place(relx=.797,rely=.90,relwidth=.18,relheight=.075)


main_window.mainloop()