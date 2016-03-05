from tkinter import *
from email.mime.text import MIMEText
import smtplib
import time

#define gui master window
class EmailSender(Frame):
    """This is a gui that makes email editing easy"""
    #Upon initialization, create the UI
    def __init__(self, parent):
        Frame.__init__(self, parent)

        #initiaize from and to boxes, including labels
        self.top_row = Frame()
        #from box, including label
        self.from_label = Label(self.top_row, text='From:', width=4)
        self.from_label.pack(side=LEFT)
        self.from_box = Entry(self.top_row, width=35)
        self.from_box.insert(0, 'from_email')
        self.from_box.pack(side=LEFT)
        #to box, including label
        self.to_label = Label(self.top_row, text='To:', width=3)
        self.to_label.pack(side=LEFT)
        self.to_box = Entry(self.top_row, width=35)
        self.to_box.insert(0, 'to_email')
        self.to_box.pack(side=LEFT)
        self.top_row.pack(side=TOP)

        #initialize subject box, including labels
        self.second_row = Frame()
        self.subject_label = Label(self.second_row, text='Subject:', width=7)
        self.subject_label.pack(side=LEFT)
        self.subject_box = Entry(self.second_row, width=74)
        self.subject_box.insert(0, 'Subject Goes Here!')
        self.subject_box.pack(side=LEFT)
        self.second_row.pack(side=TOP)

        #initialize the send button
        self.send_button=Button(text='Send', command=self.send_mail)
        self.send_button.pack(side=BOTTOM)
        self.message_box = Text(width=105, height=35)
        self.message_box.insert(END, open('message_body.txt').read())
        self.message_box.pack(side=BOTTOM)

    #When the send button is clicked, send an email
    def send_mail(self):
        #print out the from and to addresses, the subject, and the message to the python shell.
        #note: the "from" address doesn't actually do anything. the email will be sent from
        #the username and password pair located in the server.login command below
        fromaddr = self.from_box.get()
        print('\n\nNew message:\n', 'From: ', fromaddr)
        toaddr = self.to_box.get()
        print('\nTo: ', toaddr)
        self.subject_box.delete(0, END)
        self.subject_box.insert(0, 'Email')
        subject = self.subject_box.get()
        print('\nSubject: ', subject)
        message = self.message_box.get(1.0, END)
        print('\nMessage: ', message)

        #generate the message body
        email_draft = MIMEText(message)
        email_draft['Subject'] = subject
        email_draft['From'] = fromaddr
        email_draft['To'] = toaddr

        #send the email
        server = smtplib.SMTP('smtp_client')
        server.ehlo()
        server.starttls()
        #Note: Your username and password go here. The email will send from this email address
        server.login('Username', 'Password')
        server.send_message(email_draft)
        server.quit()

        #print message sent for confirmation
        print('Message sent!')

#main function
if __name__ == '__main__':
    window = Tk()
    shell = EmailSender(window)
