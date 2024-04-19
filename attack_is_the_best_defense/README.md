# Network Security Tasks

## Overview

This repository contains tasks related to network security, including network sniffing, ARP spoofing, telnet usage, Docker, and dictionary attacks. Each task is designed to demonstrate various aspects of network security and commonly used tools.

## Task 0: ARP Spoofing and Sniffing Unencrypted Traffic

In this task, we focus on sniffing unencrypted traffic and extracting information from it. We do not cover ARP spoofing but demonstrate how to sniff traffic using tcpdump. The task involves connecting to SendGrid's SMTP relay using telnet to send an email, which allows us to capture unencrypted data.

```bash
$ telnet smtp.sendgrid.net 587
Trying 167.89.121.145...
Connected to smtp.sendgrid.net.
Escape character is '^]'.
220 SG ESMTP service ready at ismtpd0013p1las1.sendgrid.net
EHLO ismtpd0013p1las1.sendgrid.net
250-smtp.sendgrid.net
250-8BITMIME
250-PIPELINING
250-SIZE 31457280
250-STARTTLS
250-AUTH PLAIN LOGIN
250 AUTH=PLAIN LOGIN
auth login           
334 VXNlcm5hbWU6
VGhpcyBpcyBteSBsb2dpbg==
334 UGFzc3dvcmQ6
WW91IHJlYWxseSB0aG91Z2h0IEkgd291bGQgbGV0IG15IHBhc3N3b3JkIGhlcmU/ISA6RA==
235 Authentication successful
mail from: sylvain@kalache.fr
250 Sender address accepted
rcpt to: julien@google.com
250 Recipient address accepted
data
354 Continue
To: Julien
From: Sylvain
Subject: Hello from the insecure world

I am sending you this email from a Terminal.
.
250 Ok: queued as Aq1zhMM3QYeEprixUiFYNg
quit
221 See you later
Connection closed by foreign host.
$ 
```

### Tools Used:

tcpdump: For network traffic sniffing.
telnet: To connect to SendGrid's SMTP relay.

### Execution Steps:


1. split Your Terminal, On Termina 0 Use tcpdump to sniff the network and extract the password from the captured traffic with use of wireshark.
```bash
sudo tcpdump -i eth0 -w dump.pcap 'not port 22'
```

2. On the other Terminal , Terminal 1, Run the script user_authenticating_into_server locally on your Ubuntu or Linux machine.[Download user_authenticating_into_server script](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/264/user_authenticating_into_server).

3. Once the script is done on Termianl 1, manually exit tcpdump On Terminal 0 by sending a SIGINT signal (Ctrl+C).

Terminal 1:
```bash
$ ./user_authenticating_into_server
$
```
Terminal 0:
```bash
$ sudo tcpdump -i eth0 -w dump.pcap 'not port 22'
tcpdump: listening on eth0 , .....
^C
$ ls
dump.pcap
```

4. to analyze  our captured packets and find the password we use wireshark, First move the file (dump.pcap) this have the packet captured ,from  WSL Ubuntu to my desktop on windows (in case of wsl).

5. Open wireshark and select the file (dump.pcap) , at The packet list pane, located at the top of the window,That shows all packets found in the active capture file. Each packet has its own row and corresponding number assigned to it, Here we look to find this outgoing smtp request packet containing the password of the user in plain text, This outgoing look like encrypted but it's Not!.
authentication parameters transported over protocols like smtp are base64 encoded ,So to decode the password Right click >> Protocol Preferences >> Simple Mail Transfer Protocol >> Decode Base64 encoded AUTH parameters.

## Task 1: Dictionary Attack

This task demonstrates a dictionary attack on an SSH account running in a Docker container. We use Hydra to perform a brute force attack on the SSH account with a given password dictionary.

### Tools Used:

Hydra: For performing dictionary attacks.
Docker: To run the SSH server in a container.

### Execution Steps:

1. Install Docker and Hydra on your Ubuntu machine if not already installed.
```bash
sudo apt update
sudo apt install docker.io
sudo apt install hydra
```
2. Pull and run the Docker image sylvainkalache/264-1 using the command `docker run -p 2222:22 -d -ti sylvainkalache/264-1`.
3. Obtain a password dictionary (you may need multiple dictionaries).
4. for brute forcing passwords, I use rockyou password list Download [Here](https://objects.githubusercontent.com/github-production-release-asset-2e65be/97553311/d4f580f8-6b49-11e7-8f70-7f460f85ab3a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240419%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240419T001605Z&X-Amz-Expires=300&X-Amz-Signature=bcb2904c09249def50b05e643bbb146a48e4f0856c4a6a278c85eecbbd6574b0&X-Amz-SignedHeaders=host&actor_id=133587229&key_id=0&repo_id=97553311&response-content-disposition=attachment%3B%20filename%3Drockyou.txt&response-content-type=application%2Foctet-stream)

4. Use Hydra to brute force the SSH account sylvain on the Docker container at IP 127.0.0.1 and port 2222.go to the Directory Where rockyou file is and run this command:
```bash
$ sudo hydra -l sylvain -P rockyou.txt ssh://127.0.0.1:2222 -t 4
```
The brute forcing attack might take a while depending on computer’s processor.
