import streamlit as st
import json,requests
import pandas as pd



# Create the top layout
col1, col2 = st.columns([14,6])

# Title of the app
with col1:
    st.title("Social Media Hashtag Trend Analyzer Application")

with col2:
    st.image(r'E:\guvi\capstone_project\census_datapipeline\census_datapipeline\Guvi.jpg')

st.markdown("<br>" * 2, unsafe_allow_html=True)

# Bottom selectbox (if you still want to keep it)
bottom_container = st.container()
with bottom_container:
    col3 = st.columns([14])
    with col3[0]:
        res = tuple(["Post","Trending Hashtag"])
        question = st.selectbox(
            "Select the type?",
            res,
            placeholder="Select type"
        )

st.markdown("<br>" * 2, unsafe_allow_html=True)

if question =="Post":
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Function to display chat messages
    def display_chat():
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    # Create a container for the chat window
    chat_container = st.container()

    # Create a container for the input
    input_container = st.container()

    # Display chat messages
    with chat_container:
        display_chat()


    # Create the input area at the bottom
    with input_container:
        user_input = st.chat_input("Type your message here...")
        
        if user_input:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_input})
            url = "https://ljv9joy583.execute-api.us-east-1.amazonaws.com/twitter/"

            # JSON body
            data = {
                "type" : "Post",
                "post": user_input,

            }

            # Convert Python dictionary to JSON string
            json_data = json.dumps(data)

            # Set the headers
            headers = {
                "Content-Type": "application/json"
            }

            # Make the POST request
            response = requests.post(url, data=json_data, headers=headers)
            res = response.text
            dict_result = json.loads(res)
           
            #print("line 82",dict_result["body"])
            a= dict_result["body"]
            #print("a",json.loads(a)["res"])
            response_post = json.loads(a)["res"]
            #res = response.get("res") 
            res_op = f"{response_post}"
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_post})
            
            # Rerun the app to display the new messages
            st.experimental_rerun()

if question =="Trending Hashtag":
    
            
        url = "https://ljv9joy583.execute-api.us-east-1.amazonaws.com/twitter/"

    
        # Make the POST request
        data = {
                "type" : "Trending Hashtag",
                

            }
        json_data = json.dumps(data)
        headers = {
                "Content-Type": "application/json"
            }
        response = requests.post(url,data=json_data, headers=headers)#, data=json_data, headers=headers)
        res = response.text
        dict_result = json.loads(res)
        dict_result = json.loads(dict_result["body"])
        #print("in treand ",dict_result)
        treand_hash_data = pd.DataFrame(list(dict_result.items()), columns=['Hashtag', 'Count'])

        treand_hash_data['Count'] = pd.to_numeric(treand_hash_data['Count'])        
        st.header('Treanding Hashtag', divider='rainbow')
        st.dataframe(treand_hash_data)
        st.markdown("<br>" * 2, unsafe_allow_html=True)
        st.header('Treanding Hashtag Bar Chart', divider='rainbow')
        st.bar_chart(data=treand_hash_data,x="Hashtag", y="Count")
        

