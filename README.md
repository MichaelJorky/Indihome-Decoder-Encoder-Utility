# Indihome Decoder & Encoder Utility

> ⚠️ **Peringatan**
> Alat ini dibuat **hanya untuk keperluan pendidikan dan penelitian**.
> Penulis **tidak bertanggung jawab** atas penyalahgunaan, kerusakan perangkat, maupun kerugian lain yang disebabkan oleh penggunaan tool ini.
> Gunakan **hanya pada perangkat milik Anda sendiri** atau perangkat yang Anda miliki izin eksplisit untuk mengaksesnya.

Utilitas ini digunakan untuk **mendecode dan mengencode file konfigurasi** dari router Indihome (Fiberhome, Huawei, dan ZTE).

💡 **Versi aplikasi GUI tersedia di sini:**
[https://github.com/MichaelJorky/Indihome-Router-Utility](https://github.com/MichaelJorky/Indihome-Router-Utility)

---

## 📱 Instalasi

### 1. Android (Termux)

```bash
apt update
apt install termux-api termux-am
termux-setup-storage
pkg install mc
mc  # membuka file explorer berbasis terminal
pkg install git python python-pip
python -m pip install setuptools
git clone https://github.com/MichaelJorky/indihome-router-decoder.git .zte-decoder
cd .zte-decoder
python setup.py install
```

### 2. Windows

1. Backup config router via browser (misal `192.168.1.1`) menggunakan:

   * admin / admin
   * user / user

2. Catat informasi router:

   * MAC: `AA:BB:CC:DD:EE:FF`
   * Serial: `ZTE123456789`
   * Model: `F670L`
   * Signature: `ZXHN F670L V9.0`

3. Instal Python & Git:

   * Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   * Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

4. Clone repository & instal dependencies:

```bash
git clone https://github.com/MichaelJorky/indihome-router-decoder.git .zte-decoder
cd .zte-decoder
python -m pip install pycryptodome pycryptodomex setuptools selenium
python -m pip install -r requirements.txt
```

5. Pindahkan file `config.bin` ke folder:

```
C:\Users\Nama_User\.zte-decoder\config\
```

6. Jalankan script:

```bash
cd .zte-decoder
python decoder.py config/config.bin config/output.xml
python encoder.py config/config.xml config/new.config.bin
```

### 3. Kali Linux / Linux

```bash
sudo apt update
sudo apt install python3 python3-pip git
python3 -m pip install --user setuptools pycryptodome pycryptodomex selenium
git clone https://github.com/MichaelJorky/indihome-router-decoder.git ~/.zte-decoder
cd ~/.zte-decoder
python3 setup.py install
```

Menjalankan decoder sama seperti di Windows / Termux:

```bash
python3 decoder.py config/config.bin config/output.xml
```

---

## 🔓 Decoder

**Kompatibel dengan router:**
ZTE F670L, F609, F660, F450, F460, MF283, F663, GM220, F600W, H108N,
H168N, H267A, H298N, H201L, H298Q, H298A, H268Q

### 🆕 Contoh Perintah Decoder (Metode Terbaru)

**1. Auto Mode (Default): normal → skip145 → trykeys**

```bash
python decoder.py config/config.bin config/output.xml
```

**2. Mode Normal (baca header biasa)**

```bash
python decoder.py config/config.bin config/output.xml --mode normal
```

**3. Paksa mode skip145 (mulai dari offset 145)**

```bash
python decoder.py config/config.bin config/output.xml --mode skip145
```

**4. Mode Aggressive: coba semua key & metode**

```bash
python decoder.py config/config.bin config/output.xml --mode trykeys
```

**5. Aktifkan verbose logging**

```bash
python decoder.py config/config.bin config/output.xml --verbose
```

**6. Simpan log ke file**

```bash
python decoder.py config/config.bin config/output.xml --log-file config/output.txt
```

**7. Decode + auto-extract + auto-check login**

```bash
python decoder.py config/config.bin config/output.xml --check-login http://192.168.1.1
```

### 📘 Daftar Opsi Lengkap Decoder

Untuk opsi terbaru & lengkap:

```bash
python decoder.py --help
```

---

## 🔐 Encoder

🚧 **Coming Soon** — Encoder versi terbaru (v2) sedang dalam pengembangan.
Fitur baru akan diumumkan setelah implementasi selesai.

Untuk referensi opsi sementara / development:

```bash
python encoder.py --help
```

---

## 🛠 Roadmap Development

* **Decoder v2** → Versi saat ini, sudah mendukung metode terbaru `normal`, `skip145`, `trykeys`, auto-check login, verbose & log file.
* **Encoder v2** → Sedang dikembangkan, akan menggantikan encoder lama. Fitur:

  * Dinamis & unified (`encoder.py`)
  * Mendukung semua router yang kompatibel
  * Integrasi auto-check & auto-signature
  * GUI versi aplikasi

---

