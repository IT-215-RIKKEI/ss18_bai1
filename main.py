from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from schemas import (
    DepartmentCreate,
    EmployeeCreate,
    EmployeeResponse,
    DepartmentDetailResponse
)
from services import (
    create_department_service,
    get_department_detail_service,
    create_employee_service
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Department Employee API"
)

@app.post("/departments")
def create_department(
    data: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return create_department_service(data, db)


@app.get(
    "/departments/{department_id}",
    response_model=DepartmentDetailResponse
)
def get_department_detail(
    department_id: int,
    db: Session = Depends(get_db)
):
    return get_department_detail_service(department_id, db)

@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=201
)
def create_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_employee_service(data, db)
