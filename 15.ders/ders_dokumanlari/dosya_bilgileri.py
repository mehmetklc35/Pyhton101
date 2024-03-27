
import os
import win32com.client

def get_file_attributes(file_path):
    try:
        # Get basic file attributes
        file_info = os.stat(file_path)

        # Extract author information using the pywin32 library
        shell = win32com.client.Dispatch('Shell.Application')
        folder = shell.Namespace(os.path.dirname(file_path))
        file_item = folder.ParseName(os.path.basename(file_path))
        
        # Get author property
        author = folder.GetDetailsOf(file_item, 20)  # 20 corresponds to the Author property

        # Display file attributes
        print(f"File Path: {file_path}")
        print(f"Size: {file_info.st_size} bytes")
        print(f"Last Modified Time: {file_info.st_mtime}")
        print(f"Author: {author}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
file_path = 'C:\\Users\\selcuk\\Desktop\\PythonEgitim\\15.ders\\ders_dokumanlari\\test.xlsx'
get_file_attributes(file_path)