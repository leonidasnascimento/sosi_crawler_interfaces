from abc import abstractmethod, ABC

class IMessageQueue(ABC):
    """
    Interface that rules how a MessageQueue component should behave under SoSI's architecture
    """

    def __init__(self):
        """
        Creates an intance of the class
        """
        pass

    @abstractmethod
    def publish(self, topic: str, message: dict): raise NotImplementedError
    """
    Publish a message to a given topic

    :param topic: Target topic name
    :param message: Object representing the JSON message to be sent to the topic. NOTE: This will be parsed to JSON.
    :type topic: str
    :type message: dict
    """

    @abstractmethod
    def consume(self, topic: str) -> dict: raise NotImplementedError
    """
    Consume a message from a topic queue

    :param topic: Target topic name
    :type topic: str
    :return: dict
    """