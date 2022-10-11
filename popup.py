#ismaeel bashir

#imports files
import tkinter as tk
from tkinter import messagebox

#pop up class

#creates class for window
class Win():

    #defines function for creating pop up
    def popup(self):

        #hides main window
        tk.Tk().withdraw()

        #creates pop up
        name = messagebox.showinfo(title="life source deleted", message="brian is now not invincible")

    #defines function to show pop up
    def showpopup(self, lifesource):

        #checks if player has deleted file
        if lifesource == False:

            #calls pop up function
            self.popup()


