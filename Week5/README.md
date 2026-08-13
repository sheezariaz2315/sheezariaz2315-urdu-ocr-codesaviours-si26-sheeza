# Urdu OCR — Code Saviours SI-26

A fine-tuned TrOCR-based Optical Character Recognition (OCR) system for extracting Urdu text from images.

## 1. Project Overview

This project focuses on Optical Character Recognition (OCR) for Urdu text. The model takes an image containing Urdu text as input and generates the corresponding text as output.

The project was developed as part of the Code Saviours ML/AI Internship — Batch SI-26.

## 2. Problem Statement

Extracting Urdu text from images is challenging because Urdu contains connected characters, different writing styles, and variations in fonts and image quality.

This project aims to provide an OCR solution that can extract Urdu text from images. It can be useful for digitizing Urdu books, newspapers, documents, signboards, and other printed Urdu content.

## 3. How It Works

The project uses Microsoft's TrOCR (Transformer-based Optical Character Recognition) model.

The pretrained TrOCR model was fine-tuned on an Urdu OCR dataset to recognize Urdu text from images.

The workflow is:

1. An Urdu image is uploaded.
2. The image is processed using the TrOCR processor.
3. The trained TrOCR model analyzes the image.
4. The model generates the predicted text.
5. The extracted text is displayed through a Streamlit web application.

The dataset was divided into training and testing data. The training data was used to fine-tune the model, while the test data was used to evaluate its performance.

## 4. Live Demo

The trained OCR model was integrated into a Streamlit web application.

**Live Demo:**  
The application was tested using a temporary Cloudflare Tunnel through Google Colab.

> Note: The Cloudflare Tunnel link is temporary and is only available while the Google Colab session and tunnel are running.

## 5. How to Run Locally

### Step 1 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME

````
### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Run the Streamlit Application

```bash
streamlit run app.py
```

### Step 4 — Use the Application

Open the Streamlit URL in your browser.

Upload an Urdu image and click **Extract Urdu Text** to generate the OCR prediction.

## 6. Dataset Details

The project uses a custom Urdu OCR dataset containing images from different categories.

The dataset includes categories such as:

* Books
* Newspapers
* Signboards
* Other Urdu text images

The images contain variations in fonts, backgrounds, text sizes, and image conditions.

The dataset was organized using image-label pairs, where each image was associated with its corresponding Urdu text label.

## 7. Results

The model was fine-tuned and evaluated during Week 4.

**My model accuracy is 0%.**


The trained model was integrated into a Streamlit web application and tested with Urdu images.

The application successfully accepts an Urdu image and generates an OCR prediction.

Some predictions may contain errors because Urdu OCR is challenging and the dataset contains variations in image quality, fonts, and text styles. Further improvement can be achieved through a larger dataset, better preprocessing, and additional fine-tuning.

## 8. Project Files

* `Week5.ipynb` — Week 5 implementation notebook
* `app.py` — Streamlit OCR application
* `requirements.txt` — Required Python dependencies
* `README.md` — Project documentation

## 9. Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* TrOCR
* Streamlit
* Pillow
* Google Colab
* Google Drive
* GitHub

## 10. Credit

**Code Saviours — SI-26**

Developed as part of the Code Saviours ML/AI Internship.

```

**Bas copy → GitHub `Week5/README.md` → paste → Commit changes.**

Sirf `X%` aur `X to X` ko baad mein Week 4 ki **exact accuracy aur training-loss values** se replace karna hai. 
```
