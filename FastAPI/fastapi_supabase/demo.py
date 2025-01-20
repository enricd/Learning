from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

is_sql_crud_demo = False
is_storage_bucket_demo = False

if is_sql_crud_demo:
    # Create a new row into table
    new_row = {"first_name": "John"}
    supabase.table("demo-table").insert(new_row).execute()

    # Update a row in table
    new_row = {"first_name": "Jane"}
    supabase.table("demo-table").update(new_row).eq("id", 2).execute()

    # Delete a row in table
    supabase.table("demo-table").delete().eq("id", 2).execute()

    # Read table
    result = supabase.table("demo-table").select("*").execute()
    print(result)

    # Read row
    result = supabase.table("demo-table").select("*").eq("id", 1).execute()
    print(result)


if is_storage_bucket_demo:
    response = supabase.storage.from_("demo-bucket").get_public_url("image_1.png")

    print(response)  # returns the public url of the file

