import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("저는 streamlit 이에요")

x = np.linspace(0,10,100)
print(f"x:{x}")
y = np.sin(x)
print(f"y:{y}")

fig, ax=plt.subplots()
ax.plot(x,y,label='sin(x)',color='blue')
ax.set_title("sine graph")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.legend()

st.pyplot(fig)