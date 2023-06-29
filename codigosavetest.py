try:
    import Tkinter as tk
    import ttk

except ModuleNotFoundError:
    import tkinter as tk
    import tkinter.ttk as ttk
import pickle

FILENAME = "save.pickle"


class Example(tk.Frame):
    def __init__(self, parent):
        self.create_widgets(parent)
        self.restore_state()

    def create_widgets(self, parent):
        tk.Frame.__init__(self, parent, borderwidth=9, relief="flat")

        self.previous_values = []

        l1 = tk.Label(self, text="Enter a mathematical expression:", anchor="w")
        l2 = tk.Label(self, text="Result:", anchor="w")
        self.expressionVar = tk.StringVar()
        self.expressionEntry = ttk.Combobox(self, textvariable=self.expressionVar, values=("No recent values",))
        self.resultLabel = tk.Label(self, borderwidth=2, relief="groove", width=1)
        self.goButton = tk.Button(self, text="Calculate!", command=self.calculate)

        l1.pack(side="top", fill="x")
        self.expressionEntry.pack(side="top", fill="x", padx=(12, 0))
        l2.pack(side="top", fill="x")
        self.resultLabel.pack(side="top", fill="x", padx=(12, 0), pady=4)
        self.goButton.pack(side="bottom", anchor="e", pady=4)

        self.expressionEntry.bind("<Return>", self.calculate)

        # this binding saves the state of the GUI, so it can be restored later
        root.wm_protocol("WM_DELETE_WINDOW", self.save_state)

    def calculate(self, event=None):
        expression = self.expressionVar.get()
        try:
            result = "%s = %s" % (expression, eval(expression))
            self.previous_values.append(expression)
            self.previous_values = self.previous_values[-8:]
            self.expressionVar.set("")
            self.expressionEntry.configure(values=self.previous_values)
        except:
            result = "invalid expression"

        self.resultLabel.configure(text=str(result))

    def save_state(self):
        try:
            data = {
                "previous": self.previous_values,
                "expression": self.expressionVar.get(),
                "result": self.resultLabel.cget("text"),
            }
            with open(FILENAME, "wb") as f:
                pickle.dump(data, f)

        except Exception as e:
            print
            "error saving state:", str(e)

        root.destroy()

    def restore_state(self):
        try:
            with open(FILENAME, "rb") as f:
                data = pickle.load(f)
            self.previous_values = data["previous"]
            self.expressionEntry.configure(values=self.previous_values)
            self.expressionVar.set(data["expression"])
            self.resultLabel.configure(text=data["result"])
        except Exception as e:
            print
            "error loading saved state:", str(e)


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()