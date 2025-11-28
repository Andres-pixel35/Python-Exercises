# DebtTracker

**DebtTracker** is a small, local Python tool to help track and simulate debts, payments, and simple debt histories. It's intended to help you experiment with debt scenarios and maintain simple CSV-backed records for personal use.

**Features**
- **Simple records**: Stores current debt records in `data/debt_records.csv` and historical entries in `data/debts_history.csv`.
- **Helpers**: Reusable helper functions are in the `helpers/` package (`debts_functions.py`, `files_helpers.py`, `user_input.py`, etc.).
- **Quick run**: Single-entry run via `main.py`.

**Requirements**
- Python 3.8+ (or your environment's supported Python 3.x)
- See `requirements.txt` for Python package dependencies.

**Installation**
1. Clone or copy the project to your local machine.
2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**Run the program**

Run the main script from the project root:

```bash
python main.py
```

Replace the command above with your usual Python invocation if different (for example, `python3` or an environment-specific command).

**Configuration**
- The file `config.py` contains several constants and settings you can change to match your needs (for example: file paths). Before making changes, make a backup of `config.py` or track changes with version control so you can revert if needed.

**Project layout**
- `main.py`: Program entry point.
- `config.py`: Changeable constants and configuration for the application.
- `helpers/`: Helper modules for file operations, user input, and debt calculations.
- `data/`: CSV files used by the app (`debt_records.csv`, `debts_history.csv`).

**Data files**
- `data/debt_records.csv`: Current active debt records.
- `data/debts_history.csv`: Historical debt and payment log entries.

**CSV Format**
The CSV files in `data/` share the same column layout. Below is each column name, the expected data type, and a short description:

- **`user_name`**: string — The owner or account name associated with the debt (e.g., `andres`).
- **`debt_name`**: string — A short descriptive name for the debt (e.g., `car loan`).
- **`start_date`**: date string (YYYY/MM/DD) — The date the debt or plan started.
- **`deadline`**: date string (YYYY/MM/DD) — The planned end date or maturity date for the debt.
- **`monthly_payment`**: number (float) — The agreed monthly payment amount.
- **`instalments`**: integer — Total number of instalments (months) for the plan.
- **`principal`**: number (float) — The initial principal amount of the debt.
- **`remaining_amount`**: number (float) — The money you will pay if you keep your debt until the end.
- **`interest_rate`**: number (float) — The monthly nominal interest rate used in calculations (represented as a decimal, e.g., `0.01` for 1%).

Notes: 
- Keep numeric fields numeric (no currency symbols) to avoid parsing errors.
- If you plan to extend the CSV format, update `FIELDNAMES` in `config.py` so the program reads the new columns correctly.

**Examples**
- Right now the `data/` folder contains files with example information that act as sample data. Before running the program with your own data, make sure to remove those two files to ensure the program works properly. To do it run the following command from the project root:

```bash
rm ./data/*
```

**Key Calculation Limitations**
* **Amortization System (French System Only):** The program is designed exclusively for debts that utilize the **French Amortization System (annuity amortization)**, where the monthly payment remains fixed throughout the life of the loan. It **will not** accurately model debts using other systems (e.g., German/declining principal amortization).
* **Prepayment Fine:** The fine calculated during the "payoff" option assumes the fine is a **percentage over the current outstanding principal balance**. The program cannot handle other types of prepayment penalties, such as a fixed fee or an amount equal to a set number of months' interest.

**Key Concepts**
- It works perfectly in any Linux distribution. For Windows and MacOS users it is no guaranteed.
- The `remaining_debt` column in the CSV files represents the total future cash flow required to fully repay the debt, which includes the current principal balance plus all future accrued interest if the current payment schedule is maintained. It is not the current outstanding principal balance.
- Always run any command here shown in the project root.
- If you change constants in `config.py`, test the program with sample data first to ensure behavior matches your expectations.

**Disclaimer & Important Warning**

Even though this program was developed with the intention of producing accurate calculations, it may still make mistakes. All calculations and outputs should be treated as simulations or approximations and NOT as financial advice or definitive facts.

Be aware that all simulations are based on the French Amortization System and assume that any prepayment fine is a percentage of the current principal balance. The results will be inaccurate for debts using different models.

For any real financial decision, negotiation, or legal matter, always contact the lender (or an appropriate financial professional) to confirm figures and obtain authoritative guidance.

**Contributing**
- Feel free to fork the repository for personal improvements. No formal contribution process is currently established.

**License**
- This project is provided as-is for personal use and educational purposes.
