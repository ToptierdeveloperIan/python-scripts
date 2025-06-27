import os
import shutil

rootdir = "C:/"
java_folder = "javaProjects"

# Create output folder if it doesn't exist
if not os.path.exists(java_folder):
    os.mkdir(java_folder)

count = 0

for root, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".java"):
            # Source path
            gotten_file_location = os.path.join(root, file)

            # Destination filename with counter to avoid collisions
            dest_filename = f"{count}_{file}"
            dest_path = os.path.join(java_folder, dest_filename)

            try:
                shutil.copy2(gotten_file_location, dest_path)
                print(f"[+] Copied: {gotten_file_location} → {dest_path}")
                count += 1

            except Exception as e:
                print(f"[!] Failed to copy {gotten_file_location}: {e}")

print("Finished scraping .java files.")
