import yaml
from jinja2 import Environment, FileSystemLoader, Template
import os

def build_resume_txt(input_file: str, template_file: str, output_file: str) -> None:
    """Build a plaintext resume from a YAML input file and a Jinja2 template.
    Args:
        input_file (str): Path to the YAML file containing resume data.
        template_file (str): Path to the Jinja2 template file for the resume.
        output_file (str): Path where the rendered resume will be saved.
    """
    data = _load_yaml(input_file)
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)
    resume_text = _render_resume(template, data)
    _write_to_file(output_file, resume_text)

def build_resume_latex(input_file: str, template_file: str, output_file: str) -> None:
    """Build a LaTeX resume from a YAML input file and a Jinja2 template.
    Args:
        input_file (str): Path to the YAML file containing resume data.
        template_file (str): Path to the Jinja2 template file for the resume.
        output_file (str): Path where the rendered LaTeX resume will be saved.
    """
    data = _load_yaml(input_file)
    template = _get_latex_template(template_file)
    resume_text = _render_resume(template, data)
    _write_to_file(output_file, resume_text)

def build_cover_letter(input_file: str, template_file: str, output_file: str) -> None:
    """Build a LaTeX cover letter from a YAML input file and a Jinja2 template.
    Args:
        input_file (str): Path to the YAML file containing cover letter data.
        template_file (str): Path to the Jinja2 template file for the cover letter.
        output_file (str): Path where the rendered LaTeX cover letter will be saved.
    """
    data = _load_yaml(input_file)
    template = _get_latex_template(template_file)
    cover_letter_text = _render_cover_letter(template, data)
    _write_to_file(output_file, cover_letter_text)

def _load_yaml(resume_file) -> any:
    """Load YAML data from a file.
    Args:
        resume_file (str): Path to the YAML file containing resume data.
    Returns:
        dict: Parsed YAML data as a dictionary."""
    with open(resume_file, 'r') as file:
        return yaml.safe_load(file)

def _latex_escape_filter(text) -> str:    
    """Escape special characters for LaTeX.
    Args:
        text (str): The text to escape.
    Returns:
        str: The escaped text suitable for LaTeX."""  
    if not isinstance(text, str):
        return text
    return text.replace('#', r'\#')

def _render_resume(template: Template, data: dict) -> str:
    """Render the resume using the provided template and data.
    Args:
        template (Template): The Jinja2 template for the resume.
        data (dict): The data to render in the template.
    Returns:
        str: The rendered resume as a string."""
    return template.render(
        Contact = data.get('Contact', {}),
        Education = data.get('Education', []),
        Experience = data.get('Experience', []),
        Skills = data.get('Skills', []),
        Projects = data.get('Projects', []),
        Honors = data.get('Honors', []),
    )

def _render_cover_letter(template: Template, data: dict) -> str:
    """Render the cover letter using the provided template and data.
    Args:
        template (Template): The Jinja2 template for the cover letter.
        data (dict): The data to render in the template.
    Returns:
        str: The rendered cover letter as a string."""
    return template.render(
        Contact = data.get('Contact', {}),
        Company = data.get('Company', {}),
        Content = data.get('Content', {}),
    )

def _get_latex_template(template_file: str) -> Template:
    """Get a LaTeX template from the templates directory.
    Args:
        template_file (str): The name of the Jinja2 template file for LaTeX.
    Returns:
        Template: The Jinja2 template object for the specified LaTeX template file."""
    env = Environment(
        loader = FileSystemLoader('templates'),
        block_start_string = '<BLOCK>',
        block_end_string = '</BLOCK>',
        variable_start_string = '<VAR>',
        variable_end_string = '</VAR>',
        comment_start_string = ' <!--',
        comment_end_string = '-->',
    )
    env.filters['latex_escape'] = _latex_escape_filter   # Ensure '#' character is escaped in LaTeX
    return env.get_template(template_file)

def _write_to_file(output_file: str, content: str) -> None:
    """Write content to a file.
    Args:
        output_file (str): The path where the content will be saved.
        content (str): The content to write to the file.
    """
    output_path = os.path.join('.build', output_file)
    with open(output_path, 'w') as file:
        file.write(content)