import ml_project as mp
import matplotlib.pyplot as plt

import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector
import trubrics

"""
## Digits Recognition Model Evaluation

Here are predictions for my digits recognition model. What do you think?
"""

st.number_input("Select a test data point", 0, len(mp.X_test) - 1, key="test_index")
test_index = st.session_state["test_index"]

image = mp.X_test[test_index].reshape(8, 8)
fig, ax = plt.subplots(figsize=(2, 2))
ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
ax.set_title(f"Prediction: {mp.predicted[test_index]}")
_, center, _ = st.columns(3)
with center:
    st.pyplot(fig)

collector = FeedbackCollector(
    data_context=mp.datacontext,
    model_name=mp.model_name,
    model_version=mp.model_version,
)
collector.st_feedback(type="thumbs", unique_key=f"point_{test_index}")

if st.session_state[f"point_{test_index}_down"]:
    """
    Please explain the error below:
    """
    collector.st_feedback(unique_key=test_index)
