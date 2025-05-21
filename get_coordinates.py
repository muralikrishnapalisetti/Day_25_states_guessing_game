import turtle
import pandas as pd

states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal", "Delhi"
]

current_state_index = 0
coordinates = []

# Setup screen
screen = turtle.Screen()
screen.title("Click on Each State (One by One)")
image = "blank_india_img.gif"
screen.addshape(image)
turtle.shape(image)

# Function to record clicked coordinates
def get_mouse_click_coor(x, y):
    global current_state_index
    state = states[current_state_index]
    print(f"{state} -> {x},{y}")
    coordinates.append({"state": state, "x": int(x), "y": int(y)})
    current_state_index += 1

    if current_state_index == len(states):
        df = pd.DataFrame(coordinates)
        df.to_csv("india_states.csv", index=False)
        print("✅ All states recorded and saved to india_states.csv")
        turtle.bye()

# Listen for mouse clicks
turtle.onscreenclick(get_mouse_click_coor)
screen.mainloop()
