from pydantic import BaseModel, ValidationError, validator
from typing import Optional
from typing_extensions import Literal

#constants
VALUE_1 = "1-9"
VALUE_2 = "10-99"
VALUE_3 = "99+"
VALUE_4 = "unknown"

class Company(BaseModel):
    name: str
    employees: Optional[Literal[VALUE_1, VALUE_2, VALUE_3, VALUE_4]]
    
    # EXTEND HERE
    # Pre makes it before the default validation
    @validator('employees', pre=True)
    def split_str(cls, v):
        if isinstance(v, str):
            v = v.strip()
        if isinstance(v, int) or (v[0] in ('-', '+') and v[1:].isdigit()) or v.isdigit():
            if int(v) < 10 and int(v) > 0:
                return VALUE_1
            elif int(v) < 100 and int(v) > 9:
                return VALUE_2
            elif int(v) >= 100:
                return VALUE_3
        return v

if __name__ == '__main__':
    data = {'name': 'Good Company B.V.', 'employees': '1-9'}
    try:
        company = Company(**data)
        print(f"{company.name} has {company.employees} number of employees")
    except ValidationError:
        print(f"Invalid data supplied")
        raise