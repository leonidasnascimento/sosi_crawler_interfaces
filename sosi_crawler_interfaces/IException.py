from abc import ABC, abstractmethod, abstractproperty

class IException(Exception, ABC):
    """
    Custom exception interface. 
    This interface was created to enable concrete implementations to pass forward the exception so it can be treated somehow
    
    It enables a method either to get an 'native' exception or to raise a custom excption by calling the method 'RaiseCustomException(...)'
    """
    @abstractmethod
    def GetExceptionMessage(self) -> str: raise NotImplementedError
    """
    Gets a custom error message from the exception

    :return: str
    """

    @abstractmethod
    def RaiseCustomException(self, message: str): raise NotImplementedError
    """
    Raises a custom excption. 
    Before raisingthe exception, the pipeline will be followed in order to pass forward the error so it can be treated somehow

    :param message: A custom message to be raised as excpetion
    :type message: str
    """