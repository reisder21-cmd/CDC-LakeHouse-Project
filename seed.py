import random
from faker import Faker
from db import get_connection

fake = Faker()

NUM_CUSTOMERS = 200
NUM_ORDERS = 1000

STATUSES = ["placed", "accepted", "picked_up", "delivered", "cancelled"]
TIERS = ["bronze", "silver", "gold"]

def make_customers(n):
    return [
       (
        fake.name(),
        fake.unique.email(),
        fake.address().replace("\n",","),
        random.choice(TIERS)
       )
       for _ in range(n)
    ]

def make_orders(n, customer_ids):
    return [
        (
            random.choice(customer_ids),
            random.choices(STATUSES, weights=[10,15,15,50,10])[0],
            round(random.uniform(8,120), 2)
        )
        for _ in range(n)
    ]

def main():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO customers (full_name, email, address, loyalty_tier)
                VALUES (%s, %s, %s, %s)
                """,
                make_customers(NUM_CUSTOMERS)
            )
            cur.execute("SELECT customer_id FROM customers")
            customer_ids = [row[0] for row in cur.fetchall()]

            cur.executemany(
                """ 
                INSERT INTO orders (customer_id, status, total_amount)
                VALUES (%s, %s, %s)
                """,
                make_orders(NUM_ORDERS, customer_ids)

            )
print(f"seeded {NUM_CUSTOMERS} customers and {NUM_ORDERS} orders")

if __name__ == "__main__":
    main()
