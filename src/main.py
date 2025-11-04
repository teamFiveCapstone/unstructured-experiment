from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.basic import chunk_elements
from unstructured.chunking.title import chunk_by_title

# !!!!!!! EXPERIMENT 1:
elements = partition(filename="../files/wwf_tigers_e_1.pdf")
with open("../files/auto-partition-output.txt", "w") as f:
    f.write("\n\n".join([str(el) for el in elements]))

# !!!!!! EXPERIMENT 2:
import os
os.makedirs("../files/images/", exist_ok=True)

# I am using extract_image_block_to_payload=False (instead I write write the images
# to the images folder)
elementsTwo = partition_pdf(filename="../files/wwf_tigers_e_1.pdf",
                            strategy="hi_res", extract_images_in_pdf=True,
                            extract_image_block_types=["Image", "Table"],
                            extract_image_block_to_payload=False,
                            extract_image_block_output_dir="../files/images/"
                            )
with open("../files/pdf-partition-output.txt", "w") as f:
    f.write("\n\n".join([str(el) for el in elements]))

# Write text content to file
with open("../files/pdf-partition-output.txt", "w") as f:
    f.write("\n\n".join([str(el) for el in elementsTwo]))

# Check how many images were saved to filesystem
import glob
saved_images = glob.glob("../files/images/*")
print(f"Total images saved to filesystem: {len(saved_images)}")
for img in saved_images:
    print(f"  {img}")

# !!!!!!!! EXPERIMENT 3: Basic Chunking
print("\n=== BASIC CHUNKING EXPERIMENT ===")
basic_chunks = chunk_elements(elements, max_characters=1000, new_after_n_chars=800)
print(f"Basic chunking created {len(basic_chunks)} chunks from {len(elements)} elements")

with open("../files/basic-chunking-output.txt", "w") as f:
    for i, chunk in enumerate(basic_chunks):
        f.write(f"=== BASIC CHUNK {i+1} ===\n")
        f.write(str(chunk))
        f.write("\n\n")

# !!!!!!!! EXPERIMENT 4: Title-based Chunking
print("\n=== TITLE-BASED CHUNKING EXPERIMENT ===")
title_chunks = chunk_by_title(elements)
print(f"Title-based chunking created {len(title_chunks)} chunks from {len(elements)} elements")

with open("../files/title-chunking-output.txt", "w") as f:
    for i, chunk in enumerate(title_chunks):
        f.write(f"=== TITLE CHUNK {i+1} ===\n")
        f.write(str(chunk))
        f.write("\n\n")
