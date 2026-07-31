import random
import time
from db import get_connection

SLEEP_SECONDS = 1.0

def main():
    with get_connection() as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("SELECT customer_id FROM customers")
            customer_ids = [r[0] for r in cur.fetchall()]

            if not customer_ids:
                raise SystemExit("no customers found - run seed.py first")
            
            print(f"loaded {len(customer_ids)} customers. ctrl-c to stop. ")
            count = 0

            try:
                while True:
                    cur.execute(
                        """
                        INSERT INTO orders (customer_id, status, total_amount)
                        VALUES (%s, 'placed', %s)
                        RETURNING order_id
                        """,
                        (
                            random.choice(customer_ids),
                            round(random.uniform(8,120), 2)
                        )
                    )
                    order_id = cur.fetchone()[0]
                    count += 1
                    print(f"inserted order {order_id} ({count} this run)")
                    time.sleep(SLEEP_SECONDS)
            except KeyboardInterrupt:
                print(f"\nstopped after {count} inserts")

if __name__ == "__main__":
    main()