import streamlit as st
import base64

st.set_page_config(
    page_title="Easton Brand | PGA Management",
    page_icon="⛳",
    layout="wide"
)

# -------------------------
# BUILT-IN EB GOLF LOGO (FIXED)
# -------------------------
logo_svg = """
<svg width="240" height="240" viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="240" height="240" rx="34" fill="#0B3D2E"/>
  <circle cx="120" cy="102" r="72" fill="none" stroke="#F5F1E8" stroke-width="6"/>
  <path d="M78 58 H130 Q150 58 150 76 Q150 91 132 96 Q148 100 148 116 Q148 138 122 138 H78 Z"
        fill="none" stroke="#F5F1E8" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M102 58 V138" fill="none" stroke="#F5F1E8" stroke-width="8" stroke-linecap="round"/>
  <path d="M102 58 H136" fill="none" stroke="#F5F1E8" stroke-width="8" stroke-linecap="round"/>
  <path d="M102 98 H130" fill="none" stroke="#F5F1E8" stroke-width="8" stroke-linecap="round"/>
  <path d="M102 138 H138" fill="none" stroke="#F5F1E8" stroke-width="8" stroke-linecap="round"/>
  <path d="M166 48 L166 124" fill="none" stroke="#F5F1E8" stroke-width="5" stroke-linecap="round"/>
  <path d="M166 48 L184 60 L166 70 Z" fill="#F5F1E8"/>
  <circle cx="166" cy="142" r="6" fill="#F5F1E8"/>
  <text x="120" y="198" text-anchor="middle" font-size="18" font-family="Georgia, serif" fill="#F5F1E8">EASTON BRAND</text>
</svg>
"""

logo_b64 = base64.b64encode(logo_svg.encode("utf-8")).decode("utf-8")
logo_html = f"""
<div style="display:flex; justify-content:center; margin-bottom: 18px; margin-top: 5px;">
    <img src="data:image/svg+xml;base64,{logo_b64}" width="210">
</div>
"""

# -------------------------
# CSS FIXES FOR LIGHT/DARK MODE
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main app area */
[data-testid="stAppViewContainer"] {
    background-color: #F5F1E8;
    color: #1f1f1f;
}

/* Main content block */
.main .block-container {
    color: #1f1f1f !important;
}

/* Force readable text everywhere */
p, li, label, div, span, input, textarea {
    color: #1f1f1f !important;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif !important;
    color: #0B3D2E !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0B3D2E;
}
section[data-testid="stSidebar"] * {
    color: #F5F1E8 !important;
}

/* Cards */
.hero-box {
    background: linear-gradient(135deg, #0B3D2E 0%, #14523f 100%);
    padding: 40px;
    border-radius: 20px;
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
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    border-left: 6px solid #0B3D2E;
}
.info-card p, .info-card li, .info-card strong, .info-card h3 {
    color: #1f1f1f !important;
}

.small-card {
    background-color: #FFFFFF;
    color: #1f1f1f !important;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
.small-card p, .small-card h3 {
    color: #1f1f1f !important;
}

.contact-box {
    background-color: #FFFFFF;
    color: #1f1f1f !important;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
}
.contact-box p, .contact-box h3, .contact-box strong {
    color: #1f1f1f !important;
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

/* Inputs */
.stTextInput input, .stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #1f1f1f !important;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background-color: #0B3D2E;
    color: #F5F1E8 !important;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
}
.stButton > button:hover {
    background-color: #14523f;
    color: #F5F1E8 !important;
}

/* Download button */
.stDownloadButton > button {
    background-color: #0B3D2E;
    color: #F5F1E8 !important;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
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

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>Unique Value Proposition</h3>
            <p>
                I bring a hardworking attitude, a personable presence, and the ability to connect with people from all backgrounds.
                My experience in golf operations, instruction, hospitality, and leadership allows me to create positive experiences
                for members, guests, and students while contributing to a strong team culture.
            </p>
            <p>
                Whether I am helping run a golf program, assisting with club operations, or teaching the game to players of different
                ages and skill levels, I aim to make every interaction professional, welcoming, and meaningful.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>Core Strengths</h3>
            <div class="badge">Hardworking</div>
            <div class="badge">Reliable</div>
            <div class="badge">Personable</div>
            <div class="badge">Leadership</div>
            <div class="badge">Golf Instruction</div>
            <div class="badge">Hospitality</div>
            <div class="badge">Teamwork</div>
            <div class="badge">Communication</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>What I Want to Be Known For</h3>
        <p>
            I want to be known as someone who works hard, connects well with others, and brings energy and professionalism to every club environment.
            My goal is to build a long-term career in the golf industry where I can teach the game, support club operations, and create experiences
            that leave a lasting impression on players and members.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# ABOUT
# -------------------------
elif page == "About Me":
    st.markdown(logo_html, unsafe_allow_html=True)
    st.header("About Me")

    st.markdown("""
    <div class="info-card">
        <p>
            My name is Easton, and I am a 21-year-old from Cairo, Nebraska. I attended high school at Centura Public Schools,
            where I graduated third in my class and earned all-state academic honors. After high school, I was accepted to the
            University of Nebraska–Lincoln, where I originally pursued architecture. While I enjoyed parts of that field, I realized
            it was not the right long-term path for me.
        </p>

        <p>
            Since the spring of 2024, I have been a part of the PGA Golf Management program at the University of Nebraska–Lincoln.
            Golf has always been a major part of my life, and I have especially developed a strong passion for understanding and teaching
            the golf swing. Being able to turn that passion into a career is something I truly enjoy, and it motivates me to keep learning
            and growing within the industry.
        </p>

        <p>
            I have gained experience at a wide range of golf facilities, from small-town public courses to large-scale country clubs.
            Through those opportunities, I have worked with people of all ages and skill levels, helping them improve their game and enjoy
            the sport more. Those experiences have strengthened my communication skills, my professionalism, and my ability to connect with others.
        </p>

        <p>
            Looking ahead, I hope my passion and talents lead me to opportunities across the country where I can continue building relationships,
            expanding my knowledge of the game, and making lifelong connections through my career in golf.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="small-card">
        <h3>Personal Values</h3>
        <p>Hard work, reliability, respect, professionalism, and creating genuine connections with people.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="small-card">
        <h3>Career Direction</h3>
        <p>
            My long-term goal is to build a successful career in the golf industry through club management, instruction,
            and member service while continuing to grow as a leader and golf professional.
        </p>
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
        <h3>Golf Industry Experience</h3>
        <p><strong>Centura Hills Golf Club – Seasonal Intern</strong></p>
        <ul>
            <li>Assisted the head professional with lessons and tournaments</li>
            <li>Worked with the course maintenance crew and gained broader knowledge of golf course operations</li>
            <li>Provided professional service to members and guests</li>
            <li>Strengthened communication and customer service skills in a golf setting</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>Youth Golf Leadership</h3>
        <p>
            One of the most meaningful parts of my experience has been helping run youth golf programming. I have worked with young golfers
            in instructional and camp settings, helping them improve fundamentals, build confidence, and enjoy the game. My commitment to
            creating a positive and engaging learning environment led to being recognized as a top camp leader.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>Additional Professional Experience</h3>
        <p><strong>Cairo Watering Hole – Bartender</strong></p>
        <ul>
            <li>Developed hospitality and service skills in a fast-paced environment</li>
            <li>Learned to stay composed under pressure while delivering strong customer experiences</li>
        </ul>

        <p><strong>Dick’s Sporting Goods – Golf Associate</strong></p>
        <ul>
            <li>Worked directly with customers to provide tailored product recommendations</li>
            <li>Built experience in retail professionalism, teamwork, and customer communication</li>
        </ul>

        <p><strong>Spring City – Shift Lead</strong></p>
        <ul>
            <li>Led employees during manager absences</li>
            <li>Managed customer-facing responsibilities and closing duties</li>
            <li>Built leadership, accountability, and team management experience</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="small-card">
        <h3>What These Experiences Show</h3>
        <p>
            Across golf, hospitality, retail, and leadership roles, I have built a strong foundation in service, communication,
            responsibility, and relationship-building. These experiences continue to prepare me for a career in golf and club management.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# RESUME
# -------------------------
elif page == "Resume":
    st.markdown(logo_html, unsafe_allow_html=True)
    st.header("Resume")

    st.markdown("""
    <div class="info-card">
        <h3>Resume Preview</h3>
        <p>
            You can view my resume below and download a copy as well.
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_display = f'''
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" 
            height="900" 
            type="application/pdf"
            style="border: 1px solid #ccc; border-radius: 12px;">
        </iframe>
        '''
        st.markdown(pdf_display, unsafe_allow_html=True)

        st.download_button(
            label="Download Resume",
            data=pdf_bytes,
            file_name="Easton_Brand_Resume.pdf",
            mime="application/pdf"
        )

    except FileNotFoundError:
        st.warning("Upload your resume PDF to GitHub and name it exactly: resume.pdf")

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
        <p>
            I am always open to opportunities to connect with others in the golf industry, discuss future career possibilities,
            and continue growing through new experiences.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Send a Message")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("Thank you for reaching out. This demo form is for display purposes only.")
        else:
            st.error("Please fill out all fields before submitting.")

    st.markdown("---")
    st.markdown("### Professional Links")
    st.markdown("- LinkedIn: add your link here")
    st.markdown("- GitHub: add your link here")
