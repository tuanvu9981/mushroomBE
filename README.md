## Mushroom classification (CLSF) backend

### Chú ý, trước khi đẩy code lên github cần xóa bỏ secret code ở file ***settings.py*** 

### Những câu lệnh cơ bản để khởi tạo dự án 
* Cài đặt gói 
```
tuanvu@:~/PycharmProjects$ sudo apt install python3-django
```
* Tạo project 
```
tuanvu@:~/PycharmProjects$ django-admin startproject djangoBE
```

* Một project django có thể chứa rất nhiều app. Mỗi app lại chứa các thành phần riêng biệt như migrations riêng, url và views riêng 
* Khởi tạo 1 app trong 1 project như sau: 
```
tuanvu81@host81:~/PycharmProjects$ cd djangoBE/
tuanvu81@host81:~/PycharmProjects/djangoBE$ python3 manage.py startapp mushroomCLSF
```

* Khởi chạy app
```
tuanvu81@host81:~/PycharmProjects/djangoBE$ python3 manage.py runserver
```

* Ứng dụng khởi chạy mặc định ở cổng 8000 của localhost

* Ghi lại các dependencies vào file 
```
python3 -m pip freeze > requirements.txt
```

* Clone về, tự động cài đặt như npm install:
```
python3 -m pip install -r requirements.txt
```