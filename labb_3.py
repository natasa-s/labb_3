
import csv


class SupportTicket:
    def __init__(self, ticket_id, customer, category, priority, status):
        self.ticket_id = ticket_id
        self.customer = customer
        self.category = category
        self.priority = priority
        self.status = status

    def __str__(self):
        return (
            f"Ticket ID: {self.ticket_id} | "
            f"Customer: {self.customer} | "
            f"Category: {self.category} | "
            f"Priority: {self.priority} | "
            f"Status: {self.status}"
        )

    def is_active(self):
        return self.status.strip().lower() != "stängt"


def load_tickets(filename):
    tickets = []

    with open(filename, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ticket = SupportTicket(
                ticket_id=row["id"],
                customer=row["kund"],
                category=row["kategori"],
                priority=row["prioritet"],
                status=row["status"]
            )

            tickets.append(ticket)

    return tickets


def main():
    tickets = load_tickets("supportarenden.csv")

    print(f"Total number of tickets: {len(tickets)}")
    print()

    for ticket in tickets:
        print(ticket)
        print(f"Active: {ticket.is_active()}")
        print("-" * 70)


if __name__ == "__main__":
    main()
