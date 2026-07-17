from pymongo import MongoClient
try:
    MONGO_URI = "mongodb+srv://muskankatare07_db_user:sutOqQaNxjMybaop@cluster0.mnravcx.mongodb.net/?appName=Cluster0"
    client = MongoClient(MONGO_URI)
    client.admin.command("ping")
    db= client["SSUS"]
    student_collection= db["student"]
    marks_collection= db["marks"]
    attendance_collection= db["attendance"]
    bmi_collection= db["bmi reports"]
    print("mongodb Succesfully connect")
except Exception as e:
    print("mongodb error",e)