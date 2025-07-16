# 🧠 Content-Based News Recommendation System

A machine learning-based content recommender system that suggests relevant articles to users based on their interaction history and the content of the articles (titles and body text). This project uses **TF-IDF vectorization**, **cosine similarity**, and **user profiles** to generate personalized article recommendations.

---

## 🚀 Live Demo
> [🔗 Click here to try the app!](https://your-render-link.onrender.com)  
*Replace the link after deployment on Render.*

---

## 📌 Features

- Personalized content recommendations using **content-based filtering**
- Text vectorization using **TF-IDF**
- Preprocessing and cleaning of article text
- **User profiles** are generated from past behavior
- Model evaluation with **Recall@5** and **Recall@10**
- Trained model is saved with **Pickle** for fast inference

---

## 🧾 Dataset Used

This project uses the dataset from the [CI&T News Recommender Challenge](https://www.kaggle.com/c/news-recommendation-challenge):

- `shared_articles.csv`: Metadata about articles.
- `users_interactions.csv`: Logs of user behavior like `VIEW`, `LIKE`, `COMMENT`, etc.

---

## 🛠️ Tech Stack

- Python (Pandas, NumPy, Scikit-learn, NLTK)
- TF-IDF Vectorization
- Cosine Similarity
- Pickle for model saving
- Jupyter / Google Colab for development
- [Render](https://render.com) for deployment

---

## 🧮 How It Works

1. **Preprocessing**:
   - Clean article titles and text.
   - Map user interaction types to numeric strengths.
   - Filter users with at least 5 interactions.

2. **Feature Extraction**:
   - Vectorize article content using `TfidfVectorizer` with stopwords in English and Portuguese.
   - Create a sparse TF-IDF matrix.

3. **User Profiles**:
   - For each user, build a profile by weighting article vectors they've interacted with.

4. **Recommendations**:
   - For each user, compute cosine similarity between their profile and all articles.
   - Recommend the top-N articles they haven’t seen yet.

5. **Evaluation**:
   - Use test data to compute `Recall@5` and `Recall@10`.

---

## 📂 Project Structure
## 💻 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/recommendation-system.git](https://github.com/MahmoudAttia111/ML-Recommendation-System)
cd recommendation-system

## Install dependencies
 - pip install -r requirements.txt
## Download NLTK stopwords
python
Copy code
import nltk
nltk.download('stopwords')

### Run the notebook
bash
Copy code
recommend system me.ipynb



