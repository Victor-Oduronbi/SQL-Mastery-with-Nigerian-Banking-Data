# SQL Mastery with Nigerian Banking Data

**Project Overview**  
This project demonstrates advanced SQL engineering and data science capabilities using **50,000+** records of synthetic Nigerian banking retail transactions. The goal was to transform raw, messy transactional data into actionable business intelligence using Python-SQL integration. The analysis focuses on the three pillars of Nigerian FinTech: Customer Retention (competing with Neobanks), Lending Risk (calculating DTI and NPLs), and Fraud Compliance (AML and Mule detection).

<br>

**🚀 Key Business Problems Solved**  
I implemented **23** complex SQL queries categorized into five strategic domains:
* Customer Insights & Segmentation: Identifying "Whale" customers and regional acquisition trends.
<br>
<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/1bead01c-aa97-46ee-bc15-400166432389" />

<br>

* Churn & Retention Analytics: Building early-warning systems to detect customers likely to switch to competitors.
<br>
<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/2be08415-78da-460a-b571-c1d820dfc43c" />

<br>

* Transactional Intelligence: Analyzing peak NIP transfer hours to optimize server reliability.
<br>
<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/26e5d0cf-c547-4f63-884c-b89af8ec589c" />

<br>

* Credit Risk & Loan Management: Calculating Debt-to-Income (DTI) ratios and behavioral credit scores.
<br>
<img width="1589" height="490" alt="image" src="https://github.com/user-attachments/assets/cbb08f94-6685-463e-b84a-e2cf65b0b1fc" />

<br>

* Fraud & AML (Anti-Money Laundering): Detecting rapid movement of funds and multi-account linkage via device_id.
<br>
<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/940e9b84-0245-470a-b957-5e637b741d57" />    

<br>
<br>

**🛠️ Tech Stack**  
* Language: Python 3.x
* Database: SQLite3
* Libraries: Pandas, Datasets (Hugging Face), Matplotlib/Seaborn (for visualization)
* Environment: Jupyter Notebook

<br>

**📁 Dataset**  
The data is sourced from the electricsheepafrica/nigerian-banking-retail-transactions dataset. It contains realistic transaction patterns including: 
* Transaction Types: Credits, Debits, NIP Transfers, POS, USSD, and Web.
* Metadata: Customer IDs, Device IDs, Location (States), and Status (Success/Failed).

<br>

**📈 Technical Highlights**  
In this project, I demonstrate mastery of:
* Window Functions: SUM() OVER, RANK(), and ROW_NUMBER().
* Common Table Expressions (CTEs): For multi-stage analysis and readability.
* Self-Joins: For time-based fraud detection (comparing transactions within the same hour).
* Cohort Analysis: To track user retention survival rates.
* Data Modeling: Splitting raw data into normalized customers and transactions tables.

<br>

**💻 How to Run**
1. Clone this repository: `git clone https://github.com`
2. Install Dependencies: `pip install pandas datasets sqlite3`
3. Run the Jupyter Notebook `SQL_Mastery_Banking.ipynb` to build the database and execute the queries.

<br>

**📊 Sample Insights**
* Fraud Detection: Found that **12.5%** of high-volume transactions show "Mule" characteristics (funds leaving the account within 60 minutes of arrival).
* System Performance: Identified **10:00 AM - 1:00 PM** as the peak window for NIP transfers, suggesting a need for increased server capacity during those hours.

<br>

Author: Oduronbi Victor
<br>
LinkedIn: www.linkedin.com/in/victor-oduronbi-62b22132b
<br>
Email: victoroduronbi@gmail.com
