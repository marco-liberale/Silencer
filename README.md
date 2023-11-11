# Silencer
Silencer is a beginner friendly Python-based tool that allows users to run commands over the Tor network.
# Installation
To install Silencer, use the following commands:


Clone the GitHub repository:
```bash
git clone https://github.com/marco-liberale/Silencer.git
```

Change the directory to the cloned repository:
```bash
cd Silencer
```

Install dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```

# Usage

To begin using Silencer, run a command with the "-c" option.

Example:
```bash
sudo python3 silencer.py -c 'nmap -sT -PN -n -p 80,22 www.marcoliberale.com'
```

You can also use "-n" to get a new IP:
```bash

sudo python3 silencer.py -n -c 'nmap -sT -PN -n -p 80,22 www.marcoliberale.com'
```

Note: Remember to put commands with spaces between quotes.

# Make it a command

To make silencer.py a global command, use the following commands:

Copy the silencer script to the /bin directory:
```bash

sudo cp bin/silencer /bin/silencer
```
Make the silencer script executable:
```bash
sudo chmod +x /bin/silencer
```

You can now run it like this:
```bash

sudo silencer -c 'nmap -sT -PN -n -p 80,22 www.scanme.marcoliberale.com'
```

enjoy :)


# Legal Disclamer
By using the repository, you acknowledge that you have read this [Disclaimer](https://github.com/marco-liberale/Silencer/blob/main/legal_disclamer.pdf) and agree to be bound by the terms hereof.
If you do not agree to abide by the above, please do not use the repository.

