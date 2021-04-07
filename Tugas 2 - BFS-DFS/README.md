#SISTEM PAKAR BFS dan DFS

Analisis PROGRAM BFS

Pada Baris 8-14 
```
Grafik yang diilustrasikan diwakili menggunakan daftar yang berdekatan. Cara mudah untuk melakukan ini di Python adalah dengan menggunakan struktur data kamus, di mana setiap vertex memiliki daftar node yang berdekatan.
```

Pada Baris 17
```
visited ;  adalah daftar yang digunakan untuk melacak node yang dikunjungi
```

Pada Baris 18 
```
queue ; adalah daftar yang digunakan untuk melacak node yang saat ini dalam antrian
```

Pada Baris 35
```
Argumen fungsi berisi daftar, bentuk kamus, dan node awal .bfs visited graph 1
```

Pada Baris 20-31
```
Mengikuti algoritma yang dijelaskan di atas :bfs
Pertama memeriksa dan menambahkan node awal ke daftar .visited .queue, bfs akan mencari dan memproses berdasarkan level bukan kedalaman.
Kemudian, menunggu antrian berdasarkan level dimulai dari '1' berada di level 0, dan mengeluarkan node yaitu 1 dari antrian,  dan menambahkan node lain atau level dibawahnya ke antrian, dan menandai node yang telah dikunjungi atau dilewati.
Ini berlanjut hingga antrean kosong.
Contoh : Node 1 di level 0 apabila sudah tidak ada node dilevel 0 maka akan menuju level 1 yang memiliki node dan jika sudah tidak ada node lagi di level 1 maka akan seperti itu seterusnya, berdasarkan level, level 0 :1
level 1 :3-2
level 2 :6-4-5 
Outputnya : 1-3-2-6-4-5
```


Analisis PROGRAM DFS

Pada Baris 41
```
adalah satu set yang digunakan untuk melacak node yang dikunjungi.
```

Pada Baris 43-52
```
Mengikuti algoritma yang dijelaskan di atas: dfs akan memproses berdasarkan kedalaman bukan level
Pertama-tama memeriksa apakah node saat ini tidak terlihat - jika ya, itu ditambahkan dalam set.visited
Contoh : pada node 1 akan dicek kedalaman dari node tersebut dan ditandai, 1 - 3 - 6 dilanjutkan 2 - 4 - 5 
Kemudian untuk setiap node saat ini, fungsi dipanggil lagi di .dfs
dan akan dipanggil ketika semua node dikunjungi. Fungsi kemudian kembali dan hingga semua node berhasil diproses diantrian.
```

Pada Baris 52
```
Fungsi ini dipanggil dan dilewatkan set, dalam bentuk kamus, dan , yang merupakan node awal.dfs visited graph 1
```