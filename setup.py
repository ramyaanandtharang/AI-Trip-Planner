from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """ This function will returns list of requirements"""
    requirements_list: List[str] = []
    
    try:
        # open and read requirements.txt file
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                # strip whitespaces and newline charecters
                requirement = line.strip()
                #ignore empty lines and -e
                if requirement and requirement !='.e':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return

print(get_requirements())

setup(
    name = "AI_TRIP_PLANNER",
    version = "0.0.1",
    author = "Ramya Javangula",
    author_email = "jvnramya.10@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements()
)