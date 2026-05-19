# CyberPi Gamepad Controller 🎮

This project transforms a **CyberPi (mBot2)** microcontroller into a functional PC gamepad using **Python**. It leverages the onboard sensors (joystick and buttons) to simulate keyboard/mouse inputs on a computer.

## 🚀 Features
- **Real-time Control:** High-speed serial communication between CyberPi and PC.
- **Custom Mapping:** Buttons are mapped to specific keyboard keys for gaming.
- **Hardware Integration:** Uses CyberPi's built-in joystick for movement.

## 🛠️ Tech Stack
- **Language:** Python (High-level, interpreted)
- **Communication:** Serial (UART) via `pyserial`
- **Input Simulation:** `pyautogui` or `pydirectinput`
- **Hardware:** Makeblock CyberPi

## 📁 Project Structure
- `src/`: Contains the main Python driver and CyberPi scripts.
- `docs/`: Technical documentation and connection guides.
- `requirements.txt`: List of necessary Python libraries.

## 🔧 Installation & Setup
1. Connect your **CyberPi** to your computer via USB.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
Run the main script:

Bash
python src/main.py
