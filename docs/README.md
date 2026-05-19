🚀 Getting Started
Follow these steps precisely to get your CyberPi Gamepad up and running.

Phase 1: CyberPi Configuration (Hardware)
Open mBlock 5: Use the Web or Desktop Python editor.

Mode Selection: Switch CyberPi to "Upload Mode".

Deploy Code:

Open src/MblockUploadMain.py from this repository.

Connect your CyberPi and click Upload.

Crucial Step: Once the upload is successful, click "Disconnect" in mBlock. This releases the COM port so the PC driver can access it.

Phase 2: PC Driver Setup (Software)
Environment: Open the project folder in VS Code.

Install Dependencies: Run the following command in your terminal to install the required bridge libraries:

Bash
pip install -r requirements.txt
Launch Driver: Execute the virtual gamepad script:

Bash
    python src/VSCodeRunVirtualGamepad.py
    ```

---

### 🛠 Troubleshooting (Common Issues)
*   **Port Access Denied:** Ensure mBlock or any other serial monitor is disconnected before running the VS Code script.
*   **Input Latency:** If you experience lag, ensure you are using a high-quality USB-C data cable.
*   **Module Not Found:** If Python throws a `ModuleNotFoundError`, double-check that you ran the `pip install` command in the correct environment.

---

### 🎯 Why This Structure?
> **Note for Evaluators:** This repository follows a modular architecture, separating the **embedded logic** (CyberPi) from the **input emulation** (PC Driver). This ensures scalability and clean code management, as required by the **Bursa Genç AR-GE** standards.

---
