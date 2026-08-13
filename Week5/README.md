# Urdu OCR — Code Saviours SI-26

A fine-tuned TrOCR-based Optical Character Recognition (OCR) system for extracting text from Urdu images.

## 1. Project Overview

This project focuses on Optical Character Recognition (OCR) for Urdu text. The model takes an image containing Urdu text as input and generates the corresponding text as output.

The project was developed as part of the Code Saviours ML/AI Internship — Batch SI-26.

## 2. Problem Statement

Extracting Urdu text from images is challenging because Urdu contains connected characters, different writing styles, and variations in fonts and image quality.

This project aims to provide an OCR solution that can extract Urdu text from images. It can be useful for digitizing Urdu books, newspapers, documents, signboards, and other printed Urdu content.

## 3. How It Works

The project uses Microsoft's TrOCR (Transformer-based Optical Character Recognition) model.

The pretrained TrOCR model was fine-tuned on an Urdu OCR dataset so that it could learn to recognize Urdu text from images.

The workflow is:

1. An Urdu image is uploaded.
2. The image is processed using the TrOCR processor.
3. The trained TrOCR model analyzes the image.
4. The model generates the predicted text.
5. The extracted text is displayed to the user through a web interface.

The dataset was divided into training and testing data. The training data was used to fine-tune the model, while the test data was used to evaluate its performance.

## 4. Live Demo

The trained OCR model was integrated into a Streamlit web application.

**Live Demo:**  
Add the working public demo link here.

> Note: The current demo uses a temporary Cloudflare Tunnel link, so it may only remain available while the Colab session and tunnel are running.

## 5. How to Run Locally

### Step 1 — Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
