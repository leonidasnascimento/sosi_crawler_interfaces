from abc import ABC, abstractmethod, abstractproperty


class IDataRepository():
    """
    Commom interface that describes a Data Repository class operarion
    """
    
    @abstractmethod
    def Connect(self, configuration: str, timeOut: int) -> bool: raise NotImplementedError

    @abstractmethod
    def Disconnect(self) -> bool: raise NotImplementedError

    @abstractmethod
    def ExecuteCommand(self, commandStr: str) -> bool: raise NotImplementedError

    @abstractmethod
    def ExecuteQuery(self, queryStr: str) -> []: raise NotImplementedError

    @abstractmethod
    def IsConnected(self) -> bool: raise NotImplementedError
    pass
