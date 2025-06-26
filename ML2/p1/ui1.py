from tkinter import *
from tkinter import messagebox
import joblib

root = Tk()
root.title("Monthy expenditure Prediction App")
root.geometry("450x300")
label = Label(root, text="Welcome to Monthy expenditure Prediction App", font=("Arial", 14))
label.pack(pady=20)

model = joblib.load("model.joblib")


def predict_height():
    try:
        age = float(age_entry.get())
        inc = float(inc_entry.get())
        if age and inc <= 0:
            raise ValueError("Input must be a positive number.")
        expence = model.predict([[age, inc]])
        # messagebox.showinfo("Prediction Result", f"Predicted Son's Height: {son_height[0]:.2f} inches")
        output_str.set(f"Your Monthly expense: {expence[0]:.2f} ")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
      



age_label = Label(root, text="Enter Age:")
age_label.pack(pady=5)
age_entry = Entry(root)
age_entry.pack(pady=5)

inc_label = Label(root, text="Enter Montly Income:")
inc_label.pack(pady=5)
inc_entry = Entry(root)
inc_entry.pack(pady=5)

sub_button = Button(root, text="Predict Expenditure ",command=predict_height)
sub_button.pack(pady=10)


output_str = StringVar()
output_label = Label(root, textvariable=output_str, font=("Arial", 12), fg="blue")
output_label.pack(pady=20)

root.mainloop()
