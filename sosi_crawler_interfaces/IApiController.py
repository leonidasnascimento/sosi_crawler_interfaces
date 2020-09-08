from abc import ABC, abstractmethod, abstractproperty
from typing import Optional

class IApiController(ABC):
    """
    Base interface responsible to standardize a common behavior of an API controller
    """

    @abstractmethod
    def Post(self, url: str, header: object, data: object, param: Optional[object]) -> str: raise NotImplementedError
    """
    Post data to an URL

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """

    @abstractmethod
    async def PostAsync(self, url: str, header: object, data: object, param: Optional[object]): raise NotImplementedError
    """
    Post data to an URL

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """

    @abstractmethod
    def Get(self, url: str, header: object, data: object, param: Optional[object]) -> str: raise NotImplementedError
    """
    Get data from an URL

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """

    @abstractmethod
    async def GetAsync(self, url: str, header: object, data: object, param: Optional[object]) -> str: raise NotImplementedError
    """
    Get data to an URL

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """

    @abstractmethod
    def Put(self, url: str, header: object, data: object, param: Optional[object]) -> str: raise NotImplementedError
    """
    Put some data to an URL

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """

    @abstractmethod
    async def PutAsync(self, url: str, header: object, data: object, param: Optional[object]) -> str: raise NotImplementedError
    """
    Put some data to an URL

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """

    @abstractmethod
    def Delete(self, url: str, header: object, data: object, param: Optional[object]) -> str: raise NotImplementedError
    """
    Delete data present into a repository (URL)

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """

    @abstractmethod
    async def DeleteAsync(self, url: str, header: object, data: object, param: Optional[object]) -> str: raise NotImplementedError
    """
    Delete data present into a repository (URL)

    :param url: Target URL
    :param header: HTTP Headers
    :param data: Data to be sent to the target URL
    :param param: Extra parameters to be sent to the target server

    :type url: str
    :type header: object
    :type data: object
    :type param: Optional[object]

    :return: str
    """