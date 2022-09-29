# Tugas 4

## Apa kegunaan '```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Kegunaannya adalah untuk memberikan proteksi agar melindungi dari serangan <i> cross site request forgery</i>. Akan terjadi error apabila tidak ada potongon kode ```{% csrf_token %}``` pada elemen ```<form>```.

##  Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }}```)? Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.
Bisa. Kita dapat membuat form secara manual dengan membuat input tag beserta labelnya. Input tag berfungsi untuk mengambil input user.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama-tama kita mengambil data dari form yang telah diisi oleh user dan membentuknya menjadi objek yang akan di simpan di database. Data yang telah disimpan di database akan bisa diambil di dalam views dan dikirim ke template untuk ditampilkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama-tama saya membuat aplikasi bernama todolist di repository tugas sebelumnya. Lalu, saya membuat path untuk todolist agar todolist dapat diakses dan membuat model Task. Setelah itu, saya menambahkan method-method untuk di views, membuat routing agar bisa menjalankan method-method di views, dan membuat template yang akan ditampilkan.<br\>
Untuk membuat suatu task baru, pertama-tama saya membuat file python baru bernama forms.py yang berisi class bernama FormForTask yang merupakan inheritance dari django.forms.Form. Saya membuat method create_task di dalam views di mana method ini berfungsi untuk menghasilkan form baru dari class FormForTask yang digunakan untuk mengambil input user dan membuat objek Task baru berdasarkan input user di dalam form. Saya juga membuat template create_task.html untuk menampilkan form pembuatan task baru. Setelah semuanya selesai dibuat, saya melakukan push ke remote repository dan melakukan deployment ke Heroku. Setelah itu, saya membuat dua akun pengguna dan 3 dummy task di dalam aplikasi saya.