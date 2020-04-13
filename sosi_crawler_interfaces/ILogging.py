from abc import ABC, abstractmethod, abstractproperty
from sosi_crawler_interfaces.IDataRepository import IDataRepository 

class ILogging():
    """
    Logging interface
    """
    
    @abstractmethod
    def SetRepository(self, repository: IDataRepository): raise NotImplementedError
    """
    Sets a repository in order to use within logging process

    :param repository: A repository object
    :type repository: IDataRepository
    """

    @abstractmethod
    def Log(self, message: str): raise NotImplementedError
    """
    Performs log operation

    :param messagem: A message to log
    :type message: str
    """
    pass