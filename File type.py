import pyautogui
import time
import random
from docx import Document

# Function to read text from a docx file
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Path to the docx file
docx_file_path = 'assignment.docx'

# Read the text from the docx file
text = read_docx(docx_file_path)

time.sleep(5)

 # typing_speed = 0.003  # Set the typing speed to 0.3 seconds per character for 40 words per minute

# Type each character in the string
for char in text:
    pyautogui.press(char)
    typing_speed = random.uniform(0.0000001, 0.0000003)
    time.sleep(typing_speed)

print("Done")