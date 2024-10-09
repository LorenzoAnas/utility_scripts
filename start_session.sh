#!/bin/bash

echo "Select the modules you want to start:"
echo "1. Updates Manager"
echo "2. Email Sender"
echo "3. Temperature Monitor"
echo "4. All"
echo "Enter your choices (e.g., 1 3 for Updates Manager and Temperature Monitor):"
read -a choices

for choice in "${choices[@]}"; do
    case $choice in
        1)
            tmux new-session -d -s updates_manager './src/updates_manager/update_upgrade.sh'
            echo "Started Updates Manager in tmux session 'updates_manager'"
            ;;
        2)
            tmux new-session -d -s email_sender 'python3 -m src.email_sender.email_sender'
            echo "Started Email Sender in tmux session 'email_sender'"
            ;;
        3)
            tmux new-session -d -s temperature_monitor 'python3 -m src.temperature_monitor.temperature_monitor'
            echo "Started Temperature Monitor in tmux session 'temperature_monitor'"
            ;;
        4)
            tmux new-session -d -s updates_manager './src/updates_manager/update_upgrade.sh'
            tmux new-session -d -s email_sender 'python3 -m src.email_sender.email_sender'
            tmux new-session -d -s temperature_monitor 'python3 -m src.temperature_monitor.temperature_monitor'
            echo "Started all modules in separate tmux sessions"
            break
            ;;
        *)
            echo "Invalid choice: $choice"
            ;;
    esac
done