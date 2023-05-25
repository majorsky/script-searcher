📋 File Search Script Description

🔍 Search Text in Files

This Python script allows you to search for a specified text within files located in the current directory and its subdirectories.

🔧 Instructions

Run the script.
Enter the text you want to search for in the files.
The script will traverse all files with extensions .txt, .py, .html, .css, and .js in the current directory and its subdirectories.
If the text is found in a file, the script will display a message in the format "Found in file: {file_path}".
If there is a Unicode decoding error in a file encoded in Windows-1251, the script will display an error message: "Error reading file: Unable to decode using Windows-1251 encoding".
📁 File Extension Limitations

The script is limited to searching for text within files with the extensions .txt, .py, .html, .css, and .js. You can add or modify the file extensions in the file.endswith(("...")) statement in the script code to expand or change the list of file extensions to be searched.

⚠️ Important

Ensure that you have sufficient access rights to the files and directories where you are running the script.

📋 Описание скрипта поиска текста в файлах

🔍 Поиск текста в файлах

Этот Python скрипт позволяет осуществлять поиск заданного текста в файлах, находящихся в текущей директории и ее поддиректориях.

🔧 Инструкция

Запустите скрипт.
Введите текст, который вы хотите найти в файлах.
Скрипт произведет обход всех файлов с расширениями .txt, .py, .html, .css и .js в текущей директории и ее поддиректориях.
Если текст найден в файле, скрипт выведет сообщение вида "Найдено в файле {путь_к_файлу}".
Если возникает ошибка декодирования файла в кодировке Windows-1251, скрипт выведет сообщение "Ошибка чтения файла {путь_к_файлу}: невозможно декодировать в кодировке Windows-1251".
📁 Ограничения по расширениям файлов

Скрипт ограничен поиском текста только в файловых типах .txt, .py, .html, .css и .js. Вы можете добавить или изменить расширения в переменной file.endswith(("...")) в коде скрипта, чтобы расширить или изменить список расширений файлов, в которых будет производиться поиск.

⚠️ Важно

Убедитесь, что у вас есть достаточные права доступа к файлам и директориям, в которых вы запускаете скрипт.
