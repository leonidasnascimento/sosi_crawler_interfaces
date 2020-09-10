from abc import abstractmethod, ABC
class ICrawlingResult(ABC):
    """
    Interface that rules how a crawler must opperate unde SoSI's architecture
    """
    @abstractmethod
    def set_message(self, message: str): raise NotImplementedError
    """
    Sets a message as crawling result

    :param message: The message to be set
    :type message: str
    """

    @abstractmethod
    def set_object(self, obj: dict): raise NotImplementedError
    """
    Sets an object as crawling result

    :param obj: The object to be set
    :type obj: dict
    """
    
    @abstractmethod
    def set_crawlingStatus(self, status: bool): raise NotImplementedError
    """
    Sets the status of crawling process

    :param status: The status 
    :type status: bool
    """

    @abstractmethod
    def get_message(self) -> str: raise NotImplementedError
    """
    Gets the message of crawling process

    :return: str
    """
    
    @abstractmethod
    def get_object(self) -> dict: raise NotImplementedError
    """
    Gets the object resulting from crawling process

    :return: dict
    """

    @abstractmethod
    def get_crawling_status(self) -> bool: raise NotImplementedError
    """
    Gets the status of crawling process

    :return: bool
    """