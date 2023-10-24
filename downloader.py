import os
from paramiko import SFTPClient, Transport

from utils import get_data_from_config

providers = ["epinion", "silverlining"]


def main():
    for provider in providers:
        sftp_to_local_folder(provider)


def sftp_to_local_folder(provider):
    sftp, transport = establish_connection(provider)

    remote_directory = get_data_from_config(provider, "remote_directory")
    local_directory = get_data_from_config(provider, "local_directory")

    # Navigate to the remote directory
    sftp.chdir(remote_directory)

    get_all_files_in_dir(sftp, remote_directory, local_directory)

    close_connection(sftp, transport)


def establish_connection(provider):
    # Server details
    hostname = get_data_from_config(provider, "hostname")
    port = int(get_data_from_config(provider, "port"))
    username = get_data_from_config(provider, "username")
    password = get_data_from_config(
        provider, "password"
    )  # Or use key-based authentication

    # Establish SSH/SFTP connection
    transport = Transport((hostname, port))
    transport.connect(
        username=username, password=password
    )  # Replace with key-based authentication if needed

    sftp = SFTPClient.from_transport(transport)

    return sftp, transport


def get_all_files_in_dir(sftp: SFTPClient, remote_directory, local_directory):
    """Download all files in a remote directory to the local machine."""
    for filename in sftp.listdir():
        remote_path = os.path.join(remote_directory, filename)
        local_path = os.path.join(local_directory, filename)
        get_file(sftp, remote_path, local_path)


def get_file(sftp: SFTPClient, remote_path, local_path):
    """Download a file from a remote server to the local machine."""
    sftp.get(remote_path, local_path)
    print(f"File downloaded from {remote_path} to {local_path}")


def close_connection(sftp: SFTPClient, transport: Transport):
    # Close the SFTP connection
    sftp.close()
    transport.close()


if __name__ == "__main__":
    main()
