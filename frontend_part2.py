from tkinter import *
from tkinter import messagebox


from PIL import Image,ImageTk

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
        password = ""
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


    

    view_all_btn = Button(sent_window,text="View All",width=12)
    view_all_btn.grid(row=2,column=5)    
    
    search_btn = Button(sent_window,text="Search",width=12)
    search_btn.grid(row=3,column=5)
   

    
    close_sent = Button(sent_window,text="Close",width=12)
    close_sent.grid(row=4,column=5)  
    
    
    listbox1=Listbox(sent_window,height=8,width=80)
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


    listbox1=Listbox(draft_window,height=8,width=80)
    listbox1.grid(row=2,column=0,rowspan=10,columnspan=5)    

    view_all_btn = Button(draft_window,text="View All",width=12)
    view_all_btn.grid(row=2,column=5)
        
    search_btn = Button(draft_window,text="Search",width=12)
    search_btn.grid(row=3,column=5)

  
    close_btn = Button(draft_window,text="Close",width=12)
    close_btn.grid(row=4,column=5)  
    

def compose_new():
    to_email_address_input_field.delete(0,END)
    subject_input_field.delete(0,END)
    compose_field.delete('1.0',END)

#background image
image = Image.open('Assets/background.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(main_window, image = photo_image)
label.pack()

#bouter uttons


compose_btn = Button(main_window,text="✍Compose",command=lambda:compose_new(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
compose_btn.place(relx=.01,rely=.4,relwidth=.18,relheight=.075)

sent_btn = Button(main_window,text="Sent",command=lambda:sent_window_f(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
sent_btn.place(relx=.01,rely=.595,relwidth=.18,relheight=.075)

draft_btn = Button(main_window,text="Drafts",command=lambda:draft_window_f(),relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
draft_btn.place(relx=.01,rely=.8,relwidth=.18,relheight=.075)

#main_frame
compose_frame = Frame(main_window,bg="#D72017")
compose_frame.place(relx=.22,rely=.13,relwidth=.775,relheight=.86)

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


save_btn = Button(compose_frame,text="Save ♥", relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
save_btn.place(relx=.55,rely=.90,relwidth=.18,relheight=.075)


send_btn = Button(compose_frame,text="Send \u2713 ",command=lambda :send_email(email_value.get().lower(),subject_value.get(),compose_field.get("1.0",END)),relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
send_btn.place(relx=.797,rely=.90,relwidth=.18,relheight=.075)


main_window.mainloop()
#python -m virtualenv .
#.\scripts\activate