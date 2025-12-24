import sqlite3


def main():
    with sqlite3.connect(
        "database/alarm_info.db", timeout=5, isolation_level=None
    ) as db:
        # Turn off WAL mode for better compatibility
        db.execute("PRAGMA journal_mode=DELETE")

        cursor = db.cursor()

        # --- CREATE TABLE ---
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS alarm (
            alarm_name TEXT PRIMARY KEY,
            alarm_description TEXT,
            alarm_category TEXT,
            alarm_time TEXT,
            alarm_day TEXT
        )
        """
        )

        # --- INSERT EXAMPLE ---
        cursor.execute(
            """
        INSERT OR IGNORE INTO alarm VALUES
        ("Wake up", "u gotta go, now", "routine", "9:00", "everyday")
        """
        )
        db.commit()

        # --- SELECT ---
        cursor.execute("SELECT * FROM alarm")
        print(cursor.fetchone())


if __name__ == "__main__":
    main()
