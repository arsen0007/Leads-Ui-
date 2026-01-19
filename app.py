# app.py

import streamlit as st
import pandas as pd
import os

from taxonomy import MAIN_CATEGORIES
from filters import filter_by_category
from filters import filter_by_category, find_unmapped_practice_areas

DATA_DIR = "data"

st.set_page_config(page_title="Lawyer Lead Filter", layout="wide")

st.title("⚖️ Lawyer Lead Filtering Tool")


# --------------------
# STATE SELECTION
# --------------------
state_files = {
    f.replace(".csv", "").title(): os.path.join(DATA_DIR, f)
    for f in os.listdir(DATA_DIR)
    if f.endswith(".csv")
}

state = st.selectbox("Select State", list(state_files.keys()))
category = st.selectbox("Select Practice Category", MAIN_CATEGORIES)

# --------------------
# FILTER BUTTON
# --------------------
if st.button("Filter Leads"):
    df = pd.read_csv(state_files[state])

    if "PracticeAreas" not in df.columns:
        st.error("❌ PracticeAreas column not found in CSV")
    else:
        filtered_df = filter_by_category(df, category)

        st.success(f"✅ Found {len(filtered_df)} lawyers")
        st.dataframe(filtered_df, use_container_width=True)

        csv = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name=f"{state.lower()}_{category.lower().replace(' ', '_')}.csv",
            mime="text/csv",
        )
df = pd.read_csv(state_files[state])

# --- Admin: Unmapped Practice Areas ---
unmapped = find_unmapped_practice_areas(df)

if unmapped:
    with st.expander("⚠️ Unmapped Practice Areas (Admin Only)"):
        st.warning("These practice areas are NOT mapped to any main category:")
        st.write(sorted(unmapped))
