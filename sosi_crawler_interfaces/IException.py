from abc import ABC, abstractmethod, abstractproperty
from sosi_crawler_interfaces.ILogging import ILogging

class IException(Exception):
    """
    Custom exception interface
    """

    @abstractmethod
    def Log(self, loggingObj: ILogging): raise NotImplementedError
    """
    Logs the error through a log object

    :param loggingObj: Object to use to perfom logging
    :return: None
    """

    @abstractmethod
    def GetExceptionMessage(self) -> str: raise NotImplementedError
    """
    Gets a custom error message from the exception

    :return: str
    """