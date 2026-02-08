from pydantic import BaseModel, EmailStr, AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',
                       description='Give the name of patient in less than 50 chars',
                       examples=['Aknimi','Rakimini'])]
    age:int
    linked_in_urls: AnyUrl
    email: EmailStr
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None, description='Is the patient married or not')]
    allergies: Optional[List[str]]=Field(max_length=5)
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains=['hdfc.com','icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value     


    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age',mode='before')
    @classmethod
    def check_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be between 0 to 100')        

def insert_patient_details(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

patient_info={'name':'yiia','age':'49','email':'kopoplu@icici.com',
        'linked_in_urls':'https://linkedin.com/yiia','weight':87.89,'married':False,
        'allergies':['pollen','dust'],'contact_details':{'phone':'9089090'}}    
    
patient1=Patient(**patient_info)     # Validation -> type coersion        

insert_patient_details(patient1)
