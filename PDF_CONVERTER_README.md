# PDF Link Converter ⬇️📄

Convert URLs to PDFs with **hidden links** - URLs are completely invisible to users but remain fully clickable!

## Features

✨ **4 Conversion Methods:**
- 📝 **Text-Only** - Clickable text (URLs hidden)
- 🔗 **Icon-Only** - Clickable icons (URLs hidden)
- 📊 **Table Layout** - Professional table format (URLs hidden in cells)
- 🔘 **Buttons** - Clickable buttons (URLs hidden)

✨ **Security:**
- URLs completely invisible to end users
- Links remain fully functional
- No URL exposed in PDF metadata
- Perfect for sharing sensitive documents

✨ **Features:**
- Batch convert multiple links
- Web interface & Python API
- Fast PDF generation
- Descriptions for each link
- Download directly after creation

## Installation

```bash
# Install dependencies
pip install -r requirements-converter.txt
```

## Usage

### Web Interface (Recommended)

```bash
python pdf_converter/app.py
```

Open: **http://localhost:5002**

### Command Line

```python
from pdf_converter.link_converter import PDFLinkConverter

# Create converter
converter = PDFLinkConverter('my_links.pdf')

# Add links
converter.add_links_batch([
    {
        'title': 'Invoice Document',
        'url': 'http://gbsrv1092:8001/DAS/jbi/ServiceBus/Oracle/GetContentServerFile/?itesoftId=TRA20260716_0002_77879',
        'description': 'Business invoice'
    },
    {
        'title': 'Financial Report',
        'url': 'http://example.com/reports/Q1_2026.pdf',
        'description': 'Q1 2026 summary'
    }
])

# Generate PDF using different methods
converter.create_pdf_method1_text_only()      # Text method
converter.create_pdf_method2_icon_only()      # Icon method
converter.create_pdf_method3_table_hidden()   # Table method
converter.create_pdf_method4_buttons()        # Button method
```

## API Reference

### Convert Links to PDF

**Request:**
```bash
curl -X POST http://localhost:5002/api/convert \
  -H "Content-Type: application/json" \
  -d '{
    "links": [
      {"title": "Document 1", "url": "http://...", "description": "..."},
      {"title": "Document 2", "url": "http://...", "description": "..."}
    ],
    "method": "text"
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "PDF created successfully using text method",
  "file_path": "/tmp/hidden_links_20250115_143045_text.pdf",
  "download_url": "/api/download/hidden_links_20250115_143045_text.pdf"
}
```

## Examples

### Example 1: Business Documents

```python
converter = PDFLinkConverter('business_docs.pdf')
converter.add_links_batch([
    {'title': 'Invoice March', 'url': 'http://company.com/invoices/march.pdf'},
    {'title': 'Contract 2026', 'url': 'http://company.com/contracts/2026.pdf'},
    {'title': 'Report Q1', 'url': 'http://company.com/reports/Q1.pdf'},
])
converter.create_pdf_method1_text_only()  # Text-only, URLs hidden
```

### Example 2: Server Files with Long URLs

```python
converter = PDFLinkConverter('server_links.pdf')
converter.add_links_batch([
    {
        'title': 'MARMEDSA Invoice',
        'url': 'http://gbsrv1092:8001/DAS/jbi/ServiceBus/Oracle/GetContentServerFile/?itesoftId=TRA20260716_0002_77879&BusinessGroup=DEFAULT',
        'description': 'Shipping invoice'
    }
])
converter.create_pdf_method4_buttons()  # Button method, URL not visible
```

## Conversion Methods Explained

### 📝 Method 1: Text-Only
- Display: Clickable text like "1. Document Title"
- URL: Completely hidden
- Best for: Simple document lists
- File: `hidden_links.pdf`

### 🔗 Method 2: Icon-Only
- Display: Clickable icons/emojis (🔗)
- URL: Completely hidden
- Best for: Minimalist design
- File: `hidden_links_icon.pdf`

### 📊 Method 3: Table Layout
- Display: Professional table with columns
- URL: Hidden in table cells
- Best for: Formal documents
- File: `hidden_links_table.pdf`

### 🔘 Method 4: Buttons
- Display: Clickable colored buttons
- URL: Completely hidden
- Best for: User-friendly interface
- File: `hidden_links_buttons.pdf`

## Security Benefits

✅ **Hide Sensitive URLs** - Internal server paths not visible  
✅ **Prevent URL Sharing** - Users can't copy the actual URL  
✅ **Professional Look** - Clean, branded appearance  
✅ **Secure Distribution** - Perfect for confidential documents  
✅ **No Metadata Exposure** - URLs not in PDF metadata  

## Use Cases

🏢 **Enterprise Documents**
- Internal file sharing
- Confidential reports
- Employee access documents

📄 **Document Management**
- Long Oracle/SAP URLs
- Server file listings
- Centralized repositories

🔐 **Sensitive Information**
- Customer data links
- Financial reports
- Legal documents

## Performance

- ⚡ Instant PDF generation
- 📊 Handles 100+ links
- 💾 Lightweight PDFs (~50KB per 10 links)
- 🔄 Batch processing supported

## Troubleshooting

### "Invalid URL format"
- Ensure URL starts with `http://` or `https://`
- Check for typos in the URL

### "PDF not opening"
- Check browser's PDF viewer
- Try a different PDF reader
- Ensure URL is still accessible

### "Links not clickable"
- Check PDF reader supports links
- Try opening in different application
- Verify URL is valid

## Deployment

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements-converter.txt .
RUN pip install -r requirements-converter.txt
COPY . .
EXPOSE 5002
CMD ["python", "pdf_converter/app.py"]
```

Run:
```bash
docker build -t pdf-converter .
docker run -p 5002:5002 pdf-converter
```

## License

MIT License

## Author

Created by GABIDAT

---

**Made with 📄 and 🔒**
