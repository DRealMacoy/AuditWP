import openai
import streamlit as st
from streamlit_chat import message
import os 
from dotenv import load_dotenv
load_dotenv('api_key.env')

st.set_page_config(layout="wide",)
def Message():
    st.title("Important Message from Mark") 
    st.write("This is web app is built on top of the OpenAi's platform.")
    st.write("This is a beta version so that auditors can test it. I will be upgrading this app and may add more features in the future. If you have any questions, please contact me via Linkedin. The link is on the left.")
    st.write("I limit the responses to 8 risks at the moment. If you want to generate more responses and want to customize, please contact me.")
    st.write("As this is part of my research, I will be limiting this and may take it out of the public domain in the future. Thank you for your support!")
    st.write("Enjoy using technology to make your life easier!")


def Process():

            st.subheader('Identify the Main Process and Subprocess')
            Main_Process = st.selectbox('Choose the main process',
            ('Sales and Marketing', 'Human Resources', 'Finance and Accounting', 'Production and Operations', 'Research and Development', 'Information Technology' , 'Customer Service' , 'Quality Assurance', 'Supply Chain Management' ,  'Logistics and Distribution')
            )

            if Main_Process == 'Sales and Marketing':
                Subprocess = st.selectbox('Choose Subprocess',('Lead Generation' , 'Market Research', 'Product Promotion', 'Pricing Strategies', 'Customer Relationship Management', 'Distribution and Channel Management', 'Sales Forecasting', 'Market Segmentation', 'Advertising and Public Relations', 'Sales Training and Development'))

            elif Main_Process == 'Human Resources':
                Subprocess = st.selectbox('Choose Subprocess',('Recruitment and Selection', 'Training and Development', 'Performance Management', 'Compensation and Benefits', 'Employee Relations', 'Employee Engagement', 'HRIS', 'HR Analytics'))

            elif Main_Process == 'Finance and Accounting':
                Subprocess = st.selectbox('Choose Subprocess',('Budgeting and Forecasting', 'Accounting and Financial Reporting', 'Accounts Receivable', 'Accounts Payable', 'Treasury', 'Cash Management', 'Taxation', 'Financial Planning and Analysis', 'Financial Risk Management'))

            elif Main_Process == 'Production and Operations':
                Subprocess = st.selectbox('Choose Subprocess',('Production Planning and Control', 'Inventory Management', 'Quality Management', 'Maintenance Management', 'Logistics Management', 'Supply Chain Management', 'Project Management', 'Warehouse Management'))

            elif Main_Process == 'Research and Development':
                Subprocess = st.selectbox('Choose Subprocess',('Product Development', 'Product Design', 'Product Testing', 'Product Launch', 'Product Maintenance', 'Product Quality', 'Product Pricing', 'Product Promotion'))

            elif Main_Process == 'Information Technology':
                Subprocess = st.selectbox('Choose Subprocess',('IT Strategy', 'IT Governance', 'IT Architecture', 'IT Service Management', 'IT Security', 'IT Risk Management', 'IT Operations', 'IT Asset Management'))

            elif Main_Process == 'Customer Service':
                Subprocess = st.selectbox('Choose Subprocess',('Customer Service Strategy', 'Customer Service Operations', 'Customer Service Quality', 'Customer Service Technology', 'Customer Service Training', 'Customer Service Metrics', 'Customer Service Reporting'))

            elif Main_Process == 'Quality Assurance':
                Subprocess = st.selectbox('Choose Subprocess',('Quality Assurance Strategy', 'Quality Assurance Operations', 'Quality Assurance Quality', 'Quality Assurance Technology', 'Quality Assurance Training', 'Quality Assurance Metrics', 'Quality Assurance Reporting'))

            elif Main_Process == 'Supply Chain Management':
                Subprocess = st.selectbox('Choose Subprocess',('Supply Chain Strategy', 'Supply Chain Operations', 'Supply Chain Quality', 'Supply Chain Technology', 'Supply Chain Training', 'Supply Chain Metrics', 'Supply Chain Reporting'))

            elif Main_Process == 'Logistics and Distribution':
                Subprocess = st.selectbox('Choose Subprocess',('Logistics Strategy', 'Logistics Operations', 'Logistics Quality', 'Logistics Technology', 'Logistics Training', 'Logistics Metrics', 'Logistics Reporting'))

            Number_risks = st.slider('Choose the number of risks you want to audit', 0, 8, 1)
            #convert slider value to a string   
            Number_risks = str(Number_risks)
            st.write('You selected the number of risks:', Number_risks)

            #write the selected options in a text area
            st.text_area('Copy and paste this into the audit work program generator', ("Identify the top " + Number_risks + " risks in " + f'{Main_Process} Process specific to {Subprocess}  ' + "and identify the adequate controls in place and create the audit testing for each risk identified."),
                         height=150,)



def Audit_Assist():

            openai.api_key = os.environ.get('API_KEY')
            def generate_response(prompt):
                completion=openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=prompt,
                    max_tokens=750,
                    stop=None,
                    temperature=0.7,   
                    top_p=1,
                    best_of=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    )
                message=completion.choices[0].text
                return message

            st.subheader("Risk Based Audit Work Program Generator")
            st.caption("This will generate your risk-based audit work program after you paste and hit Ctrl + Enter")
            #initialize the session state
            user_input=st.text_area("You:",height=120,placeholder=("Paste the text your copied from Process and Subprocess on the bottom. Once pasted, press Ctrl +Enter to generate the audit program."), key='input')
            #display out if user input is not empty
            if user_input:
                if 'adequate controls in place and create the audit testing for each risk identified.' in user_input:
                    output=generate_response(user_input)
                    st.text_area("Generated by your AI Audit Coach:",height=800, value=output, key='output')       
                else:
                    st.text_area("Generated by AI Audit Assistant:",height=800, value="Sorry. I could see that you are not using the format in the Process and Subprocess. Please copy and paste so I can generate the work program.", key='output')
            #if user input is empty, display a message
            else:
                st.text_area("Generated by AI Audit Assistant:",height=800, value="Oops, the table above is empty. Please put anything so I can start to work. Please paste something above.", key='output')



#Sidebar navigation
st.sidebar.markdown("Developed by Mark with ❤️")
love_icon = """ 
"""
st.sidebar.markdown("[Linkedin Profile](https://www.linkedin.com/in/mark-hofmann-ca-cpa-cia-crma-cfsa-20594822)")
st.sidebar.markdown(love_icon, unsafe_allow_html=True)

st.sidebar.subheader('Menu Navigator')
options = st.sidebar.radio('Choose the page the display:', ["Message", "Process & Subprocess", "Audit Program Auto Generator"])

# Navigation options
if options == 'Message':
    Message()
elif options == 'Process & Subprocess':
    Process()
elif options == 'Audit Program Auto Generator':
    Audit_Assist()
