import streamlit as st
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Optional: Specify path to tesseract executable (Windows only)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("📸 Food Label Nutrition Calculator")
st.markdown("Upload or take a picture of a food label, then enter how many grams you're consuming to calculate nutritional values.")

# Let user choose how to provide the image
upload_option = st.radio("How would you like to add the food label?", ["Take a picture", "Upload an image"])

if upload_option == "Take a picture":
    image = st.camera_input("Capture label image")
elif upload_option == "Upload an image":
    image = st.file_uploader("Choose a food label image", type=["jpg", "jpeg", "png"])
else:
    image = None

if image is not None:
    try:
        img = Image.open(image)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Extract text using OCR
        extracted_text = pytesseract.image_to_string(img)
        st.subheader("Extracted Text")
        st.text_area("OCR Output", extracted_text, height=200)

        # Simulate label data (normally you'd parse the text)
        st.markdown("---")
        st.subheader("Nutrition per 100g (example from label):")
        base_nutrition = {
            "Calories (kcal)": 250,
            "Carbohydrates (g)": 30,
            "Sugar (g)": 15,
            "Protein (g)": 10,
            "Fat (g)": 12
        }

        for key, val in base_nutrition.items():
            st.write(f"{key}: {val}")

        # Input: grams user plans to consume
        st.markdown("---")
        grams = st.number_input("Enter the amount of food in grams:", min_value=1.0, step=1.0)

        if grams:
            st.subheader(f"Nutrition for {grams}g:")
            for key, val in base_nutrition.items():
                scaled = grams / 100 * val
                st.write(f"{key}: {scaled:.2f}")
    except Exception as e:
        st.error("⚠️ Error processing the image. Please upload a valid JPG or PNG file.")
        st.stop()