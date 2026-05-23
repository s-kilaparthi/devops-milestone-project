#!/bin/bash

# Health check script - checks if app and services are running
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
LOG_FILE="health_check.log"

log() {
    echo "[$TIMESTAMP] $1" | tee -a $LOG_FILE
}

check_python() {
    log "Checking Python availability..."
    if command -v python3 &>/dev/null; then
        VERSION=$(python3 --version)
        log "Python available: $VERSION ✅"
        return 0
    else
        log "Python NOT found ❌"
        return 1
    fi
}

check_disk_space() {
    log "Checking disk space..."
    USAGE=$(df -h . | awk 'NR==2 {print $5}' | tr -d '%')
    
    if [ "$USAGE" -lt 80 ]; then
        log "Disk usage: ${USAGE}% — OK ✅"
        return 0
    else
        log "Disk usage: ${USAGE}% — WARNING ❌"
        return 1
    fi
}

check_files() {
    log "Checking required files exist..."
    REQUIRED=("app/main.py" "app/test_main.py" ".github/workflows/pipeline.yml")
    
    for file in "${REQUIRED[@]}"; do
        if [ -f "$file" ]; then
            log "Found: $file ✅"
        else
            log "MISSING: $file ❌"
        fi
    done
}

run_all_checks() {
    log "=== Starting Health Check ==="
    check_python
    check_disk_space
    check_files
    log "=== Health Check Complete ==="
}

run_all_checks
