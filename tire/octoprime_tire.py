from tire.tire import Tire

class OctoprimeTire(Tire):
    """Octoprime tire."""
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_replacement(self) -> bool:
        """Check if Octoprime tire needs replacement."""
        sum_wear = sum(self.tire_wear)
        return sum_wear >= 3.0