import numpy as np
import pickle
import streamlit as st
import math

## loading the saved model
loaded_model = pickle.load(open('C:/Users/ARNAB MANNA/PycharmProjects/diamond_price_pred_app/best_model.sav','rb'))

## creating a function

def diamond_prediction(input_data) :
    # changing input data into numpy array
    input_data_as_numpy_Array = np.array(input_data,dtype=object)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_Array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return "The price of the diamond is  {} dollar.".format(math.ceil(prediction[0]))

def main() :

    ## giving a title
    st.title('Diamond Price Prediction Application')
    ## getting the input data from user
    try :
        carat = st.text_input('weight of the diamond')
        cut = st.selectbox("Quality of the cut of diamond", (0, 1, 2, 3, 4))
        color = st.selectbox('Color of the diamond',(0,1,2,3,4,5,6))
        clarity = st.selectbox('A measurement of how clear the diamond is',(0,1,2,3,4,5,6,7))
        depth = st.text_input('Total depth percentage')
        table = st.text_input('Width of top of diamond relative to widest point')
        x = st.text_input('length in mm')
        y = st.text_input('width in mm')
        z = st.text_input('depth in mm')


        ## code for prediction
        satisfaction = ''
        ## creating a button for prediction
        if st.button('PREDICT') :
            st.text("Diamond Price prediction result")
            diamond_pred = diamond_prediction([carat,cut,color,clarity,depth,table,x,y,z])
            st.success(diamond_pred)
    except Exception as e:
        st.text(e)



if __name__ == '__main__' :
    main()


