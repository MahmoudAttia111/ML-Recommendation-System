import streamlit as st
import requests
import pandas as pd
from io import StringIO

API_URL = "https://ml-recommendation-system-production.up.railway.app/recommend/"
ARTICLES_FILE = "shared_articles.csv"

st.set_page_config(page_title="Content-Based Recommender", layout="centered")
st.title("🔍 Content-Based Recommendation System")

user_id = st.text_input("ادخل User ID:")

if st.button("اعرض التوصيات"):
    if user_id:
        try:
            # طلب البيانات من API
            response = requests.get(API_URL + user_id)
            if response.status_code == 200:
                # تحويل كل سطر JSON إلى DataFrame
                data = response.text.strip().splitlines()
                df = pd.read_json(StringIO("\n".join(data)), lines=True)

                # التأكد من الأعمدة
                if "contentId" not in df.columns or "recStrength" not in df.columns:
                    st.error("❌ لم يتم العثور على عمودي 'contentId' و 'recStrength' في البيانات.")
                else:
                    # تحميل بيانات المقالات
                    articles_df = pd.read_csv(ARTICLES_FILE)

                    if 'contentId' not in articles_df.columns:
                        st.error("❌ ملف المقالات لا يحتوي على العمود 'contentId'.")
                    else:
                        # دمج التوصيات مع المقالات
                        merged = df.merge(articles_df, on='contentId')

                        # عرض النتائج المطلوبة فقط
                        st.success("✅ تم عرض التوصيات:")
                        st.dataframe(merged[['contentId', 'recStrength', 'title']].reset_index(drop=True))
            else:
                st.error("⚠️ لم يتم العثور على توصيات لهذا المستخدم.")
        except Exception as e:
            st.error(f"❌ حصل خطأ: {e}")
    else:
        st.warning("من فضلك ادخل user ID.")
