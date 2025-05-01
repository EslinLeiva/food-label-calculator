import streamlit as st
import pytesseract
from PIL import Image, UnidentifiedImageError
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Optional: Specify path to tesseract executable (Windows only)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("📸 Food Label Nutrition Calculator")
st.markdown("Upload or take a picture of a food label, then enter how many grams you're consuming to calculate nutritional values.")

# Let user choose how to provide the image
upload_option = st.radio("How would you like to add the food label?", ["Take a picture", "Upload an image"])

image_data = None

if upload_option == "Take a picture":
    camera_image = st.camera_input("Capture label image")
    if camera_image:
        image_data = camera_image.getvalue()

elif upload_option == "Upload an image":
    uploaded_image = st.file_uploader("Choose a food label image")  # Removed type restriction
    if uploaded_image:
        image_data = uploaded_image.read()

if image_data is not None:
    try:
        img = Image.open(io.BytesIO(image_data))
        img.verify()  # verify that it's an image
        img = Image.open(io.BytesIO(image_data))  # reopen after verify
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
    except UnidentifiedImageError:
        st.error("⚠️ Unsupported or corrupted image file. Please try uploading a different JPG or PNG.")
        st.stop()
    except Exception as e:
        st.error(f"⚠️ Error processing the image: {e}")
        st.stop()
