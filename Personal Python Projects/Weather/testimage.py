from PIL import Image
try:
    img = Image.open("C:\College Work\CIS189 - Python I\Personal projects\Weather\images\daytime.jpg")
    print("Image opened successfully!")
except FileNotFoundError:
    print("Image not found!")