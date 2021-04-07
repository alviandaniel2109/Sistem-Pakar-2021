# SISTEM PAKAR Naive Bayes

Naive Bayes adalah algoritme klasifikasi yang paling mudah dan cepat, yang cocok untuk sebagian besar data. Pengklasifikasi Naive Bayes berhasil digunakan dalam berbagai aplikasi seperti pemfilteran spam, klasifikasi teks, analisis sentimen, dan sistem pemberi rekomendasi. Ini menggunakan teorema Bayes tentang probabilitas untuk prediksi kelas yang tidak diketahui

# Analisis PROGRAM

Pada Baris 1-4 
```
Merupakan Syntax dalam memanggil function dalam Library yang dibutuhkan seperti function : datasets, train_test_split, GaussianNB(naive bayes), metrics  
```

Pada Baris 7
```
Melakukan Load dataset yaitu diambil dari dataset breast cancer milik library sklearn
```

Pada Baris 10-14 
```
Menampilkan features name dan target name dari datasets breast cancer yang telah didefenisikan menjadi cancer
```

Pada Baris 17-24
```
Line 17 : Menampilkan data feature dalam bentuk shape
Line 19 : Menampilkan data dari 0 atau awal sampai 5 data terakhir dari data
Line 22 : Menampilkan target yaitu labels yang akan digunakan untuk dilakukan train data cancer
```

Pada Baris 28 
```
Melakukan training data yaitu cancer.data, dengan labels dengan size test 0,3 , dengan random state atau nomor acak semu yaitu 100
```

Pada Baris 32
```
Membuat dan Melakukan Classifier Gaussian yang telah disediakan sklearn, dan mendefenisikannya menjadi gnb
```

Pada Baris 35
```
Melakukan Training data set menggunakan model training data X_train, dan y_train
```

Pada Baris 38
```
Setelah melakukan training kita akan melakukan Predict atau prediksi terhadap data yang telah di train dan memasukkannya pada X_test
```

Pada Baris 41
```
Menampilkan score accuracy dan hasil classifier dan output y_test dan y_pred
```

# Output

Dimana dari metode naive bayes output 0 berarti orang yang tidak terkena penyakit cancer breast dan 1 untuk orang yang terkena penyakit cancer breast
