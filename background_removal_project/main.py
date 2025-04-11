import os
from rembg import remove
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font
from PIL import Image, ImageTk 


# function remove
def remove_background(input_path, output_path):
    try:
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
        output_data = remove(input_data)
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)
    except Exception as e:
        print(f"Error: {e}")



# process
def process_images_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    for file in files:
        input_path = os.path.join(folder_path, file)
        output_path = os.path.join(output_folder, f'no_bg_{file}')
        remove_background(input_path, output_path)
    messagebox.showinfo("Success", "Background removal complete!")

def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder with Images")
    if folder_path:
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if output_folder:
            process_images_in_folder(folder_path, output_folder)
        else:
            messagebox.showwarning("No Output Folder", "Please select an output folder.")
    else:
        messagebox.showwarning("No Folder", "Please select a folder with images.")

def create_gui():
    window = tk.Tk()
    window.title("Background Remover")
    window.geometry("500x500")
    window.config(bg="#f0f0f0")

    heading_font = font.Font(family="Helvetica", size=20, weight="bold")
    button_font = font.Font(family="Helvetica", size=12)

    # load picture
    try:
        image = Image.open("picture.png")
        image = image.resize((200, 200)) 
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(window, image=photo, bg="#f0f0f0")
        img_label.image = photo 
        img_label.pack(pady=20)
    except Exception as e:
        print(f"Cannot load image: {e}")

        
    heading_label = tk.Label(window, text="Background Remover", font=heading_font, bg="#cccfff", fg="#4a90e2")
    heading_label.pack(pady=10)

    process_button = tk.Button(window, text="Start Processing", command=select_folder,
                               font=button_font, bg="#4a90e2", fg="white", padx=20, pady=10,
                               relief="flat", activebackground="#357ABD")
    process_button.pack(pady=15)

    exit_button = tk.Button(window, text="Exit", command=window.quit,
                            font=button_font, bg="#e94e77", fg="white", padx=20, pady=10,
                            relief="flat", activebackground="#c0392b")
    exit_button.pack(pady=5)

    window.mainloop()

create_gui()
