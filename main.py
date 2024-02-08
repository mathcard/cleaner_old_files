import os
import datetime
import shutil

def delete_old_files(folder_path):
    current_time = datetime.datetime.now()
    days_ago = current_time - datetime.timedelta(days=10)
    files = os.listdir(folder_path)

    for file_name in files:
        if file_name.startswith(("file1", "file2", "file3")):
            file_path = os.path.join(folder_path, file_name)
            file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            if file_creation_time <= days_ago:
                try:
                    os.remove(file_path)
                    print('The directory '+file_path+' was deleted!')
                except Exception as e:
                    print("Error deleting file"+ e)

def delete_old_directories(folder_path):
    current_time = datetime.datetime.now()
    days_ago = current_time - datetime.timedelta(days=10)
    files = os.listdir(folder_path)

    for folder_sub_path in files:
        if folder_sub_path.startswith(("directory1", "directory2")):
            dir_path = os.path.join(folder_path, folder_sub_path)
            file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(dir_path))
            if file_creation_time <= days_ago:
                try:
                    shutil.rmtree(dir_path)
                    print('The directory '+dir_path+' was deleted!')
                except Exception as e:
                    print('Error deleting directory '+ e)
                    print(e)

delete_old_files('path_your_files')
delete_old_directories('path_your_directories')

print("The end!")
