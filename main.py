import tkinter as tk
from tkinter import filedialog
import os
#maintainig 
class Img_As_Pdf:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_file_name = tk.StringVar()
        self.selected_img_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image to pdf Converter", font =("Helvetica",16, "bold"))
        title_label.pack(pady=10)

        select_img_button = tk.Button(self.root, text="Image to pdf Converter", command = self.select_img )
        select_img_button .pack(pady=(0, 10))

        self.selected_img_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter Output Pdf Name:")
        label.pack()

        pdf_name_entry = tk.Entery(self.root, textvariable = self.output_pdf_name, width=40, justify="center")
        pdf_name_entry.pack()

        covert_button = tk.Button(self.root, text="convert to pdf", command = self.convert_img_to_pdf )
        covert_button .pack(pady=(20, 40))

    def select_img(self):
        self.image_paths = filedialog.askopenfilename(title="select img", filetypes= [("image files", "*.png;*jpg;*jpeg")])
        





def main():
    root = tk.Tk()
    root.title("Img to pdf")
    converter = Img_As_Pdf(root)
    root.geometry("400x600")
    root.mainloop()

if __name__ == "__main__":
    main()
        