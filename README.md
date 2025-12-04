# Folder to PDF Converter

A simple, robust Python script that automatically merges all images in the current directory into a single PDF file. The output PDF is named after the folder containing the images.

## Features

* **Natural Sorting:** Intelligently sorts filenames containing numbers (e.g., sorts `page2.png` before `page10.png` rather than after).
* **Auto-Naming:** Automatically names the output PDF based on the folder name.
* **Format Handling:** Converts images to RGB to ensure compatibility and handles common formats (`.jpg`, `.png`, `.bmp`, etc.).
* **Portable:** Works as a standalone script or can be compiled into an executable.

## Prerequisites

You need Python installed on your system.

### ⚠️ Installation (Important)

This script relies on the **Pillow** library for image processing. You must install it before running the script.

Open your terminal or command prompt and run:

```bash
pip install Pillow
