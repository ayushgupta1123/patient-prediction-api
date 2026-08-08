import streamlit as st
import requests


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="InsureAI | Premium Predictor",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# API CONFIG
# ============================================================

API_URL = "http://127.0.0.1:8000/predict"


# ============================================================
# SESSION STATE
# ============================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Light"


# ============================================================
# THEME
# ============================================================

theme = st.session_state.theme

if theme == "Dark":
    background = "#0b1120"
    card = "#111827"
    card2 = "#172033"
    text = "#f8fafc"
    muted = "#94a3b8"
    border = "#263449"
else:
    background = "#f5f7fb"
    card = "#ffffff"
    card2 = "#f8fafc"
    text = "#0f172a"
    muted = "#64748b"
    border = "#e2e8f0"


# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    f"""
    <style>

    .stApp {{
        background:
            radial-gradient(
                circle at 5% 5%,
                rgba(37, 99, 235, 0.10),
                transparent 25%
            ),
            radial-gradient(
                circle at 95% 5%,
                rgba(13, 148, 136, 0.10),
                transparent 25%
            ),
            {background};
    }}

    .block-container {{
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    header {{
        visibility: hidden;
    }}

    /* Hero */

    .hero {{
        position: relative;
        overflow: hidden;

        padding: 48px;

        border-radius: 28px;

        background:
            linear-gradient(
                135deg,
                #0f172a,
                #172554 50%,
                #0f766e
            );

        color: white;

        box-shadow:
            0 25px 60px rgba(15, 23, 42, 0.25);

        margin-bottom: 30px;
    }}

    .hero::before {{
        content: "";

        position: absolute;

        width: 280px;
        height: 280px;

        right: -80px;
        top: -130px;

        border-radius: 50%;

        background: rgba(255,255,255,0.08);
    }}

    .hero::after {{
        content: "";

        position: absolute;

        width: 200px;
        height: 200px;

        right: 100px;
        bottom: -140px;

        border-radius: 50%;

        background: rgba(255,255,255,0.05);
    }}

    .hero-content {{
        position: relative;
        z-index: 2;
    }}

    .hero-badge {{
        display: inline-block;

        padding: 7px 14px;

        border-radius: 50px;

        background: rgba(255,255,255,0.12);

        border:
            1px solid rgba(255,255,255,0.20);

        color: white;

        font-size: 12px;

        font-weight: 700;

        letter-spacing: 0.8px;

        margin-bottom: 18px;
    }}

    .hero-title {{
        color: white;

        font-size: 44px;

        font-weight: 850;

        line-height: 1.08;

        letter-spacing: -1.5px;

        margin: 0;
    }}

    .hero-text {{
        color: rgba(255,255,255,0.75);

        font-size: 16px;

        line-height: 1.7;

        max-width: 700px;

        margin-top: 16px;
    }}

    /* Cards */

    .custom-card {{
        background: {card};

        border:
            1px solid {border};

        border-radius: 20px;

        padding: 22px;

        box-shadow:
            0 10px 30px rgba(15,23,42,0.05);
    }}

    .metric-card {{
        background: {card};

        border:
            1px solid {border};

        border-radius: 18px;

        padding: 20px;

        min-height: 120px;

        box-shadow:
            0 8px 25px rgba(15,23,42,0.05);
    }}

    .metric-icon {{
        font-size: 24px;
        margin-bottom: 8px;
    }}

    .metric-label {{
        color: {muted};

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 0.8px;

        text-transform: uppercase;
    }}

    .metric-value {{
        color: {text};

        font-size: 25px;

        font-weight: 850;

        margin-top: 5px;
    }}

    /* Result */

    .result {{
        margin-top: 28px;

        padding: 35px;

        border-radius: 24px;

        text-align: center;

        background:
            linear-gradient(
                135deg,
                rgba(16,185,129,0.10),
                rgba(13,148,136,0.05)
            );

        border:
            1px solid rgba(16,185,129,0.30);

        box-shadow:
            0 18px 45px rgba(16,185,129,0.08);
    }}

    .result-icon {{
        font-size: 42px;
    }}

    .result-label {{
        color: #059669;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1px;

        text-transform: uppercase;

        margin-top: 8px;
    }}

    .result-value {{
        color: {text};

        font-size: 42px;

        font-weight: 900;

        margin-top: 5px;
    }}

    .result-description {{
        color: {muted};

        font-size: 14px;
    }}

    /* Info */

    .info {{
        background: {card2};

        border:
            1px solid {border};

        border-radius: 14px;

        padding: 13px 16px;

        color: {muted};

        font-size: 13px;

        margin-top: 15px;
    }}

    /* Footer */

    .footer {{
        text-align: center;

        margin-top: 50px;

        padding-top: 25px;

        border-top:
            1px solid {border};

        color: {muted};

        font-size: 12px;

        line-height: 1.8;
    }}

    </style>
    """
)


# ============================================================
# TOP BAR
# ============================================================

top1, top2 = st.columns([5, 1])

with top1:
    st.markdown(
        "### 🛡️ **INSUREAI**"
    )

    st.caption(
        "Machine Learning • Insurance Analytics"
    )

with top2:

    selected_theme = st.selectbox(
        "Theme",
        ["Light", "Dark"],
        index=0 if theme == "Light" else 1,
        label_visibility="collapsed",
    )

    if selected_theme != st.session_state.theme:
        st.session_state.theme = selected_theme
        st.rerun()


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-content">

            <div class="hero-badge">
                🛡️ AI-POWERED INSURANCE ANALYTICS
            </div>

            <div class="hero-title">
                Insurance Premium<br>
                Category Predictor
            </div>

            <div class="hero-text">
                Predict an insurance premium category using
                machine learning based on demographic,
                lifestyle, financial and health-related
                information.
            </div>

        </div>

    </div>
    """
)


# ============================================================
# CUSTOMER PROFILE
# ============================================================

st.subheader("👤 Customer Profile")

st.caption(
    "Enter the customer information required by the prediction model."
)


# ============================================================
# INPUTS
# ============================================================

left, right = st.columns(2, gap="large")


with left:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=119,
        value=30,
        step=1,
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=65.0,
        step=0.5,
        format="%.1f",
    )

    height = st.number_input(
        "Height (m)",
        min_value=0.5,
        max_value=2.49,
        value=1.70,
        step=0.01,
        format="%.2f",
    )

    income_lpa = st.number_input(
        "Annual Income (LPA)",
        min_value=0.1,
        max_value=1000.0,
        value=10.0,
        step=0.5,
        format="%.1f",
    )


with right:

    smoker = st.radio(
        "Smoking Status",
        [False, True],
        format_func=lambda x: "Yes" if x else "No",
        horizontal=True,
    )

    city = st.selectbox(
        "City",
        [
            "Mumbai",
            "Delhi",
            "Bangalore",
            "Chennai",
            "Kolkata",
            "Hyderabad",
            "Pune",
            "Jaipur",
            "Chandigarh",
            "Indore",
            "Lucknow",
            "Patna",
            "Ranchi",
            "Visakhapatnam",
            "Coimbatore",
            "Bhopal",
            "Nagpur",
            "Vadodara",
            "Surat",
            "Rajkot",
            "Jodhpur",
            "Raipur",
            "Amritsar",
            "Varanasi",
            "Agra",
            "Dehradun",
            "Mysore",
            "Jabalpur",
            "Guwahati",
            "Thiruvananthapuram",
            "Ludhiana",
            "Nashik",
            "Allahabad",
            "Udaipur",
            "Aurangabad",
            "Hubli",
            "Belgaum",
            "Salem",
            "Vijayawada",
            "Tiruchirappalli",
            "Bhavnagar",
            "Gwalior",
            "Dhanbad",
            "Bareilly",
            "Aligarh",
            "Gaya",
            "Kozhikode",
            "Warangal",
            "Kolhapur",
            "Bilaspur",
            "Jalandhar",
            "Noida",
            "Guntur",
            "Asansol",
            "Siliguri",
        ],
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job",
        ],
        format_func=lambda x: x.replace("_", " ").title(),
    )


# ============================================================
# BMI
# ============================================================

bmi = weight / (height ** 2)


if bmi < 18.5:
    bmi_status = "Underweight"
    bmi_icon = "🔵"

elif bmi < 25:
    bmi_status = "Normal"
    bmi_icon = "🟢"

elif bmi < 30:
    bmi_status = "Overweight"
    bmi_icon = "🟠"

else:
    bmi_status = "Obese"
    bmi_icon = "🔴"


# ============================================================
# PROFILE OVERVIEW
# ============================================================

st.subheader("📊 Profile Overview")

st.caption(
    "Live summary of the information you entered."
)


m1, m2, m3, m4 = st.columns(4)


with m1:

    st.metric(
        "🎂 Age",
        f"{age}",
    )


with m2:

    st.metric(
        "⚖️ BMI",
        f"{bmi:.1f}",
    )


with m3:

    st.metric(
        "💰 Income",
        f"₹{income_lpa:.1f} L",
    )


with m4:

    st.metric(
        "🏙️ City",
        city,
    )


st.info(
    f"{bmi_icon} BMI Classification: **{bmi_status}**"
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.write("")

predict = st.button(
    "🔮  Predict Insurance Premium Category",
    type="primary",
    use_container_width=True,
)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    # --------------------------------------------------------
    # INPUT DATA
    # --------------------------------------------------------

    input_data = {
        "age": int(age),
        "weight": float(weight),
        "height": float(height),
        "income_lpa": float(income_lpa),
        "smoker": bool(smoker),
        "city": city,
        "occupation": occupation,
    }


    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    errors = []

    if age < 1 or age > 119:
        errors.append("Age must be between 1 and 119.")

    if weight <= 0:
        errors.append("Weight must be greater than 0.")

    if height <= 0:
        errors.append("Height must be greater than 0.")

    if income_lpa <= 0:
        errors.append("Income must be greater than 0.")


    if errors:

        for error in errors:
            st.error(error)

        st.stop()


    # --------------------------------------------------------
    # CALL API
    # --------------------------------------------------------

    with st.spinner(
        "🤖 Running machine learning prediction..."
    ):

        try:

            response = requests.post(
                API_URL,
                json=input_data,
                timeout=15,
            )


            # =================================================
            # SUCCESS
            # =================================================

            if response.status_code == 200:

                result = response.json()

                prediction = result.get(
                    "predicted_category"
                )


                if prediction is not None:

                    st.html(
                        f"""
                        <div class="result">

                            <div class="result-icon">
                                🎯
                            </div>

                            <div class="result-label">
                                Machine Learning Prediction
                            </div>

                            <div class="result-value">
                                {prediction}
                            </div>

                            <div class="result-description">
                                Prediction generated successfully
                                from the customer profile.
                            </div>

                        </div>
                        """
                    )


                    st.success(
                        "Prediction completed successfully."
                    )


                    with st.expander(
                        "🔍 View API request & response"
                    ):

                        st.write(
                            "### Request sent to FastAPI"
                        )

                        st.json(input_data)

                        st.write(
                            "### API response"
                        )

                        st.json(result)


                else:

                    st.error(
                        "API responded successfully, "
                        "but no prediction was returned."
                    )


            # =================================================
            # API ERROR
            # =================================================

            else:

                st.error(
                    f"FastAPI returned HTTP "
                    f"{response.status_code}"
                )

                try:

                    st.json(response.json())

                except ValueError:

                    st.code(response.text)


        # =====================================================
        # CONNECTION ERROR
        # =====================================================

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI."
            )

            st.warning(
                "Your FastAPI server is probably not running."
            )

            st.code(
                "uvicorn app:app --reload"
            )

            st.info(
                f"Frontend is trying to reach:\n\n"
                f"{API_URL}"
            )


        # =====================================================
        # TIMEOUT
        # =====================================================

        except requests.exceptions.Timeout:

            st.error(
                "⏱️ FastAPI took too long to respond."
            )


        # =====================================================
        # REQUEST ERROR
        # =====================================================

        except requests.exceptions.RequestException as error:

            st.error(
                f"❌ Request failed: {error}"
            )


        # =====================================================
        # UNKNOWN ERROR
        # =====================================================

        except Exception as error:

            st.error(
                "❌ Unexpected application error."
            )

            st.exception(error)


# ============================================================
# HOW IT WORKS
# ============================================================

st.write("")
st.write("")

st.subheader("⚙️ How It Works")

st.caption(
    "Simple machine learning prediction pipeline."
)


p1, p2, p3 = st.columns(3)


with p1:

    with st.container(border=True):

        st.markdown("### 👤 Step 01")

        st.markdown(
            "**Enter Profile**"
        )

        st.caption(
            "Provide age, weight, height, income, "
            "smoking, city and occupation."
        )


with p2:

    with st.container(border=True):

        st.markdown("### ⚡ Step 02")

        st.markdown(
            "**FastAPI Processing**"
        )

        st.caption(
            "FastAPI validates the request and "
            "calculates derived features."
        )


with p3:

    with st.container(border=True):

        st.markdown("### 🤖 Step 03")

        st.markdown(
            "**ML Prediction**"
        )

        st.caption(
            "The trained model predicts the "
            "insurance premium category."
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    f"""
    <div class="footer">

        🛡️ <strong>InsureAI</strong>

        <br>

        Insurance Premium Category Prediction System

        <br>

        Python • FastAPI • Scikit-learn • Streamlit

    </div>
    """
)


