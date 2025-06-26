from tkinter import *
from tkinter import messagebox
import joblib

root = Tk()
root.title("Car Mileage Prediction App")
root.geometry("450x300")
label = Label(root, text="Welcome to Car Mileage Prediction App", font=("Arial", 14))
label.pack(pady=20)

model = joblib.load("model.joblib")


def predict():
    try:
        size = float(age_entry.get())
        weight = float(inc_entry.get())
        if size and weight <= 0:
            raise ValueError("Input must be a positive number.")
        expence = model.predict([[size, weight]])
        # messagebox.showinfo("Prediction Result", f"Predicted Son's Height: {son_height[0]:.2f} inches")
        output_str.set(f"Your Car Mileage: {expence[0]:.2f} ")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
      



age_label = Label(root, text="Enter your Engine Size in L:")
age_label.pack(pady=5)
age_entry = Entry(root)
age_entry.pack(pady=5)

inc_label = Label(root, text="Your your car weight in Kg:")
inc_label.pack(pady=5)
inc_entry = Entry(root)
inc_entry.pack(pady=5)

sub_button = Button(root, text="Predict Mileage ",command=predict)
sub_button.pack(pady=10)


output_str = StringVar()
output_label = Label(root, textvariable=output_str, font=("Arial", 12), fg="blue")
output_label.pack(pady=20)

root.mainloop()
