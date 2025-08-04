# 🧾 Automated Invoice Extraction & Email Reporting with Python

This project automates the process of reading invoice data from PDFs, generating detailed and summary reports in Excel, and sending them via email to multiple recipients — all using Python.

---

## 🚀 Features

- ✅ Extracts structured invoice data from **unstructured PDF files**
- ✅ Parses:
  - Invoice Number
  - Date
  - Customer Name (from "Bill To")
  - Address (from "Ship To")
  - Ship Mode
  - Total Amount
- ✅ Compiles **two Excel reports**:
  - `All_Invoices_Detail.xlsx`
  - `Invoice_Summary_By_Date.xlsx`
- ✅ Sends both reports via **automated email** using SMTP
- ✅ Fully customizable and scalable to handle thousands of invoices

---

## 🛠 Tech Stack

| Tool / Library | Purpose                       |
|----------------|-------------------------------|
| `pdfplumber`   | Extract text from PDF pages   |
| `re` (Regex)   | Pattern-based text extraction |
| `pandas`       | Data manipulation and reports |
| `openpyxl`     | Excel writing backend         |
| `smtplib`      | Send email with attachments   |
| `email.message` | Build MIME email message     |

---

## 📂 Folder Structure

```bash
├── invoices/                        # Folder with 1000+ PDF invoices
├── All_Invoices_Detail.xlsx        # Output: Detailed data
├── Invoice_Summary_By_Date.xlsx    # Output: Summary by date
├── main.py                         # Main script
├── README.md
