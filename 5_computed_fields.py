# Computed field helps us to compute the field which we needed on the go using other fields 
#  like BMI is computed using weight and height

from pydantic import BaseModel, EmailStr, AnyUrl,Field,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age:int
    linked_in_urls: AnyUrl
    email: EmailStr
    weight: float 
    height:float  
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
   

def insert_patient_details(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print('BMI', patient.bmi)
    print('inserted')

patient_info={'name':'yiia','age':'68','email':'kopoplu@icici.com',
        'linked_in_urls':'https://linkedin.com/yiia','weight':87.89,'height':1.72,'married':False,
        'allergies':['pollen','dust'],'contact_details':{'phone':'9089090','emergency':'8989880'}}    
    
patient1=Patient(**patient_info)     # Validation -> type coersion        

insert_patient_details(patient1)
