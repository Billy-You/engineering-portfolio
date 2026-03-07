from pathlib import Path

import matplotlib.pyplot as plt

from simulation import run_simulation


def plot_results() -> None:
    """
    Run simulation, plot height and velocity versus time,
    and save the figure to the results directory.
    """
    result = run_simulation(h0=20.0, t_end=10.0)

    t = result["t"]
    h = result["y"][0]
    v = result["y"][1]

    project_root = Path(__file__).resolve().parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "free_fall_base_case.png"

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    axes[0].plot(t, h, label="Height h(t)")
    axes[0].set_title("Height vs Time")
    axes[0].set_xlabel("Time [s]")
    axes[0].set_ylabel("Height [m]")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(t, v, label="Downward velocity v(t)")
    axes[1].set_title("Downward Velocity vs Time")
    axes[1].set_xlabel("Time [s]")
    axes[1].set_ylabel("Velocity [m/s]")
    axes[1].grid(True)
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

    print(f"Figure saved to: {output_path}")

    plt.show()


if __name__ == "__main__":
    plot_results()