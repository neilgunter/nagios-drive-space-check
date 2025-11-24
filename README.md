
# Nagios Disk Space Monitor

## Overview
Python script for monitoring disk space usage with Nagios-compatible exit codes and alerts. Provides warnings and critical alerts based on configurable thresholds.

## Prerequisites
- Python 3.x
- shutil module (standard library)
- Root access for disk monitoring

## Configuration
Edit these variables in the script:
```python
WARNING_THRESHOLD = 80   # 80% used space triggers warning
CRITICAL_THRESHOLD = 90  # 90% used space triggers critical alert
mount_point = "/"        # Mount point to monitor
```

## Usage
```bash
chmod +x check_disk_space.py
./check_disk_space.py
```

## Nagios Exit Codes
- **0**: OK - Disk usage below warning threshold
- **1**: WARNING - Disk usage ≥80% but <90%
- **2**: CRITICAL - Disk usage ≥90%
- **3**: UNKNOWN - Error retrieving disk usage

## Features
1. **Threshold-based alerts**: Configurable warning and critical levels
2. **Error handling**: Graceful handling of mount point errors
3. **Nagios compatibility**: Proper exit codes and formatted output
4. **Precise monitoring**: Exact percentage reporting

## Output Examples
- `OK: Disk usage at 65.42% on /.`
- `WARNING: Disk usage at 85.17% on /.`
- `CRITICAL: Disk usage at 92.31% on /.`
- `UNKNOWN: Unable to get disk usage for /. Error: [error message]`

## Integration
Designed for Nagios NRPE or direct execution from Nagios server. Can be scheduled via cron for regular monitoring.
