import os
import shutil


searchdir="C:/"
textfileholder="textFileholder"


# if our directory doesn't exist create it
if not os.path.exists(textfileholder):
    os.mkdir(textfileholder)


#loop through the desired dir using os.walk which returns a tupple then we unpackage it with variables
for root,dirs,files in os.walk(searchdir):
    for file in files:
        if file.endswith(".txt"):

         file_location = os.path.join(root,file)
         destination = os.path.join(textfileholder,file)

         try:
             shutil.copy(file_location,destination)
             print("copying")

         except Exception as e:
                print(f"[!] Failed to copy {file_location}: {e}")

print("finished copying")