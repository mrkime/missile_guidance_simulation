import matplotlib.pyplot as plt
import numpy as np


class SimulationPlot:
    def __init__(self):
        plt.ion()  # Enable interactive mode
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.setup_plot()

    def setup_plot(self):
        self.ax.clear()
        self.ax.set_xlim(-10, 150)
        self.ax.set_ylim(-10, 150)
        self.ax.grid(True)
        self.ax.set_title("Missile Guidance Simulation")
        self.ax.set_xlabel("X Position")
        self.ax.set_ylabel("Y Position")

        # Create missile trajectory line with dots at each position
        self.missile_plot, = self.ax.plot([], [], 'bo-', label='Missile',
                                          markersize=6, linewidth=1)
        self.current_pos, = self.ax.plot([], [], 'ro', label='Current Position',
                                         markersize=8)
        self.target_plot, = self.ax.plot([], [], 'r*', label='Target',
                                         markersize=10)
        self.ax.legend()
        plt.tight_layout()

    def update(self, missile_trajectory, target_pos):
        if len(missile_trajectory) > 0:
            trajectory = np.array(missile_trajectory)

            # Update missile trajectory with line
            self.missile_plot.set_data(trajectory[:, 0], trajectory[:, 1])

            # Update current position with larger marker
            current_pos = trajectory[-1]
            self.current_pos.set_data([current_pos[0]], [current_pos[1]])

            # Update target position
            self.target_plot.set_data([target_pos[0]], [target_pos[1]])

            # Ensure the plot refreshes properly
            self.fig.canvas.flush_events()
            plt.pause(0.01)