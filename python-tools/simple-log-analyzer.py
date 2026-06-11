# Simple Log Analyzer (Security Monitoring Tool)

# This script analyzes authentication logs to detect suspicious activity
# such as failed login attempts and invalid users.

log_file = "auth.log"

failed_attempts = 0
invalid_user_attempts = 0

try:
    with open(log_file, "r") as file:
        for line in file:
            line = line.lower()

            if "failed password" in line:
                print("[ALERT] Failed login detected:", line.strip())
                failed_attempts += 1

            elif "invalid user" in line:
                print("[ALERT] Invalid user detected:", line.strip())
                invalid_user_attempts += 1

    print("\n===== SUMMARY =====")
    print("Total failed login attempts:", failed_attempts)
    print("Total invalid user attempts:", invalid_user_attempts)

except FileNotFoundError:
    print("Log file not found. Please ensure 'auth.log' exists.")
