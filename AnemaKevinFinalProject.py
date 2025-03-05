"""
Author:  Kevin Anema
Date written: 03/05/2025
Assignment:   Final Project
Short Desc:  Pretzel Ordering System
"""

import tkinter as tk  
from tkinter import messagebox  

# Function to calculate total price including pretzels, dipping sauces, and drinks
def calculate_total():
    
    total_pretzel_price = 0  # Initialize total pretzel price as 0
    for pretzel, var in pretzel_entries.items():  # Go through all pretzels and their respective input variables
        try:
            # Try to get the quantity of the pretzel ordered and convert it to an integer
            quantity = int(var.get()) if var.get() else 0
            if quantity < 0:  # Ensure the quantity is not negative
                raise ValueError("Quantity cannot be negative")
            total_pretzel_price += pretzel_prices[pretzel] * quantity  # Add the cost of pretzel to the total
        except ValueError:
            var.set("")  # If input is invalid, clear the entry field
            continue  

    # Calculate the total for dipping sauces
    total_dipping_sauces_price = 0
    for sauce, var in dipping_sauce_entries.items():  # Go through through all dipping sauces
        try:
            quantity = int(var.get()) if var.get() else 0  # Get and convert the quantity of the sauce
            if quantity < 0:  # Ensure quantity is not negative
                raise ValueError("Quantity cannot be negative")
            total_dipping_sauces_price += dipping_sauces[sauce] * quantity  # Add to the total dipping sauces price
        except ValueError:
            var.set("") 
            continue

    # Similarly calculate the total for drinks
    total_drinks_price = 0
    for drink, var in drink_entries.items():  # Go through all drink entries
        try:
            quantity = int(var.get()) if var.get() else 0  # Get and convert the quantity
            if quantity < 0:  # Ensure quantity is not negative
                raise ValueError("Quantity cannot be negative")
            total_drinks_price += drinks[drink] * quantity  # Add to the total drinks price
        except ValueError:
            var.set("")  
            continue

    total = total_pretzel_price + total_dipping_sauces_price + total_drinks_price  # Calculate the total cost of the order

    tax = total * 0.07  
    total_with_tax = total + tax  # Calculate total with tax included

    total_label.config(text=f"Total: ${total_with_tax:.2f} (Including Tax)")  # Update the label to show total with tax

    return total, tax, total_with_tax  # Return total, tax, and total with tax for use in the order summary

# Function to place the order and show a summary in a new popup window
def place_order():
    order_summary = "Your Order:\n"  # Start of the order summary text
    
    total, tax, total_with_tax = calculate_total()  # Get the total, tax, and final total from the calculate_total function

    # Add pretzel orders to the summary if any pretzels are ordered
    for pretzel, var in pretzel_entries.items():
        quantity = int(var.get()) if var.get() else 0  # Get the quantity of each pretzel
        if quantity > 0:  # If the user ordered at least one of this pretzel
            order_summary += f"{pretzel} (x{quantity}): ${pretzel_prices[pretzel] * quantity:.2f}\n"  # Add to the summary

    # Add dipping sauce orders to the summary if any sauces are ordered
    for sauce, var in dipping_sauce_entries.items():
        quantity = int(var.get()) if var.get() else 0  # Get the quantity of each dipping sauce
        if quantity > 0:  # If the user ordered at least one of this sauce
            order_summary += f"{sauce} (x{quantity}): ${dipping_sauces[sauce] * quantity:.2f}\n"  # Add to the summary

    # Add drink orders to the summary if any drinks are ordered
    for drink, var in drink_entries.items():
        quantity = int(var.get()) if var.get() else 0  # Get the quantity of each drink
        if quantity > 0:  # If the user ordered at least one of this drink
            order_summary += f"{drink} (x{quantity}): ${drinks[drink] * quantity:.2f}\n"  # Add to the summary
    
    # Add the total, tax, and final price to the summary
    order_summary += f"\nTotal (Before Tax): ${total:.2f}\n"
    order_summary += f"Tax: ${tax:.2f}\n"
    order_summary += f"Total (Including Tax): ${total_with_tax:.2f}"

    # Custom popup window to show order summary
    def close_window():
        root.quit()  # Close the main window when the Exit button is clicked

    def go_back():
        popup.destroy()  # Close the popup and return to the main window

    popup = tk.Toplevel(root)  # Create a new window (popup) for the order summary
    popup.title("Order Confirmation")  # Set the popup window title
    popup.geometry("400x300")  # Set the popup window size
    popup.config(bg="#f5f5f5")  # Set the popup background color
    
    # Create a label in the popup to display the order summary
    label = tk.Label(popup, text=order_summary, font=("Arial", 12), bg="#f5f5f5")
    label.pack(pady=20)  

    # Create an Exit button in the popup
    exit_button = tk.Button(popup, text="Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=close_window)
    exit_button.pack(pady=10)  

    # Create a Go Back button in the popup
    go_back_button = tk.Button(popup, text="Go Back", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=go_back)
    go_back_button.pack(pady=10)  

# Function to exit the program
def exit_program():

    if messagebox.askyesno("Exit", "Do you want to exit the program?"):  # Ask the user for confirmation
        root.quit()  # Exit the program if the user confirms

# Main window setup
root = tk.Tk()  # Create the main window (root)
root.title("Kevin's Pretzel Ordering System")  # Set the window title

root.geometry("500x800")  # Set the size of the window
root.minsize(400, 700)  # Set the minimum size of the window
root.config(bg="#f5f5f5")  # Set the background color of the window
font = ("Arial", 10)  # Define font for text in the window

frame = tk.Frame(root, bg="#f5f5f5")  # Create a frame to hold all the widgets
frame.pack(pady=20)  # Add padding around the frame for spacing

# Create and display the title label
title_label = tk.Label(frame, text="Kevin's Pretzel Ordering System", font=("Arial", 14, "bold"), bg="#f5f5f5")
title_label.grid(row=0, column=0, columnspan=2, pady=10)  # Display the title in the frame

# Pretzel selection section
tk.Label(frame, text="Enter Quantity for Each Pretzel:", font=font, bg="#f5f5f5").grid(row=3, column=0, sticky="w", pady=5)  # Label for pretzels
pretzel_entries = {}  # Dictionary to hold pretzel quantities
pretzel_prices = {"Classic": 2.25, "Cinnamon": 2.75, "Pepperoni": 3.25, "Almond": 2.75}  # Prices for each pretzel
pretzels = list(pretzel_prices.keys())  # List of pretzel types
for i, pretzel in enumerate(pretzels):
    tk.Label(frame, text=f"{pretzel} (${pretzel_prices[pretzel]}):", font=font, bg="#f5f5f5").grid(row=4+i, column=0, sticky="w", padx=10, pady=5)  # Label for each pretzel
    pretzel_var = tk.StringVar()  # Create a variable to hold the quantity input for each pretzel
    pretzel_entries[pretzel] = pretzel_var  # Add the variable to the dictionary
    pretzel_entry = tk.Entry(frame, textvariable=pretzel_var, font=font, width=5)  # Create an entry box for quantity
    pretzel_entry.grid(row=4+i, column=1, padx=10, pady=5)  # Place the entry box in the grid
    pretzel_var.trace("w", lambda *args: calculate_total())  # Update total whenever input changes

# Dipping sauce selection section (similar structure to pretzels)
tk.Label(frame, text="Enter Quantity for Each Dipping Sauce:", font=font, bg="#f5f5f5").grid(row=8, column=0, sticky="w", pady=5)
dipping_sauce_entries = {}  # Dictionary to hold dipping sauce quantities
dipping_sauces = {"Cheese": 0.59, "Cream Cheese": 0.59, "Glaze Dip": 0
