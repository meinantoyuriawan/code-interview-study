# Astronaut Portals

### Problem Description

Terdapat sejumlah N astronaut dan portal dengan label [0, N-1] Inklusif. Setiap portal memiliki power level direpresentasikan dalam Array *`portals` dengan `portals[i]`* menyatakan power level pada portal dengan label `i`. Untuk dapat berpindah dari portal satu ke portal lain, setiap astronaut harus memakai suatu rompi yang memiliki power dengan nilai `K`. Astronaut hanya dapat berpindah dari portal awal ke portal tujuan dengan kondisi perbedaan power level kedua portal tersebut kurang dari atau sama dengan `K`. 

Pada kasus ini, setiap astronaut akan diberi tugas untuk mengunjungi portal target dengan label yang sama dengan label astronaut. Sebagai contoh, astronaut `0` akan mengunjungi portal dengan label `0`. Untuk titik keberangkatannya, telah disediakan dua buah portal dengan power level `P1` dan `P2` . Masing-masing astronaut bebas menentukan portal keberangkatannya.

Tujuan yang diminta pada kasus ini adalah berapa minimum kekuatan rompi `K` untuk setiap astronaut agar dapat mengunjungi portal tujuannya?

---

### Example Walkthrough

Sebagai contoh terdapat sejumlah N=5 astronaut dan `portals = [1,3,10,4,9]` . Portal keberangkatan yang disediakan adalah `P1=4` dan `P2=7`. Kita akan mengambil contoh untuk astronaut `2`.

1. Astronaut memilih portal keberangkatan `P2` dan menuju ke portal `4` yang memiliki power level `9` . Untuk bisa teleport, maka astronaut harus memakai rompi dengan level `|9-7| = 2`
2. Kemudian astronaut teleport ke portal `2` yang memiliki power level `10` . Untuk bisa teleport, maka astronaut harus memakai rompi dengan level minimal `|10-9|=1`
3. Karena astonaut sudah sampai di portal tujuan, maka  level rompi yang harus dikenakan agar adalah `Max[1,2] = 2` . Dengan demikian, dibutuhkan rompi dengan minimal power `2` agar astronaut `2` dapat teleport ke portal `2`.

Untuk astronaut `0, 1, 3 , 4` bisa jadi membutuhkan rompi dengan power level yang berbeda.
---
### Input and Output
Pada setiap `file` test case, baris pertama menyatakan jumlah test case. Setiap test case terdiri dari dua baris input. input baris pertama secara berurutan menyatakan `N` jumlah astronaut dan portal, `P1` power level portal keberangkatan `1` dan `P2` power level portal keberangkatan `2`. Input baris kedua menyatakan list atau array dari power level tiap portal.

Example:

Input 1
```
2
5 2 11
8 4 14 1 13
12 5 15
16 18 4 9 5 10 6 13 1 0 19 1
```
- T = 2
- Testcase 1
  - N = 5
  - P1 = 2
  - P2 = 11
  - portals = [8, 4, 14, 1, 13]
- Testcase 2
  - N = 12
  - P1 = 5
  - P2 = 15
  - portals = [16, 18, 4, 9, 5, 10, 6, 13, 1, 0, 19, 1]

Output file berisi sejumlah T baris yang tiap barisnya menyatakan array dari level rompi yang dibutuhkan tiap astronaut

Example:
```
3 2 2 1 2
1 2 1 3 0 3 1 2 3 3 2 3
```
- Output testcase 1 = [3, 2, 2, 1, 2]
- Output testcase 2 = [1, 2, 1, 3, 0, 3, 1, 2, 3, 3, 2, 3]