from tkinter import *
from tkinter import messagebox
import joblib

root = Tk()
root.title("Energy Consumption Prediction")
root.geometry("300x200")
label = Label(root, text="Welcome to Energy Consumotion App", font=("Arial", 14))
label.pack(pady=20)

model = joblib.load("energy_model.joblib")


def check_sales():
    try:
        no_app = float(app_entry.get())
        if no_app <= 0:
            raise ValueError("No of appliances must be positive.")
        en_consumed = model.predict([[no_app]])
        # messagebox.showinfo("Prediction Result", f"Predicted Son's Height: {son_height[0]:.2f} inches")
        output_str.set(f"Energy Consumed : {en_consumed[0]:.2f} kWh")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
      



app_label = Label(root, text="Enter No of Appliances being used:")
app_label.pack(pady=5)
app_entry = Entry(root)
app_entry.pack(pady=5)

sub_button = Button(root, text="Check Energy Consumption",command=check_sales)
sub_button.pack(pady=10)


output_str = StringVar()
output_label = Label(root, textvariable=output_str, font=("Arial", 12), fg="blue")
output_label.pack(pady=20)

root.mainloop()