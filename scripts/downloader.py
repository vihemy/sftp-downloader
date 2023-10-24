# external libaries
import os
from paramiko import SFTPClient, Transport

# internal libaries
from provider import Provider


class Downloader:
    """A class to download files from a given SFTP server to the local machine.

    Attributes
    ----------
    provider : Provider
        the provider from which the files should be downloaded from
    """

    def __init__(self, provider: Provider):
        self.provider = provider

    def sftp_to_local(self):
        try:
            sftp, transport = self._establish_connection()
            # Navigate to the remote directory
            sftp.chdir(self.provider.remote_directory)
            self._get_files_in_dir(sftp)
            self._close_connection(sftp, transport)
            msg = f"Successfully downloaded from {self.provider.name}.\n"
        except Exception as e:
            msg = f"Error downloading from {self.provider.name}. Error message: {e}\n"
        finally:
            return msg

    def _establish_connection(self):
        transport = Transport((self.provider.hostname, self.provider.port))
        transport.connect(
            username=self.provider.username, password=self.provider.password
        )  # Replace with key-based authentication if needed

        sftp = SFTPClient.from_transport(transport)

        return sftp, transport

    def _get_files_in_dir(self, sftp: SFTPClient):
        """Download all files in a remote directory to the local machine."""
        for filename in sftp.listdir():
            remote_path = os.path.join(self.provider.remote_directory, filename)
            local_path = os.path.join(self.provider.local_directory, filename)
            self._get_file(sftp, remote_path, local_path)

    def _get_file(self, sftp: SFTPClient, remote_path, local_path):
        """Download a file from a remote server to the local machine."""
        sftp.get(remote_path, local_path)
        print(f"File downloaded from {remote_path} to {local_path}")

    def _close_connection(self, sftp: SFTPClient, transport: Transport):
        sftp.close()
        transport.close()
