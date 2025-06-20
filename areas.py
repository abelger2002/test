import math
from colorama import *

def area_shapes():
    while True:
        do_know_area = input(Fore.YELLOW + "Do you know the area of a shape? (Y/N): \n \t >>>").lower()
        
        if do_know_area == "y":
            print(Fore.GREEN + "Great! Let's calculate the area of a shape.")
            print(Fore.LIGHTRED_EX + "change all units to cm^2")
            print(Fore.LIGHTRED_EX + "the shapes that you can calculate the area of are: \n triangle, rectangle, circle, square, parallelogram, trapezoid, ellipse, rhombus, regularpentagon, regularhexagon, sectorofacircle, kite")
            try:
                user_shap = input("enter the that you want to know the area \n \t >>>").lower().replace(" ", "")
                # dictionary of shapes and their area formulas
                # and asking the user for the necessary dimensions
                shapes = {
                    "triangle":1/2 * float(input("enter base \t :")) * float(input("enter height \t :")) 
                            if user_shap=="triangle" else None,
                    "rectangle": float(input("enter length \t :")) * float(input("enter width \t :"))
                            if user_shap=="rectangle" else None,
                    "circle":float(input("enter radius\t :")) ** 2 * math.pi
                            if user_shap=="circle" else None,
                    "square":float(input("enter side\t :")) ** 2 
                            if user_shap=="square" else None,
                    "parallelogram":float(input("enter base\t :")) * float(input("enter height\t :")) 
                            if user_shap=="parallelogram" else None,
                    "trapezoid":(float(input("enter base1\t :")) + float(input("enter base2\t :"))) * float(input("enter height\t :")) / 2 
                            if user_shap=="trapezoid" else None,
                    "ellipse":math.pi * float(input("enter semi-major axis\t :")) * float(input("enter semi-minor axis\t :")) 
                            if user_shap=="ellipse" else None,
                    "rhombus":(float(input("enter diagonal1\t :")) * float(input("enter diagonal2\t :"))) / 2
                            if user_shap=="rhombus" else None,
                    "regularpentagon":(1/4) * math.sqrt(5 *(5 + 2* math.sqrt(5)) * float(input("enter side length\t :"))) 
                            if user_shap=="regularpentagon" else None,
                    "regularhexagon":(3 * math.sqrt(3))/2 * float(input("enter side lenght\t :"))
                            if user_shap=="regularhexagon :" else None,
                    "sectorofacircle":(float(input("enter central angle(indegrees)\t :"))/360) * math.pi * (float(input("enter radius\t :"))) 
                            if user_shap=="sectorofacircle" else None,
                    "kite":1/2 * float(input("enter diagonal1\t :")) * float(input("enter diagonal2\t :"))
                            if user_shap=="kite" else None
                    
                    }
                
                if user_shap in shapes.keys():
                    print(Fore.RED + f"the area of the shape is {shapes[user_shap]:.2f}cm^2")
                    
                else:
                    print("please enter a valid shape name")
                    
            except ValueError:
                print(Fore.RED + "Please enter a valid number")
                
        elif do_know_area == "n":
            print("Have a nice day!")
            break
        
        else:
            print("enter a valid input (Y/N)")

            
    
    