from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("Loading AI model... Please wait.")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

image_path = input("Enter image path: ")

image = Image.open(image_path).convert("RGB")

inputs = processor(images=image, return_tensors="pt")

output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)

print("\nGenerated Caption:")
print(caption)