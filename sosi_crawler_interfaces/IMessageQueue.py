from abc import abstractmethod, ABC

class IMessageService(ABC):
    """
    Interface that rules how a MessageService component should behave under SoSI's architecture
    """

    def __init__(self):
        """
        Creates an intance of the class
        """
        pass

    @abstractmethod
    def publish(self, topic_queue: str, message: dict): raise NotImplementedError
    """
    Publish a message/event to a given topic/queue

    :param topic: Target topic/queue name
    :param message: Object representing the JSON message to be sent to the topic. NOTE: This will be parsed to JSON.
    :type topic: str
    :type message: dict
    """

    @abstractmethod
    def consume(self, topic_queue: str) -> dict: raise NotImplementedError
    """
    Consume a message from a topic or queue

    :param topic: Target topic/queue name
    :type topic: str
    :return: dict
    """