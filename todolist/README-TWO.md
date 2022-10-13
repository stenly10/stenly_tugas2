# Tugas 6

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming memungkinkan proses-proses yang berhubungan bisa berjalan tanpa perlu menunggu proses sebelumnya selesai, sedangkan synchronous programming hanya bisa menjalankan satu proses dalam satu waktu.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven-Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah paradigma programming di mana adanya event yang menjadi sebuah trigger untuk menjalankan suatu proses. Salah satu contohnya pada tugas ini adalah pada tombol get task yang menjadi trigger untuk mengambil task yang baru dibuat.

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX adalah dapatnya mengganti isi dari template tanpa perlunya mereload keseluruhan template.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. AJAX GET <br>
Saya membuat penerapan AJAX GET untuk mengambil task yang baru dibuat. Saya menerapkannya dengan membuat script AJAX dengan JQuery yang berada pada bagian block meta. Saya menggunakan method .get pada penerapan ini. Namun sebelumnya, saya membuat view untuk bisa mengambil HTTP response json yang mana datanya akan digunakan dalam proses pembaruan isi template beserta membuat routing agar view dapat diakses. Script akan dijalankan apabila button get task diclick yang menjadi trigger.<br>
2. AJAX POST <br>
Saya membuat penerapan AJAX POST untuk membuat suatu task baru. Saya menerapkannya dengan membuat script AJAX dengan JQuery yang berada pada bagian block meta. Saya menggunakan method .post pada penerapan ini. Namun sebelumnya, saya membuat view untuk membuat task baru dan akan diakses lewat AJAX POST beserta membuat routing agar view dapat diakses. Saya juga membuat modal yang akan dijadikan tempat untuk mengisi title dan description dari task baru. Modal akan muncul saat button Add Task diclick yang menjadi trigger. Setelah user mengisi form di modal, user klik make untuk membuat task baru dan setelah itu modal akan otomatis tertutup. Isi dari form akan diolah menjadi sebuah task baru di dalam view. Hasil task baru dapat dilihat dengan mengklik tombol get task.
