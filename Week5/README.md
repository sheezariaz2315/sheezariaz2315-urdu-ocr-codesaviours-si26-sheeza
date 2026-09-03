# Week 5 — Urdu OCR Web Application

A Gradio web application that extracts Urdu text from document images using a fine-tuned TrOCR model.

## Why This Matters

Urdu documents, newspapers, books, and other printed materials contain valuable information that is difficult to search and process when stored only as images. An Urdu OCR system can convert visual text into machine-readable text and support digitization and accessibility.

## Live Demo

Try the live Urdu OCR application:

[Open Urdu OCR Demo](PASTE_YOUR_HUGGINGFACE_SPACE_LINK_HERE)

## How It Works

The application uses a fine-tuned TrOCR model to recognize Urdu text from an uploaded image.

The image is processed using the TrOCR processor and passed to the trained model. The model generates the predicted Urdu text, which is displayed through a Gradio web interface.

The application was deployed on Hugging Face Spaces so that the Urdu OCR tool can be accessed through a public web link.

## What I Did

- Created a Gradio-based Urdu OCR web application.
- Connected the trained TrOCR model with the application.
- Added image upload functionality.
- Processed uploaded images using the TrOCR processor.
- Generated Urdu text predictions.
- Displayed the extracted text through the Gradio interface.
- Prepared the application for deployment on Hugging Face Spaces.

## Results

The Urdu OCR application was successfully developed and deployed as a public Hugging Face Space.

The application allows users to:

1. Upload an Urdu document image.
2. Process the image using the fine-tuned TrOCR model.
3. Generate predicted Urdu text.
4. View the extracted text in the application.

## Model

The application uses a fine-tuned TrOCR model based on:

`microsoft/trocr-base-printed`

## Files

- `app.py` — Gradio web application.
- `requirements.txt` — Python dependencies.
- `SI26_Week5_sheeza.ipynb` — Week 5 development notebook.

## How to Run Locally

Clone the repository:

```bash
git clone PASTE_YOUR_GITHUB_REPO_LINK_HERE
cd PASTE_YOUR_REPO_FOLDER_NAME_HERE
