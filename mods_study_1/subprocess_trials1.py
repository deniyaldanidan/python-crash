import subprocess

# * Below code throws error
# subprocess.run("ls i_dont_exist", check=True)

# * PIPING
# Below is equivalent to "cat text-outs/sub_result1.txt | grep -n out"
p1 = subprocess.run(
    "cat text-outs/sub_result1.txt", check=True, capture_output=True, text=True
)
# print(p1.stdout)

p2 = subprocess.run(
    "grep -n readme", check=True, capture_output=True, text=True, input=p1.stdout
)
print(p2.stdout)

# * Or You can do
p3 = subprocess.run(
    "cat text-outs/sub_result1.txt | grep -n requirements",
    capture_output=True,
    text=True,
    shell=True,
    check=True,
)

print(p3.stdout)
