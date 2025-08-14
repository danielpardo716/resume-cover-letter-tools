import source.tools as tools
import typer
from rich import print as rprint

app = typer.Typer()

@app.command()
def build(type: str, input_file: str, output_file: str) -> None:
    """Build a resume or cover letter based on the specified type.
    Args:
        type (str): The type of document to build ('resume_plaintext', 'resume_minimalist', 'resume_two_column', 'cover_letter').
        input_file (str): Path to the YAML file containing resume or cover letter data.
        output_file (str): Path where the rendered document will be saved.
    """
    if type == 'resume_plaintext':
        tools.build_resume_txt(input_file, 'resume-plaintext.txt.jinja2', output_file)
        rprint(f"[green]Plaintext resume built successfully: {output_file}[/green]")

    elif type == 'resume_minimalist':
        tools.build_resume_latex(input_file, 'resume-minimalist.tex.jinja2', output_file)
        rprint(f"[green]Minimalist LaTeX resume built successfully: {output_file}[/green]")

    elif type == 'resume_two_column':
        tools.build_resume_latex(input_file, 'resume-two-column.tex.jinja2', output_file)
        rprint(f"[green]Two-column LaTeX resume built successfully: {output_file}[/green]")

    elif type == 'cover_letter':
        tools.build_cover_letter(input_file, 'cover-letter.tex.jinja2', output_file)
        rprint(f"[green]Cover letter built successfully: {output_file}[/green]")
    else:
        raise ValueError(f"Unknown build type: {type}")

if __name__ == "__main__":
    app()