#Imports involving low level functionality (accessing program metadata and functionality running this program.
import subprocess
import os
import sys

#I only want to deal with one assembly program at a time for now.
program = sys.argv[1]

#Joining the file extensions to my program name argument.
assembleProgram = [program, ".asm"]
linkProgram = [program, ".o"]


#The annoying commands I'm sick of typing myself.
process = {
    "Assemble": ['nasm', '-f', 'elf64', "".join(assembleProgram)],
    "Link": ['ld', "".join(linkProgram), '-o', program]
}
#Running the annoying, repetitive commands.
subprocess.run(process["Assemble"])
print("Ran Assembler")
subprocess.run(process["Link"])
print("Ran Linker")

#Grabbing the path to the asm program.
program_path = os.path.dirname(os.path.abspath(__file__))
runner = os.path.join(program_path, program)

#Running it.
subprocess.run([runner])
print("Ran Code")

