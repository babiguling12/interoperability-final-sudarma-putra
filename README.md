# 🎓 Campus Event Registration Platform

Proyek ini dibuat untuk memenuhi **UTS Interoperabilitas**  
di **Politeknik Negeri Bali - Jurusan Teknologi Informasi**.

Dibuat oleh: **Ida Bagus Putu Sudarma Putra S (2315354006 / 5B TRPL)**

---

## 🧠 Deskripsi Singkat

Sistem ini adalah **platform pendaftaran event kampus** yang menunjukkan **interoperabilitas antar komponen sistem**:

- **Backend** → menggunakan **FastAPI**  
- **Database** → menggunakan **SQLite**  
- **Frontend** → menggunakan **HTML + Fetch API (JavaScript)**  

Aplikasi ini memungkinkan:
- 👨‍💼 **Admin**: membuat, mengedit, dan menghapus event
- 🙋‍♂️ **Peserta**: melihat daftar event dan mendaftar
- 📋 **Admin** juga bisa melihat daftar peserta yang sudah mendaftar

---

## ⚙️ Cara Menjalankan Aplikasi

### 1️⃣ Clone atau Download Repository
```bash
git https://github.com/babiguling12/interoperability-final-sudarma-putra.git
cd interoperability-final-sudarma-putra

#### ⚙️ Jalankan Backend
```bash
cd backend
pip install fastapi uvicorn
sqlite3 campus_event.db
.read create_db.sql
.tables
uvicorn main:app --reload

##### Lihat Dokumentasi API
[👉 Lihat Dokumentasi API](http://127.0.0.1:8000/docs)

