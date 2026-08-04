from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = '1. Connection string
Copy the connection details for your database.
Details:
Shared pooler
If your database password contains special characters, percent-encode them in the connection string.
Connection parameters
host:aws-0-ap-southeast-1.pooler.supabase.com
port:5432
database:postgres
user:postgres.dldkbkgmukmldfvagqjw
Code:
File: Code
```
postgresql://postgres.dldkbkgmukmldfvagqjw:MhdAkib0812@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres
```

2. Install Agent Skills (optional)
Agent Skills give AI coding tools ready-made instructions, scripts, and resources for working with Supabase more accurately and efficiently.
Code:
File: Code
```
npx skills add supabase/agent-skills
```'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
