import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout = 'wide', page_title = 'StartUp Analysis')

df= pd.read_csv('Startup_clean.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title("Overall Analysis")

    col1,col2,col3,col4 = st.columns(4)


    # total invested amount
    total = round(df['Amount'].sum())
    with col1:

        st.metric("Total Amount", str(total) + 'Cr')

    #max amount infused in a startup

    max_funding = df.groupby('start up')['Amount'].max().sort_values(ascending = False).head(1).values[0]
    with col2:
        st.metric("Max Funding", str(max_funding) + 'Cr')
    #avg  ticket size
    avg = df.groupby('start up')['Amount'].sum().mean()
    with col3:
        st.metric("Average Funding", str(avg) + 'Cr')
    # total funded startup
    num_startup= df['start up'].nunique()
    with col4:
        st.metric("Number of Startups", str(num_startup) + " " + 'Startups')

    st.header("MoM graph")
    selected_option = st.selectbox("Select Type", ['Total', 'Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['Amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['Amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')



    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'],temp_df['Amount'])

    st.pyplot(fig3)





def load_investor_details(Investors):
    st.title(Investors)

    last5_df = df[df['Investors'].str.contains(Investors)].head()[['date','start up','vertical','City','Round','Amount']]
    st.subheader("most recent investments")
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investment
        big_series = df[df['Investors'].str.contains(Investors)].groupby('start up')['Amount'].sum().sort_values(
            ascending=False).head()
        st.subheader("Biggest investments")

        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)

        st.pyplot(fig)

    with col2:
        vertical_series = df[df['Investors'].str.contains(Investors)].groupby('vertical')['Amount'].sum()
        st.subheader("Sector investments")

        fig, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels = vertical_series.index, autopct='%1.1f%%' )

        st.pyplot(fig)

    df['year'] = df['date'].dt.year
    year_series = df[df['Investors'].str.contains(Investors)].groupby('year')['Amount'].sum()
    st.subheader("YoY investments")
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index, year_series.values)


    st.pyplot(fig2)


#data cleaning
df['Investors'] = df['Investors'].fillna('Undisclosed')

st.sidebar.title("Startup Funding Analysis")
option = st.sidebar.selectbox('Select one', ['Overall Analysis','Startup', 'Investor'])

if option == "Overall Analysis":
    load_overall_analysis()



elif option == "Startup":
    st.sidebar.selectbox('Select Startup', sorted(df["start up"].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title("start up")
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['Investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)



