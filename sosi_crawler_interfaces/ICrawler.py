from abc import ABC, abstractmethod, abstractproperty
from sosi_crawler_interfaces.IDataRepository import IDataRepository
from sosi_crawler_interfaces.IConfiguration import IConfiguration
from sosi_crawler_interfaces.IException import IException
from sosi_crawler_interfaces.ILogging import ILogging
from sosi_crawler_interfaces.IApiController import IApiController

class ICrawler():
    """
    Interface that rules the commom operation for any crawler inside SoSI's architecture
    """

    def SetDataRepository(self, dataRepo: IDataRepository): raise NotImplementedError
    def SetConfiguration(self, config: IConfiguration): raise NotImplementedError
    def SetException(self, ex: IException): raise NotImplementedError
    def SetLogging(self, log: ILogging): raise NotImplementedError
    def SetApiController(self, controller: IApiController): raise NotImplementedError

    def DataRepository(self) -> IDataRepository: raise NotImplementedError

    pass