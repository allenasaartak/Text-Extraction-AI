Multilingual Text Extractor (Powered by Gemini 1.5 Pro)

A smart AI-driven Python tool designed to extract original-language text from images, using the power of Google's Gemini 1.5 Pro API.
Whether you're building a translation dataset, prepping content for machine learning, or simply organizing raw comic text — this tool handles it intelligently, slice by slice.

What It Does:
 
1. Image Slicing for Better Accuracy
The script automatically divides each vertical comic image into three logical parts — Top, Middle, and Bottom — to avoid cluttered OCR and improve extraction precision. This layout-aware slicing mimics the natural flow of most vertical comics and webtoons.

2. AI-Powered Text Extraction
Each sliced section is sent to the Gemini 1.5 Pro model along with a simple instruction: “Extract text from this image without translating. Keep the original language intact.”
Gemini intelligently reads the slice, identifies text in any language and returns it in its raw - untranslated form — perfect for later analysis or training a custom translation pipeline.

3. Structured Output Saving
The extracted text from each image part is neatly saved to a .txt file, labeled clearly by its panel position:

4. Multilingual & Flexible
While originally tailored for Korean manhwa, this tool works flawlessly with any language and any image format — Chinese, Japanese, French, Hindi, you name it.

 Built With: 

PIL (Python Imaging Library) 
Gemini 1.5 Pro – advanced OCR and content interpretation

Use Cases:

Preparing text datasets for machine translation
Extracting raw dialogue from manga, manhwa, or webtoons
Automating comic-to-text pipelines
Archiving non-translated content for fan scanlation teams
Performing language model training on comic-style conversation
