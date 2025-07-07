# from resume_parser import ResumeParser
import yaml
from jinja2 import Environment, FileSystemLoader
import os

def build_resume(data, template_file: str, output_file: str):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)

    resume_text = template.render(
        Contact = data.get('Contact', {}),
        Education = data.get('Education', []),
        Experience = data.get('Experience', []),
        Skills = data.get('Skills', []),
        Projects = data.get('Projects', []),
        Honors = data.get('Honors', []),
    )

    output_path = os.path.join('.build', output_file)
    with open(output_path, 'w') as file:
        file.write(resume_text)

def load_yaml(resume_file):
    with open(resume_file, 'r') as file:
        return yaml.safe_load(file)

def latex_escape_filter(text):      
    if not isinstance(text, str):
        return text
    return text.replace('#', r'\#')

def build_latex(data, template_file: str, output_file: str):
    env = Environment(
        loader = FileSystemLoader('templates'),
        block_start_string = '<BLOCK>',
        block_end_string = '</BLOCK>',
        variable_start_string = '<VAR>',
        variable_end_string = '</VAR>',
        comment_start_string = ' <!--',
        comment_end_string = '-->',
    )
    env.filters['latex_escape'] = latex_escape_filter   # Ensure '#' character is escaped in LaTeX
    template = env.get_template(template_file)

    resume_text = template.render(
        Contact = data.get('Contact', {}),
        Education = data.get('Education', []),
        Experience = data.get('Experience', []),
        Skills = data.get('Skills', []),
        Projects = data.get('Projects', []),
        Honors = data.get('Honors', []),
    )

    output_path = os.path.join('.build', output_file)
    with open(output_path, 'w') as file:
        file.write(resume_text)


def main():
    resume_data = load_yaml('examples/resume-full.yaml')
    build_resume(resume_data, 'resume-plaintext.txt', 'resume-plaintext-out.txt')
    build_latex(resume_data, 'resume-minimalist.tex', 'resume-minimalist-out.tex')

if __name__ == "__main__":
    main()
