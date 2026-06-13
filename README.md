# DecodeLabs-Internship  
AI Internship Projects and Assignments

---

# Project 2: Data Classification using KNN

## 📌 Project Description
This project is a supervised machine learning model that classifies Iris flowers into three species:
Setosa, Versicolor, and Virginica.

It uses features like:
- Sepal length  
- Sepal width  
- Petal length  
- Petal width  

The model uses the K-Nearest Neighbors (KNN) algorithm.

---

## 📊 Dataset Used
- Iris dataset from scikit-learn

---

## 🤖 Algorithm Used
- K-Nearest Neighbors (KNN)

---

## ⚙️ How to Run

### Step 1: Install dependencies
```bash
pip install scikit-learn
# Project 3: AI Recommendation System

## 📌 Description
This project is a content-based recommendation system that suggests job roles based on user skills.

## ⚙️ Technology Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## 🚀 How it works
1. User enters skills
2. Skills are converted into vectors using TF-IDF
3. Cosine similarity is calculated
4. Top 3 matching jobs are recommended

## 📊 Output Example
Cloud Architect  
DevOps Engineer  
Data Scientist  



# Project 4 - Text Recognition using OCR

## Objective

To extract text from an image using Optical Character Recognition (OCR).

## Tools and Libraries Used

* Python
* OpenCV
* Pytesseract
* Tesseract OCR Engine

## Project Description

This project demonstrates basic text recognition from images using a pre-trained OCR model. The input image is first preprocessed by converting it to grayscale. The Tesseract OCR engine is then used to identify and extract text from the image.

## Steps Performed

1. Load the image using OpenCV.
2. Convert the image to grayscale.
3. Apply basic preprocessing.
4. Extract text using Tesseract OCR.
5. Display the recognized text.

## Files

* project4.py : Main Python program
* sample.jpg : Input image containing text
* README.md : Project documentation

## Output

The program successfully detects and displays text present in the input image.

## Conclusion

A basic OCR system was implemented using Python and Tesseract OCR. The project demonstrates how pre-trained models can be used for text recognition tasks.
