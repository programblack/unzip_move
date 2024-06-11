ZIP Extractor with SQLite Integration
This Python script is designed to extract encrypted ZIP files and store information about these files in an SQLite database. The script checks if the ZIP file is already present in the database and only extracts new files.

Features
Database Integration: Uses SQLite to keep track of processed ZIP files.
Password Handling: Attempts to extract ZIP files with a list of potential passwords.
File Validation: Ensures that the files are valid ZIP files before processing.
Error Handling: Skips files that cannot be processed and optionally deletes them based on user input.
Requirements
Python 3.x
pyzipper library
sqlite3 library (included with Python)
Installation
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/zip-extractor.git
cd zip-extractor
Install Dependencies:

sh
Copy code
pip install pyzipper
Usage
Prepare the Output Directory:

Set the path for the output directory where the files will be extracted. Replace path_to_output_directory in the script with your desired path.
Run the Script:

sh
Copy code
python script.py
Script Overview
Database Setup
The script connects to an SQLite database (example.db) and creates a table (users) if it does not exist.

python
Copy code
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()
Password List
A list of passwords to try when extracting ZIP files.

python
Copy code
List_passwords = ["@Anime_Sekia", "TakAnime", "AnimeNin", "123", "Mangamon"]
File Validation
Checks if a file is a valid ZIP file by reading its signature.

python
Copy code
def is_zipfile(file_path):
    try:
        with open(file_path, 'rb') as f:
            signature = f.read(4)
        return signature == b'PK\x03\x04'
    except:
        return False
Extract ZIP Files
Attempts to extract a ZIP file using a list of passwords.

python
Copy code
def extract_zip(zip_file, output_dir, passwords):
    try:
        with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_STORED) as zip_ref:
            for password in passwords:
                try:
                    zip_ref.setpassword(password.encode('utf-8'))
                    zip_ref.extractall(output_dir)
                    print(f"Extraction completed successfully with password: {password}")
                    return True
                except RuntimeError:
                    print(f"Failed with password: {password}")
        return False
    except pyzipper.zipfile.BadZipFile:
        print(f"Error: '{zip_file}' is not a valid zip file.")
        return False
Delete ZIP File
Deletes the specified ZIP file.

python
Copy code
def delete_zip(zip_file):
    os.remove(zip_file)
    print("File deleted")
Find ZIP Files
Finds all ZIP files in the current directory.

python
Copy code
def find_zip_files():
    return [f for f in os.listdir() if f.endswith('.zip')]
Check if File is in Database
Checks if the file name is already in the database.

python
Copy code
def is_file_in_db(file_name):
    cursor.execute("SELECT 1 FROM users WHERE name = ?", (file_name,))
    return cursor.fetchone() is not None
Process ZIP Files
Processes each ZIP file: checks if it’s valid, not already in the database, then attempts to extract it.

python
Copy code
def process_zip_files(zip_files, output_directory, passwords):
    for zip_file in zip_files:
        if not is_zipfile(zip_file):
            print(f"Skipping '{zip_file}': not a valid zip file.")
            continue

        if is_file_in_db(zip_file):
            print(f"Skipping '{zip_file}': already in database.")
            continue
        
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (zip_file, 0))
        conn.commit()

        success = extract_zip(zip_file, output_directory, passwords)
        if not success:
            delorno = input("Failed to extract. Delete file? (yes/no): ")
            if delorno.lower() == "yes":
                delete_zip(zip_file)
Execution
Sets the output directory, finds ZIP files, and processes them.

python
Copy code
output_directory = "path_to_output_directory"
zip_files = find_zip_files()
process_zip_files(zip_files, output_directory, List_passwords)
conn.close()
Contributing
Feel free to contribute to this project by creating a pull request or opening an issue on GitHub.

License
This project is licensed under the MIT License.

Replace path_to_output_directory with the actual path where you want to extract the ZIP files. The script will skip already processed files and will ask for user confirmation before deleting any file that fails to extract.
