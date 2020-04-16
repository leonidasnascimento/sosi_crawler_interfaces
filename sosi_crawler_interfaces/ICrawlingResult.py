from abc import abstractmethod, ABC
class ICrawlingResult(ABC):
    """
    Interface that rules how a crawler must opperate unde SoSI's architecture
    """
    @abstractmethod
    def SetMessage(self, message: str): raise NotImplementedError
    """
    Sets a message as crawling result

    :param message: The message to be set
    :type message: str
    """

    @abstractmethod
    def SetObject(self, obj: dict): raise NotImplementedError
    """
    Sets an object as crawling result

    :param obj: The object to be set
    :type obj: dict
    """
    
    @abstractmethod
    def SetCrawlingStatus(self, status: bool): raise NotImplementedError
    """
    Sets the status of crawling process

    :param status: The status 
    :type status: bool
    """

    @abstractmethod
    def GetMessage(self) -> str: raise NotImplementedError
    """
    Gets the message of crawling process

    :return: str
    """
    
    @abstractmethod
    def GetObject(self) -> dict: raise NotImplementedError
    """
    Gets the object resulting from crawling process

    :return: dict
    """

    @abstractmethod
    def GetCrawlingStatus(self) -> bool: raise NotImplementedError
    """
    Gets the status of crawling process

    :return: bool
    """
    
    pass