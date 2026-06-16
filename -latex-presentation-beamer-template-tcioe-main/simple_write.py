import sys
with open("simple_out.txt", "w") as f:
    f.write("Python executed successfully!\n")
    f.write(sys.version)
print("Done writing file.")
