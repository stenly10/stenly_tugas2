https://stenlytugas2.herokuapp.com/todolist
# Tugas 4

## Apa kegunaan '```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Kegunaannya adalah untuk memberikan proteksi agar melindungi dari serangan <i> cross site request forgery</i>. Akan terjadi error apabila tidak ada potongon kode ```{% csrf_token %}``` pada elemen ```<form>```.

##  Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }}```)? Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.
Bisa. Kita dapat membuat form secara manual dengan membuat input tag beserta labelnya. Input tag berfungsi untuk mengambil input user.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama-tama kita mengambil data dari form yang telah diisi oleh user dan membentuknya menjadi objek yang akan di simpan di database. Data yang telah disimpan di database akan bisa diambil di dalam views dan dikirim ke template untuk ditampilkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama-tama saya membuat aplikasi bernama todolist di repository tugas sebelumnya. Lalu, saya membuat path untuk todolist agar todolist dapat diakses dan membuat model Task. Setelah itu, saya menambahkan method-method untuk di views, membuat routing agar bisa menjalankan method-method yang ada di views, dan membuat template yang akan ditampilkan. Untuk membuat suatu task baru, pertama-tama saya membuat file python baru bernama forms.py yang berisi class bernama FormForTask yang merupakan inheritance dari django.forms.Form. Saya membuat method create_task di dalam views di mana method ini berfungsi untuk menghasilkan form baru dari class FormForTask yang digunakan untuk mengambil input user dan membuat objek Task baru berdasarkan input user di dalam form. Saya juga membuat template create_task.html untuk menampilkan form pembuatan task baru. Setelah semuanya selesai dibuat, saya melakukan push ke remote repository dan melakukan deployment ke Heroku. Setelah itu, saya membuat dua akun pengguna dan 3 dummy task di dalam aplikasi saya.


# Tugas 5
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style
Inline: penggunaan style CSS di dalam suatu html tag<br>
Kelebihan: Bisa diterapkan langsung ke dalam kode yang ingin di pakaikan style CSS<br>
Kelemahan: Style tidak bisa digunakan untuk kode lainnya<br>
Internal: penggunaan style CSS di dalam file html dengan html tag style <br>
Kelebihan: Bisa menggunakan style CSS tanpa perlu membuat file css baru <br>
Kelemahan: Hanya bisa digunakan untuk file html tersebut.<br>
External: Penggunaan style css dengan membuat file css baru
Kelebihan: Style CSS yang dibuat bisa diterapkan untuk semua file html yang link dengan CSS tersebut
Kelemahan: Perlu untuk membuat file CSS baru meskipun hanya menggunakannya untuk 1 kode saja.

## Jelaskan tag HTML5 yang kamu ketahui.
1. ```<h1>```: untuk membuat paragraf baru<br>
2. ```<button>``` untuk membuat suatu button<br>
3. ```<body>``` untuk membuat bagian body file html<br>

## Jelaskan tipe-tipe CSS selector yang kamu ketahui
1. .class<br>
contoh: .login<br>
kegunaan: Untuk memilih elemen-elemen di dalam class login<br>
2. p<br>
Kegunaan: Untuk memilih elemen-elemen p

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Saya membuat file CSS bernama style1.css untuk mengkustomisasi template-template dari todolist.
2. Saya menggunakan bootstrap untuk membuat card yang berisikan task
3. Untuk membuat responsive saya menggunakan bootstrap yang sudah dipakaikan di base.html yang berada pada folder templates di repository tugas saya.