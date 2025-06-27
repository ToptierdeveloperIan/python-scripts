import os
import shutil

# === Config ===
search_root = "C:\\"  # or "/" on Linux/macOS
output_folder = "CollectedPythonFiles"

# === Step 1: Create output folder if it doesn't exist ===
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# === Step 2: Walk the filesystem ===
count = 0
for root, dirs, files in os.walk(search_root):
    for file in files:
        if file.endswith(".py"):
            source_path = os.path.join(root, file)
            # To avoid name collisions, include path hash or prefix
            new_name = f"{count}_{file}"
            dest_path = os.path.join(output_folder, new_name)

            try:
                shutil.copy2(source_path, dest_path)
                print(f"[+] Copied: {source_path} → {dest_path}")
                count += 1
            except Exception as e:
                print(f"[!] Failed to copy {source_path}: {e}")

print(f"\n✅ Finished. Total files copied: {count}")