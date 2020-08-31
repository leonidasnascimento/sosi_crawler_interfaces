from abc import ABC, abstractmethod, abstractproperty

class IException(ABC):
    """
    Custom exception interface. 
    This interface was created to enable concrete implementations to pass forward the exception so it can be treated somehow
    
    It enables a method either to get an 'native' exception or to raise a custom excption by calling the method 'RaiseCustomException(...)'
    """

    @abstractmethod
    def ManageException(self, ex: Exception, raise_exception: bool) -> str: raise NotImplementedError
    """
    Manages a given exception. 
    The exception managing pipeline should be the following:

    1 - Log the error into some SoSI's error logging mechanism
    2 - Raise Exception?   
        2.1 - Y: Raises the same exception with a default message stating it was safely logged
        2.2 - N: Return a default message stating it was safely logged

    :param ex: The current exception
    :type ex: Exception
    :param raise_exception: The current exception
    :type raise_exception: bool
    :return: str
    """