import tkinter
import requests
from PIL import Image,ImageTk

class Meals:
    def __init__(self):

        self.meal_Name_var = ""
        self.meal_category_var = ""


# ----------------------------Area for creating window --------------------------------------------#

        self.master = tkinter.Tk()
        self.master.title("Meal App")
        self.master.geometry("1470x750+10+10")
        self.master.resizable(False,False)

# ----------------------------Area for creating window -------------------END-------------------------#

# -------------------Area for widget to display on the window----------------------------------------#

# ---------------Area for Left Frame ---------------------------#

        self.left_frame = tkinter.Frame(self.master, width=400, height=740, background="#a84fdb")
        self.left_frame.place(x=10,y=0)

        self.title_Label = tkinter.Label(self.left_frame, text="."*22+"Meal Book"+"."*23,bg="#a84fdb",
                                         font=("bookman old style",15), fg="black")
        self.title_Label.place(x=10, y=25)

        self.meal_frame = tkinter.LabelFrame(self.left_frame, background="blue", width=380, height=300)
        self.meal_frame.place(x=10, y=70)

        self.img = Image.open("img/meal.png").resize((350,270),Image.BOX)
        self.img_now = ImageTk.PhotoImage(self.img)

        self.picLabel = tkinter.Label(self.meal_frame, text="name", image=self.img_now)
        self.picLabel.place(x=10, y=10)

        self.meal_Category_Label = tkinter.Label(self.left_frame, text="Category:", font=("bookman old style", 15),
                                               bg="#a84fdb",textvariable=self.meal_category_var)
        self.meal_Category_Label.place(x=10, y=380)

        self.meal_Name_Label = tkinter.Label(self.left_frame, text="Meal Name:", bg="#a84fdb",
                                             font=("bookman old style",15), textvariable=self.meal_Name_var)
        self.meal_Name_Label.place(x=10, y=420)

# ---------------Area for Left Frame ------------END---------------#

# ---------------Area for Right Frame ----------------------------------------#

        self.right_frame = tkinter.Frame(self.master, width=1050, height=740, background="#f4a3e1")
        self.right_frame.place(x=410,y=0)

        self.title_Label = tkinter.Label(self.right_frame, text="-"*21+"Meal Description"+"-"*22, bg="#f4a3e1",
                                        fg="#6d3e3c", font=("bookman old style",30))
        self.title_Label.place(x=10, y=20)

        self.textArea = tkinter.Text(self.right_frame, font=("bookman old style",15), width=85, height=26)
        self.textArea.place(x=10, y=75)

        self.nextbtn = tkinter.Button(self.right_frame, text="Next Meal",bg="#f4a3e1",
                                      font=("bookman old style",15),
                                      width=50, command=self.insertdata
                                      )
        self.nextbtn.place(x=200, y=690)

# ---------------Area for Right Frame --------------------END------------------#

        self.master.mainloop()

# -------------------Area for widget to display on the window-----------------------END-----------------#

# --------------------------Area for all Methods used in the requirements ---------------------------------#


    def fetch_random_meals_freeapi(self):
        url = "https://api.freeapi.app/api/v1/public/meals/meal/random"
        response = requests.get(url)
        all_data = response.json()

        if all_data["success"] and "data" in all_data:
            data = all_data["data"]

            return data


    def insertdata(self):
        self.textArea.delete(1.0,tkinter.END)

        data = self.fetch_random_meals_freeapi()

# ---------Get Image from URL -------------------------
        img_url = data["strMealThumb"]

        url_response = requests.get(img_url)

        with open('img/image.png', 'wb') as f:
            f.write(url_response.content)

        self.img = Image.open("img/image.png").resize((350,270),Image.BOX)
        self.img_now = ImageTk.PhotoImage(self.img)
        self.picLabel.config(image=self.img_now)

        self.meal_Name_var = "Meal Name: "+data["strMeal"]
        self.meal_Name_Label.config(text=self.meal_Name_var, wraplength=380)

        self.meal_category_var = "Category: "+data["strCategory"]
        self.meal_Category_Label.config(text=self.meal_category_var)

        instruction = data["strInstructions"]
        a = "-"*20

        message = f"Instruction -----------------:\n{instruction}\n\n\n"

        self.textArea.insert(tkinter.END,message)

# --------------------------Area for all Methods used in the requirements --------------END-------------------#


if __name__=="__main__":
      Meals()