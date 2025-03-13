import pygame
import sys
import vlc
import random
import time

# Initialize pygame
pygame.init()

# Window settings (set to windowed by default)
screen = pygame.display.set_mode((800, 600))  # Windowed mode by default
pygame.display.set_caption("VLC Video Player")

# VLC Media Player Setup
player = vlc.MediaPlayer()

# Get the window handle for the Pygame window (Windows only)
if sys.platform == "win32":
    hwnd = pygame.display.get_wm_info()["window"]
    player.set_hwnd(hwnd)  # Link VLC to the Pygame window

# Load video file using VLC
video_path = 'Monty_Python_Intermission-4K_HD.mp4'  # Replace with your video file path
media = vlc.Media(video_path)
player.set_media(media)

# Play settings
min_time_between_triggers = 30  # Minimum time (seconds) between video triggers
max_time_between_triggers = 600  # Maximum time (seconds) between video triggers
max_play_duration = 5  # Max duration (seconds) to play each video
play_chance = 1.0  # Probability (0 to 1) that the video will play in each trigger cycle
fullscreen_chance = 1.0  # 100% chance of going fullscreen when triggered
running = True

# Control loop for video playback
while running:
    # Randomly trigger fullscreen mode with a set chance (100% in this case)
    if random.random() < fullscreen_chance:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Switch to fullscreen
        print("Fullscreen mode activated.")

    # Randomly trigger video playback based on chance
    trigger_delay = random.uniform(min_time_between_triggers, max_time_between_triggers)
    time.sleep(trigger_delay)  # Wait for the random trigger time

    # Decide if video should play based on play_chance
    if random.random() < play_chance:
        print(f"Playing video after {trigger_delay:.2f} seconds.")
        player.play()

        # Play the video for a set amount of time
        time.sleep(max_play_duration)  # Video will play for `max_play_duration` seconds

        # Stop video playback after max_play_duration
        player.stop()
        print(f"Video stopped after {max_play_duration} seconds.")
        
        # Return to windowed mode after the video finishes
        screen = pygame.display.set_mode((800, 600))  # Switch back to windowed mode
        print("Windowed mode activated.")

    # Event handling for quitting the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.stop()  # Stop the video playback
            pygame.quit()
            sys.exit()

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
