class Battery:
    """Base class for battery."""
    def needs_service(self) -> bool:
        """Check if the battery needs service."""
        raise NotImplementedError("Battery subclass must implement needs_service()")