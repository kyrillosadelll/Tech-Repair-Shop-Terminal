from abc import ABC, abstractmethod


class RepairService(ABC):

    def __init__(self, service_id, name, labor_cost):
        self.__service_id = service_id
        self.__name = name
        self.__labor_cost = labor_cost
        self.__status = "Pending"

    def get_id(self):
        return self.__service_id

    def get_name(self):
        return self.__name

    def get_labor_cost(self):
        return self.__labor_cost

    def get_status(self):
        return self.__status

    def set_labor_cost(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            print("Error: labor cost has to be a positive number.")
            return
        self.__labor_cost = float(amount)

    def set_status(self, new_status):
        valid = ["Pending", "In Progress", "Completed", "Cancelled"]
        if new_status not in valid:
            print(f"Error: status must be one of {valid}")
            return
        self.__status = new_status

    @abstractmethod
    def calculate_service_cost(self):
        pass

    @abstractmethod
    def display_service_info(self):
        pass


class HardwareRepair(RepairService):

    def __init__(self, service_id, name, labor_cost, parts_cost, warranty_months=6):
        super().__init__(service_id, name, labor_cost)
        self.__parts_cost = parts_cost
        self.__warranty_months = warranty_months

    def get_parts_cost(self):
        return self.__parts_cost

    def get_warranty(self):
        return self.__warranty_months

    def calculate_service_cost(self):
        tax = self.__parts_cost * 0.10
        total = self.get_labor_cost() + self.__parts_cost + tax
        return total

    def display_service_info(self):
        estimated = self.calculate_service_cost()
        print(f"  [{self.get_id()}] {self.get_name():<30} | Hardware "
              f"| Labor: ${self.get_labor_cost():.2f} "
              f"| Parts: ${self.__parts_cost:.2f} "
              f"| Est. Total: ${estimated:.2f} "
              f"| Warranty: {self.__warranty_months} months")


class SoftwareRepair(RepairService):

    PROCESSING_FEE = 5.00

    def __init__(self, service_id, name, labor_cost, license_key="N/A", os_version="Any"):
        super().__init__(service_id, name, labor_cost)
        self.__license_key = license_key
        self.__os_version = os_version

    def get_license_key(self):
        return self.__license_key

    def get_os_version(self):
        return self.__os_version

    def calculate_service_cost(self):
        return self.get_labor_cost() + self.PROCESSING_FEE

    def display_service_info(self):
        estimated = self.calculate_service_cost()
        print(f"  [{self.get_id()}] {self.get_name():<30} | Software "
              f"| Labor: ${self.get_labor_cost():.2f} "
              f"| Fee: ${self.PROCESSING_FEE:.2f} "
              f"| Est. Total: ${estimated:.2f} "
              f"| OS: {self.__os_version}")


class CustomerInvoice:

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.repairs = []

    def add_repair(self, repair):
        self.repairs.append(repair)
        print(f"\n  Added \"{repair.get_name()}\" to invoice.")

    def remove_repair(self, num):
        if 1 <= num <= len(self.repairs):
            removed = self.repairs.pop(num - 1)
            print(f"\n  Removed \"{removed.get_name()}\" from invoice.")
        else:
            print("  Error: that item number doesn't exist.")

    def view_invoice(self):
        if len(self.repairs) == 0:
            print("\n  Invoice is empty.")
            return

        print("\n" + "-" * 60)
        print(f"  Invoice for: {self.customer_name}")
        print("-" * 60)
        print(f"  {'#':<5} {'Service Name':<32} {'Base Labor':>10}")
        print("  " + "-" * 50)

        for i, r in enumerate(self.repairs, 1):
            print(f"  {i:<5} {r.get_name():<32} ${r.get_labor_cost():>9.2f}")

        print("-" * 60)
        print(f"  {len(self.repairs)} item(s) on invoice.")

    def print_final_bill(self):
        if len(self.repairs) == 0:
            print("\n  Nothing to bill - invoice is empty.")
            return

        grand_total = 0.0

        print("\n" + "=" * 60)
        print("           TECH REPAIR SHOP - FINAL RECEIPT")
        print("=" * 60)
        print(f"  Customer: {self.customer_name}")
        print("-" * 60)

        for i, r in enumerate(self.repairs, 1):
            cost = r.calculate_service_cost()
            r_type = "Hardware" if isinstance(r, HardwareRepair) else "Software"

            print(f"\n  {i}. {r.get_name()} ({r_type})")

            if isinstance(r, HardwareRepair):
                parts = r.get_parts_cost()
                tax = parts * 0.10
                print(f"       Labor:              ${r.get_labor_cost():.2f}")
                print(f"       Parts:              ${parts:.2f}")
                print(f"       Parts Tax (10%):    ${tax:.2f}")
            else:
                print(f"       Labor:              ${r.get_labor_cost():.2f}")
                print(f"       Processing Fee:     ${SoftwareRepair.PROCESSING_FEE:.2f}")

            print(f"       {'─' * 30}")
            print(f"       Service Total:      ${cost:.2f}")
            grand_total += cost

        print("\n" + "=" * 60)
        print(f"  GRAND TOTAL:                          ${grand_total:.2f}")
        print("=" * 60)
        print("  Thanks for choosing Tech Repair Shop!")
        print("=" * 60)


def get_services():
    return [
        HardwareRepair(1, "Screen Replacement",    50.00,  80.00, 12),
        HardwareRepair(2, "Battery Replacement",   30.00,  25.00,  6),
        HardwareRepair(3, "Keyboard Repair",       40.00,  35.00,  6),
        HardwareRepair(4, "Motherboard Diagnosis", 70.00, 120.00,  3),
        SoftwareRepair(5, "OS Reinstallation",     45.00, "N/A",      "Windows 11"),
        SoftwareRepair(6, "Virus/Malware Removal", 35.00, "N/A",      "Any"),
        SoftwareRepair(7, "Driver Update Package", 20.00, "DRV-2026", "Any"),
        SoftwareRepair(8, "Data Recovery",         60.00, "N/A",      "Any"),
    ]


def print_menu():
    print("\n  --------------------------------")
    print("  [1] View Available Services")
    print("  [2] Add Service to Invoice")
    print("  [3] View Current Invoice")
    print("  [4] Print Final Bill")
    print("  [5] Remove Item from Invoice")
    print("  [6] Exit")
    print("  --------------------------------")


def main():
    print("=" * 60)
    print("       WELCOME TO TECH REPAIR SHOP")
    print("=" * 60)

    name = ""
    while name == "":
        name = input("  Enter customer name: ").strip()
        if name == "":
            print("  Please enter a name.")

    services = get_services()
    invoice = CustomerInvoice(name)

    print(f"\n  Hello {name}! Use the menu below to get started.")

    while True:
        print_menu()
        choice = input("  Your choice: ").strip()

        if choice == "1":
            print("\n" + "-" * 60)
            print("  AVAILABLE SERVICES")
            print("-" * 60)
            print("  -- Hardware --")
            for s in services:
                if isinstance(s, HardwareRepair):
                    s.display_service_info()
            print("  -- Software --")
            for s in services:
                if isinstance(s, SoftwareRepair):
                    s.display_service_info()
            print("-" * 60)

        elif choice == "2":
            lookup = input("  Enter service ID or name: ").strip().lower()
            match = None
            for s in services:
                if lookup == str(s.get_id()) or lookup == s.get_name().lower():
                    match = s
                    break
            if match:
                invoice.add_repair(match)
            else:
                print("  Service not found. Try option [1] to see all services.")

        elif choice == "3":
            invoice.view_invoice()

        elif choice == "4":
            invoice.print_final_bill()

        elif choice == "5":
            invoice.view_invoice()
            if len(invoice.repairs) > 0:
                try:
                    num = int(input("  Enter item number to remove: ").strip())
                    invoice.remove_repair(num)
                except ValueError:
                    print("  Please enter a valid number.")

        elif choice == "6":
            print("\n  Goodbye! Have a great day.\n")
            break

        else:
            print("  Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()