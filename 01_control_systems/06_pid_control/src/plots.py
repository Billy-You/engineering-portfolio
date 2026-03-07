from pathlib import Path

import matplotlib.pyplot as plt

from simulation import simulate_closed_loop, simulate_open_loop


def plot_results() -> None:
    """
    Plot open-loop and closed-loop PID control results,
    and save the figure to the results directory.
    """
    open_loop = simulate_open_loop(x0=1.0, v0=0.0)
    closed_loop = simulate_closed_loop()

    t_open = open_loop["t"]
    x_open = open_loop["x"]

    t_closed = closed_loop["t"]
    x_closed = closed_loop["x"]
    e_closed = closed_loop["e"]
    u_closed = closed_loop["u"]
    r_closed = closed_loop["reference"]

    gains = closed_loop["gains"]

    project_root = Path(__file__).resolve().parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "pid_control_response.png"

    fig, axes = plt.subplots(3, 1, figsize=(10, 10))

    axes[0].plot(t_open, x_open, label="Open-loop")
    axes[0].plot(t_closed, x_closed, label="Closed-loop (PID)")
    axes[0].plot(t_closed, r_closed, linestyle="--", label="Reference")
    axes[0].set_title("Position Response")
    axes[0].set_xlabel("Time [s]")
    axes[0].set_ylabel("Position [m]")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(t_closed, e_closed, label="Tracking error")
    axes[1].set_title("Error vs Time")
    axes[1].set_xlabel("Time [s]")
    axes[1].set_ylabel("Error [m]")
    axes[1].grid(True)
    axes[1].legend()

    axes[2].plot(t_closed, u_closed, label="Control force u(t)")
    axes[2].set_title(
        f"Control Effort vs Time  |  Kp={gains['kp']}, Ki={gains['ki']}, Kd={gains['kd']}"
    )
    axes[2].set_xlabel("Time [s]")
    axes[2].set_ylabel("Control force [N]")
    axes[2].grid(True)
    axes[2].legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

    print(f"Figure saved to: {output_path}")

    plt.show()


if __name__ == "__main__":
    plot_results()