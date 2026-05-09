import streamlit as st
import base64
from PIL import Image

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Easton Brand | PGA Management",
    page_icon="⛳",
    layout="wide"
)

# -------------------------
# LOAD IMAGES
# -------------------------
mountain_img = Image.open("images/mountain.jpg")
kids_golf_img = Image.open("images/kids_golf.jpg")
family_img = Image.open("images/family.jpg")

# -------------------------
# BUILT-IN EB GOLF LOGO
# -------------------------
logo_svg = """
<svg width="240" height="240" viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">

  <rect width="240" height="240" rx="34" fill="#0B3D2E"/>

  <circle cx="120" cy="105" r="85" fill="none" stroke="#FFFFFF" stroke-width="6"/>

  <path d="M85 70 H130 
           Q155 70 155 95 
           Q155 115 130 120 
           Q150 125 150 145 
           Q150 165 125 165 
           H85 Z"
        fill="none"
        stroke="#FFFFFF"
        stroke-width="10"
        stroke-linecap="round"
        stroke-linejoin="round"/>

  <path d="M85 70 V165
           M85 70 H140
           M85 118 H130
           M85 165 H140"
        fill="none"
        stroke="#00C800"
        stroke-width="10"
        stroke-linecap="round"/>

  <path d="M175 55 V130" stroke="#FFFFFF" stroke-width="4"/>

  <path d="M175 55 L190 65 L175 75 Z" fill="#E63946"/>

  <circle cx="175" cy="145" r="5" fill="#000000" stroke="#FFFFFF" stroke-width="2"/>

  <text x="120" y="210" text-anchor="middle"
        font-size="16"
        font-family="Georgia, serif"
        fill="#FFFFFF"
        letter-spacing="1.5">
        EASTON BRAND
  </text>

</svg>
"""

logo_b64 = base64.b64encode(logo_svg.encode("utf-8")).decode("utf-8")

logo_html = f"""
<div style="display:flex; justify-content:center; margin-bottom:18px; margin-top:5px;">
    <img src="data:image/svg+xml;base64,{logo_b64}" width="210">
</div>
"""

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background-color: #F5F1E8;
    color: #1f1f1f;
}

.main .block-container {
    color: #1f1f1f !important;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

p, li, label, div, span, input, textarea {
    color: #1f1f1f !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif !important;
    color: #0B3D2E !important;
}

section[data-testid="stSidebar"] {
    background-color: #0B3D2E;
}

section[data-testid="stSidebar"] * {
    color: #F5F1E8 !important;
}

.hero-box {
    background: linear-gradient(135deg, #0B3D2E 0%, #14523f 100%);
    padding: 40px;
    border-radius: 22px;
    color: #F5F1E8 !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.12);
    margin-bottom: 25px;
}

.hero-box h1, .hero-box h2, .hero-box h3, .hero-box p {
    color: #F5F1E8 !important;
}

.info-card {
    background-color: #FFFFFF;
    color: #1f1f1f !important;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    margin-bottom: 22px;
    border-left: 7px solid #0B3D2E;
}

.small-card {
    background-color: #FFFFFF;
    color: #1f1f1f !important;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    margin-bottom: 18px;
    border-left: 7px solid #0B3D2E;
}

.job-card {
    background-color: #FFFFFF;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    margin-bottom: 18px;
    border-left: 6px solid #0B3D2E;
}

.resume-card {
    background-color: #FFFFFF;
    color: #1f1f1f !important;
    padding: 26px;
    border-radius: 20px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.resume-top {
    background: linear-gradient(135deg, #0B3D2E 0%, #14523f 100%);
    color: #F5F1E8 !important;
    padding: 30px;
    border-radius: 22px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.12);
    margin-bottom: 20px;
}

.resume-top h2, .resume-top h3, .resume-top p {
    color: #F5F1E8 !important;
}

.contact-box {
    background-color: #FFFFFF;
    color: #1f1f1f !important;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
}

.badge {
    display: inline-block;
    padding: 8px 14px;
    margin: 6px 8px 6px 0;
    border-radius: 999px;
    background-color: #E4E0D7;
    color: #0B3D2E !important;
    font-weight: 600;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.markdown("## Navigation")
page = st.sidebar.radio("", ["Home", "About Me", "Portfolio", "Resume", "Contact"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Easton Brand")
st.sidebar.markdown("PGA Golf Management Student")
st.sidebar.markdown("University of Nebraska–Lincoln")

# -------------------------
# HOME
# -------------------------
if page == "Home":

    st.markdown(logo_html, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-box">
        <h1>Easton Brand</h1>
        <h3>PGA Golf Management Student | Golf Instructor | Future Club Professional</h3>
        <p>
            Building meaningful connections through golf, service, leadership, and a passion for helping others improve their game.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.image(mountain_img, use_container_width=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>Unique Value Proposition</h3>
            <p>
                I bring a hardworking attitude, a personable presence, and the ability to connect with people from all backgrounds.
                My experience in golf operations, instruction, hospitality, and leadership allows me to create positive experiences.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>Core Strengths</h3>
            <div class="badge">Hardworking</div>
            <div class="badge">Reliable</div>
            <div class="badge">Leadership</div>
            <div class="badge">Golf Instruction</div>
            <div class="badge">Hospitality</div>
            <div class="badge">Communication</div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# ABOUT ME
# -------------------------
elif page == "About Me":

    st.markdown(logo_html, unsafe_allow_html=True)

    st.header("About Me")

    st.markdown("""
    <div class="info-card">
        My name is Easton, and I am a 21-year-old from Cairo, Nebraska.
        I am currently part of the PGA Golf Management program at the University of Nebraska–Lincoln.
        Golf has always been a major part of my life and I have developed a strong passion for teaching
        the golf swing and helping people enjoy the game.
    </div>
    """, unsafe_allow_html=True)

    st.image(family_img, caption="Family & Husker Football", use_container_width=True)

    st.markdown("""
    <div class="small-card">
        <h3>Personal Values</h3>
        Hard work, reliability, professionalism, and creating genuine connections.
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# PORTFOLIO
# -------------------------
elif page == "Portfolio":

    st.markdown(logo_html, unsafe_allow_html=True)

    st.header("Portfolio & Experience")

    st.markdown("""
    <div class="info-card">
        <h3>Youth Golf Leadership</h3>
        <p>
            One of the most meaningful parts of my experience has been helping run youth golf programming.
            I enjoy helping younger golfers build confidence and enjoy the game.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.image(kids_golf_img, caption="Youth Golf Leadership Experience", use_container_width=True)

    st.markdown("""
    <div class="job-card">
        <h3>Dick’s Sporting Goods – Golf Associate</h3>
        <p>Worked directly with customers and provided golf equipment recommendations.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# RESUME
# -------------------------
elif page == "Resume":

    st.markdown(logo_html, unsafe_allow_html=True)

    st.header("Resume")

    st.markdown("""
    <div class="resume-top">
        <h2>Easton Brand</h2>
        <p>PGA Golf Management Student</p>
        <p>easton.brand3214@gmail.com | (308) 379-8091</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="resume-card">
        <h3>Professional Summary</h3>
        <p>
            Proactive student with strong communication and leadership skills.
            Passionate about golf instruction, club operations, and customer service.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# CONTACT
# -------------------------
elif page == "Contact":

    st.markdown(logo_html, unsafe_allow_html=True)

    st.header("Contact")

    st.markdown("""
    <div class="contact-box">
        <h3>Get In Touch</h3>
        <p><strong>Email:</strong> easton.brand3214@gmail.com</p>
        <p><strong>Phone:</strong> (308) 379-8091</p>
        <p><strong>Location:</strong> Lincoln, Nebraska</p>
    </div>
    """, unsafe_allow_html=True)
