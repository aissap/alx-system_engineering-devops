Webstack Debugging Series


Background Context
Welcome to the Webstack Debugging Series! This series is designed to hone your debugging skills, an essential skill for Full-Stack Software Engineers. The world of computers and software can be unpredictable, and mastering the art of debugging is crucial to ensure that systems work as intended.

In this series, you will encounter broken or bugged webstacks. Your ultimate goal is to create a Bash script that, when executed, will fix the webstack and bring it to a working state. However, before writing the script, you must identify and fix the issues manually.

Let's begin with a simple example. The server must:

Have a copy of the /etc/passwd file in /tmp.
Have a file named /tmp/isworking containing the string "OK."
Now, let's pretend that without these two elements, the web application cannot function.

bash
Copy code
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
# Output truncated for brevity
vagrant@vagrant:~$ docker ps
# Output truncated for brevity
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
# Commands executed in the container
vagrant@vagrant:~$
If the server is fixed, your answer file should resemble:

bash
Copy code
sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
sylvain@ubuntu:~$
Note: Interactive software like emacs or vi cannot be used in the Bash script. All actions must be performed from the command line, including file editing.

Installing Docker
For this project, you'll be provided with a container to solve the task. If you wish to experiment locally or solve the problem on your own machine, you can install Docker using the instructions for:

Mac OS
Windows
Ubuntu 14.04 (Note: Docker for Ubuntu 14 is deprecated; adjustments may be needed)
Ubuntu 16.04
Resources
Refer to the man or help for:

curl
Requirements
General
Allowed editors: vi, vim, emacs
All files interpreted on Ubuntu 14.04 LTS
Files should end with a new line
Mandatory README.md file at the project's root folder
All Bash script files must be executable
Bash scripts must pass Shellcheck without any errors
Bash scripts must run without errors
The first line of all Bash scripts should be #!/usr/bin/env bash
The second line of all Bash scripts should be a comment explaining the script's purpose
