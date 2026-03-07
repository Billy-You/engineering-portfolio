class PIDController:
    """
    Basic discrete PID controller.
    """

    def __init__(self, kp: float, ki: float, kd: float) -> None:
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.integral_error = 0.0
        self.previous_error = None

    def reset(self) -> None:
        """
        Reset controller memory.
        """
        self.integral_error = 0.0
        self.previous_error = None

    def compute(self, reference: float, measurement: float, dt: float) -> float:
        """
        Compute PID control action.
        """
        error = reference - measurement
        self.integral_error += error * dt

        if self.previous_error is None:
            derivative_error = 0.0
        else:
            derivative_error = (error - self.previous_error) / dt

        u = (
            self.kp * error
            + self.ki * self.integral_error
            + self.kd * derivative_error
        )

        self.previous_error = error
        return u