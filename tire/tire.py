class Tire:
    """Base class for tires."""
    def needs_replacement(self) -> bool:
        """Check if the tire needs replacement."""
        raise NotImplementedError("Tire subclass must implement needs_replacement()")