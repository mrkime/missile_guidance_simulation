from simulation import MissileSimulation
import matplotlib.pyplot as plt

def main():
    sim = MissileSimulation()
    try:
        while True:
            if not sim.run_step(0.1):  # Smaller time step for smoother animation
                break
    except KeyboardInterrupt:
        print("\nSimulation ended by user")
    finally:
        plt.close('all')

if __name__ == "__main__":
    main()