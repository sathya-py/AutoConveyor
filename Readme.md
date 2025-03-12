# 🚀 AutoConveyor – Automated Video Processing & Upload System

## 📌 Overview

AutoConveyor is a fully automated **video processing pipeline** that integrates with **DaVinci Resolve 19** for video editing, color grading, and rendering, followed by **automated uploads to YouTube**.

It is **modular, scalable, and future-ready**, supporting **multithreading, checkpointing, automated tagging, metadata enrichment, and AI-based scene color grading**.

---

## 🎯 Features

✅ **Automated Video Processing** – Detects new videos, edits, color grades, renders, and uploads them.  
✅ **Multithreading Support** – Processes multiple videos concurrently for high efficiency.  
✅ **Checkpoint System** – Automatically resumes from failures.  
✅ **AI-Based Scene Color Grading** – Enhances videos using intelligent color grading.  
✅ **YouTube Auto Upload** – Uploads videos with metadata enrichment and auto-tagging.  
✅ **Detailed Logging & Error Handling** – Ensures system reliability with retries.  
✅ **Future-Proof & Scalable** – Designed to adapt to newer DaVinci Resolve versions and cloud deployment.

---

## 📂 Project Structure

```plaintext
📂 AutoConveyor/
│── 📂 src/                      # Source Code
│   │── 📂 application/           # Application Layer
│   │── 📂 domain/                # Business Logic (Processing & Uploading)
│   │── 📂 infrastructure/        # External API Interfaces
│   │── 📂 framework/             # Background Execution & Logging
│
│── 📂 config/                    # Configuration Files
│── 📂 logs/                      # Logging directory
│── 📂 docs/                      # Documentation
│── requirements.txt              # Python dependencies
│── setup.py                      # Installation script
│── .gitignore                    # Ignore unnecessary files
```

---

## ⚙️ Installation

### **🔹 Prerequisites**

1. **Python 3.9+**
2. **DaVinci Resolve 19** (with scripting enabled)
3. **Google API Credentials** for YouTube uploads
4. **FFmpeg** (for additional processing, if needed)

### **🔹 Setup Instructions**

1️⃣ **Clone the repository**

```bash
git clone https://github.com/sathya-py/AutoConveyor.git
cd AutoConveyor
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Configure the system**

- Modify `config/config.json` to match your environment.

4️⃣ **Run AutoConveyor**

```bash
python src/application/main.py
```

---

## 🔄 How It Works

1. **Watches for new video files** in the specified directory.
2. **Automatically processes videos** using DaVinci Resolve.
3. **Applies AI-based scene color grading** for enhancement.
4. **Uploads the final video to YouTube** with metadata and auto-tagging.
5. **Logs all activities** and supports auto-recovery in case of failure.

---

## 🛠️ Configuration

Modify `config/config.json` to customize settings:

```json
{
  "watch_directory": "/videos/input/",
  "output_directory": "/videos/output/",
  "youtube_api_key": "YOUR_API_KEY",
  "default_render_preset": "YouTube 1080p",
  "resolve_version_check": true,
  "multithreading_enabled": true,
  "checkpointing_enabled": true,
  "auto_color_grading": true,
  "metadata_enrichment": true
}
```

## 📌 Breakdown of Key Components:

Core Dependencies – Environment handling, CLI progress, file monitoring.
DaVinci Resolve API – Blackmagic SDK (ensure correct installation).
AI-Based Enhancements – PyTorch, OpenCV, TensorFlow, MediaPipe for scene-based auto color grading.
Video Processing & Automation – FFmpeg, MoviePy, Pydub for handling video & audio processing.
YouTube API Integration – Google API client for automated uploads with metadata enrichment.
Multithreading & Performance – Threadpoolctl, Joblib, AsyncIO to support parallel processing.
Error Handling & Logging – Loguru, Retry for logging & failure recovery.
Configuration & Serialization – Pydantic, PyYAML, JSON5 for flexible configuration.

---

## 📊 Logging & Error Handling

AutoConveyor logs all activities to a dedicated log file and supports error recovery through a checkpoint system.

- **Log Directory**: `logs/`
- **Error Handling**: Automatically retries failed operations and resumes processing from the last checkpoint.

---

## 🚀 Future Enhancements

🔹 **Web Dashboard** – Track progress in real-time.  
🔹 **Cloud Deployment** – Support AWS/GCP/Azure processing.  
🔹 **Scheduled Uploads** – Optimize YouTube posting times.  
🔹 **Multi-Machine Processing** – Distribute workload across servers.

---

## 👨‍💻 Contributing

1. **Fork the repository**
2. **Create a feature branch**
3. **Commit changes and push**
4. **Submit a pull request**

---

## 📜 License

MIT License – Free to use and modify.

---

## 📞 Support

For issues, open a GitHub issue or contact the maintainer.
