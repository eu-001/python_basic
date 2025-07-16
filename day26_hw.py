import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

text1 = "1+1/(2**2*3)**2/1.5"
result = eval(text1)
st.write(f"{text1} = {result}")
