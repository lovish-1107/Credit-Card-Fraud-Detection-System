import sqlite3
import pandas as pd
from tkinter import messagebox


def export_transactions():

    try:

        conn = sqlite3.connect("database.db")

        df = pd.read_sql_query(
            "SELECT * FROM transactions",
            conn
        )

        df.to_csv(
            "fraud_report.csv",
            index=False
        )

        conn.close()

        messagebox.showinfo(
            "Success",
            "Report Exported Successfully!\nfraud_report.csv"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


if __name__ == "__main__":

    export_transactions()