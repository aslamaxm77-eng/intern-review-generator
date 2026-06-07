# from sqlalchemy import (
#     create_engine,
#     text
# )

# engine = create_engine(
#     "sqlite:///reviews.db"
# )

# def create_table():

#     with engine.begin() as conn:

#         conn.execute(text("""
#         CREATE TABLE IF NOT EXISTS reviews(

#             id INTEGER PRIMARY KEY,

#             intern_name TEXT,

#             week TEXT,

#             score REAL,

#             status TEXT,

#             feedback TEXT,

#             pending_topics TEXT
#         )
#         """))