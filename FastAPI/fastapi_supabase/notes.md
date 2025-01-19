## Supabase FastAPI Tutorial by Eric Roby

- Create a Supabase account, org, and project
  
- Copy the API URL and Key

### SQL Operations

- In the web interface, create a table. Then add a column called first_name

- Read: 
```python
# Read table
result = supabase.table("demo-table").select("*").execute()
print(result)

# Read row
result = supabase.table("demo-table").select("*").eq("id", 1).execute()
print(result)
```

- Create row:
```python
# Create a new row into table
new_row = {"first_name": "John"}
supabase.table("demo-table").insert(new_row).execute()
```

- Update row:
```python
# Update a row
updated_row = {"first_name": "Jane"}
supabase.table("demo-table").update(updated_row).eq("id", 1).execute()
```

- Delete row:
```python
# Delete a row
supabase.table("demo-table").delete().eq("id", 1).execute()
```



### Uploading images to Supabase

- Create a bucket in the storage section