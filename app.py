# car_motivator.py
import tkinter as tk
from tkinter import ttk
import random
import os
from PIL import Image, ImageTk
from pystray import MenuItem as item
import pystray

class CarMotivatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Executive Car Motivator")
        self.root.geometry("400x300")
        
        # Car selection setup
        self.cars = {
            "Bentley Bentayga": "car1.png",
            "Rolls-Royce Phantom": "car2.png",
            "Ferrari SF90 Stradale": "car3.png",
            "Porsche 911 GT3": "car4.png"
        }
        
        # Landing page
        self.create_landing_page()
        self.setup_system_tray()
        
    def create_landing_page(self):
        self.clear_window()
        
        lbl = ttk.Label(self.root, text="Select Your Motivational Car", font=('Arial', 14))
        lbl.pack(pady=20)
        
        self.car_var = tk.StringVar()
        car_dropdown = ttk.Combobox(self.root, textvariable=self.car_var, values=list(self.cars.keys()))
        car_dropdown.pack(pady=10)
        
        btn = ttk.Button(self.root, text="Start Motivation", command=self.start_animation)
        btn.pack(pady=20)
        
    def start_animation(self):
        self.selected_car = self.car_var.get()
        self.root.withdraw()  # Hide main window
        self.schedule_next_animation()
        
    def schedule_next_animation(self):
        interval = random.randint(2400, 3600)  # 40-60 minutes in seconds
        self.root.after(interval * 1000, self.show_car_animation)
        
    def show_car_animation(self):
        popup = tk.Toplevel()
        popup.attributes("-topmost", True)
        popup.overrideredirect(True)
        
        # Load car image (replace with your PNG files)
        img_path = self.cars[self.selected_car]
        img = Image.open(img_path)
        photo = ImageTk.PhotoImage(img)
        
        # Set up animation
        screen_width = self.root.winfo_screenwidth()
        label = tk.Label(popup, image=photo)
        label.image = photo
        label.pack()
        
        # Animation movement
        x_position = -img.width
        def move():
            nonlocal x_position
            x_position += 5
            popup.geometry(f"+{x_position}+{self.root.winfo_screenheight()//2}")
            if x_position < screen_width:
                popup.after(10, move)
            else:
                popup.destroy()
                self.schedule_next_animation()
                
        popup.geometry(f"+{x_position}+{self.root.winfo_screenheight()//2}")
        move()
        
    def setup_system_tray(self):
        image = Image.open("icon.png")  # 16x16 pixel icon
        menu = (item('Show', self.restore_window), item('Exit', self.exit_app))
        self.tray_icon = pystray.Icon("car_motivator", image, "Car Motivator", menu)
        
    def restore_window(self):
        self.root.deiconify()
        
    def exit_app(self):
        self.tray_icon.stop()
        self.root.destroy()
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.root.withdraw)
        self.tray_icon.run_detached()
        self.root.mainloop()

if __name__ == "__main__":
    app = CarMotivatorApp()
    app.run()
