# Tugas 3

## Jelaskan perbedaan antara JSON, XML, dan HTML!
Jawaban:<br/>
Javascript object notation (JSON) adalah suatu bahasa javascript untuk menyimpan dan mentransfer data. JSON memiliki beberapa keunggulan dibanding XML, seperti filenya yang memiliki ukuran yang lebih kecil dan kodenya readable sehingga mudah
bagi orang untuk membacanya.

Extensible markup language (XML) adalah suatu format yang menggunakan bahasa markup dan kegunaannya mirip seperti JSON, yaitu untuk menyimpan dan mentrasfer data. Penggunaan XML memudahkan dalam mentransfer data dari satu server ke server lain tanpa perlu mengganti format.

Hyper text markup language (HTML) adalah suatu format yang menggunakan bahasa markup. Berbeda dengan XML dan JSON, HTML merupakan
format yang digunakan untuk menampilkan data di website.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawaban:<br/>
Kita memerlukannya untuk bisa mengirimkan data yang diperlukan untuk suatu bagian pada sebuah platform dan juga bisa memodifikasi dan mengembalikannya lagi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Jawaban:<br/>
Saya membuat aplikasi bernama mywatchlist di dalam repositori tugas 2 saya sebelumnya. Setelah itu, Saya mengisi models saya dan menyiapkan suatu file json untuk menyimpan objek-objek models di mana datanya akan diperlukan untuk ditampilkan. Lalu, saya membuat fungsi di dalam views untuk menampilkan hal-hal yang dibutuhkan pada tugas 3 ini, yaitu menampilkan html, menampilkan data dalam format json, dan menampilkan data dalam format xml. Setelah itu, saya membuat routing agar fungsi-fungsi tersebut bisa terpanggil. Setelah semuanya selesai, saya push ke remote repository untuk bisa dideploy. Lalu, saya membuat unit test pada tests.py dengan membuat suatu class yang didalamnya berisi fungsi yang akan dijalankan untuk menjalankan testing. Setelah itu, saya push tests.py yang sudah dimodifikasi.

## Screenshot hasil postman
![postman_html](https://github.com/stenly10/stenly_tugas2/blob/main/mywatchlist/postman_html.png "postman_html")
![postman_json](https://github.com/stenly10/stenly_tugas2/blob/main/mywatchlist/postman_json.png "postman_json")
![postman_xml](https://github.com/stenly10/stenly_tugas2/blob/main/mywatchlist/postman_xml.png "postman_xml")
