## "Indeed, Allah will not change the condition of a people until they change what is in themselves." - Quran 13:11

# 🎯 Motivational Reminder System

A Python-based accountability tool that plays motivational audio (Quran ayats, speeches, etc.) when certain trigger words are detected in your typing. The system blocks all keyboard and mouse input until the audio finishes playing, ensuring you listen to the complete reminder.

## ⚠️ Disclaimer

This tool is designed for personal accountability and self-improvement. Use it responsibly and ensure it aligns with your personal goals and values.

## ✨ Features

- 🔍 Real-time keyboard monitoring
- 🔒 Complete input blocking during audio playback (keyboard + mouse)
- 🎵 Plays random motivational audio from your collection
- ⏱️ Configurable cooldown period to prevent spam
- 👻 Runs completely hidden in the background
- 🚀 Auto-starts on Windows boot
- 🛡️ Runs with administrator privileges automatically

## 📋 Requirements

- Windows 10/11
- Python 3.8 or higher
- Administrator privileges

## 🔧 Installation

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Complete the installation

### Step 2: Install Required Libraries

Open Command Prompt and run:

```bash
pip install pynput pygame
```

### Step 3: Download the Script

1. Clone this repository or download the files:
   - `reminder.py` - Main script
   - `start_reminder.bat` - Launcher script
   - `invisible_starter.vbs` - Hidden runner

2. Create the following folder structure:

```
MotivationalReminder/
├── reminder.py
├── start_reminder.bat
├── invisible_starter.vbs
└── motivational_audio/
    ├── quran_ayat_1.mp3
    ├── quran_ayat_2.mp3
    ├── motivational_speech_1.mp3
    └── motivational_speech_2.mp3
```

### Step 4: Add Your Audio Files

1. Create a folder named `motivational_audio` in the same directory as the script
2. Add your MP3/WAV audio files (Quran recitations, motivational speeches, etc.)
3. Supported formats: `.mp3`, `.wav`, `.ogg`

## 🚀 Usage

### Manual Run (Testing)

1. Open Command Prompt as Administrator
2. Navigate to your script directory
3. Run: `python reminder.py`

### Automated Hidden Startup

#### Method 1: Task Scheduler (Recommended)

1. **Open Task Scheduler:**
   - Press `Win + R`
   - Type `taskschd.msc`
   - Press Enter

2. **Create New Task:**
   - Click "Create Task..." (not "Create Basic Task")
   - Name: `Motivational Reminder`

3. **General Tab:**
   - ✅ Check "Run with highest privileges"
   - Configure for: Windows 10

4. **Triggers Tab:**
   - Click "New..."
   - Begin the task: "At log on"
   - ✅ Check "Enabled"
   - Click OK

5. **Actions Tab:**
   - Click "New..."
   - Action: "Start a program"
   - Program/script: Browse and select `invisible_starter.vbs`
   - Click OK

6. **Conditions Tab:**
   - ❌ Uncheck "Start the task only if the computer is on AC power"

7. **Settings Tab:**
   - ✅ Check "Allow task to be run on demand"
   - ✅ Check "Run task as soon as possible after a scheduled start is missed"

8. Click OK to save

#### Method 2: Startup Folder (Alternative)

1. Press `Win + R`, type `shell:startup`, press Enter
2. Create a shortcut to `invisible_starter.vbs`
3. Move the shortcut to the Startup folder

## ⚙️ Configuration

### Editing Trigger Words

Open `reminder.py` and modify the `banned_words` set:

```python
banned_words = {
    "word1", "word2", "word3",
    # Add or remove words as needed
}
```

### Changing Cooldown Period

Find and modify this line in `reminder.py`:

```python
COOLDOWN = 30  # Change to desired seconds
```

### Custom Audio Folder Path

Change the audio folder location:

```python
AUDIO_FOLDER = "motivational_audio"  # Change to your path
# Or use absolute path:
AUDIO_FOLDER = r"C:\Users\YourName\MyAudios"
```

## 📁 File Descriptions

### `reminder.py`
Main Python script that:
- Monitors keyboard input
- Detects trigger words
- Blocks input during playback
- Plays random audio files

### `start_reminder.bat`
Batch file that:
- Navigates to script directory
- Launches Python with correct path
- Useful for troubleshooting

Example content:
```batch
@echo off
cd /d "C:\Users\YourName\Desktop\MotivationalReminder"
C:\msys64\mingw64\bin\python.exe reminder.py
pause
```

### `invisible_starter.vbs`
VBScript that:
- Runs the batch file completely hidden
- No console window appears

Example content:
```vbscript
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run """C:\Users\YourName\Desktop\MotivationalReminder\start_reminder.bat""", 0, False
```

## 🛑 Stopping the Script

### From Task Manager:
1. Open Task Manager (`Ctrl + Shift + Esc`)
2. Go to "Details" tab
3. Find `python.exe`
4. Right-click → End Task

### From Task Scheduler:
1. Open Task Scheduler
2. Find "Motivational Reminder"
3. Right-click → Disable (or Delete)

## 🐛 Troubleshooting

### Audio folder not found
- Ensure `motivational_audio` folder exists in the same directory as `reminder.py`
- Check folder name spelling (case-sensitive)
- Verify audio files are in supported formats (MP3/WAV/OGG)

### Input blocking doesn't work
- Script must run with Administrator privileges
- Check Task Scheduler "Run with highest privileges" is checked

### Script doesn't start on boot
- Verify Task Scheduler task exists and is enabled
- Check "Last Run Result" in Task Scheduler (should be `0x0` for success)
- Test by right-clicking task → "Run"

### Python not found error
- Run `where python` in Command Prompt
- Update `start_reminder.bat` with the correct Python path
- Ensure Python is added to PATH during installation

### No audio plays
- Check audio files are not corrupted
- Try playing audio files manually in Windows Media Player
- Verify pygame is installed: `pip show pygame`

## 🔒 Security & Privacy

- All processing happens locally on your machine
- No data is sent to external servers
- No internet connection required
- Keystrokes are only monitored, never logged or stored
- Open source - you can review all code

## ⚖️ License

This project is provided as-is for personal use. Feel free to modify and adapt it to your needs.

## 🤲 Purpose

This tool is designed to help individuals stay accountable to their values and goals. It serves as a personal reminder system to redirect attention toward positive content when triggered.

> "Indeed, Allah will not change the condition of a people until they change what is in themselves." - Quran 13:11

## 🙏 Credits

Created for personal accountability and self-improvement purposes.

## 📞 Support

If you encounter issues:
1. Check the Troubleshooting section above
2. Verify all installation steps were completed
3. Test each component individually (Python → BAT → VBS)

---

**Remember:** This tool is most effective when combined with:
- Clear personal goals
- Accountability partners
- Additional content filtering (DNS, browser extensions)
- Genuine commitment to change

May this tool help you on your journey of self-improvement! 🌟