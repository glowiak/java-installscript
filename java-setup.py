#OpenJDK Java Installer for Ubuntu Linux
import Tkinter
import os

def sjre():
    os.system("sudo apt-get install openjdk-6-jre")

def sjdk():
    os.system("sudo apt-get install openjdk-6-jdk")

def vjre():
    os.system("sudo apt-get install openjdk-7-jre")

def vjdk():
    os.system("sudo apt-get install openjdk-7-jdk")

def xjre():
    os.system("sudo apt-get install openjdk-8-jre")

def xjdk():
    os.system("sudo apt-get install openjdk-8-jdk")

def ejre():
    os.system("sudo apt-get install openjdk-11-jre")

def ejdk():
    os.system("sudo apt-get install openjdk-11-jdk")

def main():
    sm = Tkinter.Tk()
    sm.title("Select Java Verison")
    l1 = Tkinter.Label(sm,text="Select OpenJDK Java Version:")
    l1.pack()
    b1 = Tkinter.Button(sm,text="Java 6",command=sjre)
    b1.pack()
    b2 = Tkinter.Button(sm,text="Java 6 JDK",command=sjdk)
    b2.pack()
    b3 = Tkinter.Button(sm,text="Java 7",command=vjre)
    b3.pack()
    b4 = Tkinter.Button(sm,text="Java 7 JDK",command=vjdk)
    b4.pack()
    b5 = Tkinter.Button(sm,text="Java 8",command=xjre)
    b5.pack()
    b6 = Tkinter.Button(sm,text="Java 8 JDK",command=xjdk)
    b6.pack()
    b7 = Tkinter.Button(sm,text="Java 11",command=ejre)
    b7.pack()
    b8 = Tkinter.Button(sm,text="Java 11 JDK",command=ejdk)
    b8.pack()
    sm.mainloop()


main()
