"""
Bowling For Father's Day! Code Challenge Description:
Follow the TODOs in the code to complete the tasks.
At the end of the lesson you will have 
created a bowling game.

with a Father's Day message!!!
"""

# This Code Imports the necessary modules from the tkinter library
import tkinter as tk
import random
import time
import math

# This Code Creates the main window
root = tk.Tk()
root.title("Bowling For Fathers Day!")

# This Code Sets the dimensions of the game window
canvas = tk.Canvas(root, width=600, height=800, bg="lightblue")
canvas.pack()


# Create the bowling lane
def create_lane(canvas):
    # TODO 1. Create 5 varibles to store the lane color, top, bottom, left, and right.  Set the lane color to "#D2B48C", the top to 30, the bottom to 775, the left to 200, and the right to 400. Change the variable names in the create_rectangle function to use the variables you created.
    lane_color = '#D2B48C'
    lane_top = 30
    lane_bottom = 775
    lane_left = 200
    lane_right = 400

    canvas.create_rectangle(
        lane_left, lane_top, lane_right, lane_bottom, fill=lane_color, outline=""
    )


# Create the bowling pins in a triangular formation
def create_pins(canvas):
    # TODO 2. Create 2 variables to store the pin color and radius.  Set the pin color to "white" and the pin radius to 10.
    pin_color = 'white'
    pin_radius = 10
    pin_positions = [
        (300, 125),  # Front pin
        (275, 100),
        (325, 100),  # Second row
        (250, 75),
        (300, 75),
        (350, 75),  # Third row
        (225, 50),
        (275, 50),
        (325, 50),
        (375, 50), ] # Fourth
    # TODO 3. Create an empty list called pins.  Hint: pins = []
    pins = []
    # This Code Creates the Bowling Pins
    for pos in pin_positions:
        pin = canvas.create_oval(
            pos[0] - pin_radius,
            pos[1] - pin_radius,

            pos[0] + pin_radius,
            pos[1] + pin_radius,
            fill=pin_color,
        )
        # TODO 4. Append the pin to the pins list in the loop.  Hint: pins.append(pin)
        pins.append(pin)
    return pins


# This code Creates the bowling ball at the bottom center of the screen
def create_ball(canvas):
    # TODO 5. Create 3 variables to store the ball radius, x position, and y position.  Set the ball radius to 25, the x position to 300, and the y position to 750. Change the variable names in the create_oval function to use the variables you created.
    ball_radius = 25
    ball_x = 300
    ball_y = 750
    ball = canvas.create_oval(
        ball_x - ball_radius,
        ball_y - ball_radius,
        ball_x + ball_radius,
        ball_y + ball_radius,
        fill="black",
    )
    return ball


# This code Handles the ball's motion when the mouse is clicked
def roll_ball(event, canvas, ball, pins):
    ball_speed = -10  # Negative value to move the ball upwards
    while canvas.coords(ball)[1] > 50:
        canvas.move(ball, 0, ball_speed)
        root.update()
        time.sleep(0.05)
    # TODO 6. Call the knock_down_pins function outside of the while loop and pass in the canvas, pins, and ball.  Hint: knock_down_pins(canvas, pins, ball)
    knock_down_pins(canvas, pins, ball)

# This code Knocks down pins and display fireworks
def knock_down_pins(canvas, pins, ball):
    canvas.delete(ball)
    for pin in pins:
        canvas.delete(pin)
    # TODO 7. Call the display_fireworks function outside of the for loop and pass in the canvas.  Hint: display_fireworks(canvas)
    display_fireworks(canvas)

# This Code Creates star-shaped fireworks
def create_star(canvas, x, y, size, color):
    # TODO 8. Create an empty list called points.  Hint: points = [] and change the variable name in the create_polygon function to use the points list.
    points = []
    for i in range(5):
        angle = i * 144  # Star points (144 degrees between each point)
        x_offset = size * math.cos(math.radians(angle))
        y_offset = size * math.sin(math.radians(angle))
        # After Todo 8 Uncomment the below line
        points.extend([x + x_offset, y + y_offset])
    star = canvas.create_polygon(points, fill=color, outline=color)
    return star


# This code Displays fireworks
def display_fireworks(canvas):
    start_time = time.time()
    while time.time() - start_time < 4:  # Display fireworks for 4 seconds
        x = random.randint(200, 500)
        y = random.randint(150, 750)
        size = random.randint(100, 200)  # Larger size for the star
        color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
        firework = create_star(canvas, x, y, size, color)
        root.update()
        time.sleep(0.5)
        canvas.delete(firework)
    # TODO 9. Call the display_message function outside of the while loop and pass in the canvas.  Hint: display_message(canvas)
    display_message(canvas)

# Display "HAPPY FATHER'S DAY!!!" message
def display_message(canvas):
    canvas.create_text(
        300, 200, text="HAPPY FATHER'S DAY!!!", font=("Arial", 35), fill="black"
    )


# The Code Below Initializes the Game Elements and Binds the Mouse Click Event
# to the roll_ball Function to Start the Game Loop
# Do not modify the code below.
# Initialize the game elements
create_lane(canvas)
pins = create_pins(canvas)
ball = create_ball(canvas)

# Bind the mouse click event to the roll_ball function
canvas.bind("<Button-1>", lambda event: roll_ball(event, canvas, ball, pins))

# Start the Tkinter main loop
root.mainloop()
