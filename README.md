# Indihome Decoder & Encoder Utility

> ⚠️ **Peringatan**
> Alat ini dibuat **hanya untuk keperluan pendidikan dan penelitian**.
> Penulis **tidak bertanggung jawab** atas penyalahgunaan, kerusakan perangkat, maupun kerugian lain yang disebabkan oleh penggunaan tool ini.
> Gunakan hanya pada perangkat milik Anda atau yang Anda memiliki izin untuk mengaksesnya.

Tool ini digunakan untuk **mendecode dan mengencode file konfigurasi** dari router ZTE Indihome.

💡 **GUI version tersedia di sini:**
[Indihome Router Utility](https://github.com/MichaelJorky/Indihome-Router-Utility)

---

## ⚙️ Instalasi

## ✅ **ANDROID (TERMUX)**

#### 1. Update package list
```bash
apt update
```
#### 2. Upgrade package
```bash
apt upgrade -y
```
#### 3. Install Termux API (opsional)
```bash
apt install termux-api
```
#### 4. Install termux-am (opsional)
```bash
apt install termux-am
```
#### 5. Beri izin storage
```bash
termux-setup-storage
```
#### 6. Install file manager (opsional)
```bash
pkg install mc
```
#### 7. Install Git
```bash
pkg install git
```
#### 8. Install Python
```bash
pkg install python
```
#### 9. Install pip
```bash
pkg install python-pip
```
#### 10. Upgrade pip, setuptools, wheel
```bash
python -m pip install --upgrade pip setuptools wheel
```
#### 11. Clone repository
```bash
git clone https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility.git .indihome-utility
```
#### 12. Masuk folder project
```bash
cd .indihome-utility
```
#### 13. Install dependency dari requirements.txt
```bash
python -m pip install -r requirements.txt
```
#### 14. Install utility
```bash
python setup.py install
```

## ✅ **WINDOWS**

> Via PowerShell atau CMD
> Jangan lupa Python & Git sudah terpasang.

#### 1. Clone repository
```powershell
git clone https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility.git .indihome-utility
```
#### 2. Masuk folder project
```powershell
cd .indihome-utility
```
#### 3. Upgrade pip, setuptools, wheel
```powershell
python -m pip install --upgrade pip setuptools wheel
```
#### 4. Install dependency dari requirements.txt
```powershell
python -m pip install -r requirements.txt
```
#### 5. Install utility
```powershell
python setup.py install
```

## ✅ **LINUX / KALI**

#### 1. Update repo
```bash
sudo apt update
```
#### 2. Install Python & pip
```bash
sudo apt install python3
```
```bash
sudo apt install python3-pip
```
#### 3. Install Git
```bash
sudo apt install git
```
#### 4. Install build tools (penting untuk pycryptodome, impacket, dll)
```bash
sudo apt install build-essential
```
```bash
sudo apt install libssl-dev
```
```bash
sudo apt install libffi-dev
```
```bash
sudo apt install python3-dev
```
#### 5. Clone repository
```bash
git clone https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility.git ~/.indihome-utility
```
#### 6. Masuk folder project
```bash
cd ~/.indihome-utility
```
#### 7. Upgrade pip, setuptools, wheel (mode user)
```bash
python3 -m pip install --user --upgrade pip setuptools wheel
```
#### 8. Install dependency dari requirements.txt
```bash
python3 -m pip install --user -r requirements.txt
```
#### 9. Install utility
```bash
python3 setup.py install --user
```

> ✅ Setelah setup selesai, semua file (decoder.py & encoder.py) akan tersedia di folder lokal `.indihome-utility` dan bisa dijalankan langsung.

---

## 🔓 Decoder

**Kompatibel dengan router:**
F620, F660 V2, F670, F670L, F670 V2, F609, F660, F450, F460, MF283, F663, GM220, F600W, H108N,
H168N, H267A, H298N, H201L, H298Q, H298A, H268Q, F680, F688, OEM ZTE (Indihome, PLDT, GLOBE)

### **Contoh Perintah Decoder (v2)**

#### **Auto mode (default)**

```bash
python decoder.py config/config.bin config/output.xml
```

#### **Normal mode (baca header biasa)**

```bash
python decoder.py config/config.bin config/output.xml --mode normal
```

#### **Skip145 mode (mulai dari offset 145)**

```bash
python decoder.py config/config.bin config/output.xml --mode skip145
```

#### **Trykeys mode (agresif, semua metode & key)**

```bash
python decoder.py config/config.bin config/output.xml --mode trykeys
```

#### **Verbose logging**

```bash
python decoder.py config/config.bin config/output.xml --verbose
```

#### **Logfile**

```bash
python decoder.py config/config.bin config/output.xml --log-file config/output.txt
```

#### **Decode + auto-extract + auto-check login**

```bash
python decoder.py config/config.bin config/output.xml --check-login http://192.168.1.1
```

**Daftar opsi lengkap:**

```bash
python decoder.py --help
```

---

## 🔐 Encoder

### **📦 Contoh Perintah Encoder (Type 0 – 6)/(v2)**

---
#### **🟦 Type 0 — RAW (Tanpa Kompresi / Tanpa Enkripsi)**
#### Raw tanpa kompresi
```bash
python encoder.py --xml config/output.xml --out config/type0_raw.bin --payload-type 0 --compress none --verbose
```
#### Dengan kompresi zlib (tetap tidak dienkripsi)
```bash
python encoder.py --xml config/output.xml --out config/type0_zlib.bin --payload-type 0 --verbose
```
---
#### **🟩 Type 1 — Compressed Only (Tidak Dienkripsi)**
#### zlib (default)
```bash
python encoder.py --xml config/output.xml --out config/type1_zlib.bin --payload-type 1 --verbose
```
#### LZMA compression
```bash
python encoder.py --xml config/output.xml --out config/type1_lzma.bin --payload-type 1 --compress lzma --verbose
```
---
#### **🟧 Type 2 — AES-ECB**
#### Key HEX
```bash
python encoder.py --xml config/output.xml --out config/type2_ecb.bin --payload-type 2 --key 11223344556677889912345678912345 --verbose
```
#### Key ASCII
```bash
python encoder.py --xml config/output.xml --out config/type2_ecb_ascii.bin --payload-type 2 --key my16bytekey1234 --verbose
```
---
#### **🟨 Type 3 — AES-CBC (Variant 1)**
Sama seperti Type-4, bedanya pada header format.
#### Menggunakan serial + mac (KP derivation)
```bash
python encoder.py --xml config/output.xml --out config/type3_auto_kp.bin --payload-type 3 --serial ZTE123456789 --mac AA:BB:CC:11:22:33 --verbose
```
#### Key manual + IV manual
```bash
python encoder.py --xml config/output.xml --out config/type3_manual.bin --payload-type 3 --key 00112233445566778899AABBCCDDEEFF --iv 0102030405060708090A0B0C0D0E0F --verbose
```
---
#### **🟥 Type 4 — AES-CBC (Variant 2, paling umum untuk GPON lama)**
#### Menggunakan serial + mac (auto key derivation)
```bash
python encoder.py --xml config/output.xml --out config/type4_auto_kp.bin --payload-type 4 --serial ZTE123456789 --mac AA:BB:CC:11:22:33 --verbose
```
#### Key manual
```bash
python encoder.py --xml config/output.xml --out config/type4_manual.bin --payload-type 4 --key 11223344556677889900AABBCCDDEEFF --iv 000102030405060708090A0B0C0D0E0F --verbose
```
---
#### **🟪 Type 5 — AES-CBC (Strict Manual Key/IV)**
Tidak memakai KP derivation, wajib key manual.
#### Key HEX + IV HEX
```bash
python encoder.py --xml config/output.xml --out config/type5_manual.bin --payload-type 5 --key 00112233445566778899AABBCCDDEEFF --iv 0102030405060708090A0B0C0D0E0F --verbose
```
#### Key ASCII + IV default
```bash
python encoder.py --xml config/output.xml --out config/type5_ascii.bin --payload-type 5 --key mysecretkey12345 --verbose
```
---
#### **🟫 Type 6 — AES-CBC + Template Header Injection (GPON produksi baru)**
#### Derivasi key via serial + mac
```bash
python encoder.py --template config/config.bin --xml config/output.xml --out config/type6_auto_kp.bin --payload-type 6 --serial ZTE123456789 --mac AA:BB:CC:11:22:33 --verbose
```
#### Manual key untuk Type-6
```bash
python encoder.py --template config/config.bin --xml config/output.xml --out config/type6_manual.bin --payload-type 6 --key 11223344556677889900AABBCCDDEEFF --verbose
```
**Daftar opsi lengkap:**
```bash
python encoder.py --help
```

---

## 🛠 Roadmap Development

* **Decoder v2** → Versi saat ini, mendukung metode: `normal`, `skip145`, `trykeys`, auto-check login, verbose & log file.
* **Encoder v2** → (pengganti encoder lama) adalah `encoder.py` unified yang: Mendukung semua payload Type `0..6`, Kompresi: `zlib`, `lzma`, `none`, Enkripsi: AES-ECB (Type2,6) dan AES-CBC (Type3,4,5), Key derivation: dari `serial`+`mac` (kp-first16 / kp-md5), atau menerima `--key` / `--iv`, Opsi verifikasi internal (decrypt & compare), verbose & logging, Bisa memakai `--template` untuk menyalin header (wajib untuk Type-6).
---

### ✅ Tips Cross-Platform

* Folder `.indihome-utility` adalah lokasi default untuk decoder.py & encoder.py setelah instalasi.
* Gunakan **Python 3.5+**.
* Untuk Android Termux, gunakan prefix `python` atau `python3` sesuai versi.
* URL di contoh perintah (`http://192.168.1.1`) ditulis **inline code** supaya tidak menjadi link otomatis.
