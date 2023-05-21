"""Resource Class"""

class Resource:
    """
    Resource class that represents resource entities e.g.: main board, PC, etc.
    """
    def __init__(self):
        """
        Initialization
        """
        self.name = None
        self.availability = True

    def set_name(self, name: str):
        """
        set name for resource
        """
        self.name = name

    def get_name(self):
        """
        get name of resource
        """
        return self.name

    def set_availability(self, status: bool):
        """
        set availability for resource
        """
        self.availability = status
    