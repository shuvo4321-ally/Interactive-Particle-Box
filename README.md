
---

# **Interactive Particle Box**  

This project is an interactive graphical simulation where users can generate, move, and manipulate colored points within a boundary box using mouse clicks and keyboard inputs. The points exhibit dynamic behavior, including movement, speed control, blinking effects, and freezing/unfreezing functionality.  

## **Features**  

### 🎯 **Random Movable Points (Right Mouse Click)**  
- Right-clicking inside the box spawns a random-colored point at the clicked position.  
- Each point moves diagonally in a random direction (e.g., top-left, top-right, bottom-left, or bottom-right).  
- Points bounce off the walls by inverting their movement direction upon collision.  

### ⚡ **Speed Control (Up & Down Arrow Keys)**  
- Pressing the **Up Arrow (↑)** increases the speed of all existing points.  
- Pressing the **Down Arrow (↓)** decreases their speed.  
- Speed control applies to all generated points simultaneously.  

### ✨ **Blinking Effect (Left Mouse Click)**  
- Left-clicking toggles a blinking effect on the points.  
- Active points alternate between their color and the background color (black) every second.  
- Clicking again restores the points to their normal state.  

### 🛑 **Freeze & Unfreeze (Spacebar)**  
- Pressing the **Spacebar** freezes all movements and interactions.  
- While frozen, speed control, movement, and blinking are temporarily disabled.  
- Pressing the **Spacebar** again resumes normal functionality.  

## **How It Works**  
https://github.com/user-attachments/assets/ab45f207-d0bb-4463-b14d-9adfdaeeac68
- The simulation operates within a fixed boundary where all points remain contained.  
- Movement is handled using velocity vectors that invert upon hitting a boundary.  
- The blinking effect is implemented using a timed toggle between the original color and the background color.  
- The freeze mechanism pauses all updates while maintaining the current state of the points.  

## **Technologies Used**  
- **Python** (with `pygame` for graphics and event handling)  



## **Future Improvements**  
- Customizable boundary size and colors  
- Additional movement patterns and interactive controls  
- Optimized rendering for handling large numbers of points  

---

