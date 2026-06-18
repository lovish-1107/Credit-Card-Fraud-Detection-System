import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def show_trend():

    # existing code here
    pass


def show_fraud_trend():

    conn = sqlite3.connect("database.db")

    query = """
    SELECT
        DATE(transaction_time) as trans_date,
        COUNT(*) as fraud_count
    FROM transactions
    WHERE prediction='Fraud'
    GROUP BY DATE(transaction_time)
    ORDER BY trans_date
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    if len(df) == 0:
        print("No Fraud Data Available")
        return

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["trans_date"],
        df["fraud_count"],
        marker="o"
    )

    plt.title("Fraud Transaction Trend")

    plt.xlabel("Date")
    plt.ylabel("Fraud Transactions")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    show_trend()