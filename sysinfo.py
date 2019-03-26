"""
Write a Python scripts to collect system info
such as operation system, version, hardware, etc
"""
import platform, os, sys

# Get info about the OS
def os_info():

    print() # Blank line for readability
    print("OS Info: ")
    print("Device Name: " + platform.node())
    print("OS: " + platform.platform())
    print("Architechture: " + str(platform.architecture()))
    print("Python Version: " + str(platform.python_version()))

# Get hardware info
def hw_info():

    print() # Blank line for readability
    print("Hardware Info: ")
    print("CPU Type: " + platform.machine())
    print("CPU Info: " + platform.processor())

def main():

    os_info()
    hw_info()

main()