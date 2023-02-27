# ---LIBRARIES--- #
import pathlib
from PIL import Image
import streamlit as st

# ---PATH SETTINGS--- #
current_dir = pathlib.Path(
    __file__).parent if "__file__" in locals() else pathlib.Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "subrata_mondal_resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"

# ---General Settings--- #
PAGE_TITLE = "Digital Resume | Subrata Mondal"
PAGE_ICON = ":wave:"
NAME = "Subrata Mondal"
DESCRIPTION = """Junior Data Scientist, assisting enterprises with data driven decision making"""
EMAIL = "subratasubha2@gmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/subratamondal1",
    "LinkedIn": "https://www.linkedin.com/in/subrata-mondal-331446188/",
    "Kaggle": "https://www.kaggle.com/subratasubha"

}

PROJECTS = {
    "🏆 Heart Attack Predictor": "https://subratamondal1-heart-attack-prediction-app-p4oz89.streamlit.app/",
    "🏆 Movie Recommendation System": "https://subratamondal1-movie-recommendation-system-app-jd8dve.streamlit.app/",
    "🏆 Laptop Price Predictor": "https://subratamondal1-laptop-price-predictor-app-sizmec.streamlit.app/"
}

# ---Set page configuration--- #
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ---Load CSS, Pdf, Profile pic--- #
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# ---Hero Section--- #
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=240, output_format="PNG")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name, mime="application/octet-stream")
    st.write("✉️", EMAIL)

# ---Social Media Links--- #
st.write("#")  # provides space
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---Experience and Qualifications--- #
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ☑️ One Year experience through participating in data science hackathons, creating projects, and not from work. 
    - ☑️ Strong hands on experience and knowledge in Python and SQL.
    - ☑️ Good understanding of statitical techniques and probability distributions.
    - ☑️ Strong hands on knowledge with Python's Machine Learning and Data Science libraries like numpy, pandas, scikit-learn, etc.
    - ☑️ Good understanding of Python's Data Visualization libraries like matplotlib, seaborn, etc.

    """
)

# ---Hard Skills--- #
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 🧑🏻‍💻 Programming: Python, SQL
    - 📊 Visualization: Matplotlib, Seaborn
    - ⚙️  Modeling: Linear, Decision Trees, Ensemble, Neighbors
    - 𝌏 Databases: PostgresSQL
    - ✊🏻 Worked With: Tableau, MS Excel
    """
)

# ---Hackathons--- #
st.write("#")
st.subheader("Hackathons")
st.write("---")


# ---Hackathon1--- #
st.write("#")
st.write("##### Green Energy Consumption")
st.caption("organized by **Analytics Vidhya**")
st.write("18-20 November 2022 - / Remote, India")
st.write(
    """
    - **‣** Created a Regression model to predict the consumption of green energy
    - **‣** Able to achieve RMSE score of 68.2 and got a leaderboard rank of 169/6388
    - **‣** Used python, numpy, pandas, matplotlib for loading, visualizing, preparing, exploring data and for modelling & evaluation used Scikit-learn library
    """
)

# ---Hackathon2--- #
st.write("#")
st.write("##### Customer Lifetime Value")
st.caption("organized by **Analytics Vidhya**")
st.write("18-20 January 2023 / Remote, India")
st.write(
    """
    - **‣** Created a model to predict the Customer Lifetime Value of the customers of an insurance company for the next 90 days using Linear Regression.
    - **‣** Able to achieve r2_score of 15.4 and got a leaderboard rank of 331/7416 Used python, numpy, pandas, matplotlib for loading, visualizing, preparing,
    - **‣** Used python, numpy, pandas, matplotlib for loading, visualizing, preparing, exploring data and for modelling & evaluation used Scikit-learn library

    """
)


# ---Projects--- #
st.write("#")
st.subheader("Projects")
st.write("---")

# ---project1--- #
st.write("#")
st.write(
    "##### 🫀 [Heart Attack Prediction](https://subratamondal1-heart-attack-prediction-app-p4oz89.streamlit.app/)")
st.caption("Supervised Learning - Classification")
st.write("College Project / Sep 2022 - Jan 2023 / Vadodara, Gujarat")
st.write(
    """
    - **‣** Created a Classification Model for Heart Attack prediction using Logistic Regression
    - **‣** Able to achieve an accuracy score of 80% and the project got selected for TechExpo
    - **‣** Used Streamlit for MLOps and hosted the Webapp in the cloud
    """
)


# ---project2--- #
st.write("#")
st.write("##### 🎬 [Movie Recommendation System](https://subratamondal1-movie-recommendation-system-app-jd8dve.streamlit.app/)")
st.caption("Unsupervised Learning")
st.write("College Project / Oct 2022 - Nov 2023 / Vadodara, Gujarat")
st.write(
    """
    - **‣** Created a Cosine Similarity model for recommending  similar movies
    - **‣** Integrated Imdb links with the recommended results for more movie details that redirects you to their movie websites
    - **‣** Used Streamlit for MLOps and hosted the Webapp in the cloud

    """
)

# ---All Projects--- #
st.write("#")
st.subheader("Project Lists")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
