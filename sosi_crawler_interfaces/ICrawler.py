from abc import ABC, abstractmethod, abstractproperty, ABCMeta
from sosi_crawler_interfaces.ICrawlingResult import ICrawlingResult

class ICrawler(ABC):
    """
    Interface that rules the commom operation for any crawler inside SoSI's architecture
    """

    @abstractmethod
    def Execute(self, args: dict) -> ICrawlingResult: raise NotImplementedError
    """
    Main method for a crawling object

    :param args: Set of arguments needed to run the crawler object
    :type args: dict
    """