import streamlit as st
import pandas as pd

def main():
    names = ['', 'Liam', 'Lyndsay K', 'Kyndsay', 'Abigail', 'Shayla', 'Sarah', 'Lesley', 'Kerry', 'Shop Floor']
    baguettes = ['Baguette Cheese', 'Baguette Ham', 'Baguette Tuna']

    # Title and instructions
    st.title("Bakery Log - Baguettes")

    # Selectbox to choose a name
    selected_name = st.selectbox("Please select your name from the list below:", names, index=0)

    st.write("You selected:", selected_name)

    if selected_name != '':
        # Question about their task
        st.write("Please enter the quantities of each Baguette left from the day before:")

        baguette_quantities = {}
        for baguette in baguettes:
            quantity = st.number_input(baguette, value=0)
            baguette_quantities[baguette] = quantity

        total_to_make = sum([18 - quantity for quantity in baguette_quantities.values()])

        st.write(f"You should make {total_to_make} Baguettes today.")

        # Create dataframe
        df = pd.DataFrame.from_dict(baguette_quantities, orient='index', columns=['Left from the day before'])
        df['To Make Today'] = [18 - quantity for quantity in baguette_quantities.values()]
        df['Made by'] = selected_name

        st.write("Dataframe:")
        st.write(df)

        # Check if all baguettes were made by the selected user
        made_all = st.radio(f"Did {selected_name} make all the baguettes?", ('Yes', 'No'), key="made_all")

        if made_all == 'Yes':
            # Check who printed and labeled the baguettes
            printed_by = st.selectbox("Who printed and labeled the baguettes today?", names[1:])
            df['Printed and Labeled by'] = printed_by

        elif made_all == 'No':
            st.write("Please update the 'Made by' column for the baguettes:")
            made_by = selected_name
            for i, baguette in enumerate(baguettes):
                made = st.radio(f"{selected_name} made {baguette}?", ('Yes', 'No'), key=f"made_{i}")
                if made == 'No':
                    made_by = st.selectbox(f"Who made {baguette}?", names[1:])
                df.loc[baguette, 'Made by'] = made_by

            st.write("Please update the 'Labeled by' column for the baguettes:")
            labeled_by = selected_name
            for i, baguette in enumerate(baguettes):
                labeled = st.radio(f"Was {baguette} labeled?", ('Yes', 'No'), key=f"labeled_{i}")
                if labeled == 'No':
                    labeled_by = st.selectbox(f"Who labeled {baguette}?", names[1:])
                df.loc[baguette, 'Labeled by'] = labeled_by

        st.write("Updated Dataframe:")
        st.write(df)

        st.button("Download Today's info as a CSV")

if __name__ == '__main__':
    main()
