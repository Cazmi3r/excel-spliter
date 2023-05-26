import customtkinter   
from pathlib import Path
from excelSpliter import excel_split

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Excel Splitter")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        # customtkinter.filedialog.askdirectory()
        
        input_path = Path("./input.xlsx")
        output_path = Path(".")
        excel_split(input_path, output_path)
        
        
        


app = App()
app.mainloop()