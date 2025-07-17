# 🧠 Content-Based News Recommendation System

A machine learning-based content recommender system that suggests relevant articles to users based on their interaction history and the content of the articles (titles and body text). This project uses **TF-IDF vectorization**, **cosine similarity**, and **user profiles** to generate personalized article recommendations.

---

## 🚀 Live Demo

> 🌍 [🔗 Click here to try the app!](https://ml-recommendation-system-xnzjaorjb5rmdrqk7ivfx6.streamlit.app/)

> Just enter a User ID and get personalized article recommendations!

---

## 📌 Features

✅ Personalized recommendations using **content-based filtering**
✅ Article representation with **TF-IDF vectorization**
✅ User profiles generated from past behavior
✅ Uses **cosine similarity** to rank recommendations
✅ Model evaluation with **Recall\@5** and **Recall\@10**
✅ Web app powered by **Streamlit**

---

## 📟 Dataset Used

From the [(https://www.kaggle.com/datasets/gspmoreira/articles-sharing-reading-from-cit-deskdrop):

* `shared_articles.csv` – Article metadata (title, content, publication info)
* `users_interactions.csv` – User interactions like `VIEW`, `LIKE`, `COMMENT`

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy, Scikit-learn, NLTK)
* TF-IDF Vectorizer
* Cosine Similarity
* Pickle (for model saving)
* Streamlit (for web interface)
* Hosted on: [Streamlit Cloud](https://share.streamlit.io/)

---

## 🧮 How It Works

1. **Preprocessing**

   * Clean article text (titles + content)
   * Map interaction types (e.g., LIKE = 3, VIEW = 1, etc.)
   * Keep users with ≥ 5 interactions

2. **TF-IDF Vectorization**

   * Articles are vectorized using TF-IDF
   * English & Portuguese stopwords removed

3. **User Profiles**

   * Weighted average of article vectors based on interaction strength

4. **Recommendation Engine**

   * Cosine similarity used to match user profiles with unseen articles
   * Top-N articles are returned

5. **Evaluation**

   * Recall\@5 and Recall\@10 used to measure quality

---

## 🧪 Sample Evaluation Results

```json
{
  "modelName": "Content_Based",
  "recall@5": 0.275,
  "recall@10": 0.17
}
```

---

## 👤 Sample User IDs for Testing

Copy and paste any of the following IDs into the app:

```
3937943558206985686
1874422396201148365
5598537709124463353
-4165818767652094649
2416280733544962613
```

---

## 📂 Project Structure

```
ML-Recommendation-System/
│
├── recommend system me.ipynb        ← Notebook for building the model
├── app.py                           ← Streamlit web app
├── requirements.txt                 ← Project dependencies
├── shared_articles.csv              ← Articles dataset
├── users_interactions.csv           ← User interaction logs
├── models/                          ← Pickled model files
└── README.md                        ← You're here!
```

---

## 💻 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/MahmoudAttia111/ML-Recommendation-System.git
cd ML-Recommendation-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download NLTK stopwords

```python
import nltk
nltk.download('stopwords')
```

### 4. Run the notebook (to train the model)

```bash
jupyter notebook "recommend system me.ipynb"
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit

This project is deployed on **Streamlit Cloud**:
👉 [https://ml-recommendation-system-xnzjaorjb5rmdrqk7ivfx6.streamlit.app/](https://ml-recommendation-system-xnzjaorjb5rmdrqk7ivfx6.streamlit.app/)

To deploy your own version:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect GitHub repo & choose `app.py` as the main file
4. Add `shared_articles.csv` to the same repo
5. Done 🎉

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to improve.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Dataset: [CI\&T News Recommendation Challenge on Kaggle](https://www.kaggle.com/datasets/gspmoreira/articles-sharing-reading-from-cit-deskdrop)
* Inspired by many great recommender system tutorials and ML best practices.

---
 



