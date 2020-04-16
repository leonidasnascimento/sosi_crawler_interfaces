from abc import ABC, abstractmethod, abstractproperty
from sosi_crawler_interfaces.ILogging import ILogging

class IException(Exception, ABC):
    """
    Custom exception interface
    """
    @abstractmethod
    def SetLog(self, logging: ILogging): raise NotImplementedError
    """
    Set a log object to enable logging within IException implementation

    :param logging: Logging object to inject
    :type logging: ILogging
    """

    @abstractmethod
    def Log(self): raise NotImplementedError
    """
    Logs the error through a log object

    :return: None
    """

    @abstractmethod
    def GetExceptionMessage(self) -> str: raise NotImplementedError
    """
    Gets a custom error message from the exception

    :return: str
    """