from engine.engine import Engine

class SternmanEngine(Engine):
    """Engine implementation for Sternman."""
    def __init__(self, warning_light: bool):
        self.warning_light = warning_light

    def needs_service(self) -> bool:
        """Check if SternmanEngine needs service."""
        return self.warning_light