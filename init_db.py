from app.database import engine, Base

# Drop all tables (optional)
Base.metadata.drop_all(bind=engine)
print("Existing tables dropped (if any).")

# Create tables
Base.metadata.create_all(bind=engine)
print("Database and tables created!")
