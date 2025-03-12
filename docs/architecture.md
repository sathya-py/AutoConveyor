# **AutoConveyor – Architecture Document**

## **1. Overview**

**AutoConveyor** is an automated **video processing pipeline** that integrates with **DaVinci Resolve 19** for editing, color grading, and rendering, followed by automated uploads to **YouTube**. It is designed to be **modular, scalable, and adaptable** for future updates and improvements.

---

## **2. Clean Code Architecture**

AutoConveyor follows **Clean Code Architecture** to ensure **separation of concerns, maintainability, and extensibility**. The system is structured into distinct layers:

### **2.1 Layered Design**

| **Layer**                     | **Responsibility**                                                                     |
| ----------------------------- | -------------------------------------------------------------------------------------- |
| **Application Layer**         | Manages configurations, execution flow, and user interaction.                          |
| **Domain Layer**              | Core business logic – video processing, tracking, and uploading.                       |
| **Infrastructure Layer**      | Interfaces with external APIs (DaVinci Resolve, YouTube) and monitors the file system. |
| **Framework & Drivers Layer** | Background execution, logging, error handling, and resilience mechanisms.              |

---

## **3. Project Structure**

```plaintext
📂 AutoConveyor/
│── 📂 src/                      # Source Code
│   │── 📂 application/           # Application Layer
│   │   │── main.py              # Entry point of the application
│   │   │── config_manager.py     # Handles system configurations
│   │
│   │── 📂 domain/                # Business Logic (Video Processing)
│   │   │── processor.py          # Video processing with DaVinci Resolve API
│   │   │── uploader.py           # YouTube upload logic
│   │   │── progress_tracker.py   # Tracks job progress
│   │   │── color_grader.py       # AI-based Scene-Based Color Grading
│   │   │── metadata_manager.py   # Automated tagging & metadata enrichment
│   │
│   │── 📂 infrastructure/        # External System Interfaces
│   │   │── file_watcher.py       # Monitors new video files
│   │   │── resolve_api.py        # Connects to DaVinci Resolve
│   │   │── youtube_api.py        # Manages YouTube API integration
│   │
│   │── 📂 framework/             # System Execution and Logging
│   │   │── background_worker.py  # Runs as a daemon process
│   │   │── error_handler.py      # Handles exceptions & retries
│   │   │── checkpoint_manager.py # Checkpoint system for recovery
│   │   │── logger.py             # Logs system activities
│
│── 📂 config/                    # Configuration Files
│   │── config.json               # User-defined settings
│
│── 📂 logs/                      # Logging directory
│   │── process_log.log           # Log file
│
│── 📂 docs/                      # Documentation
│   │── Architecture_Document.md  # This file
│   │── README.md                 # GitHub ReadMe
│
│── requirements.txt              # Python dependencies
│── setup.py                      # Installation script
│── .gitignore                    # Ignore unnecessary files
```

---

## **4. System Components & Responsibilities**

### **4.1 Application Layer**

- **Manages configurations** and **executes workflows**.
- **Reads user settings** from `config.json`.
- Acts as the **entry point** for system execution.

### **4.2 Domain Layer**

- Implements **video processing logic** using **DaVinci Resolve API**.
- Tracks **processing progress** and **upload status**.
- Handles **business rules** related to video rendering and metadata.
- **Scene-Based Auto Color Grading**: Uses AI-based detection to adjust color grading per scene.
- **Metadata Enrichment & Auto-Tagging**: Extracts relevant information for optimized YouTube discoverability.

### **4.3 Infrastructure Layer**

- **Monitors directories** for new videos.
- **Interacts with external APIs** (DaVinci Resolve, YouTube).
- **Handles external dependencies** like `watchdog`, `googleapiclient`, etc.

### **4.4 Framework & Drivers Layer**

- Runs as a **daemon/background process**.
- Implements **error handling, retry mechanisms, and logging**.
- **Multithreading Support**: Enables parallel video processing for efficiency.
- **Checkpoint System**: Saves progress and resumes jobs after failures.

---

## **5. Configuration & Adaptability**

AutoConveyor is **easily configurable** via a `config.json` file:

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

- **Auto-adapts** to newer versions of DaVinci Resolve.
- **Future-ready design** allows for easy plugin integration.

---

## **6. Included Features & Scalability**

### **6.1 Features Implemented in This Version**

✔ **Multithreading** – Support for multiple concurrent video tasks.  
✔ **Checkpoint System** – Resume processing after failures or interruptions.  
✔ **Automated Tagging & Metadata Enrichment** – Enhances YouTube discoverability.  
✔ **Scene-Based Auto Color Grading** – AI-based adjustments per scene.

### **6.2 Future Enhancements**

🚀 **Parallel Processing Across Machines** – Distribute tasks across multiple nodes.  
🚀 **Web Dashboard** – Live tracking of processing & upload status.  
🚀 **Batch Upload Scheduling** – Optimize YouTube posting for engagement.  
🚀 **Cloud Integration** – Deploy processing in **AWS/GCP/Azure** for enhanced performance.  
🚀 **Containerization** – Use **Docker** for easy deployment across platforms.

---

## **7. Conclusion**

AutoConveyor is built to be a **robust, scalable, and future-ready solution** for **automated video processing**. Its modular architecture ensures easy **maintenance, adaptability, and expansion** for future needs.
