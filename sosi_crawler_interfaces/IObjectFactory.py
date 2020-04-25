from abc import abstractmethod, ABC
from typing import Generic, TypeVar

InterfaceType = TypeVar('InterfaceType')
ConcreteClassType = TypeVar('ConcreteClassType')

class IObjectFactory(ABC):
    """
    Interface for SoSI's Depence Injection Concrete Object. It rules how a object factory should work
    """ 

    @abstractmethod
    def AddDependency(self, targetCrawler: str, interface: Generic[InterfaceType], concreteClass: Generic[ConcreteClassType]): raise NotImplementedError
    """
    Add a generic type accoding to a given interface & crawler alias

    :param interface: Interface type to be returned
    :param targetCrawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
    :param concreteClass: Concrete class type that implements the interface
    :type concreteClass: ConcreteClassType
    :type interface: Generic[InterfaceType]
    :type targetCrawler: str
    """

    @abstractmethod
    def LoadDependencies(self, filePath: str): raise NotImplementedError
    """
    Load the dependencies that were predefined for SoSI's crawlers

    :param filePath: The pre defined dependencies file path
    :type filePath: str
    """

    @abstractmethod
    def GetInstance(self, targetCrawler: str, interface: Generic[InterfaceType]) -> InterfaceType: raise NotImplementedError
    """
    Create an instance of a generic type accoding to a given interface & crawler alias

    :param interface: Interface type to be returned
    :param targetCrawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
    :type interface: Generic[InterfaceType]
    :type targetCrawler: str
    """
    pass