"""
SETTINGS / CONFIG
all constants here so easy change, no hunting in code.
"""

DB_PATH = "app/data/car_rental.db"
LOG_FILE = "logs/app.log"

DEFAULT_ADMIN_EMAIL = "admin@local.com"
DEFAULT_ADMIN_PASSWORD = "sysad1$"
DEFAULT_ADMIN_NAME = "System Admin"

# Loyalty rules (simple and explainable)
LOYALTY_REDEEM_BLOCK = 100      # must redeem by 100 points block
LOYALTY_REDEEM_VALUE = 10.0     # 100 points = $10 off
LOYALTY_EARN_PER_DOLLAR = 10.0  # 1 point per $10 spend

# Auto-approve rules (innovation)
AUTO_APPROVE_MAX_DAYS = 7
AUTO_APPROVE_MAX_EXTRA = 200.0
AUTO_APPROVE_MAX_DAILY_RATE = 150.0
