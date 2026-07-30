from db import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO customers (full_name, email, address, loyalty_tier)
            VALUES (%s, %s, %s, %s)
            RETURNING customer_id
            """,
            ("Ada Lovelace", "ada@example.com", "12 Analytical Way", "gold"),
        )
        print("inserted customer_id:", cur.fetchone()[0])

