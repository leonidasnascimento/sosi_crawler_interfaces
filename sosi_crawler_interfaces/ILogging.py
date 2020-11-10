from abc import ABC, abstractmethod, abstractproperty
from sosi_crawler_interfaces.IDataRepository import IDataRepository 

class ILogging(ABC):
    """
    Logging interface
    """
    
    __repository: IDataRepository

    def __init__(self):
        self.__repository = None

    @abstractmethod
    def set_repository(self, repository: IDataRepository): raise NotImplementedError
    """
    Sets a repository in order to use within logging process

    :param repository: A repository object
    :type repository: IDataRepository
    """

    @abstractmethod
    def _log_pipeline(self, message: str): raise NotImplementedError
    """
    Add a commando to the log operation pipeline. It can be called many times along the log pipeline execution
    IMPORTANT: The method that over writes this one should only beresponsible to expose the log message to the end user

    :param messagem: A message to log
    :type message: str
    """

    def log(self, message: str):
        """
        Performs the log operation pipeline

        :param messagem: A message to log
        :type message: str
        """
        if self.__repository is not None:
            if not self.__repository.is_connected():
                self.__repository.connect()

            persisted: bool = self.__repository.execute_command(message)

            self.__repository.disconnect()

            if persisted:
                self._log_pipeline("** LOG WAS SENT TO THE REPOSITORY **")

        self._log_pipeline(message)