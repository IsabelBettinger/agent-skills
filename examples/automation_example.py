import datetime

class AutomationExample:
    def generate_content_calendar(self, start_date, end_date):
        # Generate content calendar between two dates
        current_date = start_date
        content_calendar = []
        while current_date <= end_date:
            content_calendar.append(f"Content for {current_date.strftime('%Y-%m-%d')}")
            current_date += datetime.timedelta(days=1)
        return content_calendar

    def draft_email(self, recipient, subject, body):
        # Draft an email with provided recipient, subject, and body
        email = f"To: {recipient}\nSubject: {subject}\n\n{body}"
        return email

    def manage_files(self, file_path, action):
        # Manage files: read, write or delete
        if action == 'read':
            with open(file_path, 'r') as file:
                return file.read()
        elif action == 'write':
            with open(file_path, 'w') as file:
                file.write('File content')
                return 'File written successfully'
        elif action == 'delete':
            import os
            os.remove(file_path)
            return 'File deleted successfully'

# Usage Example
if __name__ == '__main__':
    automation = AutomationExample()
    calendar = automation.generate_content_calendar(datetime.date(2026, 3, 21), datetime.date(2026, 3, 31))
    email = automation.draft_email('example@example.com', 'Subject Line', 'Email Body')
    file_action_result = automation.manage_files('example.txt', 'write')
    
    print(calendar)
    print(email)
    print(file_action_result)