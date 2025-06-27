from tkinter import *
from tkinter import messagebox
import joblib

root = Tk()
root.title("Performance Index Predictor")
root.geometry("450x300")
label = Label(root, text="Welcome to Performance Index Predictor", font=("Arial", 14))
label.pack(pady=20)

model = joblib.load("model.joblib")


def predict():
    try:
        study_hours = float(study_hours_entry.get())
        paper_prac = float(paper_prac_entry.get())
        if study_hours and paper_prac <= 0:
            raise ValueError("Input must be a positive number.")
        ans = model.predict([[study_hours, paper_prac]])
        # messagebox.showinfo("Prediction Result", f"Predicted Son's Height: {son_height[0]:.2f} inches")
        output_str.set(f"Your Performance Index: {ans[0]:.2f} ")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
      



study_hours_label = Label(root, text="Enter study hours:")
study_hours_label.pack(pady=5)
study_hours_entry = Entry(root)
study_hours_entry.pack(pady=5)

paper_prac_label = Label(root, text="Enter paper practiced:")
paper_prac_label.pack(pady=5)
paper_prac_entry = Entry(root)
paper_prac_entry.pack(pady=5)

sub_button = Button(root, text="Predict Performance ",command=predict)
sub_button.pack(pady=10)


output_str = StringVar()
output_label = Label(root, textvariable=output_str, font=("Arial", 12), fg="blue")
output_label.pack(pady=20)

root.mainloop()
