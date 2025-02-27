import streamlit as st
import pickle
import pandas as pd

# Load model and label encoder
def load_model_and_encoder():
    with open('model_and_encoder.pkl', 'rb') as file:
        data = pickle.load(file)
    return data['model'], data['encoder']

pipeline, label_encoder = load_model_and_encoder()


def show_predict_page():
    
    st.title("Mass Casuality Incident Category Prediction ")

    st.write("""### We need some information to predict the crime category""")

        
    occ_month = (
         "January",
         "February", 
         "March", 
         "April" ,
         "May", 
         "June", 
         "July", 
         "August", 
         "September", 
         "October", 
         "November", 
         "December"
    )

    occ_dow = (
         "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    )

    occ_range = (
         'Night', 'Morning', 'Afternoon', 'Evening'
    )

    occ_hood = ('Morningside Heights', 'Malvern East', 'Pelmo Park-Humberlea',
       'Woodbine-Lumsden', 'Cliffcrest', 'Weston', 'Downsview',
       'Woburn North', 'Willowridge-Martingrove-Richview',
       'Mount Olive-Silverstone-Jamestown', 'Markland Wood',
       'St Lawrence-East Bayfront-The Islands', 'Bedford Park-Nortown',
       'Oakwood Village', 'Annex', 'Thorncliffe Park', 'Taylor-Massey',
       'West Rouge', 'St.Andrew-Windfields', 'Wexford/Maryvale',
       'Dorset Park', 'Keelesdale-Eglinton West', 'Clairlea-Birchmount',
       "Tam O'Shanter-Sullivan", 'West Humber-Clairville',
       'Rockcliffe-Smythe', 'West Queen West', 'South Riverdale',
       'Islington', 'West Hill', 'Danforth', 'Oakridge',
       'Stonegate-Queensway', 'Fenside-Parkwoods',
       'Glenfield-Jane Heights', 'Alderwood', 'Dovercourt Village',
       'East Willowdale', 'Humewood-Cedarvale', 'East End-Danforth',
       'Lansing-Westgate', 'Banbury-Don Mills', 'Briar Hill-Belgravia',
       'Woodbine Corridor', 'Scarborough Village', 'Bathurst Manor',
       'North Riverdale', 'Eglinton East', 'Pleasant View',
       'Lambton Baby Point', 'Lawrence Park South', 'Trinity-Bellwoods',
       'Rosedale-Moore Park', 'Newtonbrook West', 'Junction Area',
       'Malvern West', 'Blake-Jones', 'Church-Wellesley',
       'Bay-Cloverhill', 'Kensington-Chinatown', 'Kennedy Park', 'Rustic',
       'Newtonbrook East', 'Danforth East York', 'Morningside',
       "East L'Amoreaux", 'Junction-Wallace Emerson',
       'Yorkdale-Glen Park', 'North Toronto',
       'Agincourt South-Malvern West', 'Elms-Old Rexdale',
       'Yonge-Eglinton', 'Bayview Village', 'Avondale', 'Yonge-Doris',
       'Westminster-Branson', 'Edenbridge-Humber Valley',
       'Kingsway South', 'Guildwood', 'The Beaches',
       'Centennial Scarborough', 'Forest Hill North', 'Forest Hill South',
       'Princess-Rosethorn'
    )

    month = st.selectbox("Month", occ_month)
    occ_day = st.slider("Date", 1, 31, 1)
    dow = st.selectbox("Day of the week", occ_dow)
    occ_hour = st.slider("Hour of the day", 0, 23, 0)
    time_range = st.selectbox("Time Range", occ_range)
    hood = st.selectbox("Neighbourhood", occ_hood)
    ok = st.button("Predict 🔮")

    if ok:
        input_data = pd.DataFrame({
            'OCC_MONTH': [month],
            'OCC_DAY': [occ_day],
            'OCC_DOW': [dow],
            'OCC_HOUR': [occ_hour],
            'OCC_TIME_RANGE': [time_range],
            'NEIGHBOURHOOD_158': [hood]  # Adjust column name as needed
        })
        prediction_numeric = pipeline.predict(input_data)
        prediction_category = label_encoder.inverse_transform(prediction_numeric)[0]
        st.subheader(f"The predicted crime category is {prediction_category}")

# if __name__ == '__main__':
#     show_predict_page()
