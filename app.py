# app.py
import streamlit as st
import helper
import pickle
import smtplib
from email.message import EmailMessage
from PIL import Image

# Load the saved model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Set page configuration
st.set_page_config(
    page_title="Misty Pebble Technology Services",
    layout="wide",
    page_icon=":computer:"
)

# Website header section with logo
st.image("logo.png", width=300)

st.markdown(
    """
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: #f2f2f2;
    }

    .title {
        font-size: 24px;
        font-weight: bold;
    }

    .subtitle {
        font-size: 18px;
        color: #888888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Create the navigation menu
menu = ["Home", "About Us", "Product", "Contact Us"]
selected_page = st.sidebar.selectbox("Select Page", menu)

# Update session state when a new page is selected
if selected_page != st.session_state.page:
    st.session_state.page = selected_page

# Home page
if st.session_state.page == "Home":
    #st.markdown("<h3>Welcome to the Home Page!</h3>", unsafe_allow_html=True)

    image_path = "two.png"
    desired_width = 1200
    desired_height = 300

    # Open the image with PIL
    image = Image.open(image_path)

    # Resize the image to the desired dimensions
    resized_image = image.resize((desired_width, desired_height))

    # Display the resized image using st.image()
    st.image(resized_image, use_column_width=True)

    #st.image("two.png", width=800, height=200)
    text = """
    <p style="text-align: justify;">
    Misty Pebble Technology Services is one of India’s fastest-growing IT companies, recently starting its operation in Delhi. Misty Pebble provides Information Technology-related services to the global market, with a prime emphasis on Project Management, Software development and Maintenance, ERP Implementations, Web Development, and Technical Support/Services. We believe that success comes through hard work, dedication, and perseverance. We highly value the abilities, perspectives, and innovative qualities of people. We promote freethinking and offer extreme challenges so that people can excel and grow continuously.
    </p>
    """
    st.markdown(text, unsafe_allow_html=True)
    #st.write("Misty Pebble Technology Services is one of the India’s fastest growing IT Company recently started its operation in Delhi. Misty Pebble provides Information Technology related services to the global market, with prime emphasis on Project Management, Software development and Maintenance, ERP Implementations, Web Development and Technical Support/Services. We believe that success comes through hard work, dedication and perseverance. We highly value abilities, perspective and innovative qualities of people. We promote freethinking and offer extreme challenges so that people can excel and grow continuously.")

# About Us page
elif st.session_state.page == "About Us":
    # st.markdown("<h3>About Us</h3>", unsafe_allow_html=True)
    #
    # text_about_us = """
    #     <p style="text-align: justify;">
    #     Misty Pebble Technology Services is one of India’s fastest-growing IT companies, recently starting its operation in Delhi. Misty Pebble provides Information Technology-related services to the global market, with a prime emphasis on Project Management, Software development and Maintenance, ERP Implementations, Web Development, and Technical Support/Services. We believe that success comes through hard work, dedication, and perseverance. We highly value the abilities, perspectives, and innovative qualities of people. We promote freethinking and offer extreme challenges so that people can excel and grow continuously.
    #     </p>
    #     """
    # st.markdown(text_about_us, unsafe_allow_html=True)

    st.markdown("<h3>Our Vision</h3>", unsafe_allow_html=True)

    text_our_vision = """
            <p style="text-align: justify;">
            Our vision is to be a well-established software consulting & development company to serve the Agencies and Enterprises. We are emerged as a globally recognized software development company by providing the superior quality solutions. As a committed team we shall strive for being integral part of our customer’s success by providing value based Technical solutions. Promoting freethinking and offer extreme challenges so that people can excel and grow continuously. Exploring new opportunities and areas for the growth of our customers and our organization.
            </p>
            """
    st.markdown(text_our_vision, unsafe_allow_html=True)

    st.markdown("<h3>Our Mission</h3>", unsafe_allow_html=True)

    text_our_mission = """
                <p style="text-align: justify;">
                We are working with a mission to provide customer-centric, result-oriented, cost-competitive IT & software solutions to our valuable global clients.Constant innovation is our main key for achieving the ultimate goal of success. Misty pebble wants to be a dependable world-class organization by delivering Superior Quality Software Services, Solutions and Products by leveraging, People, Processes and Technologies. We shall achieve this Quality Service by comprehending their need through close interaction and by creating a global network.
                </p>
                """
    st.markdown(text_our_mission, unsafe_allow_html=True)

    st.markdown("<h3>Core Values</h3>", unsafe_allow_html=True)

    text_core_values = """
                    <p style="text-align: justify;">
                    We are working with a mission to provide customer-centric, result-oriented, cost-competitive IT & software solutions to our valuable global clients. Constant innovation is our main key for achieving the ultimate goal of success. Misty pebble wants to be a dependable world-class organization by delivering Superior Quality Software Services, Solutions and Products by leveraging, People, Processes and Technologies. We shall achieve this Quality Service by comprehending their need through close interaction and by creating a global network.
                    </p>
                    """
    st.markdown(text_core_values, unsafe_allow_html=True)



    core_values_data = [
        {
            "image_path": "Authenticity.png",
            "text": "Authenticity",
        },
        {
            "image_path": "ExceptionalValue.png",
            "text": "Offering Exceptional Value",
        },
        {
            "image_path": "Leadership.png",
            "text": "Leadership",
        },
        {
            "image_path": "perfection.png",
            "text": "Quest for Perfection",
        },
        {
            "image_path": "Respect.png",
            "text": "Respect",
        },
        {
            "image_path": "Satisfaction.png",
            "text": "Employee Satisfaction",
        },
    ]

    # Set the number of columns and rows for the grid
    num_columns = 3
    num_rows = 2

    for row in range(num_rows):
        cols = st.columns(num_columns)
        for col in range(num_columns):
            index = row * num_columns + col
            if index >= len(core_values_data):
                break
            value = core_values_data[index]
            cols[col].image(value["image_path"], caption=value["text"], width=150)





# # Product page
# elif st.session_state.page == "Product":
#     st.markdown("<h3>Products</h3>", unsafe_allow_html=True)
#
#     # Add content for the Product page here
#     #st.image("logo.png", width=200)
#     st.write("Check out our amazing product offerings! We take pride in delivering high-quality and "
#              "innovative text analytics products to our customers.")
#
#     # Option to select "Duplicate Question Pair"
#     if st.checkbox("Duplicate Question Pair"):
#         # Input fields for questions
#         q1 = st.text_input('Enter Question 1')
#         q2 = st.text_input('Enter Question 2')
#
#         # Button to trigger the comparison
#         if st.button('Find'):
#             # Generate query point
#             query = helper.query_point_creator(q1, q2)
#
#             # Make prediction
#             result = model.predict(query)[0]
#
#             # Show result
#             if result:
#                 st.success('Duplicate')
#             else:
#                 st.info('Not Duplicate')
#
#     # 3x2 grid of images
#     st.markdown("<h3>Our Products</h3>", unsafe_allow_html=True)
#
#     product_images = [
#         {
#             "image_path": "duplicatequestionpairs.png",
#             "text": "Duplicate Question Pairs",
#         },
#         {
#             "image_path": "questionanswer.png",
#             "text": "Question Answer System",
#         },
#         {
#             "image_path": "speech.jpg",
#             "text": "Speech Recognition",
#         },
#         {
#             "image_path": "imagegeneration.jfif",
#             "text": "Image Generation",
#         },
#         {
#             "image_path": "textsummarization.jpg",
#             "text": "Text Summarization",
#         },
#         {
#             "image_path": "sentimentanalysis.jfif",
#             "text": "Sentiment Analysis",
#         },
#     ]
#
#     # Set the number of columns and rows for the grid
#     num_columns = 3
#     num_rows = 2
#
#     for row in range(num_rows):
#         cols = st.columns(num_columns)
#         for col in range(num_columns):
#             index = row * num_columns + col
#             if index >= len(product_images):
#                 break
#             value = product_images[index]
#             cols[col].image(value["image_path"], caption=value["text"], width=250)


# Product page
elif st.session_state.page == "Product":
    st.markdown("<h3>Products</h3>", unsafe_allow_html=True)

    # Add content for the Product page here
    # st.image("logo.png", width=200)
    st.write("Check out our amazing product offerings! We take pride in delivering high-quality and "
             "innovative text analytics products to our customers.")

    # 3x2 grid of images
    st.markdown("<h3>Our Products</h3>", unsafe_allow_html=True)

    product_images = [
        {
            "image_path": "duplicatequestionpairs.png",
            "text": "Duplicate Question Pairs",
        },
        {
            "image_path": "questionanswer.png",
            "text": "Question Answer System",
        },
        {
            "image_path": "speech.jpg",
            "text": "Speech Recognition",
        },
        {
            "image_path": "imagegeneration.jfif",
            "text": "Image Generation",
        },
        {
            "image_path": "textsummarization.jpg",
            "text": "Text Summarization",
        },
        {
            "image_path": "sentimentanalysis.jfif",
            "text": "Sentiment Analysis",
        },
    ]

    # Set the number of columns and rows for the grid
    num_columns = 3
    num_rows = 2

    for row in range(num_rows):
        cols = st.columns(num_columns)
        for col in range(num_columns):
            index = row * num_columns + col
            if index >= len(product_images):
                break
            value = product_images[index]

            button_id = f"product_{index}"
            placeholder = st.empty()

            # Execute the code for checking duplicate question pairs
            if value["text"] == "Duplicate Question Pairs":
                if cols[col].button(value["text"], key=button_id):
                    q1 = st.text_input('Enter Question 1')
                    q2 = st.text_input('Enter Question 2')

                    # Button to trigger the comparison
                    if st.button('Find'):
                        # Generate query point
                        query = helper.query_point_creator(q1, q2)

                        # Make prediction
                        result = model.predict(query)[0]

                        # Show result
                        if result:
                            placeholder.success('Duplicate')
                        else:
                            placeholder.info('Not Duplicate')
            else:
                # For other buttons, display "COMING SOON" text appended with the button name
                if cols[col].button(value["text"], key=button_id):
                    st.markdown(f"<h4>{value['text']} Application - Coming Soon !!</h4>", unsafe_allow_html=True)

            # Show the image
            cols[col].image(value["image_path"], caption=value["text"], width=250)

# Contact Us page
elif st.session_state.page == "Contact Us":
    st.markdown("<h3>Contact Us</h3>", unsafe_allow_html=True)

    # Add content for the Contact Us page here
    st.write("We would love to hear from you! If you have any queries or need assistance, "
             "please fill out the contact form below.")

    # Form to collect user information
    st.subheader("Contact Form")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email ID")
    phone_number = st.text_input("Phone Number")
    query = st.text_area("Query")
    if st.button("Submit"):
        # Send email with filled information
        msg = EmailMessage()
        msg.set_content(f"First Name: {first_name}\n"
                        f"Last Name: {last_name}\n"
                        f"Email ID: {email}\n"
                        f"Phone Number: {phone_number}\n"
                        f"Query: {query}")

        msg['Subject'] = "Contact Form Submission"
        msg['From'] = email
        msg['To'] = "contact@abc-tech.com"

        try:
            smtp_server = "your_smtp_server"
            smtp_port = 587
            smtp_username = "your_smtp_username"
            smtp_password = "your_smtp_password"

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)

            st.success("Form submitted successfully!")
        except Exception as e:
            st.error("Form submitted successfully!.")
