#!/usr/bin/env python3
"""
Email Spammer Script
Sends emails every second with customizable subject, target, and message content.
"""

import smtplib
import time
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import sys

class EmailSpammer:
    def __init__(self):
        self.running = False
        self.email_count = 0
        self.smtp_server = None
        self.sender_email = None
        self.sender_password = None
        
    def get_email_credentials(self):
        """Get SMTP server and email credentials from user"""
        print("=== Email Configuration ===")
        
        # SMTP Server selection
        print("\nSelect your email provider:")
        print("1. Gmail")
        print("2. Outlook/Hotmail")
        print("3. Yahoo")
        print("4. Custom SMTP")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            self.smtp_server = "smtp.gmail.com"
            self.smtp_port = 587
        elif choice == "2":
            self.smtp_server = "smtp-mail.outlook.com"
            self.smtp_port = 587
        elif choice == "3":
            self.smtp_server = "smtp.mail.yahoo.com"
            self.smtp_port = 587
        elif choice == "4":
            self.smtp_server = input("Enter SMTP server (e.g., smtp.example.com): ").strip()
            self.smtp_port = int(input("Enter SMTP port (e.g., 587): ").strip())
        else:
            print("Invalid choice. Using Gmail as default.")
            self.smtp_server = "smtp.gmail.com"
            self.smtp_port = 587
        
        # Email credentials
        self.sender_email = input("Enter your email address: ").strip()
        self.sender_password = getpass.getpass("Enter your email password: ")
        
    def get_email_content(self):
        """Get email content from user"""
        print("\n=== Email Content ===")
        self.target_email = input("Enter target email address: ").strip()
        self.subject = input("Enter email subject: ").strip()
        self.message = input("Enter email message: ").strip()
        
    def send_email(self):
        """Send a single email"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.target_email
            msg['Subject'] = self.subject
            
            # Add body to email
            msg.attach(MIMEText(self.message, 'plain'))
            
            # Create SMTP session
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            
            # Send email
            text = msg.as_string()
            server.sendmail(self.sender_email, self.target_email, text)
            server.quit()
            
            self.email_count += 1
            print(f"✓ Email #{self.email_count} sent successfully to {self.target_email}")
            
        except Exception as e:
            print(f"✗ Error sending email: {str(e)}")
    
    def spam_emails(self):
        """Send emails every second"""
        print(f"\n🚀 Starting email spam to {self.target_email}")
        print("Press Ctrl+C to stop")
        
        self.running = True
        while self.running:
            try:
                self.send_email()
                time.sleep(1)  # Wait 1 second
            except KeyboardInterrupt:
                print("\n\n⏹️  Stopping email spam...")
                self.running = False
                break
            except Exception as e:
                print(f"Error in spam loop: {str(e)}")
                time.sleep(5)  # Wait 5 seconds before retrying
    
    def run(self):
        """Main execution function"""
        print("📧 Email Spammer Tool")
        print("=" * 30)
        
        try:
            # Get configuration
            self.get_email_credentials()
            self.get_email_content()
            
            # Confirm before starting
            print(f"\n📋 Summary:")
            print(f"From: {self.sender_email}")
            print(f"To: {self.target_email}")
            print(f"Subject: {self.subject}")
            print(f"Message: {self.message}")
            print(f"SMTP Server: {self.smtp_server}:{self.smtp_port}")
            
            confirm = input("\nStart sending emails? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Operation cancelled.")
                return
            
            # Start spamming
            self.spam_emails()
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    spammer = EmailSpammer()
    spammer.run()