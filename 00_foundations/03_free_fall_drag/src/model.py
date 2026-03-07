from typing import Sequence


def free_fall_with_drag(
    t: float,
    state: Sequence[float],
    m: float,
    g: float,
    rho: float,
    cd: float,
    area: float,
) -> list[float]:
    """
    1D vertical free-fall model with quadratic aerodynamic drag.

    State variables:
    - h: height above ground [m]
    - v: downward velocity [m/s]

    Positive velocity means downward motion.
    """

    h, v = state

    drag_force = 0.5 * rho * cd * area * v**2

    dh_dt = -v
    dv_dt = g - drag_force / m

    return [dh_dt, dv_dt]