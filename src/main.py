import os
import sys

def about():
    ProjectName = "AutoConveyor"
    ProjectVersion = "1.0.1"
    ProjectAuthor = "Sathya S Sheelan"
    ProjectDescription = "Automation for Streamlining Video processing via Davinci Resolve to Youtube"
    ProjectPlatform = str(sys.platform).capitalize()
    ascii_help = f"""
🚀 {ProjectName} {ProjectVersion} | {ProjectPlatform}
    {ProjectDescription}

    A project developed by {ProjectAuthor}.
    Features:
    ✅ Automated Video Processing | ✅ AI-Powered Enhancements
    ✅ YouTube Upload Automation | ✅ Multithreading Support
    ✅ Checkpoint System | ✅ Centralized Logging & Error Handling

    License: MIT License
    To know more about the project, visit the GitHub Repository.
    🔗 GitHub Repository: https://github.com/sathya-py/AutoConveyor
    """


    os.system("cls")    
    sys.stdout.write(f"\x1b]2;{ProjectName} Version: {ProjectVersion}\x07")
    print(ascii_help)

def main():
    about()
    sys.exit()

if __name__ == "__main__":
    main()