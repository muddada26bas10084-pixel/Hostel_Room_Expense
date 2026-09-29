# CampusSplit: Hostel & Room Expense Manager

## Project Overview
CampusSplit is a console-based Python application built to help hostel roommates and student groups track shared living expenses. The system allows users to log shared purchases, view category-wise expense breakdowns, compute net balances to determine who owes or receives money, and track spending against a fixed monthly budget.

The program is constructed purely using foundational Python constructs without any third-party packages or external libraries.

---

## Core Features
* **Add Shared Expense:** Record an expense by specifying the item, payer, amount, and spending category.
* **Input Validation:** Sanitizes and verifies amounts and roommate names to prevent invalid input or runtime crashes.
* **Category Breakdown:** Displays aggregate spending and percentage share for Food, Groceries, Internet, and Misc.
* **Smart Debt Settlement:** Calculates equal per-person shares and displays exact net balances (who owes whom).
* **Budget Alert & Log:** Compares total spend against a Rs 6000 threshold and maintains an immutable transaction history.

---

## Prerequisites & Environment Setup
* **Operating System:** Windows, macOS, or Linux
* **Environment:** Terminal, Command Prompt, or any Python 3 environment
* **Prerequisite:** Python 3.x installed

---

## Dependencies & Installation
* No external modules or packages are required.
* Standard libraries only. No `pip install` or `requirements.txt` needed.

---

## How to Run
1. Open Command Prompt or Terminal.
2. Navigate to the directory containing `main.py`:
   ```bash
   cd Desktop
