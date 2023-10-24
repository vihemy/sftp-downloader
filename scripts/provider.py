from utils import get_data_from_config


class Provider:
    """A class to store SFTP server- and directory information of a given data-provider

    Attributes
    ----------
    name : str
        the name of the data-provider
    hostname : str
        the hostname of the SFTP server
    port : int
        the port of the SFTP server
    username : str
        the username for the SFTP server
    password : str
        the password for the SFTP server
    remote_directory : str
        the directory on the SFTP server where the files are located
    local_directory : str
        the directory on the local machine where the files should be downloaded to"""

    def __init__(self, name):
        self.name = name
        self.hostname = get_data_from_config(self.name, "hostname")
        self.port = int(get_data_from_config(self.name, "port"))
        self.username = get_data_from_config(self.name, "username")
        self.password = get_data_from_config(
            self.name, "password"
        )  # Or use key-based authentication
        self.remote_directory = get_data_from_config(self.name, "remote_directory")
        self.local_directory = get_data_from_config(self.name, "local_directory")
