class BugTracker:
    def __init__(self):
        # Initialize the bugs dictionary
        self.bugs = {}

    def add_bug(self, bug_id, description, severity):
        if bug_id in self.bugs:
            print(f"Bug ID {bug_id} already exists.")
            return
        # Add a new bug with status "Open"
        self.bugs[bug_id] = {
            "description": description,
            "severity": severity,
            "status": "Open"
        }
        print(f"Bug {bug_id} added successfully.")

    def update_status(self, bug_id, new_status):
        if bug_id not in self.bugs:
            print(f"Bug ID {bug_id} does not exist.")
            return
        # Update the status of the bug
        self.bugs[bug_id]["status"] = new_status
        print(f"Bug {bug_id} status updated to '{new_status}'.")

    def list_all_bugs(self):
        if not self.bugs:
            print("No bugs to display.")
            return
        print("\nAll Bugs:")
        for bug_id, details in self.bugs.items():
            print(f"Bug ID: {bug_id}")
            print(f"  Description: {details['description']}")
            print(f"  Severity: {details['severity']}")
            print(f"  Status: {details['status']}")
            print("-" * 40)


if __name__ == "__main__":
    # Create a BugTracker object
    bug_tracker = BugTracker()

    # Add three bugs
    bug_tracker.add_bug("BUG001", "Login page crashes on submit", "High")
    bug_tracker.add_bug("BUG002", "Typo in About Us page", "Low")
    bug_tracker.add_bug("BUG003", "Payment gateway timeout", "Critical")

    # Update status of bugs
    bug_tracker.update_status("BUG001", "In Progress")
    bug_tracker.update_status("BUG003", "Closed")

    # Display all bugs
    bug_tracker.list_all_bugs()
