from tire.tire import Tire

class CarriganTire(Tire):
    """Carrigan tire."""
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_replacement(self) -> bool:
        """Check if Carrigan tire needs replacement."""
        for wear in self.tire_wear:
            if wear >= 0.9:
                return True
            
        return False