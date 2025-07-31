# from resume_parser import ResumeParser
import yaml
from jinja2 import Environment, FileSystemLoader
import os

def load_yaml(resume_file):
    with open(resume_file, 'r') as file:
        return yaml.safe_load(file)

def latex_escape_filter(text):      
    if not isinstance(text, str):
        return text
    return text.replace('#', r'\#')

def build_resume_txt(data, template_file: str, output_file: str):
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

def build_resume_latex(data, template_file: str, output_file: str):
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

def build_cover_letter_latex(data, template_file: str, output_file: str):
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

    cover_letter_text = template.render(
        Contact = data.get('Contact', {}),
        Company = data.get('Company', {}),
        Content = data.get('Content', {}),
    )

    output_path = os.path.join('.build', output_file)
    with open(output_path, 'w') as file:
        file.write(cover_letter_text)

def main():
    resume_data = load_yaml('examples/resume-full.yaml')
    build_resume_txt(resume_data, 'resume-plaintext.txt.jinja2', 'resume-plaintext.txt')
    build_resume_latex(resume_data, 'resume-minimalist.tex.jinja2', 'resume-minimalist.tex')
    build_resume_latex(resume_data, 'resume-two-column.tex.jinja2', 'resume-two-column.tex')

    cover_letter_data = load_yaml('examples/example-cover-letter.yaml')
    build_cover_letter_latex(cover_letter_data, 'cover-letter.tex.jinja2', 'cover-letter.tex')

if __name__ == "__main__":
    main()
