import time
import subprocess
import sqlite3
from src.email_sender.email_sender import EmailSender  # Import the class instead of the function
import dotenv
import os

# Load environment variables from the email_config.env file
dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '../email_sender/email_config.env'))

def get_cpu_temperature():
    try:
        # Run the shell command to get the temperature
        result = subprocess.run(['cat', '/sys/class/thermal/thermal_zone0/temp'], capture_output=True, text=True)
        # Convert from millidegrees Celsius to degrees Celsius
        temp = int(result.stdout.strip()) / 1000.0
        return temp
    except Exception as e:
        print(f"Error reading CPU temperature: {e}")
        return None

def log_temperature():
    conn = sqlite3.connect('temperature.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS temperature
                 (timestamp TEXT, temp REAL)''')

    initial_email_sent = False

    # Initialize the EmailSender class and use it within the logging loop
    with EmailSender() as email_sender:
        while True:
            temp = get_cpu_temperature()
            if temp is not None:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                c.execute("INSERT INTO temperature (timestamp, temp) VALUES (?, ?)", (timestamp, temp))
                conn.commit()

                if not initial_email_sent:
                    email_sender.send_email("Initial CPU temperature", f"Initial CPU temperature is {temp}", [os.getenv('TO_EMAIL_USER')])
                    initial_email_sent = True

                if temp > 62:
                    email_sender.send_email("Temperature too high", f"CPU Temperature is {temp}", [os.getenv('TO_EMAIL_USER')])
            else:
                email_sender.send_email("Temperature sensor error", "CPU temperature data could not be read.", [os.getenv('TO_EMAIL_USER')])

            time.sleep(60)

if __name__ == "__main__":
    log_temperature()