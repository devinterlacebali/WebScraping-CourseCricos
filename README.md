# 🦘 AusCourseMiner
**Automated Web Scraper for Australian University Course Data**

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Enabled-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Used-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📖 Overview
**AusCourseMiner** is a Python-based data engineering project that automates the extraction of course information from multiple **Australian university websites**.

It collects structured academic data such as:
- 🎓 **Course Title & Description**
- 🧾 **CRICOS Course Code**
- ⏱ **Total Course Duration**
- 💰 **Tuition Fee (Onshore & Offshore)**
- 🧍‍♂️ **Entry Requirements**
- 🔗 **Course URLs & Application Links**

The result is formatted as **SQL-ready data** for integration into databases or analytics pipelines.

---

## 🧩 Features
- Multi-site scraping with dynamic page rendering using **Playwright**
- HTML parsing via **BeautifulSoup4**
- String cleaning and normalization using **regex & pandas**
- Data export support:
  - `.xlsx`, `.csv`, `.sql`, `.json`
- Asynchronous scraping support with **asyncio**
- Modular and extendable scraping system

---

## ⚙️ Tech Stack
| Component | Library | Description |
|------------|----------|-------------|
| Headless Browser | `playwright` | For rendering and navigating dynamic content |
| HTML Parser | `beautifulsoup4` | For extracting course data from HTML |
| Data Cleaning | `re`, `pandas` | Regex-based and tabular cleaning |
| Async Runtime | `asyncio` | Concurrent scraping for performance |
| Data Export | `pandas`, `openpyxl` | To Excel, CSV, or SQL outputs |
| Database Integration | `mysql.connector` / `sqlite3` | For local storage or pipeline use |

---

## 🧰 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anakagung55/WebScraping-CourseCricos.git
   cd WebScraping-CourseCricos
   ```

2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers:**
   Since many scrapers use `playwright` to render dynamic pages, you must install the required browser binaries:
   ```bash
   playwright install chromium
   ```

---

## 🚀 How to Run

The scrapers are structured on a per-university basis. You can run them individually or use the automated runner script to run all or select scrapers.

### 1. Running All or Multiple Scrapers (Recommended)
We provide an automated runner script, `run_all.py` at the root, which scans all directories, finds the main scrapers (excluding test/utility files), determines the correct working directory for each script automatically, and runs them.

To start the runner:
```bash
python run_all.py
```

Upon launching, it will list all discovered scrapers and ask you to select:
* `all` - Runs all scrapers sequentially.
* `1,3,5` - Runs specific scrapers (comma-separated indices).
* `q` - Quits the script.

### 2. Running a Single Scraper Manually
If you want to run a specific scraper manually, it is generally recommended to run it from the **project root folder**:

```bash
# Example: Run the Apex Institute scraper
python "Apex Institute of Education/apex.py"

# Example: Run the Deakin University scraper
python "Deakin University/deakin.py"
```

> [!NOTE]
> Some scripts may assume the input files (like `Book1.xlsx` or `griffin.xlsx`) are in the active terminal directory. Ensure the input files listed in the configuration block of the script are present in the directory you run the command from, or adjust the `INPUT_FILE` / `FILE` path in the script directly.

### 3. Output
Once execution is complete, the scrapers will typically generate:
* An updated SQL file (e.g. `apex_courses_update.sql`) containing the `UPDATE` queries for your database.
* An Excel/CSV file containing the scraped results or error logs.


