import cyberpi, time

while True:
    # Joystick yönleri (D-Pad için)
    u = 1 if cyberpi.controller.is_press('up') else 0
    d = 1 if cyberpi.controller.is_press('down') else 0
    l = 1 if cyberpi.controller.is_press('left') else 0
    r = 1 if cyberpi.controller.is_press('right') else 0
    m = 1 if cyberpi.controller.is_press('middle') else 0 # Start için
    
    # Butonlar
    a = 1 if cyberpi.controller.is_press('a') else 0
    b = 1 if cyberpi.controller.is_press('b') else 0
    
    # Format: u,d,l,r,m,a,b
    print(str(u)+","+str(d)+","+str(l)+","+str(r)+","+str(m)+","+str(a)+","+str(b))
    time.sleep(0.01)
