Link ke Heroku = https://stenlytugas2.herokuapp.com/katalog/
![bagan](https://github.com/stenly10/stenly_tugas2/blob/main/katalog/bagan.jpg "bagan")


Jelaskan kenapa menggunakan virtual environment?
Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawaban:
Kita menggunakan virtual environment agar aplikasi yang kita buat dapat di-edit dan dijalankan sesuai dengan versinya
sehingga tidak bentrok dengan versi lain yang kita punyai, contohnya di aplikasi lain.
kita tetap bisa membuat aplikasi web berbasis django tanpa menggunakan virtual environment.


Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Jawaban:
Poin 1:
Saya membuat sebuah fungsi bernama show_katalog dengan parameter request. Fungsi ini bertujuan untuk mengambil request
dan mengembalikan suatu respons yang akan ditampilkan di web. Di dalam fungsi ini, terdapat dua variabel, yaitu
data_barang_katalog dan context yang menyimpan value yang digunakan di template.

Poin 2:
Saya membuat suatu routing ke fungsi show_katalog yang ada di view agar fungsi tersebut bisa digunakan.
Routing tersebut berada di dalam file urls.py yang berada pada folder yang sama.

Poin 3:
Saya membuat suatu file html yang berfungsi untuk menjadi tampilan dari web yang ingin saya buat. File tersebut 
berada di folder template. Di dalam file html tersebut, terdapat pemetaan data dengan sintaks django untuk mengambil value yang
sesuai dengan apa yang dipanggil dan bisa ditampilkan. Pemetaan data tersebut dibuat di file views.py dan digunakan pada template.

Poin 4:
Saya membuat suatu aplikasi di heroku bernama stenlytugas2. Lalu, saya membuat dua repository secret, satu untuk heroku API key aplikasi dan satu untuk nama aplikasi. Setelah itu, aplikasi bisa dilihat dengan mengakses ke link aplikasi tersebut.