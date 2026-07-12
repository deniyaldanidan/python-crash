import subprocess

# * To simply run external commands
subprocess.run("python mods_study_1/timer.py")
subprocess.run(["echo", "hello world"])
subprocess.run("ls ")
# * To use local Terminal commands
subprocess.run("dir", shell=True)

# * To check if it ran correctly
p1 = subprocess.run(["ls", "mods_study_1"], check=True)
print(p1.check_returncode())
print(p1.returncode)  # This will be 0

# * To Capture output
p2 = subprocess.run(
    ["echo", "hello-world, This is my output"],
    capture_output=True,
    text=True,
    check=True,
)
print(f"Captured Output: {p2.stdout}")

# * To Write output to File
with open("text-outs/sub_result1.txt", "w", encoding="utf-8") as f:
    subprocess.run("ls", text=True, check=True, stdout=f)
