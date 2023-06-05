import streamlit as st
import pandas as pd

# Define the candidates
candidates = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}

# Streamlit app
def main():
    st.title("Voting Application")
    st.write("Cast your vote for your favorite candidate!")

    # Display the candidates
    for candidate in candidates:
        st.write(f"- {candidate}")

    # Get user's vote
    vote = st.radio("Cast your vote:", list(candidates.keys()))

    # Vote button
    if st.button("Vote"):
        candidates[vote] += 1
        st.success("Vote cast successfully!")

        # Save voting results to Excel
        save_results_to_excel()

        # Redirect to another Streamlit page
        st.experimental_rerun()

    # Display the results
   # st.header("Results")
    #for candidate, votes in candidates.items():
     #   st.write(f"{candidate}: {votes} votes")

def save_results_to_excel():
    # Convert candidates dictionary to a Pandas DataFrame
    results_df = pd.DataFrame(list(candidates.items()), columns=["Candidate", "Votes"])

    # Save DataFrame to Excel
    results_df.to_excel("voting_results.xlsx", index=False)
    st.write("Voting results saved to voting_results.xlsx")

if __name__ == "__main__":
    main()
