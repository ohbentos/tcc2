import os

# Specify the directory containing the files
root_dir= "./results"

# Loop through each file in the directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        if file.endswith((".json", ".png")):  # Check if the file is a JSON or PNG file
            parts = file.split("_", maxsplit=2)  # Split the filename at each underscore
            name = parts[2]

            a = name.split("-")

            suffix = a[1].split(".")[-1]

            # print(a)



            test_name = a[0]
            # print(test_name)

            new_filename = f"{parts[0]}_{test_name}-{parts[1]}.{suffix}"  # Reconstruct the filename
            # print(new_filename)

            old_file_path = os.path.join(dirpath, file)
            new_file_path = os.path.join(dirpath, new_filename)
            # print(f"Renaming {old_file_path} to {new_file_path}")
            os.rename(old_file_path, new_file_path)  # Rename the file


print("Renaming complete.")
