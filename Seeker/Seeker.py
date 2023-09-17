import os

def search_files(start_paths, target_name):
    for start_path in start_paths:
        for dirpath, dirnames, filenames in os.walk(start_path):
            for dirname in dirnames:
                if target_name in dirname:
                    print("Найдена папка:", os.path.join(dirpath, dirname))

            for filename in filenames:
                if target_name in filename:
                    print("Найден файл:", os.path.join(dirpath, filename))

target_name = input("Введите название папки или файла для поиска: ")

drives = []
for drive in range(ord('A'), ord('Z')+1):
    drive_name = chr(drive) + ":\\"
    if os.path.exists(drive_name):
        drives.append(drive_name)

print("Найдено", len(drives), "дисков.")

search_files(drives, target_name)

while True:
    pass