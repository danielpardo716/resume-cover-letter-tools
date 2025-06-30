import yaml

class ResumeParser:
    def __init__(self, resume_file):
        self.resume_file = resume_file
        self.resume_data = self.load()

    def load(self):
        with open(self.resume_file, 'r') as file:
            return yaml.safe_load(file)
    
    def get_contact(self):
        return self.resume_data.get('Contact', {})

    def get_education(self):
        return self.resume_data.get('Education', [])

    def get_experience(self):
        return self.resume_data.get('Experience', [])

    def get_projects(self):
        return self.resume_data.get('Projects', [])
    
    def get_skills(self):
        return self.resume_data.get('Skills', [])
    
    def get_honors(self):
        return self.resume_data.get('Honors', [])