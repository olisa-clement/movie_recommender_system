
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
from PIL import Image
import PIL.Image as PILI
import plotly_express as px

# Data Visulization
import matplotlib.pyplot as plt

# Custom Libraries

from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
rating_df = pd.read_csv("resources/data/ratings.csv")
movie_df = pd.read_csv("resources/data/movies.csv")

# Working on data
df_merge = pd.merge(movie_df, rating_df, on='movieId')
opt = g = df_merge[["title", "rating"]]
cnt = g.title.value_counts()
df_val_counts = pd.DataFrame(cnt)
df_v = df_val_counts.reset_index()
df_v.columns = ['Movie', 'counts']
matrix = df_v.pivot_table(columns=['Movie'], values='counts')

# Loading a css stylesheet


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


load_css("resources/CSS/Styling.css")

# App declaration


def main():

    # Create page options
    page_options = ["Recommender System", "Home",
                    "About Us", "Project", "Solution Overview"]

    
    page_selection = st.sidebar.selectbox("Navigation", page_options)

    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        # st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png', use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option', title_list[14930:15200])
        movie_2 = st.selectbox('Second Option', title_list[25055:25255])
        movie_3 = st.selectbox('Third Option', title_list[21100:21200])
        fav_movies = [movie_1, movie_2, movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

    
    elif page_selection == "Home":
        # Creating header
        m = st.markdown("""<p style="text-align: justify; font-size:15px">We're thrilled to have you on board. \n We at Alpha Analytics use data to solve real-world challenges. Movies mean different things to different people. At Alpha Analytics, we regard movies as a chance to escape reality and spend time with family, friends, and loved ones. We made the decision to make the experience Awesome! Navigate to the 'Recommender System' to begin your adventure with movies created for every type of journey you desire. We'd like to know if you enjoyed seeing these films.</p>""", unsafe_allow_html=True)
        st.header("Alpha Analytics")
        st.image("images/logo.jpg")
        # st.write("--")

        # Creating "Why Choose Us columns"
        col1, col2 = st.columns([1, 2.5])
        col2.markdown("## WHY CHOOSE US")
        a1, a2, a3 = st.columns([1, 1, 1])
        # Data
        a1.markdown("#### DATA")
        a1.write("Discover and analyse important information and trends in your data")
        # Technology
        a2.markdown("#### TECHNOLOGY")
        a2.write("Cutting edge technogy to keep your business ahead in the market")
        # Innovation
        a3.markdown("#### INNOVATION")
        a3.write("Bringing your ideas to life in the toughest conditions")
        # st.write("--")

        # Creating clients columns
        v1, v2 = st.columns([23, 1])
        v1.markdown(
            "<h1 style='text-align: center; color: white;'> Our Clients</h1>", unsafe_allow_html=True)
        x1, x2, x3, x4 = st.columns([1, 1, 1, 1])
        # x1.image("https://t.ly/lGTT")
        # x2.image("https://t.ly/UxE_2")
        # x3.image("https://t.ly/96lZ")
        # x4.image("https://t.ly/AvAQ")
        st.markdown("##### The organizations above have over the years enjoyed excellent data solution delivery through our diverse services. In this time, we have maintained excellent customer relationship and always putting the client at the top of our priorities")
        # st.write("--")

        # Creating Contact columns
        col3, col4 = st.columns([1, 2])
        col4.markdown("## Contact Us")
        col5 = st.text_input("Email", "Enter your email")
        col6 = st.text_area("Message", "Your Message")
        but11, but12, but13 = st.columns([1, 4, 1])

        # Submit button
        if but11.button("Submit"):
            st.write("We are glad to hear from you")

    elif page_selection == "About Us":
        # Adding logo and title
        logo, title = st.columns(2)

        logo.image("https://t.ly/vQtS")

        title.header("Alpha Analytics")

        title.markdown("""<p style="text-align: left;">Alpha Analytics is a team of data enthusiast driven by passion for innovation. The company is well experienced in the delivery of cutting edge and innovative AI applications. The team's experience and expertise spreads across different industries.</p>""", unsafe_allow_html=True)

        # st.write("--")

        # Creating columns for images
        c1, c2, c3 = st.columns([3, 6, 1])
        c2.markdown("## Meet the Alphas")
        d1, d2, d3 = st.columns([1, 1, 1])
        e1, e2, e3 = st.columns([1, 1, 1])
        d1.image("images/francis.jpg")
        d1.write("#### Francis Egah, CEO")
        d2.image("images/olisa (1).png")
        d2.write("#### Olisa Clement,  Chief AI Engineer")
        d3.image("images/abdul.jfif")
        d3.write("#### Abdulrasheed Musa, Product Manager")
        e1.image("images/sibu.jpg")
        e1.write("#### Sibusiso Mashabela, Sales Manager")
        e2.image("images/karabo (1).PNG")
        e2.write("#### Karabo Molema, Business Analyst")
        # st.write("--")
        st.write("<h1 style='text-align: center; color: red;'>Alpha Analytics</h1>",
                 unsafe_allow_html=True)

    elif page_selection == "Project":
        st.title("Movie Recommender")
        st.subheader("Project Overview")
        st.write("In today's technology-driven society, recommender systems are socially and economically vital for ensuring that individuals can make proper decisions about the information they interact with on a regular basis. One instance where this is especially true is in movie content recommendations, where clever algorithms may assist viewers identify exceptional titles among tens of thousands of possibilities.")
        st.video("https://youtu.be/DeGHnp_oJSQ")
        st.subheader("Project Information")
        st.write("We a love to enjoy good movies. Our aim in this project is to enhance your movie experience through a robust recommendation engine putting into consideration your preferences as well  those of many other movie lovers. You can use the 'Content-based' engine to get movies similar to your preferences or 'Collaborative' engine to see what other people are watching. Enjoy your experience!!")
        st.subheader("Interact with Our Data")
        st.write("No worries about choosing which movie to see. Use our movie database to see what ratings other moviegoers have given to some of their favorite films.")
        #
        x_ax_val = st.selectbox("Select Movie", options=matrix.columns)

        rtin = opt[opt["title"] == x_ax_val].value_counts(opt["rating"])
        rect = pd.DataFrame(rtin)
        df_vn = rect.reset_index()
        df_vn.columns = ['Rating', 'Rating Count']

        fig = px.bar(df_vn, x=df_vn["Rating"], y=df_vn["Rating Count"],
                     color=df_vn["Rating Count"], title=x_ax_val)
        st.plotly_chart(fig)

    elif page_selection == "Solution Overview":
        st.title("Solution Overview")

        # Detailing the approach
        st.subheader("Our Approach")
        st.write("To create an efficient system for our customers, we designed two types of recommender engines: content-based filtering and collaborative filtering systems to ensure that the movies list recommended by the corresponds to their preferences. The goal of content-based techniques is to attempt to construct a model based on the given 'features' that explains the observed user-item interactions. Considering users and movies, we will try to model the fact that 'User1' enjoys 'action' movies, therefore we can recommend some action movies to him.")
        st.write("In collaborative filtering, new movies are recommended to consumers based on the interests and preferences of other like users. It is a very intelligent recommender system that is based on the similarities of various users. It analyzes the preferences of similar users and makes recommendations.")

        # EDA section
        st.subheader("EDA")
        st.write("Let's give you some insight to understand our data")
        # Creating plots to show statistics
        st.markdown("##### Movie Production by Year")
        st.image("images/movie_produc_yr.png")
        st.write("We can see that 2015 and 2016 represent the years with most movie production amongst the years. This could be a direct impact of the increase in sequels of several movies. It might be interesting to see if the sequels are as good as the original movies")
        st.markdown("##### Top 20 Movies by Rating")
        st.image("images/top20rted.png")
        st.write(
            "The 90's must have had people going to the movies as movies from that era has most ratings")
        st.markdown("##### Genres to look out for")
        st.image("images/genre.png")
        st.write("It is obvious that peope want to see some action and thrillers that is why the top  genres seen are action packed movies")

        # Modelling section
        st.subheader("Models")
        st.markdown(
            "Two algorithmic approach will be used for the model development. Namely Content-based filtering and Collaborative-based filtering")
        st.markdown("##### Content-based filtering")
        st.write("Content-based filtering methods are based on the description of a product and a profile of the user’s preferred choices. In this recommendation system, products are described using keywords, and a user profile is built to express the kind of item this user likes.")
        st.image("images/cbf.PNG")
        st.write("For instance, if a user likes to watch movies such as Iron Man, the recommender system recommends movies of the superhero genre or films describing Tony Stark.")
        st.markdown("##### Collaborative-based filtering")
        st.write("The collaborative filtering method is based on gathering and analyzing data on user’s behavior. This includes the user’s online activities and predicting what they will like based on the similarity with other users.")
        st.image("images/clbf.PNG")
        st.write("For example, if user A has seen Spiderman, Batman and Godzilla while user B likes Godzilla, Batman, and Superman, they have similar interests. So, it is highly likely that A would like Superman and B would enjoy Spiderman. This is how collaborative filtering takes place.")

        # st.write("--")
        w1, w2, w3 = st.columns([1, 1, 1])
        w2.image("https://t.ly/vQtS")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
