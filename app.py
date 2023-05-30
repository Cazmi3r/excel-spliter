import customtkinter   
from pathlib import Path
from excelSpliter import excel_split

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.file_path = ""
        self.output_path = ""

        self.title("Excel Splitter")
        self.geometry("400x90")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.file_button = customtkinter.CTkButton(self, text="Select a File", command=self.file_button_callback)
        self.file_button.grid(row=0, column=0, padx=10, pady=10, sticky="ews")

        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.submit_button_callback)
        self.submit_button.grid(row=0, column=1, padx=10, pady=10, sticky="ews")
        
    def set_output_path(self):
        self.output_path = self.file_path.parent

    def submit_button_callback(self):
        excel_split(self.file_path, self.output_path)
        
    def file_button_callback(self):
        f = customtkinter.filedialog.askopenfile(parent=app,mode='rb',title='Choose a file')
        self.file_path = Path(f.name)
        self.set_output_path()
        
app = App()
app.mainloop()