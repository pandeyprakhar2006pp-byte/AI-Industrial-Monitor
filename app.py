import streamlit as st
import pandas as pd
import numpy as np

st.title("Smart Industrial Monitor (AI + IoT)")

# Generate data
data = pd.DataFrame({
    "Energy": np.random.randint(40, 80, 50),
    "Temperature": np.random.randint(60, 90, 50),
    "Waste": np.random.randint(20, 50, 50)
})

st.metric("Avg Energy", round(data["Energy"].mean(), 2))
st.metric("Avg Temp", round(data["Temperature"].mean(), 2))
st.metric("Avg Waste", round(data["Waste"].mean(), 2))

st.subheader("System Health Status")

energy = data["Energy"].mean()
temp = data["Temperature"].mean()
waste = data["Waste"].mean()

if energy > 65 or temp > 80 or waste > 40:
    st.error("🔴 System Status: Critical")
elif energy > 55 or temp > 75 or waste > 35:
    st.warning("🟡 System Status: Moderate")
else:
    st.success("🟢 System Status: Optimal")

# Show data
st.subheader("Live Data")
st.write(data)

# Graph
st.subheader("System Graph")
st.line_chart(data)

# AI Alerts (simple logic)
st.subheader("AI Alerts")

if data["Energy"].mean() > 65:
    st.warning("⚠️ High Energy Usage Detected")

if data["Temperature"].mean() > 80:
    st.error("🔥 Machine Overheating")

if data["Waste"].mean() > 40:
    st.warning("♻️ High Waste Generation")

# Smart Suggestions
st.subheader("Suggestions")

suggestions_given = False

if data["Energy"].mean() > 65:
    st.warning("⚡ High energy usage → Reduce machine load")
    suggestions_given = True

if data["Temperature"].mean() > 80:
    st.error("🔥 High temperature → Cooling or maintenance required")
    suggestions_given = True

if data["Waste"].mean() > 40:
    st.warning("♻️ Excess waste → Improve recycling process")
    suggestions_given = True

if not suggestions_given:
    st.success("✅ System running efficiently")