# prusadjs.cz

from Tkinter import *
import tkFileDialog
import socket
import time
BUFFER_SIZE = 1024
HI="Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! Hi! "

class EtheRep:

    def __init__(self, master):

        frame = Frame(master)

        # Connection section 
        grid_row_offset = 0
        self.connection_label = Label(text='Connection',anchor=W,justify=LEFT)
        self.connection_label.grid(row=grid_row_offset+0,column=0,columnspan=2)

        self.ip_label = Label(text='IP: ').grid(row=grid_row_offset+1)
        self.ip_input = Entry(master, width=18)
        self.ip_input.grid(row=grid_row_offset+1,column=1)
        self.ip_input.insert(0, '192.168.1.111')

        self.port_label = Label(text='Port: ').grid(row=2)
        self.port_input = Entry(master, width=10)
        self.port_input.grid(row=grid_row_offset+2,column=1)
        self.port_input.insert(0, '7')

        self.button1 = Button(text="Connect", command=self.say_hi)
        self.button1.grid(row=grid_row_offset+1, column=2)

        # Status section
        self.grid_row_offset = 2
        self.scrollbar = Scrollbar(root)
        self.debug = Listbox()
        self.debug.config(yscrollcommand=self.scrollbar.set)
        self.debug.insert(master.END, "Hello")
        self.scrollbar.grid(row=4,column=4)
        self.text1.grid(row=4,column=3)
       


        
    def say_hi(self, data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(( self.ip_input.get() , int(self.port_input.get()) ))
        s.send(data)
        s.close()
        
    def send_file(self):
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
        if file != None:
            data = file.readlines()
            file.close()
            print "I got %d bytes from this file." % len(data)
            now = time.time()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = self.ip_input.get()
            port = int(self.port_input.get())
            for item in data:
                print item
                s.connect(( ip , port  ))
                s.sendall(item)
                s.close()
            print time.time()-now



root = Tk()

app = EtheRep(master)


root.title('Etherep')
root.resizable(0, 0)

root.mainloop()



