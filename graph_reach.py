import os

# Read in the path of the repository

path = (r"/Users/haleykarp/Desktop/projects/git/hk_socyb/Reachability")

files = []
for dirpath, subdirs, files in os.walk(path):
    for x in files:
        files.append(os.path.join(dirpath, x))

print(files)


# Build levels to the repository to show children and parent relationships




# Build network graph of the parent and child relationships based on the entire repository
# Possible getting weighted relationships here 