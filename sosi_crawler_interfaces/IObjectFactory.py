from abc import abstractmethod, ABC
from typing import Generic, TypeVar

T = TypeVar('T')

class IObjectFactory(ABC):
    """
    Interface for SoSI's Depence Injection Concrete Object. It rules how a object factory should work
    """ 
    @abstractmethod
    def LoadDependencies(self): raise NotImplementedError
    """
    Load the dependencies set for SoSI's crawlers
    """

    @abstractmethod
    def GetInstance(self, interface: Generic[T], targetCrawlerAlias: str, ) -> T: raise NotImplementedError
    """
    Create an instance of a generic type accoding to a given interface & crawler alias
    """
    
    pass