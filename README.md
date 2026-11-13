# 🍵 KulitYea &mdash; 3D Interactive Packaging Prototype

Prototype 3D interaktif berbasis web untuk kemasan teh herbal celup kulit buah **KulitYea (Dried Tropical Peels Tea)**, dilengkapi dengan script automasi untuk Blender 3D (Cycles / EEVEE).

![Preview 3D Packaging](https://img.shields.io/badge/Prototype-3D%20Web-orange?style=for-the-badge)
![Blender Ready](https://img.shields.io/badge/Blender-3.x%20%7C%204.x-E87D0D?style=for-the-badge&logo=blender&logoColor=white)
![HTML5 / CSS3D](https://img.shields.io/badge/Engine-CSS%203D%20Hardware%20Accelerated-blue?style=for-the-badge)

---

## 🌟 Fitur Utama

- **Rotasi 360° Bebas (Orbit Control):** Pengguna dapat memutar box kemasan dari segala sudut pandang (depan, belakang, samping kiri, samping kanan, atas, dan bawah).
- **Preset Sudut Pandang Cepat:**
  - 📸 **Studio Hero 3D:** Sudut miring estetik khas showcase produk.
  - 🔲 **Tampak Depan & Belakang:** Memeriksa grafis utama dan deskripsi.
  - ◀️ **Tampak Samping Kiri:** Informasi *Cara Penyajian*, komposisi, dan perijinan.
  - ▶️ **Tampak Samping Kanan:** Informasi edukasi *Tahukah Kamu?* & khasiat kulit buah.
  - 🔼 **Tampak Atas:** Tutup atas dengan orientasi logo KulitYea.
  - 🔽 **Tampak Bawah:** Bagian alas kemasan.
- **4 Pilihan Varian Rasa Tropis:**
  - 🍊 **Tropical Orange** &mdash; Teh Ekstrak Kulit Jeruk
  - 🌺 **Tropical Dragon Fruit** &mdash; Teh Ekstrak Kulit Buah Naga
  - 🍇 **Tropical Mangosteen** &mdash; Teh Ekstrak Kulit Manggis
  - 🌰 **Tropical Snakeskin Fruit** &mdash; Teh Ekstrak Kulit Salak
- **Simulasi Buka Tutup Box:** Animasi interaktif untuk melihat tutup kemasan terangkat (*unboxing preview*).
- **Pencahayaan Studio & Bayangan Realistis:** Efek bayangan kontak lantai dan pencahayaan specular menyerupai hasil render software 3D.
- **Dukungan Blender Otomatis:** Termasuk script Python untuk merender mockup box di Blender secara otomatis.

---

## 📐 Spesifikasi Kemasan (Dieline Specs)

| Parameter | Keterangan |
| :--- | :--- |
| **Model Kemasan** | Straight Tuck Box (Carton) |
| **Dimensi Realistis** | **7.5 cm &times; 7.5 cm &times; 13.5 cm** (Rasio 1 : 1 : 1.8) |
| **Rekomendasi Bahan** | Ivory / Art Carton 310 gsm + Doff Lamination |
| **Kapasitas** | 25 Kantong Teh Celup (*Tea Bags*) |

---

## 🚀 Cara Menjalankan Prototype Web

### Opsi 1: Buka Langsung
Cukup klik ganda file `index.html` untuk langsung membukanya di browser apa pun (Google Chrome, Edge, Safari, Firefox). Tanpa perlu instalasi apa pun!

### Opsi 2: Jalankan Local Server
```bash
# Menggunakan Python
python -m http.server 8080

# Buka di browser:
# http://localhost:8080
```

---

## 🎨 Menjalankan di Blender 3D (Cycles / EEVEE)

File script automasi tersedia di `render_kulityea_blender.py`. Script ini akan otomatis membuat objek box beveled, menempelkan tekstur kemasan di setiap sisi, membuat panggung studio, mengatur pencahayaan 3-point light, dan mengarahkan kamera 85mm.

1. Buka aplikasi **Blender**.
2. Masuk ke workspace tab **Scripting**.
3. Klik **Open** &rarr; pilih file `render_kulityea_blender.py`.
4. Klik **Run Script** (atau tekan shortcut `Alt + P`).
5. Mockup studio 3D siap dirender!

---

## 📁 Struktur File

```
├── index.html                  # Aplikasi Web 3D Prototype Interaktif
├── render_kulityea_blender.py  # Script automasi untuk Blender 3D
├── textures/                   # Aset tekstur kemasan 6 sisi per varian
│   ├── orange_*.png
│   ├── dragonfruit_*.png
│   ├── mangosteen_*.png
│   ├── salak_*.png
│   └── data.json
└── README.md                   # Dokumentasi proyek
```

---

© 2026 KulitYea. All rights reserved.
