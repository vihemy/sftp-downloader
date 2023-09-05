import os
import paramiko

from utils import get_data_from_config

provider = "epinion"  # "epinion" or "silverlining"

# Server details
hostname = get_data_from_config(provider, "hostname")
port = get_data_from_config(provider, "port")
username = get_data_from_config(provider, "username")
password = get_data_from_config(provider, "password")  # Or use key-based authentication

# paths
remote_directory = get_data_from_config(provider, "remote_directory")
remote_filename = get_data_from_config(provider, "remote_filename")
local_directory = get_data_from_config(provider, "local_directory")


# Establish SSH/SFTP connection
transport = paramiko.Transport(
    (hostname, int(port))
)  # Port should be integer, but is treated as outputted as string in get_data_from_config
transport.connect(
    username=username, password=password
)  # Replace with key-based authentication if needed

sftp = paramiko.SFTPClient.from_transport(transport)

# Navigate to the remote directory
sftp.chdir(remote_directory)

# Download the file
remote_path = os.path.join(remote_directory, remote_filename)
local_path = os.path.join(local_directory, remote_filename)

sftp.get(remote_path, local_path)

# Close the SFTP connection
sftp.close()
transport.close()

print(f"File downloaded from {remote_path} to {local_path}")
