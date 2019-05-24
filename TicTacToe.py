from tkinter import *
from tkinter import messagebox
ttt = Tk()

ttt.title("I cordially invite you to the game of TIC-TAC-TOE.")
ttt.geometry("600x400")

lb1 = Label(ttt, text = "TIC-TAC-TOE", font = ('Game of Thrones', '16'))
lb1.grid(row = 0, column =0,)
lb1 = Label(ttt, text = "Player 1: X", font = ('Game of Thrones', '10'))
lb1.grid(row = 1, column =0)
lb1 = Label(ttt, text = "Player 2: O", font = ('Game of Thrones', '10'))
lb1.grid(row = 3, column =0)

turn =1;
def clicked1():
	global turn
	if btn1["text"] == " ":
		if turn ==1:
			turn = 2
			btn1["text"] = "X"
			btn1["bg"] = "cyan"
			btn1["fg"] = "red"
		elif turn ==2:
			turn =1
			btn1["text"] = "O"
			btn1["bg"] = "pink"
			btn1["fg"] = "green"
		check()

def clicked2():
	global turn
	if btn2["text"] ==" ":
		if turn ==1:
			turn = 2
			btn2["text"] = "X"
			btn2["bg"] = "cyan"
			btn2["fg"] = "red"
		elif turn ==2:
			turn =1
			btn2["text"] = "O"
			btn2["bg"] = "pink"
			btn2["fg"] = "green"
		check()
def clicked3():
	global turn
	if btn3["text"] == " ":
		if turn ==1:
			turn = 2
			btn3["text"] = "X"
			btn3["bg"] = "cyan"
			btn3["fg"] = "red"
		elif turn ==2:
			turn =1
			btn3["text"] = "O"
			btn3["bg"] = "pink"
			btn3["fg"] = "green"
		check()
def clicked4():
	global turn
	if btn4["text"] == " ":
		if turn ==1:
			turn = 2
			btn4["text"] = "X"
			btn4["bg"] = "cyan"
			btn4["fg"] = "red"
		elif turn ==2:
			turn =1
			btn4["text"] = "O"
			btn4["bg"] = "pink"
			btn4["fg"] = "green"
		check()
def clicked5():
	global turn
	if btn5["text"] == " ":
		if turn ==1:
			turn = 2
			btn5["text"] = "X"
			btn5["bg"] = "cyan"
			btn5["fg"] = "red"
		elif turn ==2:
			turn =1
			btn5["text"] = "O"
			btn5["bg"] = "pink"
			btn5["fg"] = "green"
		check()
def clicked6():
	global turn
	if btn6["text"] == " ":
		if turn ==1:
			turn = 2
			btn6["text"] = "X"
			btn6["bg"] = "cyan"
			btn6["fg"] = "red"
		elif turn ==2:
			turn =1
			btn6["text"] = "O"
			btn6["bg"] = "pink"
			btn6["fg"] = "green"
		check()
def clicked7():
	global turn
	if btn7["text"] == " ":
		if turn ==1:
			turn = 2
			btn7["text"] = "X"
			btn7["bg"] = "cyan"
			btn7["fg"] = "red"
		elif turn ==2:
			turn =1
			btn7["text"] = "O"
			btn7["bg"] = "pink"
			btn7["fg"] = "green"
		check()
def clicked8():
	global turn
	if btn8["text"] == " ":
		if turn ==1:
			turn = 2
			btn8["text"] = "X"
			btn8["bg"] = "cyan"
			btn8["fg"] = "red"
		elif turn ==2:
			turn =1
			btn8["text"] = "O"
			btn8["bg"] = "pink"
			btn8["fg"] = "green"
		check()
def clicked9():
	global turn
	if btn9["text"] == " ":
		if turn ==1:
			turn = 2
			btn9["text"] = "X"
			btn9["bg"] = "cyan"
			btn9["fg"] = "red"
		elif turn ==2:
			turn =1
			btn9["text"] = "O"
			btn9["bg"] = "pink"
			btn9["fg"] = "green"
		check()
flag = 1

def check():
	global flag
	b1 = btn1["text"]
	b2 = btn2["text"]
	b3 = btn3["text"]
	b4 = btn4["text"]
	b5 = btn5["text"]
	b6 = btn6["text"]
	b7 = btn7["text"]
	b8 = btn8["text"]
	b9 = btn9["text"]
	
	won = 0

	if ((b1 == b2 and b1 == b3 and b1 == "O") or (b1 == b2 and b1 == b3 and b1 == "X")):
		won = win(btn1["text"])
	if ((b4 == b5 and b4 == b6 and b4 == "O") or (b4 == b5 and b4 == b6 and b4 == "X")):
		won = win(btn4["text"])
	if ((b7 == b8 and b7 == b9 and b7 == "O") or (b7 == b8 and b7 == b9 and b7 == "X")):
		won = win(btn7["text"])
	if ((b1 == b4 and b1 == b7 and b1 == "O") or (b1 == b4 and b1 == b7 and b1 == "X")):
		won = win(btn1["text"])
	if ((b2 == b5 and b2 == b8 and b2 == "O") or (b2 == b5 and b2 == b8 and b2 == "X")):
		won = win(btn2["text"])
	if ((b3 == b6 and b3 == b9 and b3 == "O") or (b3 == b6 and b3 == b9 and b3 == "X")):
		won = win(btn3["text"])
	if ((b1 == b5 and b1 == b9 and b1 == "O") or (b1 == b5 and b1 == b9 and b1 == "X")):
		won = win(btn1["text"])
	if ((b7 == b5 and b7 == b3 and b7 == "O") or (b7 == b5 and b7 == b3 and b7 == "X")):
		won = win(btn7["text"])

	flag += 1
	print(flag)
	print(won)

	if flag == 10 and won == 0:
		messagebox.showinfo("TIE!", "Try Again :)")
		ttt.destroy()

def win(player):
	ans = player + " wins!"
	messagebox.showinfo("Congratulations! ", ans)
	ttt.destroy()
	return 1

btn1 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked1)
btn1.grid(column = 1, row  = 1)
btn2 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked2)
btn2.grid(column = 2, row  = 1)
btn3 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked3)
btn3.grid(column = 3, row  = 1)
btn4 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked4)
btn4.grid(column = 1, row  = 2)
btn5 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked5)
btn5.grid(column = 2, row  = 2)
btn6 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked6)
btn6.grid(column = 3, row  = 2)
btn7 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked7)
btn7.grid(column = 1, row  = 3)
btn8 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked8)
btn8.grid(column = 2, row  = 3)
btn9 = Button(ttt, text = " ", bg = "gray", fg = "white", width = 5, height = 3, font = ('Game of Thrones', '20'), command = clicked9)
btn9.grid(column = 3, row  = 3)

ttt.mainloop()

lavendertown = input()
