file_magic = magic.Magic()

# Specify the path to the magic file
file_magic = magic.Magic(magic_file=r'C:\\GnuWin32\\share\\misc\\magic.mgc c:\users\tkae6m\anaconda3\envs\py38_env\lib\site-packages')  # Adjust the path as needed

# Test file type detection
print(file_magic.from_file(r'C:\\GnuWin32\\share\\misc\\magic.mgc c:\users\tkae6m\anaconda3\envs\py38_env\lib\site-packages'))  # Replace with a valid file path
