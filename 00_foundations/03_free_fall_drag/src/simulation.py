import numpy as np
from scipy.integrate import solve_ivp

from model import free_fall_with_drag


def hit_ground_event(
    t: float,
    state: list[float],
    m: float,
    g: float,
    rho: float,
    cd: float,
    area: float,
) -> float:
    """
    Event function to stop integration when the object reaches the ground.

    The event is triggered when height h = 0.
    """
    h, _ = state
    return h


hit_ground_event.terminal = True
hit_ground_event.direction = -1


def run_simulation(
    m: float = 80.0,
    g: float = 9.81,
    rho: float = 1.225,
    cd: float = 1.0,
    area: float = 0.7,
    h0: float = 1000.0,
    v0: float = 0.0,
    t_end: float = 60.0,
    num_points: int = 1000,
):
    """
    Run a free-fall simulation with quadratic drag.

    The integration stops automatically when the object reaches the ground.
    If an impact event occurs, the exact impact point is appended to the output.
    """
    initial_state = [h0, v0]
    t_eval = np.linspace(0.0, t_end, num_points)

    solution = solve_ivp(
        fun=free_fall_with_drag,
        t_span=(0.0, t_end),
        y0=initial_state,
        t_eval=t_eval,
        args=(m, g, rho, cd, area),
        events=hit_ground_event,
    )

    t = solution.t.copy()
    y = solution.y.copy()

    impact_detected = solution.t_events[0].size > 0

    if impact_detected:
        impact_time = solution.t_events[0][0]
        impact_state = solution.y_events[0][0]

        last_time_is_impact = np.isclose(t[-1], impact_time)

        if not last_time_is_impact:
            t = np.append(t, impact_time)
            y = np.column_stack((y, impact_state))

    return {
        "t": t,
        "y": y,
        "raw_solution": solution,
        "impact_detected": impact_detected,
        "impact_time": solution.t_events[0][0] if impact_detected else None,
        "impact_state": solution.y_events[0][0] if impact_detected else None,
    }


if __name__ == "__main__":
    result = run_simulation(h0=20.0, t_end=10.0)

    t = result["t"]
    y = result["y"]

    h = y[0]
    v = y[1]

    raw_solution = result["raw_solution"]

    print(f"Simulation status: {raw_solution.message}")
    print(f"Final time: {t[-1]:.2f} s")
    print(f"Final height: {h[-1]:.2f} m")
    print(f"Final velocity: {v[-1]:.2f} m/s")

    if result["impact_detected"]:
        impact_time = result["impact_time"]
        impact_height = result["impact_state"][0]
        impact_velocity = result["impact_state"][1]

        print("\nImpact detected:")
        print(f"Impact time: {impact_time:.2f} s")
        print(f"Impact height: {impact_height:.2f} m")
        print(f"Impact velocity: {impact_velocity:.2f} m/s")