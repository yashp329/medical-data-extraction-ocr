import re
from backend.src.parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        super().__init__(text)

    def parse(self):
        return {
            "patient_name": self.get_patient_name(),
            "phone_number":self.get_phone_no(),
            "medical_problems":self.get_medical_problems(),
            "hepatitis_B_vaccination":self.get_hepatitis_B_vaccination()
        }

    def get_patient_name(self):
        pattern = r'Patient Information Birth Date(.*?)\(\d{3}\) '
        matches = re.findall(pattern, self.text, re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name

    def remove_noise_from_name(self, name):
        pattern = r'((Jan|Feb|Mar|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]++)'
        date_matches = re.findall(pattern, name, re.DOTALL)
        date = date_matches[0][0]
        name_match = name.replace(date, '').strip()
        return name_match

    def get_phone_no(self):
        pattern = r'Patient Information Birth Date(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, re.DOTALL)
        return matches[0][1].strip()

    def get_medical_problems(self):
        pattern = r'List any Medical Problems.*?:\s*([^\n]+)'
        matches = re.findall(pattern, self.text, re.DOTALL)
        return matches[0].strip()

    def get_hepatitis_B_vaccination(self):
        pattern = r'Have you had the Hepatitis B vaccination\?(.*)(Yes|No)'
        matches = re.findall(pattern, self.text, re.DOTALL)
        return matches[0][1].strip()

if __name__ == '__main__':
    text = '''
 Patient Medical Record

    Patient Information Birth Date

    Jerry Lucas May 2 1998

    (279) 920-8204 Weight:

    4218 Wheeler Ridge Dr 57

    Buffalo, New York, 14201 Height:

    United States gnt
    170

    In Case of Emergency

    eee

    Joe Lucas . 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    Home phone United States
    Work phone

    General Medical History

    Chicken Pox (Varicelia): Measles: ..

    IMMUNE NOT IMMUNE

    Have you had the Hepatitis B vaccination?

    ‘Yes

    | List any Medical Problems (asthma, seizures, headaches):
    N/A

    7?
    v

    17/12/2020

    '''
    pp = PatientDetailsParser(text)
    print(pp.parse())