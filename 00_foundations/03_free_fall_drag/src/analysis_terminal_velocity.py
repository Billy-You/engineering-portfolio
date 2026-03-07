from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from simulation import run_simulation


def terminal_velocity(m: float, g: float, rho: float, cd: float, area: float) -> float:
    return np.sqrt((2.0 * m * g) / (rho * cd * area))


def time_to_reach_fraction(
    t: np.ndarray,
    v: np.ndarray,
    v_target: float,
    fraction: float = 0.99,
):
    threshold = fraction * v_target
    indices = np.where(v >= threshold)[0]

    if len(indices) == 0:
        return None, threshold

    first_idx = indices[0]
    return t[first_idx], threshold


def analyze_case(
    name: str,
    m: float,
    g: float,
    rho: float,
    cd: float,
    area: float,
):
    result = run_simulation(
        m=m,
        g=g,
        rho=rho,
        cd=cd,
        area=area,
        h0=1000.0,
        v0=0.0,
        t_end=60.0,
        num_points=1500,
    )

    t = result["t"]
    h = result["y"][0]
    v = result["y"][1]

    v_t = terminal_velocity(m, g, rho, cd, area)
    t_99, v_99 = time_to_reach_fraction(t, v, v_t, fraction=0.99)

    print(f"\n--- {name} ---")
    print(f"Mass: {m:.3f} kg")
    print(f"Area: {area:.4f} m^2")
    print(f"Cd: {cd:.3f}")
    print(f"Theoretical terminal velocity: {v_t:.2f} m/s")
    print(f"Final simulated velocity: {v[-1]:.2f} m/s")

    if result["impact_detected"]:
        print(f"Impact time: {result['impact_time']:.2f} s")

    if t_99 is not None:
        print(f"Time to reach 99% of terminal velocity: {t_99:.2f} s")
    else:
        print("99% of terminal velocity was not reached in the simulated interval.")

    return {
        "name": name,
        "t": t,
        "h": h,
        "v": v,
        "v_t": v_t,
        "t_99": t_99,
        "v_99": v_99,
        "m": m,
        "cd": cd,
        "area": area,
    }


def plot_comparison(cases) -> None:
    project_root = Path(__file__).resolve().parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "terminal_velocity_comparison.png"

    plt.figure(figsize=(11, 7))

    for case in cases:
        label_curve = f'{case["name"]}'
        label_terminal = f'{case["name"]} - v_t = {case["v_t"]:.1f} m/s'

        plt.plot(case["t"], case["v"], label=label_curve)
        plt.axhline(case["v_t"], linestyle="--", label=label_terminal)

        if case["t_99"] is not None:
            plt.scatter(case["t_99"], case["v_99"], marker="o")
            plt.text(
                case["t_99"],
                case["v_99"],
                f'  {case["t_99"]:.1f}s',
                fontsize=9,
            )

    plt.title("Velocity vs Time — Terminal Velocity Comparison")
    plt.xlabel("Time [s]")
    plt.ylabel("Downward Velocity [m/s]")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path, dpi=300)
    print(f"\nFigure saved to: {output_path}")

    plt.show()


def main():
    g = 9.81
    rho = 1.225

    cases = [
        analyze_case("Human", 80.0, g, rho, 1.0, 0.7),
        analyze_case("Squirrel compact", 0.6, g, rho, 1.0, 0.015),
        analyze_case("Squirrel open posture", 0.6, g, rho, 1.1, 0.025),
        analyze_case("Dense compact object", 5.0, g, rho, 0.47, 0.008),
    ]

    plot_comparison(cases)


if __name__ == "__main__":
    main()