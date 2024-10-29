# Missile Guidance Simulation

A Python-based simulation of a missile guidance system featuring real-time plotting with Matplotlib, text-to-speech (TTS) updates for distance announcements, and color-coded console output for a more interactive experience.

## Features
- **Missile Guidance Simulation**: Calculates and updates the missile's trajectory toward a moving target using proportional navigation algorithms.
- **Real-Time Visualization**: Animates the missile and target's positions on a 2D plot, showcasing the missile's path.
- **Text-to-Speech (TTS) Announcements**: Announces the missile's distance to the target at regular intervals for an immersive experience.
- **Color-Coded Console Output**: Uses color to distinguish different types of messages, including missile position, target position, and status updates.

## Project Structure
- `main.py`: Runs the main simulation loop, initializing the missile guidance and handling updates.
- `simulation.py`: Contains the `MissileSimulation` class, managing the core simulation logic, including position updates and proximity calculations.
- `entities.py`: Defines the main entities, such as `Missile`, `Target`, and `Obstacle`, with their respective properties and methods.
- `guidance.py`: Implements guidance algorithms and helper functions for calculating heading and updating positions.
- `visualization.py`: Manages real-time plotting with Matplotlib to visualize the missile and target positions on a 2D grid.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/missile_guidance_simulation.git
   cd missile_guidance_simulation
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Make sure `requirements.txt` includes:
   - `matplotlib`
   - `pyttsx3`
   - `colorama`

## Usage

Run the main simulation by executing:
```bash
python src/main.py
```

This will initialize the missile guidance simulation, animate the missile’s progress, and provide real-time updates through text-to-speech and console output.

## Customization

- **Adjust Simulation Parameters**: Modify parameters like speed, heading, or target position in `simulation.py` to customize the simulation.
- **Change TTS Voice**: To set a specific TTS voice, edit the `voice` property in `main.py` or `simulation.py` based on available voices on your system.

## Example Output

Console output may look like this:
```plaintext
Time: 5.4s
Missile Position: (12.4, 30.2) [BLUE]
Target Position: (14.9, 35.6) [GREEN]
Distance to Target: 5.1m [YELLOW]
Status: Near obstacle, adjusting course [RED]
```

## Requirements
- **Python 3.8 or later**
- Libraries: `matplotlib`, `pyttsx3`, `colorama`

## Troubleshooting
- **Voice Selection**: If the desired voice isn’t available, list available voices with `pyttsx3` and set one manually.
- **Matplotlib Plotting**: If real-time animation isn’t smooth, try reducing the frame rate in `visualization.py`.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Author
Developed by [Andrew Kime](https://github.com/mrkime)
