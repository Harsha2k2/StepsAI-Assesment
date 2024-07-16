import PyPDF2

def extract_text_from_pdf(pdf_file):
    """
    Extract text content from a PDF file.
    
    Args:
    - pdf_file (str): Path to the PDF file.
    
    Returns:
    - str: Extracted text content from the PDF.
    """
    text = ''
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def clean_text(text):
    """
    Clean the text by removing unnecessary characters and normalizing it.
    
    Args:
    - text (str): Input text to be cleaned.
    
    Returns:
    - str: Cleaned text.
    """
    cleaned_text = ' '.join(text.split())  # Remove extra whitespaces
    cleaned_text = cleaned_text.lower()    # Convert to lowercase
    
    return cleaned_text

def save_text_to_file(text, file_path):
    """
    Save text content to a file.
    
    Args:
    - text (str): Text content to be saved.
    - file_path (str): File path where the text will be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

# Example usage:
if __name__ == "__main__":
    pdf_file_path = r'C:\Users\uhars\Downloads\PPL_2ND_EDITION_Navigation_Oxford_Aviati.pdf'
    extracted_text = extract_text_from_pdf(pdf_file_path)
    
    # Clean the extracted text
    cleaned_text = clean_text(extracted_text)
    
    # Save cleaned text to a file in the repository
    save_file_path = 'cleaned_text.txt'  # Adjust the file path as needed
    save_text_to_file(cleaned_text, save_file_path)
    
    # Print cleaned text (for verification)
    print("Cleaned Text:")
    print(cleaned_text)
