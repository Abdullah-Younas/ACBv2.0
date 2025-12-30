from pynput import keyboard
import os
import random
import threading
from pygame import mixer
import time
import ctypes

# Initialize audio mixer
mixer.init()

# Windows API for blocking input
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

is_audio_playing = False

# Full words to trigger reminder
banned_words = {
    "porn", "sex", "tits", "boobs", "ass", "ntr", "milf", "hentai",
    "fap haven", "aunt hina", "princess peach", "force", "comic", 
    "damp lips", "spankbang", "plainprxy", "plainproxy", "jill valentine", 
    "3d porn", "porn comic", "brutality", "chuhai", "hung", "yamato", 
    "valentine", "jill", "zombie porn", "cartoonporn", "pln prxy", 
    "proxy", "prxy", "big boobs", "huge ass", "skylar vox", "alexa croft", 
    "porn comics", "xxx", "9xbddy", "9xbuddy", "nsfw"
}

# Path to your audio files folder
AUDIO_FOLDER = r"//"  # Change this to your folder path

typed_buffer = ""
last_trigger_time = 0
COOLDOWN = 30  # Cooldown period in seconds to avoid spam

def get_audio_files():
    """Get all audio files from the folder"""
    if not os.path.exists(AUDIO_FOLDER):
        print(f"[!] Audio folder not found: {AUDIO_FOLDER}")
        print("[!] Please create the folder and add MP3/WAV files")
        return []
    
    audio_files = [f for f in os.listdir(AUDIO_FOLDER) 
                   if f.endswith(('.mp3', '.wav', '.ogg'))]
    return [os.path.join(AUDIO_FOLDER, f) for f in audio_files]

def check_banned(buffer):
    buffer = buffer.lower()
    words = buffer.replace("\n", " ").split()
    for word in words:
        if word in banned_words:
            return word
    return None

def block_input():
    """Block keyboard and mouse input"""
    ctypes.windll.user32.BlockInput(True)

def unblock_input():
    """Unblock keyboard and mouse input"""
    ctypes.windll.user32.BlockInput(False)

def play_reminder(trigger):
    global last_trigger_time, is_audio_playing
    current_time = time.time()
    
    # Check cooldown to prevent spam
    if current_time - last_trigger_time < COOLDOWN:
        return
    
    # Don't trigger if already playing
    if is_audio_playing:
        return
    
    last_trigger_time = current_time
    is_audio_playing = True
    
    print(f"\n[⚠️] REMINDER TRIGGERED by: {trigger}")
    print("[🔒] Input blocked - Audio must play completely")
    
    audio_files = get_audio_files()
    if not audio_files:
        print("[!] No audio files found. Please add files to:", AUDIO_FOLDER)
        is_audio_playing = False
        return
    
    # Pick random audio file
    audio_file = random.choice(audio_files)
    print(f"[♪] Playing: {os.path.basename(audio_file)}\n")
    
    try:
        # BLOCK ALL INPUT
        block_input()
        
        mixer.music.load(audio_file)
        mixer.music.set_volume(1.0)  # Maximum volume
        mixer.music.play()
        
        # Wait for audio to finish - cannot be interrupted
        while mixer.music.get_busy():
            time.sleep(0.1)
        
        # Small delay before unblocking
        time.sleep(0.5)
        
    except Exception as e:
        print(f"[!] Error playing audio: {e}")
    finally:
        # UNBLOCK INPUT
        unblock_input()
        is_audio_playing = False
        print("[✓] Audio finished - Input restored\n")

def on_press(key):
    global typed_buffer
    
    # Ignore all input while audio is playing
    if is_audio_playing:
        return
    
    try:
        if hasattr(key, 'char') and key.char is not None:
            typed_buffer += key.char
            typed_buffer = typed_buffer[-100:]  # Limit size
            match = check_banned(typed_buffer)
            if match:
                # Run in separate thread so it doesn't block typing
                threading.Thread(target=play_reminder, args=(match,), daemon=True).start()
    except:
        pass
    
    if key == keyboard.Key.space:
        typed_buffer += ' '
    elif key == keyboard.Key.enter:
        typed_buffer += '\n'
    elif key == keyboard.Key.backspace:
        typed_buffer = typed_buffer[:-1]

print("[✓] Motivational reminder system started")
print(f"[i] Audio folder: {AUDIO_FOLDER}")
print(f"[i] Cooldown: {COOLDOWN} seconds")
print("[⚠️] WARNING: When triggered, your input will be BLOCKED until audio finishes")
print("[i] Press Ctrl+C to stop (only works when audio is not playing)\n")

try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\n[!] Stopping...")
    unblock_input()  # Ensure input is unblocked on exit