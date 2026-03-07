from pathlib import Path

import matplotlib.pyplot as plt

from simulation import run_simulation


def plot_results() -> None:
    """
    Run the projectile simulation, generate plots,
    and save the figure to the results directory.
    """
    result = run_simulation()

    t = result["t"]
    state = result["y"]

    x = state[0]
    y = state[1]
    vx = state[2]
    vy = state[3]

    project_root = Path(__file__).resolve().parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "projectile_base_case.png"

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].plot(x, y, label="Trajectory")
    axes[0, 0].set_title("Projectile Trajectory")
    axes[0, 0].set_xlabel("x [m]")
    axes[0, 0].set_ylabel("y [m]")
    axes[0, 0].grid(True)
    axes[0, 0].legend()

    axes[0, 1].plot(t, x, label="x(t)")
    axes[0, 1].set_title("Horizontal Position vs Time")
    axes[0, 1].set_xlabel("Time [s]")
    axes[0, 1].set_ylabel("x [m]")
    axes[0, 1].grid(True)
    axes[0, 1].legend()

    axes[1, 0].plot(t, y, label="y(t)")
    axes[1, 0].set_title("Vertical Position vs Time")
    axes[1, 0].set_xlabel("Time [s]")
    axes[1, 0].set_ylabel("y [m]")
    axes[1, 0].grid(True)
    axes[1, 0].legend()

    axes[1, 1].plot(t, vy, label="vy(t)")
    axes[1, 1].set_title("Vertical Velocity vs Time")
    axes[1, 1].set_xlabel("Time [s]")
    axes[1, 1].set_ylabel("vy [m/s]")
    axes[1, 1].grid(True)
    axes[1, 1].legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

    print(f"Figure saved to: {output_path}")

    plt.show()


if __name__ == "__main__":
    plot_results()