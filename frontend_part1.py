from tkinter import *
from PIL import Image,ImageTk


main_window = Tk()
main_window.title (" DevNgecu Email Sender")


#background image
image = Image.open('Assets/background.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(main_window, image = photo_image)
label.pack()


compose_btn = Button(main_window,text="✍Compose",relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
compose_btn.place(relx=.01,rely=.4,relwidth=.18,relheight=.075)

sent_btn = Button(main_window,text="Sent",relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
sent_btn.place(relx=.01,rely=.595,relwidth=.18,relheight=.075)

draft_btn = Button(main_window,text="Drafts",relief=FLAT,bg="#303841",fg="white",font = ('courier', 30, 'bold') )
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


save_btn = Button(compose_frame,text="Save ♥",relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
save_btn.place(relx=.55,rely=.90,relwidth=.18,relheight=.075)


send_btn = Button(compose_frame,text="Send \u2713 ",relief=FLAT,bg="#737373",fg="white",font = ('courier', 30, 'bold') )
send_btn.place(relx=.797,rely=.90,relwidth=.18,relheight=.075)


main_window.mainloop()
#python -m virtualenv .
#.\scripts\activate