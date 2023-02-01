import tkinter as tk
from tkinter import messagebox

# Made by David Pokorák

counter = 0
cps = 0
cpc = 1
upgrade_cost = 10
cpc_upgrade_cost = 20
notfullcookie = 0
clickedd = 0
achieve_count = 10
# Incrementation of cookie count


def clicked():
    global counter, cpc, clickedd, achieve_count
    counter += cpc
    clickedd += 1
    ct['text'] = f'{counter}'
    if clickedd >= achieve_count:
        messagebox.showinfo("Achivement unlocked!!",
                            "Congratulations you have clicked" + str(achieve_count) + "times!")
        achieve_count *= 10


# Incrementation of cookie per click

def cpcup():
    global counter, cpc, cpc_upgrade_cost
    if(counter >= cpc_upgrade_cost):
        counter -= cpc_upgrade_cost
        cpc_upgrade_cost *= 3
        cpc_upgrade_cost = round(cpc_upgrade_cost)
        cpc += 1
        cpc_count['text'] = f'{cpc}'
        cpc_cost_counter['text'] = f'{cpc_upgrade_cost}'
        ct['text'] = f'{counter}'

# Incrementation of cookies per second count


def lvlup():
    global counter, cps, upgrade_cost
    if(counter >= upgrade_cost):
        counter -= upgrade_cost
        upgrade_cost *= 1.5
        upgrade_cost = round(upgrade_cost)
        cps += 0.10
        cps = round(cps, 2)
        cps_count['text'] = f'{cps}'
        Up_cost_counter['text'] = f'{upgrade_cost}'
        ct['text'] = f'{counter}'

# passive income


def my_mainloop():
    global counter, cps, notfullcookie
    notfullcookie += cps
    if notfullcookie >= 1:
        counter += 1
        notfullcookie -= 1
        ct['text'] = f'{counter}'
    sdf.after(1000, my_mainloop)


# Window parameters
sdf = tk.Tk()
sdf.title("Cookie Clicker!")
sdf.geometry("512x512")

# Cokie counter
ct_label = tk.Label(sdf, text="Cookie count", font=("Arial", 18))
ct_label.pack()

ct = tk.Label(sdf, text="Zero", font=("Arial", 18))
ct.pack()

# "Click me!" button
click = tk.Button(sdf, text="Click me!", command=clicked, font=("Arial", 18))
click.pack()

# Cokie per click show
cpc_label = tk.Label(sdf, text="Cookies per click", font=("Arial", 18))
cpc_label.pack()

cpc_count = tk.Label(sdf, text="1", font=("Arial", 18))
cpc_count.pack()

# Cookies per second -- pasivní přijem
cps_label = tk.Label(sdf, text="Cookies per second", font=("Arial", 18))
cps_label.pack()

cps_count = tk.Label(sdf, text="0.0", font=("Arial", 18))
cps_count.pack()

# Upgrade cost - Show
Up_cost_label = tk.Label(
    sdf, text="Cookies per second Upgrade cost", font=("Arial", 18))
Up_cost_label.pack()

Up_cost_counter = tk.Label(sdf, text=upgrade_cost, font=("Arial", 18))
Up_cost_counter.pack()


# Cokie per click upgrade cost
cpc_cost_label = tk.Label(
    sdf, text="Cookies per click Upgrade cost", font=("Arial", 18))
cpc_cost_label.pack()

cpc_cost_counter = tk.Label(sdf, text=cpc_upgrade_cost, font=("Arial", 18))
cpc_cost_counter.pack()


# Upgrades
# CPS
upg = tk.Button(sdf, text="Upgrade CPS!", command=lvlup, font=("Arial", 18))
upg.pack()

# CPC
cpc_upg = tk.Button(sdf, text="Upgrade CPC!",
                    command=cpcup, font=("Arial", 18))
cpc_upg.pack()

sdf.after(1000, my_mainloop)

sdf.mainloop()
