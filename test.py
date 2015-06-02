def factorial(x):
	if x<1:
		return 1 
	return factorial(x-1)*x
# s = 0
# for x in xrange(0,101):
# 	s = s + 1.0/factorial(x)
# print s
from tkinter import *
import random
import string
# str = random.choice (['麵攤','自助餐','遠征','中視'])
# print(str)






class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    # def sendMail(me,you,text):
    #     msg['Subject'] = '今天午餐吃 ： %s' % text
    #     msg['From'] = me
    #     msg['To'] = you

    #     # Send the message via our own SMTP server.
    #     s = smtplib.SMTP('smtp.gmail.com', 587)
    #     s.send_message(msg)
    #     s.quit()
    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "吃:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=6)
 
        self.new = Button(self)
        self.new["text"] = "今天吃什麼"
        self.new.grid(row=2, column=4)
        self.new["command"] = self.tellme
        self.new = Button(self)
        self.new["text"] = "發送信件"
        self.new.grid(row=2, column=5)
        self.new["command"] = self.sendmail
    def tellme(self):
        self.inputField.delete(0, END)
        # sendtext = '今天午餐吃 : '
        sendtext = ''
        sendtext += random.choice(['麵攤','麵攤','麵攤','麵攤','小火鍋','自助餐','自助餐','自助餐','自助餐','新開的熱炒','新開的熱炒','新開的熱炒','八方雲集','中視','鹿過','北大荒水餃','牛肉麵','上何小館'])
        self.inputField.insert(0, sendtext)
    def sendmail(self):
        # 引入函式庫
        import smtplib
        import os
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        
        COMMASPACE = ', '
        # 帳號密碼
        sender = 'hermit.lin@topctek.com'
        gmail_password = 'vwz2zpnz'
        # 收件人
        # recipients = ['hermit.lin@topctek.com','kim.ye@topctek.com','hardy.wang@topctek.com','allick.wang@topctek.com','invers.c@topctek.com','retsu.yang@topctek.com']
        recipients = ['hermit.lin@topctek.com']
        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        # 信件主旨
        outer['Subject'] = '午餐通知'
        outer['To'] = COMMASPACE.join(recipients)
        outer['From'] = sender
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
        # 信件內容
        msg = '今天午餐吃 ： '+self.inputField.get() + '！！ '
        outer.attach(MIMEText(msg))
        # List of attachments
        composed = outer.as_string()

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, gmail_password)
                s.sendmail(sender, recipients, composed)
                s.close()
            print("Email sent!")
        except:
            print("Unable to send the email. Error: ", sys.exc_info()[0])
            raise
        
if __name__ == '__main__':
    root = Tk()
    app = GUIDemo(master=root)
    app.mainloop()
# import matplotlib.pyplot as plt
# import numpy as np



# h = 1
# y1 = (np.sin(h)-np.sin(-h))/(h*2)
# y2 = np.cos(0)



# plt.plot(h,y1,'o',label="h = 1")
# h = 0.1
# y1 = (np.sin(h)-np.sin(-h))/(h*2)
# plt.plot(h,y1,'o',label="h = 0.1")
# h = 0.01
# y1 = (np.sin(h)-np.sin(-h))/(h*2)
# plt.plot(h,y1,'o',label="h = 0.01")
# h = 0.001
# y1 = (np.sin(h)-np.sin(-h))/(h*2)
# plt.plot(h,y1,'o',label="h = 0.001")
# plt.plot(h,y2,'o',color="red",label="cos(0)") 
# # plt.plot(x,y,label="$tan(x)$",color="red",linewidth=2)

# plt.xlim(-0.006,1.02)
# plt.ylim(0.82,1.04)
# # plt.y2lim(-1.5,1.5)

# plt.xlabel("h-value") 
# plt.ylabel("y-axis") 
# plt.title("The Title") 



# plt.legend()
# plt.show() 