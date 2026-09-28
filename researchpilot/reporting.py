from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def markdown_report(report):
    return report["markdown"]

def pdf_report(report, sources):
    data = report["data"]
    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = [
        Paragraph(data["title"], styles["Title"]),
        Spacer(1, 12),
        Paragraph("Executive Summary", styles["Heading2"]),
        Paragraph(data["executive_summary"], styles["BodyText"]),
        Spacer(1, 10),
    ]

    sections = [
        ("Key Points", "key_points"),
        ("Important Findings", "important_findings"),
        ("Actionable Insights", "actionable_insights"),
        ("Limitations", "limitations"),
        ("References", "references"),
    ]

    for heading, key in sections:
        story.append(Paragraph(heading, styles["Heading2"]))
        for item in data.get(key, []):
            story.append(Paragraph("• " + item, styles["BodyText"]))
            story.append(Spacer(1, 4))

    story.append(Paragraph("Source Registry", styles["Heading2"]))

    for source in sources:
        story.append(
            Paragraph(
                f'[{source["id"]}] {source["title"]} — {source["url"]}',
                styles["BodyText"],
            )
        )

    document.build(story)
    return buffer.getvalue()
