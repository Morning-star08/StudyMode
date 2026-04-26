"""
Run this ONCE to generate all study mode voice files.
"""
import asyncio
import edge_tts
import os

VOICE      = "en-US-AriaNeural"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "study_voices")
os.makedirs(OUTPUT_DIR, exist_ok=True)

LINES = {
    # Start phrases
    "start_0": "Alright sir, let's get to work.",
    "start_1": "Study mode activated. Let's go Krish.",
    "start_2": "Time to focus sir. You've got this.",
    "start_3": "Let's make this session count, sir.",
    # Pomodoro break
    "break":   "Great work sir. Take a five minute break. You earned it.",
    "resume":  "Break's over sir. Back to work. Let's go.",
    # End phrases by mood
    "end_crushed":   "Outstanding session sir. You absolutely crushed it today.",
    "end_okay":      "Good work sir. Every session counts. Keep going.",
    "end_struggled": "Rest up sir. Hard days build the foundation. Tomorrow is a new day.",
}

async def generate():
    total = len(LINES)
    for i,(name,text) in enumerate(LINES.items(),1):
        path = os.path.join(OUTPUT_DIR, f"{name}.mp3")
        if os.path.exists(path):
            print(f"[{i}/{total}] Skipping {name} — already exists")
            continue
        print(f"[{i}/{total}] Generating: {text}")
        c = edge_tts.Communicate(text, voice=VOICE, rate="-5%", volume="+10%")
        await c.save(path)
        print(f"           Saved → {name}.mp3")

asyncio.run(generate())
print("\n✅ All study voice files ready!")