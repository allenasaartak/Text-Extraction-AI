import google.generativeai as genai
import PIL.Image
import os

# Change it to your own API key
genai.configure(api_key="")


image_path = r"" # Specify the image path directly in the code

model = genai.GenerativeModel("gemini-1.5-pro")

def process_image(image_path):
    image = PIL.Image.open(image_path)
    width, height = image.size
    slice_height = height // 3
    image_parts = {
        "Top": image.crop((0, 0, width, slice_height)),
        "Middle": image.crop((0, slice_height, width, 2 * slice_height)),
        "Bottom": image.crop((0, 2 * slice_height, width, height))
    }
    image_name = os.path.splitext(image_path)[0]
    output_filename = f"{image_name}_korean_trans.txt"
    
    with open(output_filename, "w", encoding="utf-8") as f:
        for part_name, slice_img in image_parts.items():
            
            response = model.generate_content([
                "Extract text from this image without translating. Keep the original language intact.",
                slice_img
            ], stream=False)
            extracted_text = response.text if response else "No text detected"
            lines = extracted_text.split('\n')
            f.write(f"--- {part_name} Part of {os.path.basename(image_name)} ---\n")
            for line in lines:
                f.write(f'{line}\n')
            f.write("\n") 

    print(f"--> Text saved in: {output_filename}")

process_image(image_path)
