# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="wide", page_icon="📝", page_title="Online Resume Builder")
st.title("📝 Online Resume Builder")

st.write(
    "This app helps you create Professional Resume with few Clicks!"
)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

col1,col2,col3=st.columns(3)
with col1.expander('Personal Details'):
    fp = st.form("Personal Information")
    name= fp.text_input("Your Full Name")
    email=fp.text_input("Your E-mail ID")
    ph=fp.text_input("Your Contact Number")
    city=fp.text_input("Your Current City")
    country=fp.text_input("Country You Are From")
    linkedin=fp.text_input("Link to Your LinkedIn Profile")
    tagline=fp.text_area("Say something about yourself in less than 60 words")
    meta1=fp.text_input("key-skill#1")
    meta2=fp.text_input("key-skill#2")
    meta3=fp.text_input("key-skill#3")
    position=fp.text_input("position")
    subp = fp.form_submit_button("SUBMIT")
    

if subp:
    html = template.render(
        name=name,
        email=email,
        ph=ph,
        city=city,
        country=country,
        linkedin=linkedin,
        meta1=meta1,
        meta2=meta2,
        meta3=meta3,
        position=position
        
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    st.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="resume.pdf",
        mime="application/octet-stream",
    )
    