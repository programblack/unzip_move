import pyzipper
import os
import sqlite3

# اتصال به دیتابیس (اگر دیتابیس وجود نداشته باشد، آن را ایجاد می‌کند)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# ایجاد جدول users اگر از قبل وجود نداشته باشد
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()

# لیست رمزهای عبور برای امتحان کردن روی فایل‌های زیپ
List_passwords = ["yor","list","passwords"]

# تابع برای بررسی اینکه آیا فایل واقعاً یک فایل زیپ است یا خیر
def is_zipfile(file_path):
    try:
        with open(file_path, 'rb') as f:
            signature = f.read(4)
        return signature == b'PK\x03\x04'
    except:
        return False

# تابع برای اکسترکت کردن فایل زیپ با استفاده از لیست رمزهای عبور
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

# تابع برای حذف فایل زیپ
def delete_zip(zip_file):
    os.remove(zip_file)
    print("File deleted")

# تابع برای پیدا کردن تمامی فایل‌های زیپ در دایرکتوری فعلی
def find_zip_files():
    return [f for f in os.listdir() if f.endswith('.zip')]

# تابع برای بررسی اینکه آیا نام فایل در دیتابیس موجود است یا خیر
def is_file_in_db(file_name):
    cursor.execute("SELECT 1 FROM users WHERE name = ?", (file_name,))
    return cursor.fetchone() is not None

# تابع اصلی برای پردازش فایل‌های زیپ
def process_zip_files(zip_files, output_directory, passwords):
    for zip_file in zip_files:
        if not is_zipfile(zip_file):
            print(f"Skipping '{zip_file}': not a valid zip file.")
            delorno = input("Failed to extract. Delete file? (yes/no): ")
            if delorno.lower() == "yes":
                delete_zip(zip_file)
            continue

        if is_file_in_db(zip_file):
            print(f"Skipping '{zip_file}': already in database.")
            continue
        
        # اضافه کردن نام فایل زیپ به دیتابیس
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (zip_file, 0))
        conn.commit()

        # تلاش برای اکسترکت کردن فایل زیپ
        success = extract_zip(zip_file, output_directory, passwords)
        if not success:
            delorno = input("Failed to extract. Delete file? (yes/no): ")
            if delorno.lower() == "yes":
                delete_zip(zip_file)

# دایرکتوری خروجی برای اکسترکت کردن فایل‌ها
output_directory = "path_to_output_directory"

# پیدا کردن تمامی فایل‌های زیپ
zip_files = find_zip_files()

# پردازش فایل‌های زیپ
process_zip_files(zip_files, output_directory, List_passwords)

# بستن اتصال به دیتابیس
conn.close()
