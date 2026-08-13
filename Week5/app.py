
import streamlit as st
import torch
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

st.set_page_config(
    page_title="Urdu OCR — Code Saviours SI-26",
    page_icon="📖"
)

st.title("Urdu OCR — Code Saviours SI-26")
st.write("Upload an image containing Urdu text and get the extracted text.")

model_path = "/content/drive/MyDrive/Urdu-OCR/trocr-urdu-model"

@st.cache_resource
def load_model():
    processor = TrOCRProcessor.from_pretrained(model_path)
    model = VisionEncoderDecoderModel.from_pretrained(model_path)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return processor, model, device

processor, model, device = load_model()

uploaded_file = st.file_uploader(
    "Upload Urdu Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Extract Urdu Text"):

        pixel_values = processor(
            image,
            return_tensors="pt"
        ).pixel_values.to(device)

        with torch.no_grad():

            generated_ids = model.generate(
                pixel_values,
                max_new_tokens=64,
                num_beams=4
            )

        prediction = processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

        st.subheader("Extracted Urdu Text")
        st.text_area(
            "Result",
            prediction,
            height=120
        )
