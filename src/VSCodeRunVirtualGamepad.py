import serial
import vgamepad as vg
import time

# Sanal gamepad oluştur
gamepad = vg.VX360Gamepad()
PORT = 'COM4'

try:
    ser = serial.Serial(PORT, 115200, timeout=0.01)
    print("SANAL XBOX KOLU AKTİF!")
    print("Düzen: Joystick=D-Pad, A=A, B=X, Middle=Start")
except:
    print("HATA: Port açılamadı. mBlock kapalı mı?")
    exit()

while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            data = line.split(',')
            
            if len(data) == 7:
                u, d, l, r, m, btn_a, btn_b = map(int, data)
                
                # --- D-PAD (Joystick) Ayarları ---
                if u: gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                else: gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                
                if d: gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                else: gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                
                if l: gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                else: gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                
                if r: gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                else: gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

                # --- BUTONLAR ---
                # A -> Xbox A
                if btn_a: gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                else: gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                
                # B -> Xbox X
                if btn_b: gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                else: gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                
                # Middle Click -> Xbox Start
                if m: gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                else: gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

                # Değişiklikleri bilgisayara gönder
                gamepad.update()
                
    except Exception as e:
        print("Hata:", e)
        continue
    
    time.sleep(0.001)
