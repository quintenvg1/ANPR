# program to run the guis
import wx
import database_handler

global dbmanager #kinda want to access the controller from every function
dbmanager = database_handler.Databasecontroller #define the manager to be a database controller

loggedin = False
x = 25
y = 25

def printhello():
    print("hello")

class window1(wx.Frame): #
    def __init__(self, *args, **kw):
        super(window1, self).__init__(parent=None, title='ANPR main', size=(480,320)) #super is usefull to run the class anyway, and call the methods and variables from another program
        panel = wx.Panel(self)
        
        label1 = wx.StaticText(panel, pos=(7 * x, 1 * y), label="status")
        text1 = wx.TextCtrl(panel, pos=(12 *  x, 2 * y), value="text")
        text1.Bind(wx.EVT_TEXT, self.updateText)
        
        btn1 = wx.Button(panel,  pos=(7 * x, 2 * y ) ,label="emergency")
        btn1.Bind(wx.EVT_BUTTON, self.emergency)
        

        self.Show()
    def emergency(self, event):
        print("emergency active opening the gates")
    #end-emergency
    
    def updateText(self, event):
        text = event.GetString()
        print(text)
    #end-updateText
        
#end-window1
        
name = ""
password = ""
plaat = ""
class window2(wx.Frame): #anpr manager
    def __init__(self, *args, **kw): #runs automatically
        super(window2, self).__init__(parent=None, title='window2', size=(480,320))
        panel = wx.Panel(self)
        
        #nametag
        text_ctrl1 = wx.TextCtrl(panel, pos=(5, 5), value="naam")
        text_ctrl1.Bind(wx.EVT_TEXT, self.nametext)
        
        #passwordtag
        text_ctrl2 = wx.TextCtrl(panel, pos=(5, 50), value="paswoord")
        text_ctrl2.Bind(wx.EVT_TEXT, self.passwordtext)
        
        #license plate tag
        text_ctrl3 = wx.TextCtrl(panel, pos=(5, 100), value="plaat")
        
        #
        text_ctrl4 = wx.TextCtrl(panel, pos=(5, 150), size=(250, 75), value="program log")
        
        st = wx.StaticText(panel, label="userid:", pos=(300, 50))
        uid = wx.StaticText(panel, label="1", pos=(350, 50))
        #loginbutton
        my_btn = wx.Button(panel, label='login', pos=(100, 50))
        my_btn.Bind(wx.EVT_BUTTON, self.login)
        my_btn1 = wx.Button(panel, label='update', pos=(100, 100))
        my_btn1.Bind(wx.EVT_BUTTON, self.update)
        my_btn2 = wx.Button(panel, label="logout", pos=(300, 100))
        my_btn2.Bind(wx.EVT_BUTTON, self.logout)
        my_btn3 = wx.Button(panel, label="delete account", pos=(300,150))
        my_btn3.Bind(wx.EVT_BUTTON, self.delete_account)
        version_icon = wx.StaticText(panel, pos=(300, 175), label="version 0.0.1b")
        connection_status = wx.StaticText(panel, pos=(300, 200), label="not connected")
        
        self.Show()
    
    #text handling
    def nametext(self, event):
        global name
        name = event.GetString()
        print(name)
    #end-nametext
    def passwordtext(self, event):
        global password
        password = event.GetString()
        print(password)
    #end-passwordtext
        
    def login(self, event):
        user = ""
        global loggedin #because global...?
        global name
        global password
        print(name)
        print(password)
        #query the database on username and 
        print("attempting login")
        #loggedin = True
        user = dbmanager.getuserfromcredentials(name, password)
        if(user != ""):
            loggedin = True # the uses is logged in now
        print(user)
    #end-login
    
    def update(self, event):
        global loggedin #because global...?
        #query the database to update where username is correct
        
        print("attempting update")
        #write to text_ctrl4 'updating'
        if loggedin:
            pass
        else:
            wx.MessageBox("you have to login first")
    #end-update
    
    def logout(self, event):
        global loggedin
        loggedin = False
    #endlogout
    
    def delete_account(self, event):
        pass
    #end-delete_account
#end-window2

if __name__ == '__main__':
    app = wx.App()
    frame = window1()
    frame2 = window2()
    app.MainLoop()
#end-if