import streamlit as st
import pandas as pd
import datetime
import base64

def main():
    names = ['', 'Liam', 'Lyndsay K', 'Lyndsay', 'Abigail', 'Shayla', 'Sarah', 'Lesley', 'Kerry', 'Shop Floor']
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
        df['Baguette'] = baguettes

        current_date = datetime.date.today()
        df['Date'] = current_date.strftime("%Y-%m-%d")

        labeled_by = st.selectbox("Who labeled the baguettes?", names[1:])
        df['Labeled by'] = labeled_by

        df = df[['Date', 'Baguette', 'Left from the day before', 'To Make Today', 'Made by', 'Labeled by']]

        st.write("Dataframe:")
        st.write(df)

        comments = st.text_area("Comments (max 1000 characters)", max_chars=1000)
        df['Comments'] = comments

        # Download button
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        filename = f"Bakery_Log_{selected_name}_{current_date}.csv"
        href = f"<a href='data:file/csv;base64,{b64}' download='{filename}'>Download Today's info as a CSV</a>"
        st.markdown(href, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
