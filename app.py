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
        
        self.label = customtkinter.CTkLabel(self, text="Please select a file!", fg_color="transparent")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ewn", columnspan=2)
        
        self.file_button = customtkinter.CTkButton(self, text="Select a File", command=self.file_button_callback)
        self.file_button.grid(row=0, column=0, padx=10, pady=10, sticky="ews")

        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.submit_button_callback)
        self.submit_button.grid(row=0, column=1, padx=10, pady=10, sticky="ews")
    
    def validate_file_path(self):
        
        if self.file_path == "":
            self.label.configure(text="ERROR! No file selected!")
            return False
            
        file_suffix = self.file_path.suffix
        if ".xlsx" not in file_suffix:
            self.label.configure(text="ERROR! Only .xls or .xlsx files work!")
            return False
        
        return True
            
        
    def set_output_path(self):
        self.output_path = self.file_path.parent

    def submit_button_callback(self):
        if self.validate_file_path():    
            excel_split(self.file_path, self.output_path)
            self.label.configure(text="File has been split!")
            self.file_path = ""
            self.output_path = ""
        
    def file_button_callback(self):
        f = customtkinter.filedialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        self.file_path = Path(f.name)
        self.set_output_path()
        self.label.configure(text=f"Selected File: {self.file_path.name}")
        
app = App()
app.mainloop()