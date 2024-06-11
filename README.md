استخراج فایل‌های ZIP با استفاده از پایتون و ذخیره‌سازی در دیتابیس SQLite

این اسکریپت پایتون برای استخراج فایل‌های ZIP رمزگذاری شده و ذخیره‌سازی اطلاعات این فایل‌ها در یک دیتابیس SQLite طراحی شده است. این اسکریپت بررسی می‌کند که آیا فایل ZIP قبلاً در دیتابیس موجود است و تنها فایل‌های جدید را استخراج می‌کند.

ویژگی‌ها:
- یکپارچه‌سازی با دیتابیس: استفاده از SQLite برای نگهداری اطلاعات فایل‌های پردازش شده.
- مدیریت رمز عبور: تلاش برای استخراج فایل‌های ZIP با استفاده از یک لیست از رمزهای عبور.
- اعتبارسنجی فایل: اطمینان از معتبر بودن فایل‌های ZIP قبل از پردازش.
- مدیریت خطا: نادیده گرفتن فایل‌هایی که نمی‌توان پردازش کرد و حذف آن‌ها بر اساس ورودی کاربر.

پیش‌نیازها:
- پایتون 3.x
- کتابخانه pyzipper
- کتابخانه sqlite3 (به صورت پیش‌فرض با پایتون نصب است)

نصب:
1. کلون کردن مخزن:
   git clone https://github.com/programblack/unzip_move.git

2. نصب وابستگی‌ها:
   pip install pyzipper

استفاده:
1. آماده‌سازی دایرکتوری خروجی:
   مسیر دایرکتوری خروجی را که فایل‌ها در آن استخراج می‌شوند تنظیم کنید. مقدار path_to_output_directory را در اسکریپت با مسیر مورد نظر خود جایگزین کنید.

2. اجرای اسکریپت:
   python script.py

مروری بر اسکریپت:
- تنظیم دیتابیس: اسکریپت به دیتابیس SQLite (example.db) متصل شده و یک جدول (users) ایجاد می‌کند اگر وجود نداشته باشد.
- لیست رمزهای عبور: یک لیست از رمزهای عبور برای امتحان کردن روی فایل‌های زیپ.
- اعتبارسنجی فایل: بررسی می‌کند که آیا فایل دارای امضای ZIP است یا خیر.
- استخراج فایل‌های زیپ: تلاش می‌کند فایل زیپ را با استفاده از لیست رمزهای عبور استخراج کند.
- حذف فایل زیپ: فایل زیپ را حذف می‌کند.
- پیدا کردن فایل‌های زیپ: تمامی فایل‌های زیپ موجود در دایرکتوری جاری را پیدا می‌کند.
- بررسی وجود فایل در دیتابیس: بررسی می‌کند که آیا نام فایل زیپ در دیتابیس موجود است یا خیر.
- پردازش فایل‌های زیپ: هر فایل زیپ را پردازش می‌کند: بررسی می‌کند که آیا معتبر است و در دیتابیس موجود نیست، سپس تلاش برای استخراج آن.

اجرا
مسیر خروجی را تنظیم کرده، فایل‌های زیپ را پیدا کرده و آن‌ها را پردازش می‌کند.

output_directory = "path_to_output_directory"
zip_files = find_zip_files()
process_zip_files(zip_files, output_directory, List_passwords)
conn.close()

مشارکت
برای مشارکت در این پروژه می‌توانید یک pull request ایجاد کنید یا یک issue در GitHub باز کنید.

مجوز
این پروژه تحت مجوز MIT است.

مقدار path_to_output_directory را با مسیر واقعی که می‌خواهید فایل‌های ZIP در آن استخراج شوند جایگزین کنید. اسکریپت فایل‌های پردازش شده را رد می‌کند و از کاربر قبل از حذف هر فایلی که استخراج نشده است، تأیید می‌گیرد.
