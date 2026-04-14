import tkinter as tk
from tkinter import simpledialog
from github_utils import push_to_github, pull_from_github

data = pull_from_github()

def save_data():
    push_to_github(data)

def add_player():
    name = simpledialog.askstring("Add Player", "Player Name:")
    role = simpledialog.askstring("Role", "Ground / Branch Walls:")
    if name and role:
        data["players"].append({"name": name, "points": 0, "role": role})
        save_data()
        refresh_list()

def adjust_points(player, delta):
    player["points"] += delta
    save_data()
    refresh_list()

def refresh_list():
    for widget in list_frame.winfo_children():
        widget.destroy()
    for player in data["players"]:
        frame = tk.Frame(list_frame, pady=2)
        color = "green" if player["role"].lower() == "ground" else "brown"
        tk.Label(frame, text=f"{player['name']} ({player['role']}) - {player['points']}", fg=color).pack(side="left")
        tk.Button(frame, text="+", command=lambda p=player: adjust_points(p, 1)).pack(side="left")
        tk.Button(frame, text="-", command=lambda p=player: adjust_points(p, -1)).pack(side="left")
        frame.pack()

root = tk.Tk()
root.title("GitHub Tier List")
tk.Button(root, text="Add Player", command=add_player).pack()
list_frame = tk.Frame(root)
list_frame.pack()
refresh_list()
root.mainloop()
