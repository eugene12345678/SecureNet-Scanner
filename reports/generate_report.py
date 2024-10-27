from jinja2 import Environment, FileSystemLoader
import pdfkit  # Optional for PDF generation

def generate_report(ip_range, vulnerabilities, output_file='scan_report.html'):
    env = Environment(loader=FileSystemLoader('reports/templates'))
    template = env.get_template('report_template.html')

    rendered_html = template.render(ip_range=ip_range, vulnerabilities=vulnerabilities)

    with open(output_file, 'w') as file:
        file.write(rendered_html)

    # Convert to PDF
    pdfkit.from_file(output_file, output_file.replace('.html', '.pdf'))
