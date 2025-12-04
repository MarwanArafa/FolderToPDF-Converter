# 📑 Folder to PDF Converter

A lightweight, robust tool to automatically merge a folder of images into a single, high-quality PDF file. 🚀

## ✨ Features

* **🔢 Natural Sorting:** Smartly handles page numbers (e.g., sorts `Page 2` before `Page 10`).
* **📂 Auto-Organization:** Automatically names the output PDF based on the parent folder name.
* **🖼️ Multi-Format Support:** Compatible with JPG, PNG, BMP, TIFF, and more.
* **⚡ Fast & Efficient:** Converts files instantly with memory-safe processing.

---

## 🛠️ Prerequisites

Before running the tool, ensure you have the following ready:

* **Python 3.x** installed on your system.
* **Pillow (PIL)** library for image processing.

---

## ⚙️ Installation

1.  Open your terminal or command prompt (cmd).
2.  Install the required image library by running:

    ```bash
    pip install Pillow
    ```

---

## 🚀 How to Use

Follow these simple steps to create your PDF:

1.  **📍 Place the Script**
    Copy the `image_to_pdf.py` file into the folder containing your images.

2.  **🏃 Run the Converter**
    Open your terminal in that folder and run:
    ```bash
    python image_to_pdf.py
    ```

3.  **✅ Done!**
    The script will detect your images, sort them, and generate a PDF file named after the folder (e.g., `MyChapter.pdf`).

---

## 📄 Supported Formats

The tool automatically detects the following file types:
* ✅ `.jpg` / `.jpeg`
* ✅ `.png`
* ✅ `.bmp`
* ✅ `.tiff`

---

## ❓ Troubleshooting

| Error Message | Solution |
| :--- | :--- |
| `ModuleNotFoundError: No module named 'PIL'` | You forgot to install Pillow. Run `pip install Pillow`. |
| `No images found` | Make sure the `.py` file is inside the **same folder** as your images. |
| `Permission denied` | Close any open files and try running the script as Administrator. |

---

*Made with ❤️ and Python.*
