import os
import paramiko

from utils import get_data_from_config

# Server details
hostname = get_data_from_config("silverlining", "hostname")
port = get_data_from_config("silverlining", "port")
username = get_data_from_config("silverlining", "username")
password = get_data_from_config(
    "silverlining", "password"
)  # Or use key-based authentication

# Paths
remote_directory = "/"
remote_filename = "Kattegatcentret.txt"
local_directory = "C:/Users/vhm/OneDrive - Kattegatcentret/Økonomi og statistik/Analyser & undersøgelser/Silverlining"

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
