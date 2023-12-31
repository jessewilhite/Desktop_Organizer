import os
import shutil

def organize_desktop(desktop_path):
    folder_mapping = {
        'txt': 'TextFiles',
        'pdf': 'PDFs',
        'jpg': 'Images',
        'png': 'Images',
        'xlsx': 'Spreadsheets',
        # Add more mappings for different file types
    }

    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)
        
        if os.path.isfile(file_path):
            file_type = file_name.split('.')[-1].lower()

            destination_folder = folder_mapping.get(file_type, 'Miscellaneous')
            destination_path = os.path.join(desktop_path, destination_folder)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            new_file_path = os.path.join(destination_path, file_name)
            shutil.move(file_path, new_file_path)
            print(f"Moved {file_name} to {destination_folder}")

def main():
    desktop_path = 'ENTER PATH TO DESKTOP'  # Use the specified path
    organize_desktop(desktop_path)

if __name__ == "__main__":
    main()
