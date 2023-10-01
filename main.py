import streamlit as st
import streamlit.components.v1 as components

# Page layout
st.set_page_config(layout="wide")
st.title("Unlocking Telangana's Potential: Unveiling Growth Patterns and Delivering Key Insights to the Government")
st.markdown('''<p style = "text-align: right"><i>Prasanna Phanindran S</i></p>''', unsafe_allow_html=True)
st.subheader("Codebasics Resume Project Challenge #7")

st.header("About the Project:")
file_path = "research_questions_and_recommendations.pdf"
st.markdown(f'''Telangana is one of the fastest-growing states in India and one of the states with an open data policy. (They have published all their data online).
Analyse Telangana’s growth among different sectors quantitatively and provide useful Insights to the Telangana government that would help them to make data-informed decisions that would further support the growth of the state.
            ''')
download_button = st.download_button(label=" Questions to be Answered can be Downloaded here", data=open(file_path, "rb").read(), file_name="research_questions_and_recommendations.pdf")

st.header("Presentation:")
st.markdown('''
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/DoVcyOjFo7Y?si=zZC7s-R3w-BUKiQY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
''', unsafe_allow_html=True)


st.title("General Dataset Overview - Insights")


st.write("dim_dates and dim_districts datasets provides information about Fiscal year and district details which will make sense when mapped with the main dataset")

st.markdown("**<u>Column Description for fact_stamps (Stamp Registeration Dataset)</u> :**", unsafe_allow_html=True)
st.write("The dataset provides information on the revenue generated from document registrations and estamp challan payments aggregated at the district and monthly level.")
st.write("- dist_code: This column uniquely Identifies the districts column on dim_districts dataset. It is a Categorical Variable")
st.write("- month: This column represents the starting date of each month. Provides more details when mapped with dim_dates dataset")
st.write("- documents_registered_cnt: This column represents the total count of documents registered.")
st.write("- documents_registered_rev: This column represents the total revenue generated from the registered documents.")
st.write("- estamps_challans_cnt: This column represents the count of e-stamps challans.")
st.write("- estamps_challans_rev: This column represents the revenue generated from e-stamps challans.")

st.markdown("**<u>Column description for fact_transport (Vehicle Sales Dataset)</u> :**", unsafe_allow_html=True)
st.write("The dataset provides information about the individual vehicle sales data from the RTA(Regional Transport Authority) of the state of Telangana categorized by fuel type,vehicle class, seating capacity, and other general categories aggregated at the district and monthly level.")
st.write("- dist_code: This column uniquely Identifies the districts column on dim_districts dataset. It is a Categorical Variable")
st.write("- month: This column represents the starting date of each month. Provides more details when mapped with dim_dates dataset")
st.write("Vehicle sales categorized by different fuel types:")
st.write("- fuel_type_petrol: Number of vehicles sold with fuel type as petrol.")
st.write("- fuel_type_diesel: Number of vehicles sold with fuel type as diesel.")
st.write("- fuel_type_electric : Number of vehicles sold with electric type")
st.write("- fuel_type_other: Number of vehicles sold with other fuel types")
st.write("Vehicle sales categorized by different vehicle class:")
st.write("- vehicleClass_Motorcycles: This category includes all two-wheeled vehicles, such as motorcycles, scooters etc.")
st.write("- vehicleClass_Motorcars: This category includes all four-wheeled vehicles, such as cars, vans etc.")
st.write("- vehicleClass_Auto rickshaws: This category includes three-wheeled vehicles, such as auto rickshaws.")
st.write("- vehicleClass_Agriculture: This category includes all vehicles used for agricultural purposes, such as tractors and harvesters.")
st.write("- vehicleClass_Others: This category includes all vehicles belonging to other classes.")
st.write("Vehicle sales categorized by seating capacity")
st.write("- seatCapacity_1_to_3: Number of vehicles sold with a seating capacity ranging from 1 to 3.")
st.write("- seatCapacity_4_to_6: Number of vehicles sold with a seating capacity ranging from 4 to 6.")
st.write("- seatCapacity_above_6: Number of vehicles sold with a seating capacity above 6.")
st.write("Sales of vehicles by other categories:")
st.write("- Brand_new_vehicles: Number of brand new vehicles sold.")
st.write("- Pre-owned_vehicles: Number of pre-owned vehicles sold.")
st.write("- category_Non-Transport: Number of vehicles in the non-transport category sold. The Non-Transport category typically includes vehicles that are not primarily used for public transportation of passengers or goods. Instead, these vehicles are generally intended for personal use, recreational activities, agriculture, construction, and other non-commercial purposes.")
st.write("- category_Transport: Number of vehicles in the transport category sold. The Transport category comprises vehicles primarily designed and used for the transportation of goods, passengers, or both. These vehicles are generally associated with commercial and public transportation purposes.")

st.markdown("**<u>Column description for fact_TS_iPASS (Investments Dataset)</u> :**", unsafe_allow_html=True)
st.write("The TS-iPASS dataset in Telangana comprises data concerning units or businesses established within the state under the 'Industrial Project Approval and Self-Certification System' (iPASS). This government initiative aims to foster industrial growth and investment by streamlining project approvals and enabling self-certification for businesses.")
st.write("For further details, visit: [TS-iPASS](https://ipass.telangana.gov.in/)")
st.write("- dist_code: This column uniquely Identifies the districts column on dim_districts dataset. It is a Categorical Variable")
st.write("- month: This column represents the starting date of each month. Provides more details when mapped with dim_dates dataset")
st.write("- sector: This column represents the industry category. Examples of sectors include 'Automobiles', 'Beverages', 'Engineering', 'Food Processing', etc.")
st.write("- investment in cr: The column represents the investment made in the specific sector, measured in crores (a unit of currency), for the corresponding district and month.")
st.write("- number_of_employees: This column represents the number of employees associated with that sector for the given district and respective month.")

st.markdown('''
<p style = "font-size: 50px; font-weight: bold; text-align: center; text-decoration: underline;">Primary Questions</p>
''', unsafe_allow_html=True)
# Page title
st.title("Stamp Registration Revenue Analysis")
# Question 1
st.header("Question 1: Revenue Variation across Districts")
st.write("The revenue generated from document registration varies significantly across districts in Telangana.")
st.image("p1/p1a.png", width=700)
st.write("Here are the top 5 districts that showed the highest document registration revenue growth between FY 2019 and 2022:")
st.image("p1/p1b.png", width=700)
st.write("1. Rangareddy: Contributed 37.3%")
st.write("2. Medchal_Malkajgiri: Contributed 21.2%")
st.write("3. Hyderabad: Contributed 12.7%")
st.write("4. Sangareddy: Contributed 7.2%")
st.write("5. Hanumakonda: Contributed 2.7%")

# Question 2
st.header("Question 2: Revenue Comparison - Document Registration vs. E-stamp Challans")
st.write("In FY 2022, the revenue generated from e-stamp challans surpassed the revenue generated from document registration in several districts. Here are the top 5 districts where e-stamp revenue contributes significantly more to the total revenue:")
st.image("p2/p2b_i.png", width=700)
st.write("1. Rangareddy: E-stamp revenue of more than 65 crores")
st.write("2. Hyderabad: E-stamp revenue of more than 10 crores")
st.write("3. Hanumakonda: E-stamp revenue of more than 2 crores")
st.write("4. Yadadri Bhuvanagiri: E-stamp revenue of more than 1 crore")
st.write("5. Khammam: E-stamp revenue of more than 3 crores")
st.write("However, overall, the revenue derived from document registration surpasses the revenue generated from e-stamp challans, as demonstrated in the following breakdown.")
st.image("p2/p2a.png", width=700)

# Question 3
st.header("Question 3: Alteration in E-Stamp Challan and Document Registration Pattern")
st.write("The E-Challan was implemented in December 2020. Since the implementation of e-Stamp challan, there has been a significant change in the count pattern of e-Stamp challans and document registrations as shown below:")
st.image("p3/p3a.png", width=700)
st.write("The data reveals a noticeable surge in the count, and upon comparing the revenue generated before and after the implementation of e-stamp, it becomes evident that the revenue generation significantly increased in the post-implementation phase, as illustrated below.")
st.image("p3/p3b.png", width=700)
st.write("Some suggestions to the government for further improvement include streamlining the e-stamp issuance process, enhancing user awareness, and implementing regular training programs for the stakeholders.")

# Question 4
st.header("Question 4: Categorization of Districts based on Revenue Generation")
st.write("Based on stamp registration revenue generation during the fiscal year 2021 to 2022, the districts can be categorized into three segments:")
image_urls = [
    "p4/p4b.jpg",
    "p4/Telangana-New-Map-33-Districts.png",
    "p4/p4a.png"
]
images_per_row = 3
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)

st.write("1. High Revenue: Districts with the highest stamp registration revenue, approximately greater than 167 crores (66th quantile)")
st.write("2. Moderate Revenue: Districts with moderate stamp registration revenue, approximately between 62 crores and 167 crores (between 33rd and 66th quantile)")
st.write("3. Low Revenue: Districts with comparatively lower stamp registration revenue, approximately lesser than 62 crores (33rd quantile)")

st.title("Transportation/Vehicle Sales Analysis")
# Question 5
st.header("Question 5: Correlation between Vehicle Sales and Months/Seasons")
st.write("Based on the dataset analysis, Hyderabad ranks highest in overall vehicle sales for all fuel types, while Kumurambheem Asifabad ranks lowest across all years. Taking a monthly view of sales, the following breakdown emerges:")
st.caption("Hyderabad")
image_urls = [
    "p5/p5a.png",
    "p5/p5b.png",
]
image_urls2 = [
    "p5/p5c.png",
    "p5/p5d.png",
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
for i in range(0, len(image_urls2), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls2))):
        with columns[j - i]:
            st.image(image_urls2[j], use_column_width=True)
st.caption("Kumurambheem Asifabad")
image_urls = [
    "p5/a.png",
    "p5/b.png",
]
image_urls2 = [
    "p5/c.png",
    "p5/d.png",
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
for i in range(0, len(image_urls2), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls2))):
        with columns[j - i]:
            st.image(image_urls2[j], use_column_width=True)
st.write("For both districts, it is evident that during Q3, there is a spike in sales, especially in October and November, due to festive offers. However, in FY2022, the Q3 spike pattern does not follow, and it is even lower compared to other months. Festive offers seem to have an influence, but not consistently.")
# Question 6
st.header("Question 6: Distribution of Vehicles by Vehicle Class across Districts")
st.write("Upon examining the FY2022 data, motorcycles remain the most preferred vehicles, with significant sales in every district. Further analysis provides the following breakdowns for each vehicle class:")
st.write("- Motorcycles and cars are popular in Hyderabad and neighboring districts Medchal-Malkajgiri, Rangareddy, and Sangareddy.")
st.caption("Motorcycles")
st.image("p6/a.png", use_column_width=True)
image_urls = [
    "p6/bike_sales.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.caption("Motorcars")
st.image("p6/b.png", use_column_width=True)
image_urls = [
    "p6/car_sales.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("This suggests that most people in and around the state's capital can afford their own vehicles, indicating the development and opportunities in those districts.")
st.write("- Autorickshaws are primarily used for public transportation and are most popular in Hyderabad, Sangareddy, and Khammam.")
st.image("p6/c.png", use_column_width=True)
image_urls = [
    "p6/auto_sales.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("This indicates the demand for transportation in Hyderabad, Sangareddy, and Khammam.")
st.write("- Agricultural vehicles are used for various purposes in the agricultural fields. Nalgonda tops the list, followed by Siddipet, Khammam, and Bhadradri Kothagudem.")
st.image("p6/d.png", use_column_width=True)
image_urls = [
    "p6/agri_sales.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("Overall, most districts in Telangana show high sales rates for agricultural vehicles, highlighting Telangana's contribution to the agricultural sector.")
st.write("- For other vehicle types, Rangareddy tops the list, followed by Medchal-Malkajgiri, Hyderabad, and Karimnagar.")
st.image("p6/e.png", use_column_width=True)
image_urls = [
    "p6/other_sales.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("These other types of vehicles fall under the non-transport category and are predominantly used for logistics purposes, indicating Telangana's involvement in the logistics sector.")
# Question 7
st.header("Question 7: Top and Bottom Districts for Vehicle Sales Growth")
st.write("I analyzed the data to identify the districts that experienced the most and least significant growth in vehicle sales from FY 2021 to FY 2022. Our analysis considered all fuel types, including Petrol, Diesel, Electric, and other alternatives. Here are the results:")
st.write("- Initially, when comparing overall sales for all fuel types, we found that:")
st.image("p7/a.png", use_column_width=True)
image_urls = [
    "p7/aa-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("Rangareddy, Hyderabad, Medchal-Malkajgiri, Karimnagar, and Sangareddy saw an increase in sales, while other districts had a decline in sales compared to FY 2021. Of these, Warangal, Nizamabad, and Nalgonda experienced a significant decline in sales, indicating the considerable influence of Hyderabad on vehicle sales.")
st.write("- For vehicles with Petrol fuel type, only Rangareddy and Hyderabad saw an increase in sales compared to FY 2021, while all other districts experienced a significant decline in sales, with Warangal, Nizamabad, and Mahabubnagar showing a steep decline in sales.")
st.image("p7/b.png", use_column_width=True)
image_urls = [
    "p7/bb-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("- For vehicles with Diesel fuel type, Karimnagar, Rangareddy, and Sangareddy had good sales compared to the previous year, though Warangal, Nalgonda, and Mahabubnagar experienced a decline in Diesel vehicle sales.")
st.image("p7/c.png", use_column_width=True)
image_urls = [
    "p7/cc-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("- Electric vehicle sales increased significantly, with Hyderabad leading in sales compared to the previous year, followed by Rangareddy and Medchal-Malkajgiri. While there was no decline in sales rate, Wanapathy, Jogulamba Gadwal, and Mancherial had lower electric vehicle sales.")
st.image("p7/d.png", use_column_width=True)
image_urls = [
    "p7/dd-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("- Other fuel types also saw predominant sales in FY2022 compared to FY2021, with Hyderabad, Rangareddy, and Khammam having high sales rates compared to lower-performing districts such as Nalgonda, Yadadri Bhuvanagiri, and Nirmal, which experienced a decrease in sales.")
st.image("p7/e.png", use_column_width=True)
image_urls = [
    "p7/ee-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.write("The analysis also suggests that many consumers are considering the transition to renewable energy-based vehicles, which can help reduce carbon emissions in the state.")


# Heading
st.title("Telangana State Industrial Project Approval and Self Certification System (TS-iPASS) - Analysis")

# Question 8
st.header("Question 8: Top 5 Sectors with Significant Investments in FY 2022")
st.write("The top 5 sectors that witnessed the most significant investments in FY 2022 are as follows:")
st.image("p8/a.png", use_column_width=True)
st.markdown("""
1. Plastic and Rubber
2. Pharmaceuticals and Chemicals
3. Real Estate, Industrial Parks and IT Buildings
4. Solar and Other Renewable Energy
5. Engineering
""")

# Question 9
st.header("Question 9: Top 3 Districts Attracting Significant Sector Investments (FY 2019-2022)")
st.write("The top 3 districts that have attracted the most significant sector investments during FY 2019 to 2022 are as follows:")
st.image("p9/a.png", use_column_width=True)
st.markdown("""
1. Rangareddy
2. Sangareddy
3. Medchal_Malkajgiri
""")
image_urls = [
    "p9/aa-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown("""
The substantial investments in these districts can primarily be attributed to the impact of the capital city, Hyderabad, which facilitated:
- Proximity to transportation hubs
- Availability of skilled labor
- Government incentives and policies
- Infrastructure development
""")

# Question 10
st.header("Question 10: Relationship between District Investments, Vehicle Sales, and Stamps Revenue (FY 2021-22)")
st.markdown("""
I evaluated each dataset separately to better understand the connections between stamp registration, vehicle sales, and district investments in FY2021–2022, and I have divided the dataset into districts as shown below.
""")
st.image("p10/a.png", use_column_width=True)
st.image("p10/b.png", use_column_width=True)
st.image("p10/c.png", use_column_width=True)
st.image("p10/d-1.png", use_column_width=True)

st.markdown("""
- While there isn't an exact alignment between the datasets, it is evident that in all three datasets, the top-performing districts consistently include Hyderabad or its neighboring districts. This suggests that investments in and around the city are stimulating growth in the real estate sector and driving vehicle sales for logistics and transportation purposes.
- If a district witnesses substantial investments in industries like manufacturing or technology, it can result in heightened vehicle sales as businesses expand their operations and necessitate transportation services. Likewise, an upsurge in stamps revenue can indicate increased real estate transactions or overall economic activity within the district.
""")

# Question 11
st.header("Question 11: Sectors with Substantial Investments in Multiple Districts (FY 2021-2022)")
st.write("To identify sectors with substantial investments in multiple districts, we first need to determine the sectors with high investments:")
st.image("p11/a.png", use_column_width=True)
st.markdown(""" 
From the above illustration, it is evident that the investment-heavy sectors are:
- Pharmaceuticals and Chemicals
- Plastic and Rubber
- Real Estate, Industrial Parks and IT Buildings
- Beverages
- Food Processing 
""")
st.write("Now, breaking down these sectors district-wise, we can examine their contributions to multiple districts.")
st.write("- Firstly, let's explore the breakdown of the Pharmaceuticals and Chemicals Sector:")
st.image("p11/b.png", use_column_width=True)
image_urls = [
    "p11/bb-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown('''
The Pharmaceuticals and Chemicals sector has made significant contributions district-wise, with Sangareddy and Medchal_Malkajgiri showing very high investments, and Nagarkurnool with some medium investments.
''')
st.write("- Secondly, let's explore the breakdown of the Plastics and Rubbers Sector:")
st.image("p11/c.png", use_column_width=True)
image_urls = [
    "p11/cc-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown('''
The Plastics and Rubber sector has contributed significantly to multiple districts, with Sangareddy, Rangareddy, and Medchal_Malkajgiri at the top of the list. It should be noted that not all districts are covered, and Pedapalli has the lowest investments.
''')
st.write("- Thirdly, let's explore the breakdown of the Real Estate, Industrial Parks and IT Buildings Sector:")
st.image("p11/d.png", use_column_width=True)
image_urls = [
    "p11/dd-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown('''
Although investments are significant, they are concentrated in only three districts, namely Rangareddy, Sangareddy, and Karimnagar.
''')
st.write("- Next, let's explore the breakdown of the Beverages Sector:")
st.image("p11/e.png", use_column_width=True)
image_urls = [
    "p11/ee-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown('''
The Beverages sector has made significant contributions district-wise, with Narayanapet having the highest investment and Hanumanakonda with the lowest.
''')
st.write("- Finally, let's explore the breakdown of the Food Processing Sector:")
st.image("p11/f.png", use_column_width=True)
image_urls = [
    "p11/ff-1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown('''
The Food Processing sector is the 5th most significant sector, with the highest investment in Kamareddy and the lowest in Adilabad.
''')

# Question 12
st.header("Question 12 : Seasonal Patterns or Cyclicality in Investment Trends for Specific Sectors")
st.markdown("""
In terms of investment patterns within the sectors, there is a lack of consistency. Some sectors, like IT and Real Estate, exhibit significant investments in the same month but with a three-year difference. Conversely, apart from sectors such as thermal power plants, engineering, pharma, research and development (R&D), fertilizers, and related industries, as well as solar and other renewable energy sectors, all other sectors have recently experienced a notable surge in substantial investments. However, the above mentioned sectors showed inconsistent patterns in their investment trends.
""")

import streamlit as st
import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="./")

imageUrls = [
"p12/a.png",
"p12/b.png",
"p12/c.png",
"p12/d.png",
"p12/e.png",
"p12/f.png",
"p12/g.png",
"p12/h.png",
"p12/i.png",
"p12/j.png",
"p12/k.png",
"p12/l.png",
"p12/m.png",
"p12/n.png",
"p12/o.png",
"p12/p.png",
"p12/q.png",
"p12/r.png",
"p12/s.png",
"p12/t.png"

]

selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

if selectedImageUrl is not None:
    st.image(selectedImageUrl)

st.markdown('''
<p style="font-size: 50px; font-weight: bold; text-align: center; text-decoration: underline;">Secondary Questions</p>
''', unsafe_allow_html=True)

# Question 1
st.header("Question 1: Top 5 Districts to Buy Commercial Properties")
st.write("Commercial property, commonly referred to as commercial real estate, investment property, or income property, is real estate utilized for commercial purposes. It primarily refers to structures that host commercial operations, but it can also be used to describe huge residential rental units and land used to generate income. The classification of a property as a commercial property has an impact on how it is funded, taxed, and subject to legislation.")
st.markdown('''Hence, when investing in a commercial property, the main factors to be considered are:
- Economic Health of the Location
- Infrastructure and Amenities in the Location
- Scope of Marketability in the Location
- Demographics of the Location
- Future Prospects of the Location
            
Considering all these factors, here are the Top 5 districts to buy commercial properties in Telangana:
''')

image_urls = [
    "s1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown("""
1. Hyderabad
2. Rangareddy
3. Medchal-Malkajgiri
4. Sangareddy
5. Warangal and Hanumakonda""")

st.write("Hyderabad and surrounding districts take the top four positions as they are already in the midst of development with more stamp registrations, vehicle purchases, and investments in various sectors. As for Warangal and Hanumakonda, recent investments suggest good future prospects for commercial property investments.")
st.markdown(''' Please refer to the following answers for justification:
1. <a href="#question-1-revenue-variation-across-districts">Primary Question -> Question 1</a>
2. <a href="#question-4-categorization-of-districts-based-on-revenue-generation">Primary Question -> Question 4</a>
3. <a href="#question-6-distribution-of-vehicles-by-vehicle-class-across-districts">Primary Question -> Question 6</a>
4. <a href="#question-9-top-3-districts-attracting-significant-sector-investments-fy-2019-2022">Primary Question -> Question 9</a>
5. <a href="#question-10-relationship-between-district-investments-vehicle-sales-and-stamps-revenue-fy-2021-22">Primary Question -> Question 10</a>
    
''', unsafe_allow_html=True)

st.header("Question 2: Notable Policies of The Telangana Government")
st.write("Over the last 9 years, The Telangana Government has introduced a lot of policies to improve the economy and growth of the state. Below are some of the notable initiatives taken by the government:")
st.markdown(''' 
1. <strong>Telangana Gruha Lakshmi Scheme</strong>
2. <strong>Residence Certificate Scheme</strong>
3. <strong>Double Bedroom or 2BHK Housing Policy</strong>
4. <strong>Driver Empowerment Program</strong>
5. <strong>Grama Jyothi Scheme</strong>
6. <strong>Mana ooru - Mana badi</strong>
7. <strong>T-Hub</strong>
8. <strong>Dalit Bandhu</strong>
9. <strong>TASK and SoFTNET</strong>
10. <strong>TS-iPass</strong>    
''', unsafe_allow_html=True)
st.write("The above schemes have helped the government incentivize growth, and The Telangana Government should accelerate these schemes even further. Please check the [Suggestions](#usg) for more information.")

st.markdown('''
<p id="usg" style="font-size: 50px; font-weight: bold; text-align: center; text-decoration: underline;">Suggestions and Recommendations</p>
''', unsafe_allow_html=True)

st.markdown('''
- <strong>Investigate the Absence of Stamp Registration Records in Jayshankar Bhupalapally District:</strong>

    Explore the reasons for the lack of stamp registration records in the district and investigate what is preventing people from purchasing properties in the area. Consider potential factors such as infrastructure issues (e.g., problems with State Highways), resource constraints (financial and logistical), and data collection errors. Conduct a comprehensive analysis to identify the root causes and potential solutions for this issue.
- <strong>Investigate the Absence of Vehicle Sales Data in Narayanpet, Mulugu, and Hanumakonda Districts:</strong>

    Examine the underlying causes for the absence of vehicle sales data in these districts and investigate potential barriers preventing people from purchasing vehicles in these areas. Explore factors such as infrastructure limitations, economic constraints, and data collection discrepancies. Conduct a thorough analysis to identify the root causes and recommend solutions to address this issue, ensuring a comprehensive understanding of the situation.
''', unsafe_allow_html=True)
image_urls = [
    "r1.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown('''
- <strong>Promote Industrial Growth in Low-Concentration Districts:</strong>

    In districts like Adilabad, Kumurabheem Asifabad, Mulugu, Wanapathy, Bhadadri Kothagudem, with limited investments through TS-iPass in FY2021, implement a two-step approach:

    - First, assess infrastructure sufficiency and skilled labor availability. If both checks pass positively, incentivize and subsidize industries to establish themselves in these districts.
    - In cases of infrastructure insufficiency, invest in infrastructure development or review the implementation of the Grama Jyoti Scheme in district villages.
    If a skilled labor force is lacking, expand policies like "Mana Ooru - Mana Badi," TASK, and SoFTNET to enhance workforce skills and capabilities.

<br>''', unsafe_allow_html=True)
image_urls = [
    "r2.png",
    "p6/telen.png"
]
images_per_row = 2
for i in range(0, len(image_urls), images_per_row):
    columns = st.columns(images_per_row)

    for j in range(i, min(i + images_per_row, len(image_urls))):
        with columns[j - i]:
            st.image(image_urls[j], use_column_width=True)
st.markdown('''
- **Industry Sector Investments and Environmental Caution:**

            
    Based on the FY2021 data analysis, it's evident that sectors like Pharmaceuticals and Chemicals, Plastics and Rubber, and Beverages have made significant investments in multiple districts. It is essential to exercise caution with these sectors:
    - Pharmaceuticals and Chemicals, Plastics and Rubber:
        - Be vigilant about the potential environmental impact, as raw waste from these industries can harm the environment.
        - Ensure strict adherence to environmental guidelines by industries in these sectors.
    - Beverages Sector:
        - Monitor waste disposal practices to ensure proper waste management.
        - Keep a close watch on water consumption by beverage industries.
        - Prioritize water allocation for agricultural purposes to support local farmers.

            <br>
- **Addressing the Rapid Growth Discrepancy:**
    
    - Hyderabad and its neighboring districts have exhibited remarkable growth, consistently ranking among the top 10, often within the top 5 in various analyses. While this positions Hyderabad as a formidable contender in India's startup ecosystem, we must act promptly to prevent a scenario similar to Karnataka, where northern districts lagged behind Bangalore's progress.
    
    - To tackle this situation and promote equitable development, we can expedite the implementation of policies such as T-Hub. By providing incentives and subsidies to startup founders who choose to establish their startups in low-investment districts, we can encourage balanced growth across the region.            
- **Enhancing the TASK Scheme through Collaborations:**
    
    To enhance the effectiveness of the TASK scheme, the government has the opportunity to establish Memorandums of Understanding (MoUs) with organizations like Zoho. Zoho, with its specialized division, Zoho Schools, is committed to delivering high-quality programming training and facilitating the employment of candidates after assessment.
            ''', unsafe_allow_html=True)

st.markdown('''
<p id="usg" style="font-size: 50px; font-weight: bold; text-align: center; text-decoration: underline;">Thank you</p>
''', unsafe_allow_html=True)

