from entities import Missile, Target
from guidance import calculate_heading, update_missile_position
from visualization import SimulationPlot
import math
import pyttsx3
from colorama import init, Fore, Style
import threading


class MissileSimulation:
    def __init__(self):
        # Initialize colorama
        init()

        # Initialize entities
        self.missile = Missile(0, 0, 10.0, 45)  # Start with lower speed
        self.target = Target(100, 100, 3.0)
        self.obstacles = []
        self.time_elapsed = 0
        self.max_speed = 50.0  # Maximum speed
        self.acceleration = 5.0  # Speed increase per second

        # Initialize visualization
        self.plot = SimulationPlot()

        # Initialize TTS with male voice
        self.tts_engine = pyttsx3.init()
        voices = self.tts_engine.getProperty('voices')
        # Try to find a male or deeper-sounding voice
        male_voice = next((voice for voice in voices
                          if 'male' in voice.name.lower() or 'baritone' in voice.name.lower()), voices[38])
        self.tts_engine.setProperty('voice', male_voice.id)
        self.tts_engine.setProperty('rate', 130)  # Adjusted rate for a slower, more authoritative tone
        self.tts_engine.setProperty('volume', 1.0)  # Maximize volume for clarity
        self.last_announcement_distance = float('inf')

    def get_distance_to_target(self) -> float:
        """Calculate distance between missile and target"""
        dx = self.target.x - self.missile.x
        dy = self.target.y - self.missile.y
        return math.sqrt(dx * dx + dy * dy)

    def announce_distance(self, distance: float):
        """Announce distance using text-to-speech"""
        if abs(distance - self.last_announcement_distance) >= 10:  # Announce every 10 meters
            self.last_announcement_distance = distance
            announcement = f"{int(distance)} meters to target"
            # Run TTS in a separate thread to avoid blocking
            threading.Thread(target=lambda: self.tts_engine.say(announcement)).start()
            self.tts_engine.runAndWait()

    def run_step(self, time_step: float = 0.2) -> bool:
        """Run one step of the simulation"""
        current_distance = self.get_distance_to_target()

        if current_distance < 1.0:
            print(f"{Fore.GREEN}Target reached!{Style.RESET_ALL}")
            self.tts_engine.say("Target acquired")
            self.tts_engine.runAndWait()
            return False

        # Update missile speed (accelerate over time)
        self.missile.speed = min(
            self.max_speed,
            self.missile.speed + self.acceleration * time_step
        )

        new_heading = calculate_heading(self.missile, self.target)
        update_missile_position(self.missile, new_heading, time_step)
        self.time_elapsed += time_step

        # Update visualization
        self.plot.update(self.missile.trajectory, (self.target.x, self.target.y))

        # Announce distance
        self.announce_distance(current_distance)

        self._print_status()
        return True

    def _print_status(self):
        """Print current simulation status"""
        print(f"\nTime: {Fore.YELLOW}{self.time_elapsed:.1f}s{Style.RESET_ALL}")
        print(f"Missile Position: {Fore.BLUE}({self.missile.x:.1f}, {self.missile.y:.1f}){Style.RESET_ALL}")
        print(f"Target Position: {Fore.GREEN}({self.target.x:.1f}, {self.target.y:.1f}){Style.RESET_ALL}")
        print(f"Distance to target: {Fore.YELLOW}{self.get_distance_to_target():.1f}m{Style.RESET_ALL}")
        print(f"Current Speed: {Fore.CYAN}{self.missile.speed:.1f} units/s{Style.RESET_ALL}")
        print("-" * 40)