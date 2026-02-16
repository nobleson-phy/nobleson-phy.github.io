#!/usr/bin/env python3
"""Generate a professional academic CV as PDF using fpdf2."""

from fpdf import FPDF

# --- Colors ---
NAVY = (0, 51, 102)
DARK_GRAY = (51, 51, 51)
MED_GRAY = (100, 100, 100)
LIGHT_GRAY = (220, 220, 220)
ACCENT = (0, 102, 179)

class AcademicCV(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 15, 20)

    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(*MED_GRAY)
            self.cell(0, 8, 'Nobleson Kunjappy - Curriculum Vitae', align='R')
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(*MED_GRAY)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def add_name_header(self):
        # Name
        self.set_font('Helvetica', 'B', 28)
        self.set_text_color(*NAVY)
        self.cell(0, 14, 'Nobleson Kunjappy', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(2)

        # Title
        self.set_font('Helvetica', '', 12)
        self.set_text_color(*MED_GRAY)
        self.cell(0, 6, 'Postdoctoral Researcher', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(1)

        # Contact line
        self.set_font('Helvetica', '', 9)
        self.set_text_color(*ACCENT)
        contact = 'nobleson@kumamoto-u.ac.jp  |  ORCID: 0000-0003-2715-4504  |  Kumamoto University, Japan'
        self.cell(0, 5, contact, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(1)

        # Divider
        self.set_draw_color(*NAVY)
        self.set_line_width(0.8)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(6)

    def section_heading(self, title):
        self.ln(3)
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(*NAVY)
        self.cell(0, 7, title.upper(), new_x='LMARGIN', new_y='NEXT')
        # Underline
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.4)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(4)

    def subsection(self, title, right_text=''):
        self.set_font('Helvetica', 'B', 10.5)
        self.set_text_color(*DARK_GRAY)
        w = self.get_string_width(title)
        self.cell(w + 2, 5.5, title)
        if right_text:
            self.set_font('Helvetica', '', 9.5)
            self.set_text_color(*MED_GRAY)
            self.cell(0, 5.5, right_text, align='R')
        self.ln(5.5)

    def detail_italic(self, text):
        self.set_font('Helvetica', 'I', 9.5)
        self.set_text_color(*MED_GRAY)
        self.multi_cell(0, 4.5, text)
        self.ln(1)

    def bullet(self, text, indent=5):
        x = self.get_x()
        self.set_x(x + indent)
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(*DARK_GRAY)
        bullet_w = self.get_string_width('- ') + 1
        self.cell(bullet_w, 4.5, '- ')
        self.multi_cell(170 - indent - bullet_w, 4.5, text)
        self.ln(0.5)

    def pub_entry(self, role, authors, title, venue, doi=''):
        self.set_font('Helvetica', 'B', 8.5)
        self.set_text_color(*ACCENT)
        role_w = self.get_string_width(role) + 3
        self.cell(role_w, 4.5, role)

        self.set_font('Helvetica', '', 9)
        self.set_text_color(*DARK_GRAY)
        remaining_w = 170 - role_w
        self.multi_cell(remaining_w, 4.5, f'{authors}, "{title}", {venue}')
        self.ln(1.5)


def build_cv():
    pdf = AcademicCV()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.add_name_header()

    # ===== RESEARCH INTERESTS =====
    pdf.section_heading('Research Interests')
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(*DARK_GRAY)
    pdf.multi_cell(0, 4.5,
        'Gravitational wave astronomy using pulsar timing arrays; '
        'noise modelling and Bayesian data analysis for PTA datasets; '
        'neutron star structure and properties in modified gravity theories; '
        'precision pulsar timing with low-frequency radio observations.'
    )
    pdf.ln(1)

    # ===== EDUCATION =====
    pdf.section_heading('Education')

    pdf.subsection('Ph.D.', 'Jan 2018 -- Nov 2023')
    pdf.detail_italic('Birla Institute of Technology & Science (BITS), Pilani, Hyderabad Campus, India')
    pdf.detail_italic('Thesis: "Advanced Studies on Neutron Stars and Pulsars"')

    pdf.subsection('M.Sc. in Astronomy & Astrophysics', 'Aug 2016 -- Jun 2018')
    pdf.detail_italic('Osmania University, Hyderabad, India')
    pdf.detail_italic('Thesis: "Parametric study of short-period eclipsing Post Common Envelope Binaries"')

    pdf.subsection('M.Sc. in Mathematics', 'Jun 1998 -- Apr 2000')
    pdf.detail_italic('Osmania University, Hyderabad, India')

    pdf.subsection('B.Sc. in Mathematics, Physics & Chemistry', 'Jun 1995 -- Apr 1998')
    pdf.detail_italic('Govt. Giriraj College (Osmania University), Nizamabad, India')

    # ===== RESEARCH POSITIONS =====
    pdf.section_heading('Research Positions')

    pdf.subsection('Postdoctoral Researcher', 'Nov 2023 -- Nov 2025')
    pdf.detail_italic('Kumamoto University, Kumamoto, Japan')
    pdf.bullet('InPTA Data Release 2: dataset processing and timing analysis')
    pdf.bullet('InPTA DR2 Noise Analysis: customised single-pulsar noise modelling')
    pdf.bullet('IPTA Data Combination: contributing to the international data release')

    # ===== TEACHING =====
    pdf.section_heading('Teaching Experience')

    pdf.subsection('Teaching Assistant: Introduction to Radio Astronomy', '2022')
    pdf.detail_italic('BITS Pilani, Hyderabad Campus, India')
    pdf.bullet('Introduction to Radio Astronomy course for masters students')

    pdf.subsection('Teaching Assistant: Introduction to Astrophysics', '2022')
    pdf.detail_italic('BITS Pilani, Hyderabad Campus, India')
    pdf.bullet('Introduction to Astrophysics course for masters students')

    #pdf.subsection('Invited Lecture', '2022')
    #pdf.detail_italic('Research Facility Training Program, Osmania University, Hyderabad, India')
    #pdf.bullet('"Neutron stars as tools to study Advanced Astrophysics"')

    pdf.subsection('Teaching Assistant: PHY F110 Physics Laboratory', '2019 -- 2021')
    pdf.detail_italic('BITS Pilani, Hyderabad Campus, India')
    pdf.bullet('Classical Physics laboratory course for undergraduate students (40 hours per semester)')

    pdf.add_page()

    # ===== PUBLICATIONS =====
    pdf.section_heading('Selected Publications')
    pdf.set_font('Helvetica', 'I', 9)
    pdf.set_text_color(*MED_GRAY)
    pdf.cell(0, 4.5, 'Full list: ORCID 0000-0003-2715-4504  |  20 peer-reviewed publications', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)

    # First-author papers
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 5, 'First-Author Papers', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)

    pdf.pub_entry('[1]', 'K. Nobleson, S. Banik, T. Malik',
        'Unveiling a universal relationship between the f(R) parameter and neutron star properties',
        'Phys. Rev. D 107, 124045 (2023)')

    pdf.pub_entry('[2]', 'K. Nobleson, N. Agarwal, R. Girgaonkar, et al.',
        'Low-frequency wideband timing of InPTA pulsars observed with the uGMRT',
        'MNRAS 512(1), 1234-1243 (2022)')

    pdf.pub_entry('[3]', 'K. Nobleson, T. Malik, S. Banik',
        'Tidal deformability of neutron stars with exotic particles within a density dependent relativistic mean field model in R-squared gravity',
        'JCAP 2021(08), 012 (2021)')

    pdf.pub_entry('[4]', 'K. Nobleson, A. Ali, S. Banik',
        'Comparison of perturbative and non-perturbative methods in f(R) gravity',
        'Eur. Phys. J. C 82, 32 (2022)')

    # Co-lead papers
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 5, 'Co-Lead Papers', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)

    pdf.pub_entry('[5]', 'P. Rana, P. Tarafdar, K. Nobleson, et al.',
        'The Indian Pulsar Timing Array Data Release 2: I. Dataset and Timing Analysis',
        'PASA 42, e108 (2025)')

    pdf.pub_entry('[6]', 'P. Tarafdar, K. Nobleson, P. Rana, et al.',
        'The Indian Pulsar Timing Array: First data release',
        'PASA 39, e053 (2022)')

    pdf.pub_entry('[7]', 'A.K. Paladi, C. Dwivedi, P. Rana, K. Nobleson, et al.',
        'Multiband extension of the wideband timing technique',
        'MNRAS 527(1), 213-231 (2023)')

    # Selected co-author papers
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 5, 'Selected Co-Author Papers', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)

    pdf.pub_entry('[8]', 'J. Antoniadis, et al. (EPTA & InPTA)',
        'The second data release from the European Pulsar Timing Array: III. Search for gravitational wave signals',
        'A&A 678, A50 (2023)')

    pdf.pub_entry('[9]', 'J. Antoniadis, et al. (EPTA & InPTA)',
        'The second data release from the European Pulsar Timing Array: IV. Implications for massive black holes, dark matter, and the early Universe',
        'A&A 685, A94 (2024)')

    pdf.pub_entry('[10]', 'G. Agazie, et al. (IPTA)',
        'Comparing Recent Pulsar Timing Array Results on the Nanohertz Stochastic Gravitational-wave Background',
        'ApJ 966(1), 105 (2024)')

    pdf.pub_entry('[11]', 'A. Srivastava, et al.',
        'Noise analysis of the Indian Pulsar Timing Array data release I',
        'Phys. Rev. D 108, 023008 (2023)')

    pdf.pub_entry('[12]', 'F. Iraci, et al. (EPTA & InPTA)',
        'Combining the second data release of the European Pulsar Timing Array with low-frequency pulsar data',
        'A&A 704, A109 (2025)')

    pdf.pub_entry('[13]', 'A. Susobhanan, et al.',
        'pinta: The uGMRT data processing pipeline for the Indian Pulsar Timing Array',
        'PASA 38, e017 (2021)')

    # ===== TALKS =====
    pdf.section_heading('Talks & Presentations')

    pdf.subsection('International Pulsar Timing Array (IPTA) 2025')
    pdf.bullet('K. Nobleson, et al., "The Indian Pulsar Timing Array Data Release 2: II. Noise Analysis" (Presenter)')

    pdf.subsection('32nd Meeting of IAGRG, 2022')
    pdf.bullet('Nobleson K., Malik T., Banik S., "Tidal Deformability of Neutron Stars in R-Squared Gravity" (Presenter)')

    pdf.subsection('IPTA Catchup Meeting, 2022')
    pdf.bullet('Tarafdar P., et al., "The Indian Pulsar Timing Array: First data release" (Presenter)')

    pdf.subsection('Research Facility Training Program, Osmania University, 2022')
    pdf.bullet('"Neutron stars as tools to study Advanced Astrophysics" (Invited Talk)')

    pdf.subsection('Science at Low Frequencies VIII, 2021')
    pdf.bullet('Nobleson K., et al., "Low-frequency Wideband Timing on uGMRT Data" (Presenter)')

    pdf.subsection('27th Intl. Conf. on Advances in Relativity and Cosmology, 2021')
    pdf.bullet('Nobleson K., Malik T., Banik S., "Tidal deformability of NS in R-squared gravity" (Presenter)')

    pdf.subsection('Astronomical Society of India, 2020')
    pdf.bullet('Nobleson K., Ali A., Banik S., "Neutron Stars with realistic EoS in f(R) theories of gravity" (Presenter)')

    pdf.subsection('Compact Stars in QCD Phase Diagram VIII, ICTS Bangalore, 2020')
    pdf.bullet('Attendee')

    # ===== EMPLOYMENT =====
    pdf.section_heading('Prior Employment')

    pdf.subsection('Graphic Designer', 'May 2005 -- Aug 2016')
    pdf.detail_italic('Deloitte Support Services India Pvt. Ltd., Hyderabad, India')
    pdf.bullet('Designed marketing materials (print and digital) for branding and visual identity')
    pdf.bullet('Mentored junior colleagues and managed designer-client communications')

    pdf.subsection('Medical Transcriptionist / Proofreader', 'Aug 2000 -- May 2005')
    pdf.detail_italic('Vasant Scribes Pvt. Ltd., Hyderabad, India')
    pdf.bullet('Transcribed and proofread medical reports with high accuracy across multiple specialties')

    # ===== MEMBERSHIPS =====
    pdf.section_heading('Professional Memberships')
    pdf.bullet('Astronomical Society of India (ASI), 2018 -- present')
    pdf.bullet('Indian Pulsar Timing Array (InPTA), 2019 -- present')
    pdf.bullet('International Pulsar Timing Array (IPTA), 2021 -- present')

    # Output
    out_path = '/Users/kujovi/Desktop/KU/github_research_profile.profile/Research_CV.pdf'
    pdf.output(out_path)
    print(f'CV generated: {out_path}')

if __name__ == '__main__':
    build_cv()
