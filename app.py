from ctypes import alignment
from tkinter import CENTER
import pandas as pd
import time
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image 
from libraries import *
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete)


def load_lottie_url(url: str): 
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


selected = option_menu(None, ["About Covid-19", "Treatments", 'Covid-19 Prevention', 'Covid-19 Visualization'], 
    icons=['file-medical', 'eyedropper', 'check-circle', 'clipboard-data'], 
    menu_icon="cast", default_index=1, orientation="horizontal")

if selected == "About Covid-19":
       
    
    st.header(f"You have selected {selected}")

    animation = "https://assets8.lottiefiles.com/packages/lf20_y1eqwwb2.json"
    
    lottie = load_lottie_url(animation)
    

    st_lottie(lottie, height=300)


    time.sleep(5)

    st.title('What is Covid-19')
    st.write("Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age.")
    st.title('How it spreads')
    st.write('The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols. You can be infected by breathing in the virus if you are near someone who has COVID-19, or by touching a contaminated surface and then your eyes, nose or mouth. The virus spreads more easily indoors and in crowded settings.')
    video1 = open("COVID19.mp4", "rb")
    st.video("https://www.youtube.com/watch?v=BPc1DQaoDxY")
    st.write("[Learn More >](https://www.who.int/emergencies/diseases/novel-coronavirus-2019)")

if selected == "Treatments":
    st.header(f"You have selected {selected}")
    
    animation5 = "https://assets1.lottiefiles.com/packages/lf20_vckswclv.json"
    
    lottie5 = load_lottie_url(animation5)
    

    st_lottie(lottie5, height=300)

    st.title('Self care')
    st.header('After exposure to someone who has COVID-19, do the following:')
    st.markdown('- Call your health care provider or COVID-19 hotline to find out where and when to get a test.-')
    st.markdown('- Cooperate with contact-tracing procedures to stop the spread of the virus.')
    st.markdown('- If testing is not available, stay home and away from others for 14 days.')
    animation4 = "https://assets1.lottiefiles.com/packages/lf20_imsphcho.json"
    lottie4 = load_lottie_url(animation4)
    st.markdown('- Keep at least a 1-metre distance from others, even from your family members.')
    st.markdown('- Stay in a separate room from other family members, and if not possible, wear a medical mask.')
    animation3 = "https://assets4.lottiefiles.com/packages/lf20_uidhg9jw.json"
    lottie3 = load_lottie_url(animation3)
    st.markdown('- Keep the room well-ventilated.')
    animation2 = "https://assets5.lottiefiles.com/packages/lf20_3ayip1qu.json"
    lottie2 = load_lottie_url(animation2)
    st.markdown('- Monitor yourself for any symptoms for 14 days.')
    st.markdown('- Call your health care provider immediately if you have any of these danger signs: difficulty breathing, loss of speech or mobility, confusion or chest pain.')
    st.markdown('- Clean your hands frequently.')
    animation ="https://assets5.lottiefiles.com/packages/lf20_6v5h4ckl.json"
    lottie = load_lottie_url(animation)
    st.markdown('- While you are in quarantine do not go public places')

    st_lottie(lottie4, height=200)
    st_lottie(lottie3, height=200)
    st_lottie(lottie2, height=200)
    st_lottie(lottie, height=200)



if selected == "Covid-19 Prevention":
    st.header(f"You have selected {selected}")
    st.write('The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently. Get vaccinated when it’s your turn and follow local guidance.')
    animation ="https://assets1.lottiefiles.com/packages/lf20_1ntvvmsz.json"
    animation2 ="https://assets1.lottiefiles.com/packages/lf20_vyixuzos.json"
    animation3 ="https://assets1.lottiefiles.com/packages/lf20_zczlo413.json"
    animation4 ="https://assets1.lottiefiles.com/packages/lf20_xbeapo0i.json"
    animation5 ="https://assets1.lottiefiles.com/packages/lf20_rv8lfct8.json"
    lottie = load_lottie_url(animation)
    lottie2 = load_lottie_url(animation2)
    lottie3 = load_lottie_url(animation3)
    lottie4 = load_lottie_url(animation4)
    lottie5 = load_lottie_url(animation5)

    st_lottie(lottie4, height=200,)
    st_lottie(lottie3, height=200)
    st_lottie(lottie2, height=200)
    st_lottie(lottie, height=200)
    st_lottie(lottie5, height=200)


    st.image("https://www.c19.mhlw.go.jp/images/sp/kv_en.png")

    st.title('Symptoms')
    st.header('Most common symptoms:')
    st.markdown('- Fever')
    st.markdown('- Cough')
    st.markdown('- Tiredness')
    st.markdown('- Loss of taste or smell')
    st.header('Less common symptoms:')
    st.markdown('- sore throat')
    st.markdown('- Headache')
    st.markdown('- Aches and pains')
    st.markdown('- Diarrhoea')
    st.markdown('- A rash on skin, or discolouration of fingers or toes')
    st.markdown('- Red or irritated eyes')
    st.header('Serious symptos')
    st.markdown('- Difficulty breathing or shortness of breath')
    st.markdown('- Loss of speech or mobility, or confusion')
    st.markdown('- Chest pain')

  

if selected == "Covid-19 Visualization":

    animation ="https://assets1.lottiefiles.com/packages/lf20_8axjdnts.json"
    lottie = load_lottie_url(animation)
    st_lottie(lottie, height=300)

    
    countries = ['China','Srilanka','India','France','United States','Russia', 'Italy', 'Japan', 'United Kingdom']
    data_types = ['cases','deaths','recovered']
    country_code = {'Sri Lanka': 'lk', 'United States': 'us','China': 'cn',
                  'India': 'in', 'Russia': 'ru','France' : 'fr', 'Italy' : 'it',
                  'Japan' : 'jp', 'United Kingdom' : 'gb', 'Canada' : 'ca'}

    country = st.sidebar.selectbox('What is your country', countries)
    days = st.sidebar.slider('days',min_value=1,max_value=90, step=1)
    data_type = st.sidebar.multiselect('pick data types',data_types)


    total_cases = get_historic_cases(country,str(days))
    total_deaths = get_historic_deaths(country,str(days))
    total_recoveries = get_historic_recoveries(country,str(days))
    total_df = pd.concat([total_cases,total_deaths,total_recoveries],axis=1).astype(int)

    daily_cases = get_daily_cases(country,str(days))
    daily_deaths = get_daily_deaths(country,str(days))
    daily_recoveries = get_daily_recoveries(country,str(days))
    daily_df = pd.concat([daily_cases,daily_deaths,daily_recoveries],axis=1).astype(int)

    yesterday_cases = get_yesterday_cases(country,)
    yesterday_deaths = get_yesterday_deaths(country,)
    yesterday_recoveries = get_yesterday_recoveries(country,)


    st.title('Covid-19 Visualization Dashboard')

    st.info(f"{country}'s Covid-19 Report")

    st.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")

    col1, col2, col3 = st.columns(3)

    st.metric('selected country',country)
    col1.metric('Yesterday Cases',yesterday_cases)
    col2.metric('Yesterday Deaths',yesterday_deaths)
    col3.metric('Yesterday Recoveries',yesterday_recoveries)

    

    st.line_chart(daily_df)

    st.dataframe(daily_df)


