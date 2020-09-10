from abc import abstractmethod, ABC
from typing import Generic, TypeVar

InterfaceType = TypeVar('InterfaceType')
ConcreteClassType = TypeVar('ConcreteClassType')

class IObjectFactory(ABC):
    """
    Interface for SoSI's Depence Injection Concrete Object. It rules how a object factory should work
    """ 

    @abstractmethod
    def add_dependency(self, target_crawler: str, interface: Generic[InterfaceType], concrete_class: Generic[ConcreteClassType]): raise NotImplementedError
    """
    Add a generic type accoding to a given interface & crawler alias

    :param interface: Interface type to be returned
    :param target_crawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
    :param concrete_class: Concrete class type that implements the interface
    :type concrete_class: ConcreteClassType
    :type interface: Generic[InterfaceType]
    :type target_crawler: str
    """

    @abstractmethod
    def load_dependencies(self, file_path: str): raise NotImplementedError
    """
    Load the dependencies that were predefined for SoSI's crawlers

    :param file_path: The pre defined dependencies file path
    :type file_path: str
    """

    @abstractmethod
    def get_instance(self, target_crawler: str, interface: Generic[InterfaceType]) -> InterfaceType: raise NotImplementedError
    """
    Create an instance of a generic type accoding to a given interface & crawler alias

    :param interface: Interface type to be returned
    :param target_crawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
    :type interface: Generic[InterfaceType]
    :type target_crawler: str
    """