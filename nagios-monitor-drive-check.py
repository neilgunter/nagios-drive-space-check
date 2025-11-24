#!/usr/bin/env python3

import shutil
import sys

# Define thresholds
WARNING_THRESHOLD = 80  # 80% used space triggers a warning
CRITICAL_THRESHOLD = 90  # 90% used space triggers a critical alert

def check_disk_usage(mount_point):
    """Check the disk usage of the specified mount point."""
    try:
        # Get disk usage statistics for the mount point
        total, used, free = shutil.disk_usage(mount_point)
        percent_used = (used / total) * 100
        return percent_used
    except Exception as e:
        # If there's an error, print it and return UNKNOWN status
        print(f"UNKNOWN: Unable to get disk usage for {mount_point}. Error: {e}")
        sys.exit(3)  # Nagios status code 3 = UNKNOWN

def main():
    # Define the mount point to check
    mount_point = "/"
    
    # Check disk usage
    disk_usage = check_disk_usage(mount_point)

    # Print the status and exit with the appropriate Nagios status code
    if disk_usage < WARNING_THRESHOLD:
        print(f"OK: Disk usage at {disk_usage:.2f}% on {mount_point}.")
        sys.exit(0)  # Nagios status code 0 = OK
    elif WARNING_THRESHOLD <= disk_usage < CRITICAL_THRESHOLD:
        print(f"WARNING: Disk usage at {disk_usage:.2f}% on {mount_point}.")
        sys.exit(1)  # Nagios status code 1 = WARNING
    elif disk_usage >= CRITICAL_THRESHOLD:
        print(f"CRITICAL: Disk usage at {disk_usage:.2f}% on {mount_point}.")
        sys.exit(2)  # Nagios status code 2 = CRITICAL
    else:
        print(f"UNKNOWN: Disk usage at {disk_usage:.2f}% on {mount_point}.")
        sys.exit(3)  # Nagios status code 3 = UNKNOWN

if __name__ == "__main__":
    main()
