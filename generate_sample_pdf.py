from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

def create_sample_medical_report():
    # Create the output directory if it doesn't exist
    if not os.path.exists('sample_pdfs'):
        os.makedirs('sample_pdfs')
    
    # Create the PDF document
    doc = SimpleDocTemplate("sample_pdfs/sample_medical_report.pdf", pagesize=letter)
    
    # Get styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=20
    )
    
    normal_style = styles['Normal']
    
    # Build the document content
    content = []
    
    # Title
    content.append(Paragraph("MEDICAL CONSULTATION REPORT", title_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Patient Information
    content.append(Paragraph("PATIENT INFORMATION", heading_style))
    
    patient_data = [
        ["Name:", "John Smith"],
        ["Date of Birth:", "05/15/1978"],
        ["Gender:", "Male"],
        ["Medical Record Number:", "MRN-12345678"],
        ["Date of Visit:", "06/10/2023"]
    ]
    
    patient_table = Table(patient_data, colWidths=[1.5*inch, 4*inch])
    patient_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    content.append(patient_table)
    content.append(Spacer(1, 0.2*inch))
    
    # Chief Complaint
    content.append(Paragraph("CHIEF COMPLAINT", heading_style))
    content.append(Paragraph("Patient presents with persistent fatigue, joint pain, and morning stiffness for the past 3 months. Reports occasional fever and weight loss of approximately 10 pounds over the same period.", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # History of Present Illness
    content.append(Paragraph("HISTORY OF PRESENT ILLNESS", heading_style))
    content.append(Paragraph("The patient is a 45-year-old male with a history of hypertension and hyperlipidemia who presents with symptoms consistent with possible rheumatoid arthritis. Symptoms began approximately 3 months ago with morning stiffness lasting more than 1 hour and symmetric joint pain affecting the wrists, hands, and knees. The patient denies any recent trauma or infection that might have triggered these symptoms.", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Past Medical History
    content.append(Paragraph("PAST MEDICAL HISTORY", heading_style))
    content.append(Paragraph("• Hypertension (diagnosed 5 years ago)<br/>• Hyperlipidemia (diagnosed 3 years ago)<br/>• Type 2 Diabetes Mellitus (diagnosed 2 years ago)<br/>• Obstructive Sleep Apnea (diagnosed 1 year ago)<br/>• History of Coronary Artery Disease (diagnosed 1 year ago)", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Medications
    content.append(Paragraph("CURRENT MEDICATIONS", heading_style))
    content.append(Paragraph("• Lisinopril 10mg daily for hypertension<br/>• Atorvastatin 20mg daily for hyperlipidemia<br/>• Metformin 500mg twice daily for diabetes<br/>• Aspirin 81mg daily for cardiovascular protection<br/>• CPAP therapy for sleep apnea", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Family History
    content.append(Paragraph("FAMILY HISTORY", heading_style))
    content.append(Paragraph("• Father: Deceased at age 65 from myocardial infarction, history of hypertension and diabetes<br/>• Mother: Alive, age 70, with rheumatoid arthritis and osteoporosis<br/>• Sister: Alive, age 42, with systemic lupus erythematosus<br/>• Brother: Alive, age 38, with psoriasis", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Social History
    content.append(Paragraph("SOCIAL HISTORY", heading_style))
    content.append(Paragraph("• Occupation: Software engineer<br/>• Tobacco: Former smoker, quit 10 years ago, 20 pack-years<br/>• Alcohol: Occasional use, 1-2 drinks per week<br/>• Exercise: Sedentary lifestyle due to recent symptoms", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Physical Examination
    content.append(Paragraph("PHYSICAL EXAMINATION", heading_style))
    content.append(Paragraph("Vital Signs:<br/>• Temperature: 99.8°F<br/>• Blood Pressure: 138/82 mmHg<br/>• Heart Rate: 82 bpm<br/>• Respiratory Rate: 16 breaths/min<br/>• Weight: 185 lbs (decreased from 195 lbs 3 months ago)", normal_style))
    content.append(Spacer(1, 0.1*inch))
    content.append(Paragraph("General: Well-appearing male in no acute distress<br/>HEENT: Normal<br/>Cardiovascular: Regular rate and rhythm, no murmurs<br/>Respiratory: Clear to auscultation bilaterally<br/>Abdomen: Soft, non-tender, non-distended<br/>Musculoskeletal: Symmetric swelling and tenderness of MCP and PIP joints of both hands, wrists, and knees. Morning stiffness noted.<br/>Skin: No rash noted<br/>Neurological: Intact", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Laboratory Results
    content.append(Paragraph("LABORATORY RESULTS", heading_style))
    
    lab_data = [
        ["Test", "Result", "Reference Range", "Units"],
        ["WBC", "8.2", "4.5-11.0", "K/uL"],
        ["Hgb", "13.5", "13.5-17.5", "g/dL"],
        ["Hct", "41", "41-50", "%"],
        ["Platelets", "245", "150-450", "K/uL"],
        ["ESR", "45", "0-20", "mm/hr"],
        ["CRP", "2.8", "<0.5", "mg/dL"],
        ["RF", "60", "<14", "IU/mL"],
        ["Anti-CCP", "Positive", "Negative", ""],
        ["ANA", "1:160", "<1:40", ""],
        ["Creatinine", "1.1", "0.7-1.3", "mg/dL"],
        ["ALT", "28", "7-56", "U/L"],
        ["AST", "24", "10-40", "U/L"],
        ["HbA1c", "6.8", "4.0-5.6", "%"],
        ["LDL", "98", "<100", "mg/dL"],
        ["HDL", "42", ">40", "mg/dL"],
        ["Triglycerides", "150", "<150", "mg/dL"]
    ]
    
    lab_table = Table(lab_data, colWidths=[1.2*inch, 1*inch, 1.5*inch, 0.8*inch])
    lab_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    content.append(lab_table)
    content.append(Spacer(1, 0.2*inch))
    
    # Assessment
    content.append(Paragraph("ASSESSMENT", heading_style))
    content.append(Paragraph("1. Rheumatoid Arthritis - New diagnosis based on clinical presentation, positive RF and anti-CCP antibodies, and elevated inflammatory markers.<br/>2. Hypertension - Well-controlled on current medication.<br/>3. Type 2 Diabetes Mellitus - Suboptimal control based on HbA1c of 6.8%.<br/>4. Hyperlipidemia - Well-controlled on statin therapy.<br/>5. Obstructive Sleep Apnea - Compliant with CPAP therapy.<br/>6. Coronary Artery Disease - Stable on current therapy.", normal_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Plan
    content.append(Paragraph("PLAN", heading_style))
    content.append(Paragraph("1. Rheumatoid Arthritis:<br/>   - Start Methotrexate 15mg weekly with folic acid 1mg daily<br/>   - Prednisone 10mg daily for 2 weeks, then taper<br/>   - Refer to Rheumatology for specialized care<br/>   - Physical therapy referral for joint protection and exercise program<br/><br/>2. Diabetes:<br/>   - Increase Metformin to 1000mg twice daily<br/>   - Continue current diet and exercise recommendations<br/>   - Follow up in 3 months for HbA1c check<br/><br/>3. Continue current medications for hypertension, hyperlipidemia, and cardiovascular protection.<br/><br/>4. Follow up in 2 weeks to assess response to RA treatment and adjust medications as needed.", normal_style))
    
    # Build the PDF
    doc.build(content)
    
    print(f"Sample medical report PDF created at: {os.path.abspath('sample_pdfs/sample_medical_report.pdf')}")

if __name__ == "__main__":
    create_sample_medical_report() 