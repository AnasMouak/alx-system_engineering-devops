# Using SFTP and SCP for File Transfer

This guide provides step-by-step instructions for transferring files using the SFTP command-line tool and SCP.

## Using SFTP (SSH File Transfer Protocol)

SFTP is a secure method for transferring files between hosts over a secure shell (SSH) connection. Follow these steps to use SFTP:

1. **Open a Terminal**: On your local machine, open a terminal window.

2. **Connect to the Remote Host**: Use the following command to connect to the remote host:
   ```bash
   sftp username@remote_host
Replace username with your username on the remote server and remote_host with the hostname or IP address of the remote server. You'll be prompted to enter your password.

Navigate to the Desired Directory: Once connected, use cd to navigate to the directory where you want to upload or download files.

Transfer Files: Use commands like put to upload files to the remote server and get to download files from the remote server. For example:

bash
Copy code
put localfile.txt
This command uploads localfile.txt from your local machine to the current directory on the remote server.

Close the Connection: After transferring files, type exit to close the SFTP session.

Using SCP (Secure Copy Protocol)
SCP is another secure method for transferring files between hosts over an SSH connection. Follow these steps to use SCP:

Open a Terminal: On your local machine, open a terminal window.

Transfer Files: Use the scp command to transfer files between your local machine and the remote server. For example, to copy a file from your local machine to the remote server:

bash
Copy code
scp /path/to/local/file username@remote_host:/path/to/destination
Replace /path/to/local/file with the path to the file you want to upload, username with your username on the remote server, remote_host with the hostname or IP address of the remote server, and /path/to/destination with the path where you want to upload the file on the remote server.

Enter Password (if Required): If prompted, enter your password for the remote server.

File Transfer: The file will be transferred securely to the specified destination on the remote server.

Close the Terminal: Once the file transfer is complete, you can close the terminal window.
