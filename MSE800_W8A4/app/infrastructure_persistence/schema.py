"""
SCHEMA SQL
keep schema separate so DB manager is clean.
"""

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
  user_id        INTEGER PRIMARY KEY AUTOINCREMENT,
  name           TEXT NOT NULL,
  email          TEXT NOT NULL UNIQUE,
  password_hash  TEXT NOT NULL,
  role           TEXT NOT NULL,
  loyalty_points INTEGER NOT NULL DEFAULT 0,
  created_at     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cars (
  car_id               INTEGER PRIMARY KEY AUTOINCREMENT,
  car_type             TEXT NOT NULL,
  make                 TEXT NOT NULL,
  model                TEXT NOT NULL,
  year                 INTEGER NOT NULL,
  mileage              INTEGER NOT NULL,
  available_now        INTEGER NOT NULL,
  min_rent_days        INTEGER NOT NULL,
  max_rent_days        INTEGER NOT NULL,
  daily_rate           REAL NOT NULL,
  service_interval_km  INTEGER NOT NULL,
  next_service_mileage INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS bookings (
  booking_id            INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id           INTEGER NOT NULL,
  car_id                INTEGER NOT NULL,
  start_date            TEXT NOT NULL,
  end_date              TEXT NOT NULL,
  status                TEXT NOT NULL,
  total_fee             REAL NOT NULL,
  estimated_km          INTEGER NOT NULL DEFAULT 0,
  auto_approved         INTEGER NOT NULL DEFAULT 0,
  decided_by_admin_id   INTEGER,
  decided_at            TEXT,
  created_at            TEXT NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES users(user_id),
  FOREIGN KEY(car_id) REFERENCES cars(car_id),
  FOREIGN KEY(decided_by_admin_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS maintenance_alerts (
  alert_id          INTEGER PRIMARY KEY AUTOINCREMENT,
  car_id            INTEGER NOT NULL,
  triggered_mileage INTEGER NOT NULL,
  message           TEXT NOT NULL,
  status            TEXT NOT NULL,
  created_at        TEXT NOT NULL,
  closed_at         TEXT,
  FOREIGN KEY(car_id) REFERENCES cars(car_id)
);

CREATE INDEX IF NOT EXISTS idx_bookings_car ON bookings(car_id);
CREATE INDEX IF NOT EXISTS idx_bookings_status ON bookings(status);
CREATE INDEX IF NOT EXISTS idx_alerts_status ON maintenance_alerts(status);
"""
