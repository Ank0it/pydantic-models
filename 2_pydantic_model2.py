from pydantic import BaseModel, EmailStr, AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',
                       description='Give the name of patient in less than 50 chars',
                       example=['Aknimi','Rakimini'])]
    age:int=Field(gt=0,lt=120)
    linked_in_urls: AnyUrl
    email: EmailStr
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None, description='Is the patient married or not')]
    allergies: Optional[List[str]]=Field(max_length=5)
    contact_details: Dict[str,str]

def insert_patient_details(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_details(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info={'name':'yiia','age':'49','email':'kopoplu@gmail.com',
        'linked_in_urls':'https://linkedin.com/yiia','weight':87.89,'married':False,
        'allergies':['pollen','dust'],'contact_details':{'phone':'9089090'}}    
    
patient1=Patient(**patient_info)

insert_patient_details(patient1)
