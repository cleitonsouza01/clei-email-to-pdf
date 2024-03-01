import os
import sys

import extract_msg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def main(input_file_path):
    """Main function to convert date format in a CSV file."""
    print(f"Converting file: {input_file_path}")

    file_name, file_extension = os.path.splitext(input_file_path)
    output_file_path = f"{file_name}.pdf"

    # Extract the .msg file content
    with extract_msg.openMsg(input_file_path) as msg:
        subject = msg.subject
        body = msg.body if msg.body else msg.htmlBody  # Use HTML body if available

    # Create a PDF file
    c = canvas.Canvas(output_file_path, pagesize=letter)
    width, height = letter
    c.drawString(72, height - 72, "Subject: " + subject)

    # Simple text wrapping for demonstration purposes
    text = c.beginText(72, height - 100)
    text.setFont("Times-Roman", 12)
    wrapped_text = "\n".join([body[i:i + 100] for i in range(0, len(body), 100)])
    text.textLines(wrapped_text)
    c.drawText(text)

    c.showPage()
    c.save()


if __name__ == "__main__":
    print("### clei-Email-to-PDF - version 0.01 ###")
    print("Author: Cleiton Souza")
    print("Script to convert email file (.MSG) to a Adobe Acrobat PDF format.\n")
    if len(sys.argv) < 2:
        print("Usage: clei-email-to-pdf.exe <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        try:
            main(input_file_path)
            print("\nConversion complete successfully!")
        except FileNotFoundError:
            print(f"File not found: {input_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    input("\nPress Enter to exit...")
