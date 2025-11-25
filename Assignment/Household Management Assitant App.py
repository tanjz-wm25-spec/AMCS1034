import tkinter as tk
from tkinter import messagebox

def open_grocery_page():
    grocery_page.pack()
    main_menu.pack_forget()

def open_chore_page():
    chore_page.pack()
    main_menu.pack_forget()

def open_budget_page():
    budget_page.pack()
    main_menu.pack_forget()

def open_meal_page():
    meal_page.pack()
    main_menu.pack_forget()
    
def back_to_menu():
    grocery_page.pack_forget()
    chore_page.pack_forget()
    budget_page.pack_forget()
    meal_page.pack_forget()

    main_menu.pack()
    
# main window
window = tk.Tk()
window.title("Household Management Assistant App")
window.geometry("400x300")  # width x height

#page
main_menu = tk.Frame(window)
grocery_page = tk.Frame(window)
chore_page = tk.Frame(window)
budget_page = tk.Frame(window)
meal_page = tk.Frame(window)

# main menu
btn_grocery = tk.Button(main_menu, text="Grocery List Manager", font=("Helvetica", 8, "bold"), command=open_grocery_page,width=20, height=2, padx=10)
btn_grocery.pack(pady=(40,8))

btn_chore = tk.Button(main_menu, text="Chore Scheduler", font=("Helvetica", 8, "bold"), command=open_chore_page,width=20, height=2, padx=10)
btn_chore.pack(pady=8)

btn_budget = tk.Button(main_menu, text="Budget Tracker", font=("Helvetica", 8, "bold"), command=open_budget_page,width=20, height=2, padx=10)
btn_budget.pack(pady=8)

btn_meal = tk.Button(main_menu, text="Meal Planner", font=("Helvetica", 8, "bold"), command=open_meal_page,width=20, height=2, padx=10)
btn_meal.pack(pady=8)

main_menu.pack()  # show main menu

# ---- Grocery Page ----
grocery_page = tk.Frame(window)
tk.Label(grocery_page, text="Welcome to Grocery Page!").pack(pady=20)
btn_back = tk.Button(grocery_page, text="Back", command=back_to_menu)
btn_back.pack(side="bottom", pady=10)

# ---- Chore Page ----
chore_page = tk.Frame(window)
tk.Label(chore_page, text="Welcome to Chore Scheduler!").pack(pady=20)
btn_back = tk.Button(chore_page, text="Back", command=back_to_menu)
btn_back.pack(side="bottom", pady=10)

# ---- Budget Page ----
budget_page = tk.Frame(window)
tk.Label(budget_page, text="Welcome to Budget Tracker!").pack(pady=20)
btn_back = tk.Button(budget_page, text="Back", command=back_to_menu)
btn_back.pack(side="bottom", pady=10)

# ---- Meal Planner Page ----
meal_page = tk.Frame(window)
tk.Label(meal_page, text="Welcome to Meal Planner!").pack(pady=20)
btn_back = tk.Button(meal_page, text="Back", command=back_to_menu)
btn_back.pack(side="bottom", pady=10)

window.mainloop()   # start