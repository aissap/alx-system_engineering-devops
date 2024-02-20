ckground Context

Old-school system administrators usually only know Bash, and that is what they use to build their scripts. While Bash is perfectly fine for many tasks, it can quickly become messy and inefficient compared to other programming languages. The new generation of system administrators, often called SREs (Site Reliability Engineers), are essentially regular software engineers, but instead of building products, they manage systems. One significant difference with their predecessors is that they are proficient in more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. APIs are often the public-facing parts of websites and microservices, allowing outsiders to interact with them – accessing and modifying their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This project is a perfect example of a task that is not well-suited for Bash scripting, so let's build Python scripts.

## Resources
Read or watch:

- [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API?](https://www.webopedia.com/definitions/api/)
- [What is a REST API?](https://restfulapi.net/)
- [What are microservices?](https://microservices.io/)
- [PEP8 Python style](https://pep8.org/) - Having clean code that respects the style guide is highly appreciated in the industry.

## Learning Objectives
At the end of this project, you are expected to be able to explain, without the help of Google:

### General
- What Bash scripting should not be used for
- What an API is
- What a REST API is
- What microservices are
- What the CSV format is
- What the JSON format is
- Pythonic package and module name style
- Pythonic class name style
- Pythonic variable name style
- Pythonic function name style
- Pythonic constant name style
- The significance of CapWords or CamelCase in Python

## Copyright - Plagiarism
You are tasked with coming up with solutions for the tasks below yourself to meet the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

### Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use `get` to access dictionary values by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

