from typing import Sequence


def projectile_motion(
    t: float,
    state: Sequence[float],
    g: float,
) -> list[float]:
    """
    2D projectile motion model without aerodynamic drag.

    State variables:
    - x: horizontal position [m]
    - y: vertical position [m]
    - vx: horizontal velocity [m/s]
    - vy: vertical velocity [m/s]
    """
    x, y, vx, vy = state

    dx_dt = vx
    dy_dt = vy
    dvx_dt = 0.0
    dvy_dt = -g

    return [dx_dt, dy_dt, dvx_dt, dvy_dt]