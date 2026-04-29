# 🔐 Secure File Storage Web App

A modern, secure web application for encrypting and decrypting files using AES-256 encryption (via Fernet). This tool ensures your sensitive files are protected with a password and preserves the original file extension upon decryption.

## ✨ Features

- **🔒 Strong Encryption**: Uses AES-256 encryption through the `cryptography` library.
- **📁 Extension Preservation**: Automatically embeds the original filename and extension inside the encrypted payload, so your files (like images, PDFs, etc.) are perfectly restored.
- **📊 Real-time Dashboard**: Track your activity with encryption/decryption counters and a recent activity log.
- **🎨 Modern UI**: Clean, responsive design with interactive elements and smooth gradients.
- **🛡️ Secure Handling**: Uses `secure_filename` to prevent path traversal attacks.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone or download** this repository to your local machine.
2. **Navigate** to the project directory:
   ```bash
   cd secure_file_storage_web
   ```
3. **Install dependencies**:
   ```bash
   pip install flask cryptography
   ```

## 🛠️ How to Run

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## 📖 How to Use

### Encrypting a File
1. Go to the **Dashboard**.
2. Select the file you want to protect.
3. Enter a strong **Password**.
4. Click **Encrypt**. Your browser will download a `.enc` file.

### Decrypting a File
1. In the **Dashboard**, under the Decrypt section, select the `.enc` file you downloaded earlier.
2. Enter the **exact same password** used for encryption.
3. Click **Decrypt**. The app will restore and download your original file with its correct name and extension.

## 📁 Project Structure

```text
secure_file_storage_web/
├── app.py              # Main Flask application
├── encrypt.py          # Encryption logic & filename embedding
├── decrypt.py          # Decryption logic & filename recovery
├── templates/          # HTML templates (index, dashboard)
├── uploads/            # Temporary storage for uploaded files
└── encrypted/          # Storage for encrypted files
```

## ⚠️ Security Note

- **Password Recovery**: There is no way to recover your password. If you lose it, the data cannot be decrypted.
- **Development Server**: This is running on a Flask development server. For production use, consider using a WSGI server like Gunicorn.

---
*Built for Secure Cloud Infrastructure and Private Data Management.*
