from engine.engine import Engine

class CapuletEngine(Engine):
    """Engine implementation for Capulet."""
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        """Check if CapuletEngine needs service."""
        return self.current_mileage - self.last_service_mileage > 30000