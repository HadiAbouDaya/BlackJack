from random import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import pandas
import folium
import webbrowser

mainWindow=None

def tri(tab):
   for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
       tab[i],tab[min]=tab[min],tab[i]
   return tab

def login():
    if mainWindow:
       mainWindow.deiconify()
    flag=True
    u=open('Accounts.txt','r')
    l=u.readlines()
    u.close()
    usrs=[]
    for elt in l:
        if len(elt)>4:
            j=elt.rstrip('\n').split(',')
            k=(j[0],j[1],j[4])
            usrs.append(k)
    for elt in usrs:
        if use.get()==elt[0] and pas.get()==elt[1] and float(elt[2])!=0.0:
            flag=False
    if flag==False:
        f.destroy()
    else:
        messagebox.showwarning('Attention!','Username or Password is incorrect!')

def saveaccount():
    if mainWindow:
       mainWindow.deiconify()
    data = pandas.read_csv("Accounts.txt")
    userna = list(data["Username"])
    a=user.get()
    b=pasw.get()
    c=lat.get()
    d=lon.get()
    txt=a+','+b+','+str(c)+','+str(d)+',100'
    if a in userna:
        messagebox.showwarning('Attention!','Username already existing!')
    else:
        with open('Accounts.txt',"a") as h:
            h.write('\n')
            h.write(txt)
            h.close()
        f.destroy()

def openboard():
   d={}
   u=open('Accounts.txt','r')
   l=u.readlines()
   u.close()
   usrs=[]
   l.pop(0)
   r=1
   for elt in l:
       if len(elt)>4:
           j=elt.rstrip('\n').split(',')
           d[j[0]]=float(j[4])
   coins=list(set(d.values()))
   coins=tri(coins)
   coins.reverse()
   nf=Toplevel(f)
   nf.title('Leaderborad Table')
   la1=ttk.Label(nf,text="Username")
   la1.grid(column=1,row=1)
   la2=ttk.Label(nf,text="Coins in pocket")
   la2.grid(column=3,row=1)
   for i in coins:
      l=list(d.keys())
      for elt in l:
         if d[elt]==i:
            l.remove(elt)
            ttk.Label(nf,textvariable=str(r)).grid(column=0,row=r+2)
            ttk.Label(nf,text=elt).grid(column=1,row=r+2)
            ttk.Label(nf,text=i).grid(column=3,row=r+2)
            r+=1
   for child in nf.winfo_children(): child.grid_configure(padx=5, pady=5)
     
def openmap():
    data = pandas.read_csv("Accounts.txt")
    usern = list(data["Username"])
    coins = list(data["coins"])
    lat= list(data["lat"])
    lon = list(data["lon"])
    map = folium.Map(location=[33.8547, 35.8623], zoom_start=8, tiles="Stamen Terrain")
    fg = folium.FeatureGroup(name="users")
    for a, b, c, d in zip(usern, coins,lat, lon):
        fg.add_child(folium.CircleMarker(location=[c,d],radius = 6,popup=(a+'\n'+str(b)+' coins'), fill=True,  color = 'red', fill_opacity=0.7))
    map.add_child(fg)
    map.save("Mapleaderboard.html")
    webbrowser.open("Mapleaderboard.html")

def openabout():
    global f
    fff=Toplevel(f)
    fff.title('About')
    lab1=ttk.Label(fff, text='This app was successfully built by :',font=("Times New Roman",15))
    lab1.grid()
    lab2=ttk.Label(fff, text='ABOU DAYA Hadi\nGEDEON Christian',font=("Times New Roman",15))
    lab2.grid()
    lab3=ttk.Label(fff, text='Contact us at :',font=("Times New Roman",15))
    lab3.grid()
    lab4=ttk.Label(fff, text='gedeon_c_01@live.com',font=("Times New Roman",15))
    lab4.grid()
    lab5=ttk.Label(fff, text='or',font=("Times New Roman",15))
    lab5.grid()
    lab6=ttk.Label(fff, text='hadiaboudaya1@gmail.com',font=("Times New Roman",15))
    lab6.grid()
    lab7=ttk.Label(fff, text='ALL RIGHTS RESERVED.')
    lab7.grid(pady=20)
    for child in fff.winfo_children(): child.grid_configure(padx=5, pady=5)
    

def openhow():
    global f
    ffff=Toplevel(f)
    ffff.title('How to play?')
    lab1=ttk.Label(ffff, text='THE PACK:',font=("Times New Roman",15))
    lab1.grid(row=0,sticky=(W))
    lab2=ttk.Label(ffff, text='The standard 52-card pack is used, but this an eight-deck game.')
    lab2.grid(row=1,sticky=(W))
    lab3=ttk.Label(ffff, text='Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.')
    lab3.grid(row=3,sticky=(W))
    lab4=ttk.Label(ffff, text='OBJECT OF THE GAME:',font=("Times New Roman",15))
    lab4.grid(row=2,sticky=(W))
    lab5=ttk.Label(ffff, text='CARD VALUES/SCORING:',font=("Times New Roman",15))
    lab5.grid(row=4,sticky=(W))
    lab6=ttk.Label(ffff, text='It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.')
    lab6.grid(row=5,sticky=(W))
    lab7=ttk.Label(ffff, text='BETTING:',font=("Times New Roman",15))
    lab7.grid(row=6,sticky=(W))
    lab8=ttk.Label(ffff, text='Before the deal begins,the player places a bet in chips, double or nothing.')
    lab8.grid(row=7,sticky=(W))
    lab9=ttk.Label(ffff, text='The player to the left goes first and must decide whether to "stand" (not ask for another card) or "hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly).\nThus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under),\nor goes "bust" (if it is over 21). In the latter case, the player loses and the dealer collects the bet wagered.')
    lab9.grid(row=9,sticky=(W))
    lab10=ttk.Label(ffff, text='The combination of an ace with a card other than a ten-card is known as a "soft hand," because the player can count the ace as a 1 or 11,\nand either draw cards or not. For example with a "soft 17" (an ace and a 6), the total is 7 or 17.')
    lab10.grid(row=10,sticky=(W))
    lab11=ttk.Label(ffff, text='THE PLAY:',font=("Times New Roman",15))
    lab11.grid(row=8,sticky=(W))
    lab12=ttk.Label(ffff, text='While a count of 17 is a good hand, the player may wish to draw for a higher total. If the draw creates a bust hand by counting the ace as an 11,\nthe player simply counts the ace as a 1 and continues playing by standing or "hitting" (asking the dealer for additional cards, one at a time).')
    lab12.grid(row=11,sticky=(W))
    lab13=ttk.Label(ffff, text="THE DEALER'S PLAY:",font=("Times New Roman",15))
    lab13.grid(row=12,sticky=(W))
    lab14=ttk.Label(ffff, text='When the dealer has served the player, the dealers face-down card is turned up.\nIf the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.')
    lab14.grid(row=13,sticky=(W))
    lab15=ttk.Label(ffff, text=" If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand.\nThe dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.")
    lab15.grid(row=14,sticky=(W))


    for child in ffff.winfo_children(): child.grid_configure(padx=5, pady=5)

class Chips:
    def __init__(self):
        self.total=100
        self.bet=0

    def winbet(self):
        self.total+=self.bet

    def losebet(self):
        self.total-=self.bet
        if self.total==0:
            messagebox.showwarning('You lost!',"You don't have any chips left, your account has been deleted. Please Sign up over again!")
            Main_window()

def load_images(card_images):
    suits=['heart','club','diamond','spade']
    facecards=['jack','queen','king']
    for suit in suits:
        for card in range(1,11):
            name='cards/{}_{}.png'.format(str(card),suit)
            image=PhotoImage(file=name)
            card_images.append((card,image,))
        for card in facecards:
            name='cards/{}_{}.png'.format(card,suit)
            image=PhotoImage(file=name)
            card_images.append((10,image,))
            
def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card

def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

def deal_dealer():
    global username
    f=True
    p.bet=int(Chipsbet.get())
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        p.losebet()
        f=False
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set(username+" Wins!")
        p.winbet()
        f=False
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
        p.losebet()
        f=False
    else:
        result_text.set("Draw!")
        f=False
    if f==False:
        player_button.state(['disabled'])
        dealer_button.state(['disabled'])

def deal_player():
    
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        p.losebet()
        player_button.state(['disabled'])
        dealer_button.state(['disabled'])

def betting():
    global yourbet
    p.bet=int(Chipsbet.get())
    yourbet.set("Your bet is {} chips".format(p.bet))
    player_button.state(['!disabled'])
    dealer_button.state(['!disabled'])
    bet_but.state(['disabled'])

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global pagestyle
    global numb
    global comb
    global player_button
    global dealer_button
    global Chipsbet
    global yourbet

    numb['text']="You have {} chips".format(int(p.total))
    comb['values']=list(range(int(p.total),0,-1))
    
    dealer_card_frame.destroy()
    dealer_card_frame = ttk.Frame(card_frame, style='G.TFrame')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    
    player_card_frame = ttk.Frame(card_frame, style='G.TFrame')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")
    yourbet.set('')

    
    dealer_hand = []
    player_hand = []
    
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    Chipsbet.set(0)
    player_button.state(['disabled'])
    dealer_button.state(['disabled'])
    bet_but.state(['!disabled'])

def Shuffle():
    shuffle(deck)

def Main_window():
   global use
   global user
   global pas
   global pasw
   global f
   global lat
   global lon
   f=Tk()
   f.title("BLACKJACK")
   f.grid()
   fr1=ttk.LabelFrame(f,text='New to the app? Sign Up Here!')
   fr1.grid(row=2,column=0,padx=10,pady=10)
   fr=ttk.Frame(f)
   fr.grid(row=1,column=0,padx=10,pady=10)
                  
   l1=ttk.Label(fr,text='Sign in and start the journey!',foreground='green',font=("Times New Roman",20))
   l1.grid(row=0,column=0,columnspan=3)
   l2=ttk.Label(fr,text='Username :')
   l2.grid(row=1,column=0,columnspan=2)
   l3=ttk.Label(fr,text='Password :')
   l3.grid(row=2,column=0,columnspan=2)

   use=StringVar()
   use.set('')
   pas=StringVar()
   user=StringVar()
   user.set('')
   pasw=StringVar()
   lat=DoubleVar()
   lon=DoubleVar()
   e1=ttk.Entry(fr,textvariable=use)
   e1.grid(row=1,column=2)
   e2=ttk.Entry(fr,textvariable=pas,show='*')
   e2.grid(row=2,column=2)

   b1=ttk.Button(fr,text='Sign In',command=login)
   b1.grid(row=3,column=2)

   l5=ttk.Label(fr1,text='Welcome to BLACKJACK!',foreground='green')
   l6=ttk.Label(fr1,text='Username :')
   l7=ttk.Label(fr1,text='Password :')
   l8=ttk.Label(fr1,text='Latitude :')
   l9=ttk.Label(fr1,text='Longitude :')
   e3=ttk.Entry(fr1,textvariable=user)
   e4=ttk.Entry(fr1,textvariable=pasw)
   e5=ttk.Entry(fr1,textvariable=lat)
   e6=ttk.Entry(fr1,textvariable=lon)
   b3=ttk.Button(fr1,text='Sign Up',command=saveaccount)
   l5.grid(row=5,column=0,columnspan=3)
   l6.grid(row=6,column=0,columnspan=2)
   l7.grid(row=7,column=0,columnspan=2)
   l8.grid(row=8,column=0,columnspan=2)
   l9.grid(row=9,column=0,columnspan=2)
   e3.grid(row=6,column=2)
   e4.grid(row=7,column=2)
   e5.grid(row=8,column=2)
   e6.grid(row=9,column=2)
   b3.grid(row=10,column=1,columnspan=2)

   menubar=Menu(f)
   f['menu']=menubar
   mlead=Menu(menubar)
   mhelp=Menu(menubar)
   menubar.add_cascade(menu=mlead,label='Leaderboard')
   menubar.add_cascade(menu=mhelp,label='Help')
   mlead.add_command(label="Table",command=openboard)
   mlead.add_command(label='Map',command=openmap)
   mhelp.add_command(label="About",command=openabout)
   mhelp.add_command(label='How to play?',command=openhow)

   for child in fr1.winfo_children(): child.grid_configure(padx=10, pady=10)
   for child in fr.winfo_children(): child.grid_configure(padx=10, pady=10)
   f.mainloop()

Main_window()

p=Chips()

u=open('Accounts.txt','r')
r=u.readlines()
u.close()
users=[]
for elt in r:
    if len(elt)>4:
        j=elt.rstrip(',\n').split(',')
        k=(j[0],j[4])
        users.append(k)

if use.get()=='':
    username=user.get()
else:
    username=use.get()

if username=='':
   sys.exit()

for elt in users:
    if elt[0]==username:
        p.total=float(elt[1])
        break


mainWindow = Tk()

mainWindow.title("BlackJack")
mainWindow.minsize(615,595)
mainWindow.configure(background='green')

pagestyle = ttk.Style()
pagestyle.configure('G.TFrame' , background='green')

FRAME=ttk.Frame(mainWindow,relief='sunken', borderwidth=1,style='G.TFrame')
FRAME.grid()
FRAME.place(relx=0.5, rely=0.5, anchor=CENTER)

Chipsbet=IntVar()
frame1=ttk.Frame(FRAME, borderwidth=2,style='G.TFrame')
frame1.grid(row=0,columnspan=3)
im=PhotoImage(file="cards/play.png")
Label(frame1, image=im, background="green").grid(row=0, column=0)
ttk.Label(frame1, text="BLACK JACK", background="dark green", foreground='light green', font = ("Times New Roman",30)).grid(row=0, column=1)
numb=ttk.Label(frame1, text="You have {} chips".format(p.total), background="green", foreground='white', font = ('Arial',16))
numb.grid(row=1, column=0)
ttk.Label(frame1, text="How many chips do you like to bet?", background="green", foreground='white', font = ('Arial',16)).grid(row=2, column=0)
comb=ttk.Combobox(frame1, textvariable=Chipsbet,state='readonly')
comb.grid(row=2, column=1)
yourbet=StringVar()
bet_lab=ttk.Label(frame1, textvariable=yourbet, background="green", foreground='white', font = ('Arial',16))
bet_lab.grid(row=3,column=0)
bet_but=ttk.Button(frame1, text="Take Bet", command=betting)
bet_but.grid(row=3, column=1)
result_text = StringVar()
result = ttk.Label(frame1, textvariable=result_text, background="green", foreground="white", font=("Times New Roman",20))
result.grid(row=4, column=0, columnspan=2)

card_frame = ttk.Frame(FRAME, borderwidth=1,style='G.TFrame')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = IntVar()
ttk.Label(card_frame, text="Dealer", background="green", foreground='white', font = ('Arial',13)).grid(row=0, column=0,padx=10)
ttk.Label(card_frame, textvariable=dealer_score_label, background="green", foreground="white", font = ('Arial',13)).grid(row=1, column=0,padx=10)

dealer_card_frame = ttk.Frame(card_frame, style='G.TFrame')
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = IntVar()

ttk.Label(card_frame, text="Player", background="green", foreground="white", font = ('Arial',13)).grid(row=2, column=0,padx=10)
ttk.Label(card_frame, textvariable=player_score_label, background="green", foreground="white", font = ('Arial',13)).grid(row=3, column=0,padx=10)

player_card_frame = ttk.Frame(card_frame, style='G.TFrame')
player_card_frame.grid(row=2, column=1, rowspan=2)

button_frame = ttk.Frame(FRAME,style='G.TFrame')
button_frame.grid(row=3,columnspan=3)

dealer_button = ttk.Button(button_frame, text="Stand", command=deal_dealer)
dealer_button.grid(row=0, column=0,padx=10)

player_button = ttk.Button(button_frame, text="Hand", command=deal_player)
player_button.grid(row=0, column=1,padx=15,pady=24)

new_game_button = ttk.Button(button_frame, text="New Hand", command=new_game)
new_game_button.grid(row=0, column=2,padx=15)

quit_button = ttk.Button(button_frame, text="QUIT", command=mainWindow.destroy)
quit_button.grid(row=0,column=3,padx=10)
for child in frame1.winfo_children(): child.grid_configure(padx=5, pady=5)


cards = []
load_images(cards)

deck = list(cards)*8
Shuffle()

dealer_hand = []
player_hand = []
new_game()
mainWindow.mainloop()

w=[]
for elt in r:
    if len(elt)>4:
        j=elt.rstrip('\n').split(',')
        if j[0]==username:
            j[4]=str(p.total)
        k=','.join(j)
        k+='\n'
        w.append(k)

u=open('Accounts.txt','w')
u.writelines(w)
u.close()
