class Engine:
    """Base class for engine."""
    def needs_service(self) -> bool:
        """Check if the engine needs service."""
        raise NotImplementedError("Engine subclass must implement needs_service()")