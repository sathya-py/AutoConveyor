# **AutoConveyor – Automated Video Processing Pipeline**

🚀 **AutoConveyor** is a fully automated **video processing and YouTube upload pipeline** designed for **DaVinci Resolve 19+**. It streamlines video **editing, color grading, rendering, and uploading** with AI-driven enhancements and metadata enrichment.

🔗 **GitHub Repository**: [AutoConveyor](https://github.com/sathya-py/AutoConveyor)

---

## **✨ Features**

✅ **Automated Video Processing** – Uses DaVinci Resolve API for timeline creation, editing, and rendering.  
✅ **AI-Powered Enhancements** – Scene detection, auto color grading, and metadata enrichment.  
✅ **YouTube Upload Automation** – Handles video uploads, scheduling, and tagging.  
✅ **Multithreading Support** – Efficient parallel video processing.  
✅ **Checkpoint System** – Resume processing after failures.  
✅ **Centralized Logging & Error Handling** – Tracks issues and system activity.  
✅ **CLI & Configurable Settings** – Flexible and user-friendly operation.

---

## **📂 Project Structure**

```plaintext
📂 AutoConveyor/
│── 📂 src/                      # Source Code
│   │── monitor/                 # File monitoring module
│   │── processing/              # Video processing logic
│   │── ai_engine/               # AI-based enhancements
│   │── upload/                  # YouTube upload automation
│   │── framework/               # Logging, errors, multithreading, and testing
│   │── config/                  # Configuration management
│
│── 📂 scripts/                  # Automation scripts
│── 📂 logs/                     # Log files for tracking errors & execution
│── 📂 tests/                    # Unit & integration tests
│── 📂 docs/                     # Documentation
│
│── requirements.txt             # Python dependencies
│── setup.py                     # Installation script
│── README.md                    # This file
│── .gitignore                   # Ignore unnecessary files
```

---

## **⚙️ Installation**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/sathya-py/AutoConveyor.git
cd AutoConveyor
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Configure Settings**

Modify `config/config.json` to set up:

- **Watch Directory** – Location for new videos.
- **Output Directory** – Where processed videos will be saved.
- **YouTube API Key** – Required for upload automation.

Example:

```json
{
  "watch_directory": "/videos/input/",
  "output_directory": "/videos/output/",
  "youtube_api_key": "YOUR_API_KEY",
  "default_render_preset": "YouTube 1080p"
}
```

---

## **🚀 Usage**

### **Start Monitoring & Processing**

```bash
python src/application/main.py
```

### **Run a Batch Process**

```bash
python scripts/batch_process.py
```

### **Reprocess Failed Videos**

```bash
python scripts/reprocess_failed.py
```

---

## **🛠 Development & Contributions**

### **Run Tests**

```bash
pytest tests/
```

### **Contribute to the Project**

1. **Fork the repository**.
2. **Create a new branch** (`feature-new-functionality`).
3. **Commit your changes** (`git commit -m "Added new feature"`).
4. **Push to GitHub** (`git push origin feature-new-functionality`).
5. **Submit a Pull Request**.

---

## **📜 License**

This project is licensed under the **MIT License**.

---

🚀 **AutoConveyor – Automating Video Processing & Uploads with AI!**
