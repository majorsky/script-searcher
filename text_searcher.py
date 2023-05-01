import os

search_text = input("Введите текст для поиска: ")

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith((".txt", ".py", ".html", ".css", ".js")):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, encoding='windows-1251') as f:
                    file_content = f.read()
                    if search_text in file_content:
                        print(f"Найдено в файле {file_path}")
            except UnicodeDecodeError:
                print(f"Ошибка чтения файла {file_path}: невозможно декодировать в кодировке Windows-1251")

