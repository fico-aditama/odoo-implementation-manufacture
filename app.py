import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import math
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime
import threading

class AdvancedManufacturingSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Manufacturing Industry Simulator")
        self.master.geometry("1200x800")
        
        # Initialize variables
        self.production_running = False
        self.quality_data = []
        self.production_data = []
        self.efficiency_data = []
        self.current_temperature = 25.0
        self.current_pressure = 1.0
        self.current_humidity = 50.0
        
        self.create_notebook()
        self.create_menu()
        self.init_animation_canvas()

        self.root = root
        self.root.title("Advanced Manufacturing Simulator")
        
        # Initialize data
        self.is_running = False
        self.production_data = []
        self.efficiency_data = []
        
        # Create notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")
        
        # Create tabs
        self.create_production_tab()
        self.create_analytics_tab()
        self.create_hr_tab()

    def create_production_tab(self):
        production_frame = ttk.Frame(self.notebook)
        self.notebook.add(production_frame, text="Production Line")
        
        # Control panel
        control_frame = ttk.LabelFrame(production_frame, text="Control Panel")
        control_frame.pack(side="top", padx=5, pady=5, fill="x")
        
        self.start_button = ttk.Button(control_frame, text="Start", command=self.toggle_production)
        self.start_button.pack(side="left", padx=5)
        
        # Production line visualization
        line_frame = ttk.LabelFrame(production_frame, text="Production Line")
        line_frame.pack(padx=5, pady=5, fill="both", expand=True)
        
        # Create Tkinter Canvas for production line animation
        self.line_canvas = tk.Canvas(line_frame, height=100, bg='white')
        self.line_canvas.pack(fill="both", expand=True)
        
        # Create production line elements
        self.create_production_elements()

    def create_production_elements(self):
        # Create conveyor belt
        self.line_canvas.create_rectangle(50, 40, 550, 60, fill='gray')
        
        # Create initial product
        self.product = self.line_canvas.create_rectangle(50, 30, 70, 70, fill='blue')
        
        # Create stations
        station_positions = [150, 300, 450]
        for x in station_positions:
            self.line_canvas.create_rectangle(x-10, 20, x+10, 80, fill='red')

    def toggle_production(self):
        self.is_running = not self.is_running
        self.start_button.config(text="Stop" if self.is_running else "Start")
        if self.is_running:
            self.start_animation()

    def start_animation(self):
        if self.is_running:
            self.update_production_line()
            # Update production data
            self.production_data.append(random.randint(80, 120))
            self.efficiency_data.append(random.randint(70, 100))
            if len(self.production_data) > 50:
                self.production_data.pop(0)
                self.efficiency_data.pop(0)
            self.plot_analytics()
            self.root.after(100, self.start_animation)

    def update_production_line(self):
        # Get current position
        pos = self.line_canvas.coords(self.product)
        
        # Check if product reached the end
        if pos[2] > 550:
            self.line_canvas.coords(self.product, 50, 30, 70, 70)
        else:
            # Move product
            self.line_canvas.move(self.product, 2, 0)


    def create_maintenance_tab(self):
        maintenance_frame = ttk.Frame(self.notebook)
        self.notebook.add(maintenance_frame, text="Maintenance")

        # Maintenance Schedule
        schedule_frame = ttk.LabelFrame(maintenance_frame, text="Maintenance Schedule")
        schedule_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        self.maintenance_tree = ttk.Treeview(schedule_frame, columns=("Equipment", "Last Maintenance", "Next Maintenance"), show="headings")
        self.maintenance_tree.heading("Equipment", text="Equipment")
        self.maintenance_tree.heading("Last Maintenance", text="Last Maintenance")
        self.maintenance_tree.heading("Next Maintenance", text="Next Maintenance")
        self.maintenance_tree.pack(fill="both", expand=True)

        # Sample data
        sample_data = [
            ("Machine A", "2023-05-01", "2023-06-01"),
            ("Machine B", "2023-05-15", "2023-06-15"),
            ("Machine C", "2023-05-10", "2023-06-10")
        ]
        for item in sample_data:
            self.maintenance_tree.insert("", "end", values=item)

        # Maintenance Status
        status_frame = ttk.LabelFrame(maintenance_frame, text="Maintenance Status")
        status_frame.pack(side="right", padx=5, pady=5, fill="both", expand=True)

        self.maintenance_figure = Figure(figsize=(5, 4))
        self.maintenance_canvas = FigureCanvasTkAgg(self.maintenance_figure, master=status_frame)
        self.maintenance_canvas.get_tk_widget().pack(fill="both", expand=True)

        self.plot_maintenance_status()

    def plot_maintenance_status(self):
        labels = 'Up-to-date', 'Due Soon', 'Overdue'
        sizes = [60, 30, 10]
        colors = ['#66b3ff', '#ff9999', '#ff0000']

        ax = self.maintenance_figure.add_subplot(111)
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        self.maintenance_canvas.draw()

    def plot_hr_analytics(self):
        # Clear figure sebelumnya
        self.hr_figure.clear()

        # Buat subplot grid 2x2
        gs = self.hr_figure.add_gridspec(2, 2)

        # 1. Department Distribution (Pie Chart)
        ax1 = self.hr_figure.add_subplot(gs[0, 0])
        departments = ['Production', 'Quality', 'Maintenance', 'HR', 'R&D']
        dept_counts = [45, 15, 20, 10, 25]
        ax1.pie(dept_counts, labels=departments, autopct='%1.1f%%')
        ax1.set_title('Department Distribution')

        # 2. Employee Status (Bar Chart)
        ax2 = self.hr_figure.add_subplot(gs[0, 1])
        status = ['Active', 'On Leave', 'Training']
        status_counts = [90, 5, 15]
        ax2.bar(status, status_counts)
        ax2.set_title('Employee Status')
        ax2.tick_params(axis='x', rotation=45)

        # 3. Experience Distribution (Histogram)
        ax3 = self.hr_figure.add_subplot(gs[1, 0])
        experience = np.random.normal(5, 2, 100)  # Sample data
        ax3.hist(experience, bins=10)
        ax3.set_title('Years of Experience')
        ax3.set_xlabel('Years')
        ax3.set_ylabel('Count')

        # 4. Training Completion (Line Chart)
        ax4 = self.hr_figure.add_subplot(gs[1, 1])
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        completion = [75, 80, 85, 82, 88]
        ax4.plot(months, completion, marker='o')
        ax4.set_title('Training Completion Rate')
        ax4.set_ylabel('Completion %')
        ax4.tick_params(axis='x', rotation=45)

        # Adjust layout
        self.hr_figure.tight_layout()
        
        # Draw canvas
        self.hr_canvas.draw()

    def create_hr_tab(self):
        hr_frame = ttk.Frame(self.notebook)
        self.notebook.add(hr_frame, text="Human Resources")

        # Buat layout dengan dua kolom
        left_frame = ttk.Frame(hr_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        right_frame = ttk.Frame(hr_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        # Employee Information di kolom kiri
        info_frame = ttk.LabelFrame(left_frame, text="Employee Information")
        info_frame.pack(fill="both", expand=True)

        # Treeview untuk data karyawan
        columns = ("ID", "Name", "Position", "Department", "Status")
        self.employee_tree = ttk.Treeview(info_frame, columns=columns, show="headings")
        
        # Atur heading dan kolom
        for col in columns:
            self.employee_tree.heading(col, text=col)
            self.employee_tree.column(col, width=100)
        
        # Tambah scrollbar
        scrollbar = ttk.Scrollbar(info_frame, orient="vertical", command=self.employee_tree.yview)
        self.employee_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview dan scrollbar
        self.employee_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Tambah sample data
        sample_data = [
            ("001", "John Doe", "Engineer", "Production", "Active"),
            ("002", "Jane Smith", "Manager", "Quality", "Active"),
            ("003", "Bob Johnson", "Technician", "Maintenance", "Active"),
            ("004", "Alice Brown", "Supervisor", "Production", "Active"),
            ("005", "Charlie Wilson", "Analyst", "Quality", "Active"),
        ]
        for item in sample_data:
            self.employee_tree.insert("", "end", values=item)

        # HR Analytics di kolom kanan
        analytics_frame = ttk.LabelFrame(right_frame, text="HR Analytics")
        analytics_frame.pack(fill="both", expand=True)

        # Buat figure dan canvas untuk grafik
        self.hr_figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.hr_canvas = FigureCanvasTkAgg(self.hr_figure, master=analytics_frame)
        self.hr_canvas.get_tk_widget().pack(fill="both", expand=True)

        # Buat beberapa grafik HR
        self.plot_hr_analytics()

    def plot_analytics(self):
        # Plot production and efficiency analytics
        if len(self.production_data) > 0:
            self.production_figure.clear()
            ax = self.production_figure.add_subplot(111)
            ax.plot(self.production_data, label='Production Rate', color='blue')
            ax.legend()
            self.production_canvas.draw()

            self.efficiency_figure.clear()
            ax = self.efficiency_figure.add_subplot(111)
            ax.plot(self.efficiency_data, label='Efficiency', color='green')
            ax.legend()
            self.efficiency_canvas.draw()


    def create_notebook(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both")
        
        # Create tabs
        self.create_production_line_tab()
        self.create_quality_control_tab()
        self.create_analytics_tab()
        self.create_maintenance_tab()
        self.create_hr_tab()
        
    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Data", command=self.save_data)
        file_menu.add_command(label="Load Data", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        
        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Preferences", command=self.show_preferences)
        
    def create_production_line_tab(self):
        prod_frame = ttk.Frame(self.notebook)
        self.notebook.add(prod_frame, text="Production Line")
        
        # Production control panel
        control_frame = ttk.LabelFrame(prod_frame, text="Control Panel")
        control_frame.pack(side="left", padx=5, pady=5, fill="y")
        
        # Start/Stop button
        self.start_button = ttk.Button(control_frame, text="Start Production",
                                     command=self.toggle_production)
        self.start_button.pack(pady=5)
        
        # Speed control
        ttk.Label(control_frame, text="Production Speed:").pack(pady=2)
        self.speed_scale = ttk.Scale(control_frame, from_=0, to=100, 
                                   orient="horizontal")
        self.speed_scale.set(50)
        self.speed_scale.pack(pady=5)
        
        # Production line canvas
        self.production_canvas = tk.Canvas(prod_frame, width=800, height=400,
                                         bg='white')
        self.production_canvas.pack(side="right", padx=5, pady=5)
        
        # Initialize production line elements
        self.init_production_line()
        
    def init_production_line(self):
        # Create conveyor belt animation
        self.belt_positions = []
        for i in range(10):
            x = 50 + i * 80
            rect = self.production_canvas.create_rectangle(x, 200, x+60, 220,
                                                         fill='gray')
            self.belt_positions.append(rect)
            
        # Create machines
        self.machines = []
        machine_positions = [(100, 100), (300, 100), (500, 100)]
        for x, y in machine_positions:
            machine = self.production_canvas.create_rectangle(x, y, x+80, y+80,
                                                            fill='blue')
            self.machines.append(machine)
            
        # Create products
        self.products = []
        
    def create_quality_control_tab(self):
        quality_frame = ttk.Frame(self.notebook)
        self.notebook.add(quality_frame, text="Quality Control")
        
        # Quality metrics
        metrics_frame = ttk.LabelFrame(quality_frame, text="Quality Metrics")
        metrics_frame.pack(side="left", padx=5, pady=5, fill="y")
        
        # Quality parameters
        self.quality_vars = {}
        parameters = ["Temperature", "Pressure", "Humidity", "Defect Rate"]
        for param in parameters:
            frame = ttk.Frame(metrics_frame)
            frame.pack(pady=5)
            ttk.Label(frame, text=f"{param}:").pack(side="left")
            var = tk.StringVar()
            var.set("0")
            self.quality_vars[param] = var
            ttk.Label(frame, textvariable=var).pack(side="left")
            
        # Quality chart
        self.quality_figure = plt.Figure(figsize=(6,4))
        self.quality_canvas = FigureCanvasTkAgg(self.quality_figure, 
                                               master=quality_frame)
        self.quality_canvas.get_tk_widget().pack(side="right", padx=5, pady=5)
        
    def create_analytics_tab(self):
        analytics_frame = ttk.Frame(self.notebook)
        self.notebook.add(analytics_frame, text="Analytics")
        
        # Create multiple charts
        charts_frame = ttk.Frame(analytics_frame)
        charts_frame.pack(expand=True, fill="both")
        
        # Efficiency chart
        self.efficiency_figure = plt.Figure(figsize=(5,3))
        self.efficiency_canvas = FigureCanvasTkAgg(self.efficiency_figure,
                                            master=charts_frame)
        self.efficiency_canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)
        
        # Production chart
        self.production_figure = plt.Figure(figsize=(5,3))
        self.production_canvas = FigureCanvasTkAgg(self.production_figure,
                                            master=charts_frame)
        self.production_canvas.get_tk_widget().grid(row=0, column=1, padx=5, pady=5)
        
    def init_animation_canvas(self):
        # Initialize animation elements and variables
        self.animation_items = []
        self.animation_speed = 1.0            

    def update_plot(self):
        # Bersihkan plot
        self.production_figure.clear()
        ax = self.production_figure.add_subplot(111)
        
        # Gambar ulang dengan data terbaru
        ax.plot(self.production_data, label='Production Rate', color='blue')
        ax.legend()
        
        # Perbarui canvas
        self.production_canvas.draw()

    def move_canvas(self, x, y):
        # Dapatkan widget Tkinter dari FigureCanvasTkAgg
        widget = self.production_canvas.get_tk_widget()
        # Gunakan metode geometri Tkinter untuk memindahkan widget
        widget.place(x=x, y=y)

    def animate_plot(self):
        def update(frame):
            self.production_data.append(random.randint(80, 120))
            if len(self.production_data) > 50:
                self.production_data.pop(0)
            
            self.update_plot()

        self.animation = FuncAnimation(self.production_figure, update, interval=1000)

    def update_quality_metrics(self):
        # Simulate quality metrics
        self.current_temperature += random.uniform(-0.5, 0.5)
        self.current_pressure += random.uniform(-0.01, 0.01)
        self.current_humidity += random.uniform(-0.5, 0.5)
        defect_rate = random.uniform(0, 0.1)

        self.quality_vars["Temperature"].set(f"{self.current_temperature:.2f} °C")
        self.quality_vars["Pressure"].set(f"{self.current_pressure:.2f} atm")
        self.quality_vars["Humidity"].set(f"{self.current_humidity:.2f} %")
        self.quality_vars["Defect Rate"].set(f"{defect_rate:.2%}")

        self.quality_data.append((self.current_temperature, self.current_pressure, self.current_humidity, defect_rate))
        self.plot_quality_metrics()

    def plot_quality_metrics(self):
        # Plot quality metrics
        if len(self.quality_data) > 0:
            temperatures, pressures, humidities, defect_rates = zip(*self.quality_data)
            self.quality_figure.clear()
            plt.subplot(2, 2, 1)
            plt.plot(temperatures, label='Temperature (°C)')
            plt.legend()
            plt.subplot(2, 2, 2)
            plt.plot(pressures, label='Pressure (atm)', color='orange')
            plt.legend()
            plt.subplot(2, 2, 3)
            plt.plot(humidities, label='Humidity (%)', color='green')
            plt.legend()
            plt.subplot(2, 2, 4)
            plt.plot(defect_rates, label='Defect Rate', color='red')
            plt.legend()
            self.quality_canvas.draw()

    def update_analytics(self):
        # Simulate production and efficiency data
        production_rate = self.speed_scale.get()
        self.production_data.append(production_rate)
        self.efficiency_data.append(random.uniform(0.7, 1.0))

        self.plot_analytics()

    def save_data(self):
        # Save data to a file (implementation needed)
        messagebox.showinfo("Save Data", "Data saved successfully!")

    def load_data(self):
        # Load data from a file (implementation needed)
        messagebox.showinfo("Load Data", "Data loaded successfully!")

    def show_preferences(self):
        # Show preferences dialog (implementation needed)
        messagebox.showinfo("Preferences", "Preferences dialog not implemented.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedManufacturingSimulator(root)
    root.mainloop()