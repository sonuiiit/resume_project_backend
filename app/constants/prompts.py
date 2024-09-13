pdf_to_html_prompt='''
Generate an HTML resume with a modern, stylish design. The resume should be well-structured with the following sections, each having a clear heading and aesthetically pleasing layout. Use CSS to style the resume with a professional color scheme, modern typography, and clean lines. The design should be responsive and visually engaging.

    Header Section:
    - Name: [Candidate Name] (Bold and prominent)
    - Job Title: [Candidate Job Title] (Subtle font size difference)
    - Contact Information: (Icons for phone, email, LinkedIn, and website)
      - Phone: [Phone Number]
      - Email: [Email Address]
      - LinkedIn: [LinkedIn URL]
      - Website/Portfolio: [Website URL]
    - Style: Centered text, bold name, and job title with icons for contact information.

    Summary Section:
    - Create a brief, engaging summary (3-4 lines) highlighting key skills, experiences, and career goals.
    - Style: Use a different background color or border to distinguish this section.

    Skills Section:
    - List skills with bullet points or graphical progress bars/icons.
    - Style: Use icons or bars to visually represent proficiency levels.

    Work Experience Section:
    - For each job:
      - Job Title: [Job Title]
      - Company Name: [Company Name]
      - Dates: [Start Date] - [End Date]
      - Responsibilities and Achievements:
        - Use bullet points for responsibilities.
        - Highlight achievements and results.
    - Style: Clean layout with subtle borders or shading for each job entry.

    Education Section:
    - Degree: [Degree Name]
    - Institution: [Institution Name]
    - Dates: [Start Date] - [End Date]
    - Additional Information: (Honors, Awards, GPA, Relevant Courses, etc.)
    - Style: Consistent with the work experience section.

    Certifications Section:
    - List certifications relevant to the candidate's career.
    - Style: Use icons or badges for certifications if applicable.

    Languages Section:
    - List languages and proficiency levels.
    - Style: Use flags or graphical elements to represent proficiency.

    Hobbies and Interests Section:
    - List hobbies or interests to add a personal touch.
    - Style: Keep this section visually appealing with icons or small graphics.

    CSS Styling Notes:
    - Color Scheme: Professional color scheme like navy blue, dark gray, and white.
    - Fonts: Modern, clean fonts for headings and body text. (e.g., 'Arial', 'Helvetica', 'Roboto')
    - Layout: Ensure responsive design.
    - Visual Elements: Subtle lines or shapes to separate sections.
    
    Do not include anything that is not a part of details

 details:{details} Kindly use these details to do so.
 
 
 Stricly give the code only.


'''