from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from ..database import supabase, SUPABASE_BUCKET, SUPABASE_URL
from ..models import EmployeeCreate, EmployeeUpdate
from ..forms import as_form
from fastapi.templating import Jinja2Templates
from ..auth import get_current_user


router = APIRouter()
templates = Jinja2Templates(directory="./employee_repo/templates")


@router.get("/", response_class=HTMLResponse)
async def read_employees(request: Request, current_user: dict = Depends(get_current_user)):
    response = supabase.from_("employees").select("*").eq("is_active", True).execute()
    employees = response.data
    return templates.TemplateResponse("index.html", {"request": request, "employees": employees})


@router.get("/add", response_class=HTMLResponse)
async def add_employee_form(request: Request, current_user: dict = Depends(get_current_user)):
    return templates.TemplateResponse("add_employee.html", {"request": request})


@router.post("/add")
async def add_employee(
    request: Request,
    employee: EmployeeCreate = Depends(EmployeeCreate.as_form),
    image: UploadFile = File(None),
    current_user: dict = Depends(get_current_user),
):
    image_url = None
    if image and image.filename != "":
        image_filename = f"{employee.first_name}_{employee.last_name}_{image.filename}"
        file_content = await image.read()
        response = supabase.storage.from_(SUPABASE_BUCKET).upload(image_filename, file_content)
        if response.status_code == 200:
            image_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{image_filename}"

    supabase.table("employees").insert(
        {
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "email": employee.email,
            "salary": employee.salary,
            "image_url": image_url,
        }
    ).execute()

    return RedirectResponse("/", status_code=303)


@router.get("/edit/{employee_id}", response_class=HTMLResponse)
async def edit_employee_form(request: Request, employee_id: int, current_user: dict = Depends(get_current_user)):
    response = supabase.table("employees").select("*").eq("id", employee_id).execute()
    employee = response.data[0] if response.data else None
    if not employee:
        return templates.TemplateResponse("error.html", {"request": request, "errors": ["Employee not found"]}, status_code=404)
    return templates.TemplateResponse("edit_employee.html", {"request": request, "employee": employee})


@router.post("/edit/{employee_id}")
async def edit_employee(
    request: Request,
    employee_id: int,
    employee: EmployeeUpdate = Depends(EmployeeUpdate.as_form),
    image: UploadFile = File(None),
    current_user: dict = Depends(get_current_user),
):
    image_url = None
    if image and image.filename != "":
        image_filename = f"{employee.first_name}_{employee.last_name}_{image.filename}"
        file_content = await image.read()
        response = supabase.storage.from_(SUPABASE_BUCKET).upload(image_filename, file_content)
        if response.status_code == 200:
            image_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{image_filename}"

    update_data = employee.model_dump()
    if image_url:
        update_data["image_url"] = image_url
    supabase.table("employees").update(update_data).eq("id", employee_id).execute()

    return RedirectResponse("/", status_code=303)


@router.get("/deactivate/{employee_id}")
async def deactivate_employee(employee_id: int, current_user: dict = Depends(get_current_user)):
    supabase.table("employees").update({"is_active": False}).eq("id", employee_id).execute()

    return RedirectResponse("/", status_code=303)