from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
# The 'PIL' import is not needed, only these specific modules
from PIL import ImageTk, Image

# Main Class --Application--
class application:
    # Constructor
    def __init__(self, master):
        # self.master is our root window
        self.master = master
        # Canvas Size
        self.c_size = (700, 500)
        # Creates All Of Our Widgets
        self.setup_gui(self.c_size)
        self.img = None

    # Making Widgets
    def setup_gui(self, s):
        Label(self.master, text='Image Viewer', pady=5, bg='white',
              font=('Ubuntu', 30)).pack()
        self.canvas = Canvas(self.master, height=s[1], width=s[0],
                             bg='black', bd=10, relief='ridge')
        self.canvas.pack()
        txt = '''
                !
             No Image
        '''
        # Text On Canvas Saying No Current Image Open.
        self.wt = self.canvas.create_text(s[0] / 2, s[1] / 2, text=txt,
                                          font=('', 30), fill='white', anchor=CENTER) # Centered the text
        f = Frame(self.master, bg='white', padx=10, pady=10)
        Button(f, text='Open New Image', bd=2, fg='white', bg='black', font=('', 15),
               command=self.make_image).pack(side=LEFT)
        f.pack()
        # Status Bar
        self.status = Label(self.master, text='Current Image: None', bg='gray',
                            font=('Ubuntu', 15), bd=2, fg='black', relief='sunken', anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def make_image(self):
        try:
            # Open Image File (use a more descriptive variable name)
            filepath = fd.askopenfilename()
            
            # --- FIX 1: Check if a file was actually selected ---
            if not filepath:
                return # If no file is chosen, do nothing and exit the function

            self.pilImage = Image.open(filepath)
            
            # --- FIX 2: Replace deprecated Image.ANTIALIAS ---
            # Use Image.Resampling.LANCZOS for high-quality downsampling
            resized_image = self.pilImage.resize((700, 500), Image.Resampling.LANCZOS)
            
            self.img = ImageTk.PhotoImage(resized_image)
            # Delete all canvas content(text,image)
            self.canvas.delete(ALL)
            # Create Image (centering it properly)
            self.canvas.create_image(self.c_size[0] / 2, self.c_size[1] / 2,
                                     anchor=CENTER, image=self.img)
            # Update Status Bar
            self.status['text'] = 'Current Image: ' + filepath
        except Exception as e:
            # Show a more helpful error message
            print(f"An error occurred: {e}") # Prints the real error to the console
            ms.showerror('Error!', 'An error occurred. Make sure the file is a valid image.')

if __name__ == '__main__':
    # Create Object And Run Programme
    root = Tk()
    root.configure(bg='white')
    root.title('Image Viewer')
    application(root)
    root.resizable(False, False) # Using booleans is more standard
    root.mainloop()