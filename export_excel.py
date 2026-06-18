import sqlite3
import pandas as pd
from tkinter import messagebox


def export_excel():

    try:

        conn = sqlite3.connect("database.db")

        df = pd.read_sql_query(
            "SELECT * FROM transactions",
            conn
        )

        df.to_excel(
            "fraud_report.xlsx",
            index=False
        )

        conn.close()

        messagebox.showinfo(
            "Success",
            "Excel Report Exported Successfully!"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


if __name__ == "__main__":

    export_excel()