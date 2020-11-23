from abc import ABC, abstractmethod, abstractproperty

class IConfiguration(ABC):
    """
    Commom interface that describes a configuration class operarion
    """
    
    @abstractmethod
    def load(self, file_path: str, section_name: str): raise NotImplementedError
    """
    Loads in memory a configuration section from a given file path. 
    It's only accepted a JSON file as configuration file
    
    :param file_path: Configuration file path
    :param section_name: Section to be load by the configuration loader mechanism 
    :type file_path: str
    :type section_name: str
    :return: void
    """

    @abstractmethod
    def read(self, field: str, default_value: str = None) -> str: raise NotImplementedError
    """
    Read a field value within the in-memory configuration section.
    If either field or value are not found, the default value will be returned.

    :param field: Field name
    :param defaultValue: Default value to be returned in case either field or value are not present 
    :type field: str
    :type default_value: str
    :default default_value: None
    :return: str
    """
