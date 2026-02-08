# Model validator are for scenerio where we need to validate two or fileds fields together
# like for age gt 60 there must be a emergency contact number, otherwise patient detail will not be saved

from pydantic import BaseModel, EmailStr, AnyUrl,Field,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age:int
    linked_in_urls: AnyUrl
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is must for a patient having age gt 60')
        return model    

             

def insert_patient_details(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

patient_info={'name':'yiia','age':'68','email':'kopoplu@icici.com',
        'linked_in_urls':'https://linkedin.com/yiia','weight':87.89,'married':False,
        'allergies':['pollen','dust'],'contact_details':{'phone':'9089090','emergency':'8989880'}}    
    
patient1=Patient(**patient_info)     # Validation -> type coersion        

insert_patient_details(patient1)
