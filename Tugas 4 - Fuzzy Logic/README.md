# SISTEM PAKAR Fuzzy Logic

logika Fuzzy adalah teknik atau metode yang sering dipakai untuk mengatasi hal yang tidak pasti pada masalah – masalah yang mempunyai banyak jawaban
Study kasus yang menghitung waktu kelembaban dari beberapa faktor pendukung lainnya menggunakan algoritma Skfuzzy
Tingkat Kelembaban dinilai berdasarkan 3 penilaian yaitu temperature, moisture, humidity 

RULENYA :
```
rule1 = temprature['poor'] | moisture['poor'] | humidity['poor'], minutes['low']
rule2 = temprature['average'] | moisture['average'] | humidity['average'], minutes['medium']
rule3 = temprature['good'] | moisture['good'] | humidity['good'], minutes['high']
```

Penentuan Waktu Kelembaban berdasarkan Rules(aturan) yang dibuat diatas yaitu
```
JIKA temperature rendah atau moisture rendah atau humidity rendah, MAKA Waktu kelembaban Semakin KECIL. 
JIKA temperature sedang atau moisture sedang atau humidity Sedang, MAKA Waktu kelembaban Semakin SEDANG. 
JIKA temperature Tinggi atau moisture Tinggi atau humidity Tinggi, MAKA Waktu kelembaban Semakin TINGGI. 
```
Contoh pemberian penilaian temperature, moisture dan humidity untuk menentukan waktu kelembaban :
```
temperature = 1
moisture = 1
humidity = 1
```
Maka Waktu Kelembaban yang harus dilaju menurut rule yang telah dibentuk adalah 8.085852534617038
