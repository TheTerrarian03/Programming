from tkinter import
import tkinter.messagebox

def _area_making():
	def _help():
		tkinter.messagebox.showinfo("Help / Title", "")
	
	def check():
		var1 = var1_entry.get()
		var2_unfloated = var2_entry.get()
		var3 = var3_entry.get()
		
		def clear_all():
			var1_entry.delete(0, END)
			var2_entry.delete(0, END)
			var3_entry.delete(0, END)
			answer_entry.delete(0, END)
		
		try:
			var2 = float(var2_unfloated)
		except ValueError:
			tkinter.messagebox.showinfo("ERROR", "BAD")
			clear_all()
		
		try:
			[[[if statements]]]
		except UnboundLocalError:
			tkinter.messagebox.showinfo("ERROR", "You may try again.")
		
		def clear_text():
			answer_entry.delete(0, END)
	
	# title creating
	
	# guide labels 
    
    # Entry fields creating
    
    # check box and help creating
    
    # answer entry field creating
    
    # placing