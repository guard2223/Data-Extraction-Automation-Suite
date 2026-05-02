import re
import os

# DATA EXTRACTION SUITE - PDF & TEXT PARSER
# Specialized in extracting structured information from unstructured reports.

class DataExtractor:
    def __init__(self, source_directory):
        self.source_directory = source_directory
        # Professional Regex patterns for identifying accounts, emails, and IDs
        self.patterns = {
            "account": r"Account\s*#?\s*:?\s*(\d{8,12})",
            "email": r"[\w\.-]+@[\w\.-]+\.\w+",
            "amount": r"\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)"
        }

    def process_file(self, filename):
        """Simulates extraction logic from a document."""
        print(f"[*] Processing document: {filename}...")
        extracted_data = {}
        
        # In a real scenario, we would use libraries like PyPDF2 or pdfplumber
        # Here we demonstrate the parsing logic
        mock_content = "Customer Account: 9988776655 | Email: support@example.com | Total: $1,250.50"
        
        for key, pattern in self.patterns.items():
            match = re.search(pattern, mock_content)
            if match:
                extracted_data[key] = match.group(1) if key != "email" else match.group(0)
        
        return extracted_data

    def run_batch(self):
        print("[!] Starting Batch Extraction Process...")
        # Simulate processing multiple files
        results = []
        for i in range(1, 4):
            data = self.process_file(f"invoice_00{i}.pdf")
            results.append(data)
        
        print(f"[+] Extraction complete. Processed {len(results)} files.")
        return results

if __name__ == "__main__":
    extractor = DataExtractor(source_directory="./invoices")
    final_results = extractor.run_batch()
    for result in final_results:
        print(f"Found: {result}")
