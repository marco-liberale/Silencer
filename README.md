# Silencer
Silencer is a Python-based tool that allows users to run commands over the Tor network.
# Installation
To install Silencer, use the following commands:


Clone the GitHub repository:
<code-block lang="plain text">git clone https://github.com/marco-liberale/Silencer.git</code-block>

Change the directory to the cloned repository:
<code-block lang="plain text">cd Silencer</code-block>


Install dependencies from requirements.txt:
<code-block lang="plain text">pip install requirements.txt}</code-block>


# Usage

To begin using Silencer, run a command with the "-c" option.

Example:
<code-block lang="plain text">python3 silencer.py -c 'nmap -sT -PN -n -p 80,22 www.scanme.marcoliberale.com'</code-block>
You can also use "-n" to get a new IP:
<code-block lang="plain text">python3 silencer.py -n -c 'nmap -sT -PN -n -p 80,22 www.scanme.marcoliberale.com'</code-block>
Note: Remember to put commands with spaces between quotes.

# Make it a command

To make silencer.py a global command, use the following commands:

<code-block lang="plain text">sudo cp bin/silencer /bin/silencer</code-block>


<code-block lang="plain text">chmod +x /bin/silencer</code-block>
You can now run it like this:
<code-block lang="plain text">silencer -c 'nmap -sT -PN -n -p 80,22 www.scanme.marcoliberale.com'</code-block>

