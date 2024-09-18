URL PWS: http://muhammad-yahya32-sigmart.pbp.cs.ui.ac.id/

1. Bagaimana step by step saya mengerjakan tugas ini.
- Membuat sebuah proyek Django baru.
Dengan menginisiasi Django di folder lokal menggunakan prompt 
- Membuat aplikasi dengan nama main pada proyek tersebut.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib nama, harga, dan deskripsi.
- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git merupakan sistem yang berfungsi sebagai version control. Version control secara singkat adalah sistem yang memudahkan pengembang perangkat lunak untuk melacak perubahan yang terjadi dalam kodenya serta dapat kembali ke versi kode yang diinginkan jika terjadi kesalahan dalam pengembangan.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django merupakan framework yang sederhana dalam penggunaannya dan memprovide banyak fitur yang memudahkan web developer pemula dalam membuat website. Misalnya, Django menyediakan manajemen URL dan routing, serta model ORM yang sederhana. Selain itu, framework MTV Django melatih web developer untuk melakukan best practice dalam web development, dengan memisahkan logika data (backend), logika tampilan website, dan alur kerja website yang dibuat. Alasan lainnya adalah karena Django memiliki dokumentasi yang lengkap yang memudahkan pemula untuk membangun web pertamanya. Django juga dilengkapi dengan keamanan bawaan untuk menghalau serangan siber yang sering terjadi lewat website.

5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ini untuk menghubungkan objek-objek di aplikasi Python dengan tabel-tabel di database. ORM memungkinkan developer bekerja dengan database menggunakan kode Python tanpa harus menulis query SQL secara langsung. Setiap model Django mewakili sebuah tabel dalam database, dan setiap atribut pada model mewakili kolom dalam tabel tersebut. Dengan ORM, kita dapat melakukan operasi seperti membaca, menulis, memperbarui, atau menghapus data di database hanya dengan menggunakan metode dan objek Python, sehingga mempermudah integrasi antara kode aplikasi dan sistem manajemen database (DBMS).

Tugas 3:
 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam pengembangan platform, data delivery sangat penting karena memungkinkan pertukaran informasi antara berbagai komponen sistem, baik itu antara server dan klien maupun antar layanan dalam sistem yang kompleks. Tanpa mekanisme pengiriman data yang efisien, platform tidak bisa berfungsi dengan baik, terutama ketika pengguna membutuhkan informasi secara real-time. Data delivery memastikan bahwa data dikirim, diterima, dan diproses dengan cepat dan aman sehingga platform dapat memberikan pengalaman yang mulus bagi penggunanya.

 Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON dianggap lebih baik dibandingkan XML dalam banyak situasi modern karena JSON lebih ringan, lebih mudah dibaca oleh manusia, dan lebih mudah diuraikan oleh mesin. JSON menggunakan lebih sedikit karakter dan tidak memerlukan tag penutup yang rumit seperti XML, sehingga lebih efisien dalam hal penyimpanan dan transmisi data. Selain itu, karena JSON adalah format native untuk JavaScript, JSON sangat cocok untuk aplikasi web modern. XML masih digunakan di beberapa domain seperti sistem warisan atau dokumen kompleks, tetapi popularitas JSON meningkat karena kesederhanaan dan kompatibilitas yang lebih baik dengan teknologi web saat ini.

 Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

 Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang diinput ke dalam form sudah sesuai dengan aturan validasi yang telah ditentukan. Jika data valid, method ini akan mengembalikan nilai True dan form akan menyimpan data yang sudah dibersihkan (cleaned data). Kita memerlukan method ini agar form bisa memproses data yang sesuai standar sebelum disimpan ke database atau digunakan lebih lanjut, menghindari kesalahan atau serangan yang mungkin terjadi akibat input yang tidak valid atau berbahaya.

 Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token dibutuhkan pada form di Django untuk mencegah serangan CSRF (Cross-Site Request Forgery), di mana penyerang dapat mengirimkan permintaan berbahaya yang tampak seperti berasal dari pengguna sah. Jika kita tidak menambahkan csrf_token, form kita menjadi rentan terhadap serangan ini, di mana penyerang bisa memanfaatkan kelemahan tersebut untuk mengakses atau memanipulasi data sensitif tanpa sepengetahuan pengguna. Dengan menambahkan csrf_token, server memastikan bahwa setiap permintaan form benar-benar berasal dari pengguna yang mengakses situs secara sah.

 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

 ![XML](images/img.jpg)
 ![JSON](images/img.jpg)
 ![XML by ID](images/img.jpg)
 ![JSON by ID](images/img.jpg)