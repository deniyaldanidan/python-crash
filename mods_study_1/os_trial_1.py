import os

# print(os.getcwd())

# os.chdir("E:\\Work\\py-world")  # This change current working-directory

# print(os.getcwd())

# os.chdir("E:\\Work\\py-world\\python-crash")

# print(os.listdir())  # List out all the contents in the current-working-directory

# print(os.listdir("outputs/"))  # List out all the contents in the outputs-folder

# os.mkdir("new-dir")  # This will create a new-folder in the current-working-directory

# os.makedirs(
#     "new-dir0/new-dir1/new-dir2"
# )  # This will create a nest of new-folders in the CWD

# For removing-folders use rmdir & removedirs

# os.rmdir("new-dir")  # For deleting folder use rmdir

# os.removedirs(
#     "new-dir0/new-dir1/new-dir2"
# )  # for deleting nested-folders use removedirs. THIS IS NOT RECOMMENDED, CUZ IT CAN CAUSE ISSUES. IF NOT HANDLED WELL

# os.rename("text-outs/sample.txt", "text-outs/demo.txt")  # To rename a file

# print(os.stat("text-outs/demo.txt"))  # Get Info's of file


# for dirpath, dirname, filename in os.walk(os.getcwd()): # This will list out all the contents & folders in a directory & its children
#    print(f"{dirpath} {dirname} {filename}")


# print(os.environ.get("HOMEPATH"))  # This will gets all environment variables

# For path-string concatentation use:
print(os.path.join(os.getcwd(), "text-outs", "demo.txt"))

# For extracting filename from a path use:
print(os.path.basename("text-outs\\demo.txt"))  # THis will return demo.txt

print(os.path.dirname("text-outs\\demo.txt"))  # This will return text-outs\

print(
    os.path.split("python-crash\\text-outs\\demo.txt")
)  # This will return: ('python-crash\\text-outs', 'demo.txt')

SAMPLE_PATH = os.path.join("text-outs", "demo.txt")

print(os.path.exists(SAMPLE_PATH))  # This will return True

print(os.path.isdir("text-outs/"))  # This will return True


print(os.path.isfile(SAMPLE_PATH))  # This will return True

print(
    os.path.splitext(SAMPLE_PATH)
)  # This will split extension and other parts of a path and returns ('text-outs\\demo', '.txt')
