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

- Create a bucket in the storage section and upload an image 

```python	
response = supabase.storage.from_("demo-bucket").get_public_url("image_1.png")
print(response)  # returns the public url of the file
```


### Employee Management System

- Create a table called employees

In Supabase web sql editor:
```sql
create table employees (
    id serial primary key,
    first_name text not null,
    last_name text not null,
    email text unique not null,
    salary numeric not null,
    image_url text,
    is_active boolean default true
);
```

