# **AutoConveyor – Final Architecture Document**

---

## **1. Overview**

**AutoConveyor** is an **automated video processing pipeline** that integrates with **DaVinci Resolve 19+** for **timeline creation, editing, color grading, and rendering**, followed by **automated YouTube uploads** with **AI-driven metadata enrichment**.

This system is built using a **Hybrid Modular-Layered Architecture**, combining:

- **Modular Structure** for independent, replaceable components (e.g., `monitor`, `processing`, `upload`).
- **Layered Separation** inside modules to ensure clean-code, maintainability, and scalability.
- **Centralized Logging, Error Handling & Testing** to ensure reliability and debugging efficiency.
- **Scripts for automation** to streamline execution and maintenance.

---

## **2. Hybrid Architecture Design**

Each **module** follows a **layered design** internally while remaining loosely coupled with other modules.

### **2.1 Modules**

| **Module**       | **Responsibility**                                                               |
| ---------------- | -------------------------------------------------------------------------------- |
| **Monitor**      | Watches directories, detects new files, triggers processing.                     |
| **Processing**   | Handles timeline creation, editing, rendering via DaVinci Resolve API.           |
| **AI Engine**    | Enhances videos with **scene detection, auto color grading, metadata tagging**.  |
| **Upload**       | Automates YouTube uploads, manages retries, and schedules posts.                 |
| **Framework**    | Manages **logging, error handling, multithreading, checkpointing, and testing**. |
| **Config & CLI** | Handles **user configuration, CLI commands, and API interactions**.              |
| **Scripts**      | Automation scripts for batch processing, cleanup, and system maintenance.        |

---

### **2.2 Layered Structure inside Modules**

Each module follows a **three-layered structure**:

| **Layer**                | **Responsibility**                                                            |
| ------------------------ | ----------------------------------------------------------------------------- |
| **Application Layer**    | Controls execution, workflows, and high-level interactions.                   |
| **Domain Layer**         | Contains business logic (e.g., video processing, AI tagging).                 |
| **Infrastructure Layer** | Manages external integrations (DaVinci Resolve API, YouTube API, filesystem). |

---

## **3. Project Structure**

```plaintext
📂 AutoConveyor/
│── 📂 src/                      # Source Code
│   │── 📂 monitor/               # File Monitoring Module
│   │   │── application/
│   │   │   │── monitor_service.py   # Starts and manages monitoring process
│   │   │── domain/
│   │   │   │── file_tracker.py      # Detects new files, triggers processing
│   │   │── infrastructure/
│   │   │   │── fs_watcher.py        # Uses watchdog to track file system events
│   │
│   │── 📂 processing/            # Video Processing Module
│   │   │── application/
│   │   │   │── process_manager.py   # Manages video processing workflow
│   │   │── domain/
│   │   │   │── resolve_editor.py    # Handles timeline, editing, and rendering
│   │   │── infrastructure/
│   │   │   │── resolve_api.py       # Interface with DaVinci Resolve API
│   │
│   │── 📂 ai_engine/              # AI Enhancements Module
│   │   │── application/
│   │   │   │── ai_service.py      # AI-driven operations manager
│   │   │── domain/
│   │   │   │── scene_detector.py  # Scene change detection
│   │   │   │── color_grader.py    # Auto color grading logic
│   │   │── infrastructure/
│   │   │   │── ai_models.py       # Pre-trained models for video analysis
│   │
│   │── 📂 upload/                # YouTube Upload Module
│   │   │── application/
│   │   │   │── upload_manager.py   # Manages upload process
│   │   │── domain/
│   │   │   │── metadata_generator.py  # Creates video titles, descriptions, tags
│   │   │── infrastructure/
│   │   │   │── youtube_api.py     # Handles API interactions
│   │
│   │── 📂 framework/              # System Execution, Logging, Errors & Testing
│   │   │── logger.py              # Centralized logging
│   │   │── error_handler.py       # Exception handling, retry mechanisms
│   │   │── checkpoint_manager.py  # Failure recovery checkpoints
│   │   │── background_worker.py   # Manages multi-threading
│   │   │── test_runner.py         # Runs all unit and integration tests
│   │
│   │── 📂 config/                 # Configuration & CLI
│   │   │── config_manager.py      # Reads and writes config settings
│   │   │── cli.py                 # Command-line interface
│
│── 📂 scripts/                    # Automation Scripts
│   │── cleanup.py                 # Deletes old files & logs
│   │── batch_process.py           # Automates batch processing
│   │── reprocess_failed.py        # Re-runs failed jobs
│
│── 📂 logs/                       # Logs & Error Tracking
│   │── auto_conveyor.log          # Main system logs
│   │── error.log                  # Error logs
│   │── test_reports.log           # Logs test results
│
│── 📂 tests/                      # Unit & Integration Testing
│   │── test_monitor.py            # Tests monitoring logic
│   │── test_processing.py         # Tests video processing
│   │── test_ai_engine.py          # Tests AI-based features
│   │── test_upload.py             # Tests YouTube uploads
│
│── 📂 docs/                       # Documentation
│   │── Architecture.md            # This document
│   │── Naming_Conventions.md      # Naming conventions guide
│   │── README.md                  # Project overview
│
│── requirements.txt               # Python dependencies
│── setup.py                        # Installation script
│── .gitignore                      # Ignore unnecessary files
```

---

## **4. Centralized Logging & Error Handling**

### **4.1 Logging System**

A centralized logging system captures:  
✅ **INFO logs** – General application workflow logs.  
✅ **ERROR logs** – Captures critical failures.  
✅ **DEBUG logs** – Useful for developers.  
✅ **TEST logs** – Stores unit test results.

Example Log Entry (`auto_conveyor.log`):

```plaintext
[2025-03-13 14:45:32] INFO - New video detected: sample_video.mp4
[2025-03-13 14:45:35] ERROR - Failed to process video: sample_video.mp4 - TimeoutError
[2025-03-13 14:45:37] DEBUG - Retrying video processing...
```

---

### **4.2 Error Handling Strategy**

1️⃣ **Try-Catch Blocks** – Prevents system crashes.  
2️⃣ **Automatic Retries** – Handles temporary failures.  
3️⃣ **Failsafe Mode** – Skips problematic videos and continues processing.  
4️⃣ **Alerts & Logs** – Saves issues to `error.log` for later debugging.

---

## **5. Automated Testing**

✅ **Unit Tests** – Test individual functions (e.g., scene detection).  
✅ **Integration Tests** – Ensure modules work together (e.g., full workflow).  
✅ **Test Reports** – Results stored in `logs/test_reports.log`.

---

## **6. Automation Scripts**

📌 `cleanup.py` – Deletes old processed videos and logs to free space.  
📌 `batch_process.py` – Automates batch processing of multiple files.  
📌 `reprocess_failed.py` – Detects failed jobs and reattempts processing.

---

## **7. Conclusion**

AutoConveyor now has **a complete hybrid modular-layered architecture** with:  
✔ **Scalability** for new features.  
✔ **Reliability** via logging, error handling, and retry mechanisms.  
✔ **Automation** for streamlined workflow and maintenance.

This **final architecture** ensures that AutoConveyor is **production-ready, future-proof, and adaptable** 🚀.
