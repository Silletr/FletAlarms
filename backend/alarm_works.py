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
        db.commit()

        # --- SELECT ---
        cursor.execute(
            "SELECT alarm_name, alarm_description, alarm_category, alarm_time, alarm_day FROM alarm ORDER BY alarm_time"
        )

        rows = cursor.fetchall()

    if not rows:
        print("There`s no alarm in this DB.")
    else:
        for row in rows:
            name, desc, category, time, day = row
            print(f"🔔 {name}")
            print(f"   Description: {desc}")
            print(f"   Category: {category}")
            print(f"   Time: {time}")
            print(f"   Day(-s): {day}")
            print("-" * 30)


if __name__ == "__main__":
    main()
