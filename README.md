# Ubuntu Utility Scripts

## Scripts

- **Update and Upgrade**: Automatically updates and upgrades the system.
  - Location: `scripts/updates_manager/update_upgrade.sh`
  - Usage: `./update_upgrade.sh`
  - Remember: Make it executable with "chmod +x scripts/updates_manager/update_upgrade.sh"  

- **Email Sender**: Sends emails via terminal interface.
  - Location: `scripts/email_sender/email_sender.py`
  - Usage: `python3 email_sender.py`
  - Remember: 
        - Configure a SMTP authentication profile from your email provider.
        - Modify the src/email_sender/email_config.txt and then change it to a email_config.env 

- **Temperature Monitor**: Logs temperature data to a SQLite database.
  - Location: `scripts/temperature_monitor/temperature_monitor.py`
  - Usage: `python3 temperature_monitor.py`
  - Remember: 
        - Configure the email_sender before activating the temperature_monitor.
        - Example of db usage:
            $ cd /path/to/temperature_monitor
            $ sqlite3 temperature.db
            SQLite version 3.31.1 2020-01-27 19:55:54
            Enter ".help" for usage hints.
            sqlite> .tables
            temperature
            sqlite> .schema temperature
            CREATE TABLE temperature (
                timestamp TEXT,
                temp REAL
            );
            sqlite> SELECT * FROM temperature;
            2023-10-01 12:00:00|45.0
            2023-10-01 12:01:00|46.0
            ...
            sqlite> .exit

  - **Start Sessions**: Interactive script to start selected modules in `tmux` sessions.
  - Location: `start_sessions.sh`
  - Usage: `./start_sessions.sh`
  - Remeber: Make it executable with "chmod +x start_sessions.sh"  