# Urdu OCR Project | Code Saviours SI-26 | Sheeza Riaz

## Project Overview

This repository contains my work for the Code Saviours ML/AI Internship (SI-26). The project focuses on building an Urdu Optical Character Recognition (OCR) pipeline by collecting, organizing, preprocessing, and evaluating Urdu text images using Python, OpenCV, and Tesseract OCR.

---

# Week 1

## Research Summary

### What is OCR?

Optical Character Recognition (OCR) is a technology that converts text from images or scanned documents into machine-readable text. It enables computers to recognize printed or handwritten characters so they can be searched, edited, and analyzed digitally.

### Why is Urdu OCR harder than English OCR?

Urdu OCR is more challenging because Urdu is a cursive language with connected characters, different character shapes, and complex ligatures. Variations in fonts, writing styles, and image quality make accurate recognition more difficult than English OCR.

### Real-World Applications

- Digitizing Urdu books, newspapers, and historical documents.
- Extracting text from Urdu signboards, forms, and government records.

## Week 1 Tasks Completed

- Created GitHub repository
- Set up Google Colab
- Connected GitHub with Colab
- Collected and organized 100 Urdu text images
- Created folder structure
- Generated labels.csv file

---

# Week 2

## Image Preprocessing

- Converted images to grayscale
- Resized images to a standard size (512 × 128)
- Removed image noise
- Applied binary thresholding
- Saved processed images

## OCR Evaluation

- Installed Tesseract OCR with Urdu language support
- Tested OCR on processed Urdu images
- Compared OCR results with actual labels
- Performed gap analysis

# Why We Need a Better Model

This project evaluated the performance of Tesseract OCR on an Urdu OCR dataset after applying image preprocessing techniques.

## Observations

- Some Urdu images produced no OCR output.
- Several Urdu characters and words were incorrectly recognized.
- OCR performance varied depending on image quality and text style.
- Connected Urdu characters were difficult for Tesseract to recognize accurately.

## Conclusion

Tesseract fails on Urdu because Urdu is a cursive script with connected characters, varying writing styles, and complex ligatures. The baseline Tesseract OCR model struggles to accurately recognize these features, often producing missing words, incorrect characters, or empty outputs. This demonstrates the need for a better OCR model specifically trained for Urdu text.
# Week 3 – Dataset Preparation for Urdu OCR

## Objective
Prepare the Urdu OCR dataset for fine-tuning the TrOCR model.

## Work Completed

- Collected and organized 200+ Urdu text images.
- Updated `labels.csv` with image paths and corresponding Urdu text.
- Split the dataset into:
  - Training Set
  - Validation Set
  - Test Set
- Created a custom `UrduOCRDataset` class using PyTorch.
- Successfully loaded all images using the Hugging Face TrOCR processor.
- Verified that the dataset loads correctly without errors.
- Dataset is ready for TrOCR fine-tuning.

## Dataset Statistics

| Split | Images |
|--------|--------|
| Train | 160 |
| Validation | 20 |
| Test | 20 |
| Total | 200 |

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- TrOCR
- Pandas
- PIL
- Google Colab

## Status

✅ Dataset prepared successfully.

✅ Dataset loads correctly.

✅ Ready for model training.
## Week 4 — TrOCR Model Training & Evaluation

### Objective
Fine-tune the pretrained TrOCR model on the Urdu OCR dataset, evaluate its performance on unseen test images, and save the trained model for further use.

### Work Completed

- Loaded the pretrained `microsoft/trocr-base-printed` TrOCR model.
- Configured the model for Urdu OCR generation.
- Used GPU acceleration through Google Colab.
- Prepared training and testing DataLoaders.
- Configured the AdamW optimizer with a learning rate of `5e-5`.
- Fine-tuned the TrOCR model on the Urdu OCR training dataset.
- Monitored training loss across multiple epochs.
- Tested the trained model on unseen test images.
- Compared predicted text with the ground-truth text.
- Evaluated the model using exact text matching accuracy.
- Saved the trained model and processor to Google Drive.

### Training Results

The training loss decreased during training, showing that the model was learning from the Urdu OCR training data.

**Training Loss:** 5.7914 → 3.0700

### Model Evaluation

The trained model was evaluated on the test dataset using exact text matching between the predicted and ground-truth text.

**Model Accuracy:** 0.00%

The current accuracy indicates that the model did not produce an exact match for the evaluated test samples. The prediction results will be further analyzed and improved in the next stage of the project.

### Week 4 Deliverables

- TrOCR training notebook
- Training loop and loss monitoring
- Test-set evaluation code
- Model predictions and ground-truth comparison
- Trained model saved to Google Drive
- Training output showing decreasing loss

### Technologies Used

- Python
- Google Colab
- PyTorch
- Hugging Face Transformers
- TrOCR
- AdamW
- Google Drive
---

# Week 5

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
