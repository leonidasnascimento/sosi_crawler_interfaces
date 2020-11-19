from abc import abstractmethod, ABC
class ICrawlingResult(ABC):
    """
    Interface that rules how a crawler must opperate unde SoSI's architecture
    """
    __message: str
    __success: bool
    __object: dict    
    
    def __init__(self):
        """
        Creates an intance of the class
        """
        self.__message = ""
        self.__success = False
        self.__object = None

    def set_result(self, message: str, success: bool, obj: dict):
        """
        Sets the Crawling result

        :param message: The message to be set
        :type message: str
        :param obj: The object to be set
        :type obj: dict
        :param success: The status 
        :type success: bool
        """
        self.__message = message
        self.__success = success
        self.__object = obj

    def get_message(self) -> str:
        """
        Gets the message of crawling process

        :return: str
        """
        return self.__message
    
    def get_object(self) -> dict: 
        """
        Gets the object resulting from crawling process

        :return: dict
        """
        return self.__object

    def get_crawling_status(self) -> bool: 
        """
        Gets the status of crawling process. Wether success or not

        :return: bool
        """
        return self.__success