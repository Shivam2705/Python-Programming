# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 00:18:54 2017

@author: A1144
"""
#LECTURE-1
#Event Driven programming
#Start ---> Initialize---->wait--->Handler---->Quit--->End
#Events: Input: (Button, Textbox), Keyboard:(KeyDown, Keyup), Mouse:(Click and Drag) and Timer: Periodically

# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Event handler
def tick():
    print ("tick!")

# Register handler
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()


#Event Queue






#LECTURE-2
#Local vs Gloabal Variable 
# global vs local examples

# num1 is a global variable

num1 = 1
print num1

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print num2
    
fun()


# the scope of global num1 is the whole program, num 1 remains defined
print num1

# the scope of the variable num2 is fun(), num2 is now undefined
# print num2


# why use local variables?
# give a descriptive name to a quantity
# avoid computing something multiple times

def fahren_to_kelvin(fahren):
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)





# the risk/reward of using global variables

# risk - consider the software system for an airliner
#		critical piece - flight control system
#		non-critical piece - in-flight entertainment system

# both systems might use a variable called "dial"
# we don't want possibility that change the volume on your audio
# causes the plane's flaps to change!



# example
num = 4

def fun1():
    global num
    num = 5
    
def fun2():
    global num
    num = 6

# note that num changes after each call with no obvious explanation    
print num
fun1()
print num
fun2()
print num

# global variables are an easy way for event handlers
# to communicate game information.

# safer method - but they required more sophisticated
# object-programming techniques






#LECTURE3: Simple GUI

# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)

# Define "helper" functions

# Define event handler functions

# Create a frame

# Register event handlers

# Start frame and timers
