from abc import ABC, abstractmethod, abstractproperty
class IDataRepository(ABC):
    """
    Commom interface that describes a Data Repository class operarion
    """
        
    @abstractmethod
    def Connect(self, *configuration) -> bool: raise NotImplementedError
    """
    Create a connection to the data repository

    :param configuration: List of required settings to create the connection
    :return: bool
    """

    @abstractmethod
    def Disconnect(self) -> bool: raise NotImplementedError
    """
    Terminate the connection to the data repository

    :return: bool
    """

    @abstractmethod
    def ExecuteCommand(self, command_obj: object) -> bool: raise NotImplementedError
    """
    Execute a given commend against the data repository

    :param command_obj:  Represents a command object. 
                        Its type depends on the command 
                        type expected by the target date 
                        repository abstraction
    :type command_obj: object
    :return: bool 
    """

    @abstractmethod
    def ExecuteQuery(self, query_obj: object) -> []: raise NotImplementedError
    """
    Execute a given query against the data repository.
    The query is expected to return some result, otherwise a blank list will be returned

    :param query_obj:    Represents a query object. 
                        Its type depends on the query 
                        type expected by the target date 
                        repository abstraction
    :type query_obj: object
    :return: List of results
    """

    @abstractmethod
    def IsConnected(self) -> bool: raise NotImplementedError
    """
    Shows whether the connection to the data repository is both active & open or not
    """