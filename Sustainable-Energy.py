import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
Energy_data = pd.read_csv("Energy_data.csv")
#TiTle
st.title("☀️Sustainable-Energy☀️")
# Use a radio button 
menu = st.radio("Navigation", ["Project Objectives and Methodology", "Overview", "Features", "Analysis", "Conclusion"], index=0, horizontal=True)

# Home Page
if menu == "Project Objectives and Methodology":
    st.image("Energy.webp",width = 800)
    st.subheader("Project Objective and Methodology")
    # Project Objectives
    st.markdown("### Project Objectives")
    st.markdown("""
    This project aims to analyze global trends in sustainable energy with a specific focus on the following key areas:
    
    #### Access to Electricity:
    - Evaluate disparities in electricity access across regions and identify trends over time.
    - Understand the relationship between access to electricity, economic development, and geographic factors.
    
    #### Renewable Energy Adoption:
    - Assess the share of renewable energy in total energy consumption.
    - Explore factors influencing renewable energy adoption, including economic, geographic, and policy-related drivers.
    
    #### CO2 Emissions:
    - Identify countries with the highest and lowest CO2 emissions.
    - Investigate how renewable energy and economic growth impact emission trends.
    - Highlight countries that have successfully reduced their emissions over time.
    """)
    
    # Methodology
    st.markdown("### Methodology")
    st.markdown("""
    #### Data Preprocessing:
    - **Missing Values Handling**:
      - Missing values for key variables like population, energy consumption, and renewable energy share were calculated using derived formulas and external data sources.
      - Key metrics like population were estimated using relationships such as \( P = D \\times Area \) (where \( D \) is density).
    - **Column Renaming**:
      - Simplified column names for clarity and consistency during analysis.
    
    #### Outlier Detection:
    - Anomalies in metrics such as CO2 emissions, renewable energy share, and GDP per capita were identified and addressed to ensure robust insights.
    - Visual tools like scatter plots and descriptive statistics were employed for outlier analysis.
    
    #### Feature Engineering:
    - **Energy Metrics**:
      - Calculated metrics such as primary energy consumption per capita, renewable energy share in total energy, and low-carbon electricity percentages.
    - **Geographic Analysis**:
      - Incorporated variables like land area, population density, latitude, and longitude to analyze geographic influences on energy trends.
    
    #### Data Visualization and Analysis:
    - **Interactive Visualizations**:
      - Used Plotly for dynamic plots (e.g., choropleth maps and scatter plots) to explore global energy patterns.
    - **Time-Series Analysis**:
      - Tracked changes in key metrics like electricity access and renewable energy adoption over decades.
    - **Correlation Analysis**:
      - Examined relationships between energy metrics (e.g., access to electricity, GDP, and emissions) to uncover key insights.
    """)

# Overview
elif menu == "Overview":
    st.header("Dataset Overview")
    st.dataframe(Energy_data.head(10))
    st.write(f"**Shape of the dataset:** {Energy_data.shape[0]} rows, {Energy_data.shape[1]} columns")
    st.write("### Summary Statistics")
    st.write(Energy_data.describe())

# Features description  
elif menu == "Features":
    st.title("Features Description")

    with st.expander("Access to clean fuels for cooking (% of population)"):
        st.write("""
        This shows the percentage of the population using clean fuels for cooking. 
        It's essential for understanding public health and energy access.
        """)

    with st.expander("Renewable electricity generating capacity per capita"):
        st.write("""
        This indicates the renewable energy capacity per person, providing insight 
        into how much renewable energy infrastructure is available relative to the population.
        """)

    with st.expander("Financial flows to developing countries (US $)"):
        st.write("""
        This represents aid from developed countries for clean energy projects, 
        useful for understanding global financial support for sustainable energy.
        """)

    with st.expander("Renewable energy share in total final energy consumption (%)"):
        st.write("""
        This gives the proportion of total energy consumption coming from renewable sources, 
        which is essential for tracking sustainability progress.
        """)

    with st.expander("Electricity from fossil fuels (TWh)"):
        st.write("""
        The amount of electricity generated from fossil fuels, which can be compared 
        to the electricity from renewables to assess the country's carbon footprint.
        """)

    with st.expander("Electricity from nuclear (TWh)"):
        st.write("""
        The share of nuclear power in the electricity mix, providing insight into 
        the country’s reliance on non-renewable low-carbon energy sources.
        """)

    with st.expander("Electricity from renewables (TWh)"):
        st.write("""
        The amount of electricity generated from renewable sources, 
        which helps track the growth of renewable energy adoption.
        """)

    with st.expander("Low-carbon electricity (% electricity)"):
        st.write("""
        Percentage of electricity generated from low-carbon sources (nuclear + renewables). 
        This is critical for understanding the country's progress in decarbonizing its electricity generation.
        """)

    with st.expander("Primary energy consumption per capita (kWh/person)"):
        st.write("""
        Tracks energy consumption per person. This is helpful for assessing 
        energy demand in relation to population size.
        """)

    with st.expander("Energy intensity level of primary energy (MJ/$2011 PPP GDP)"):
        st.write("""
        Measures how much energy is used per unit of GDP, which is a useful indicator of energy efficiency.
        """)

    with st.expander("Value CO2 emissions (metric tons per capita)"):
        st.write("""
        Carbon dioxide emissions per person, which is key for evaluating the 
        environmental impact of a country's energy consumption.
        """)

    with st.expander("Renewables (% equivalent primary energy)"):
        st.write("""
        The percentage of primary energy derived from renewable sources, 
        which can be used to assess the country’s commitment to clean energy.
        """)

    with st.expander("GDP growth (annual %)"):
        st.write("""
        The annual growth rate of the GDP, useful for understanding economic 
        performance and its correlation with energy consumption.
        """)

    with st.expander("GDP per capita"):
        st.write("""
        The economic output per person, which is helpful for understanding the 
        relationship between energy consumption and economic activity.
        """)

    with st.expander("Density (P/Km2)"):
        st.write("""
        The population density, which can be important for understanding 
        the energy infrastructure needs.
        """)

    with st.expander("Land Area (Km2)"):
        st.write("""
        The total land area, which is useful for spatial planning and understanding 
        energy distribution across larger areas.
        """)

    with st.expander("Latitude and Longitude"):
        st.write("""
        These geographic coordinates are important for spatial analysis, 
        particularly when studying the potential for solar or wind energy in different regions.
        """)

# Analysis
elif menu == "Analysis":
    st.title("Analysis")
    st.subheader("📈Category")
    tab1, tab2, tab3, tab4,tab5 = st.tabs(["GDP Analysis (2020)",
                                      "Electricity Access",
                                      "Regional Insights",
                                      "Low CO2 Emitters",
                                           "Entities have reduced CO2 emissions over time"])



 #################GDP Analysis (2020)######################
    with tab1:
        Tab1,Tab2,Tab3,Tab4=st.tabs(["countries with Highst GDP in the year 2020",
                          "countries with Lowest GDP in the year 2020",
                                     "Lowest 3 Countries performance since 2000",
                                     "Highest 3 Countries performance since 2000"])
        with Tab1:
            #Show 10 countries with higher GDP in the year 2020
            higher_gdp_countries_in_2020 = Energy_data[Energy_data['Year'] == 2020].sort_values(by='gdp_per_capita',
                                                                                    ascending = False)[['Year',
                                                                                                        'Entity',
                                                                                                        'gdp_per_capita']][0:10]
            st.dataframe(higher_gdp_countries_in_2020)
            plt.figure(figsize=(14, 5))
            sns.barplot(x='Entity', y='gdp_per_capita', data=higher_gdp_countries_in_2020)
            plt.xlabel("Country name")
            plt.ylabel("GDP per Capita ($)")
            plt.title("Ten countries with highest GDP in the year 2020")
            st.pyplot(plt)
        with Tab2:
            #Show 10 countries with lowest GDP in the year 2020
            lowest_gdp_countries_in_2020 = Energy_data[Energy_data['Year'] == 2020].sort_values(by='gdp_per_capita', ascending = True)[['Year', 'Entity', 'gdp_per_capita']][0:10]
            st.dataframe(lowest_gdp_countries_in_2020)
            Lowest= px.bar(lowest_gdp_countries_in_2020,
                           x='gdp_per_capita',
                           y='Entity',
                           title='Ten Countries with the Lowest GDP in the Year 2020', height= 500, width=600,
                           labels={'gdp_per_capita': 'GDP per Capita ($)', 'Entity': 'Country Name'})
            st.plotly_chart(Lowest, use_container_width=True)

        with Tab3:
            lowest_gdp_countries=lowest_gdp_countries_in_2020["Entity"].unique()# Creating list for the lowest Coungtry for plotting
            lowest_gdp_countries_list = lowest_gdp_countries.tolist()
            Country_lowest_gdp = Energy_data[Energy_data['Entity'].isin(lowest_gdp_countries_list[0:3])][['Year', 'Entity', 'gdp_per_capita']]
            fig=px.line(Country_lowest_gdp,
                    x='Year',
                    y='gdp_per_capita',
                    color='Entity',
                    title='lowest 3 GDP per Capita Over Time',
                    labels={'Year': 'Year', 'gdp_per_capita': 'lowest 3 GDP per Capita ($)'})
            st.plotly_chart(fig, use_container_width=True)
        with Tab4:
            highest_gdp_countries=higher_gdp_countries_in_2020["Entity"].unique().tolist()
            Country_highest_gdp = Energy_data[Energy_data['Entity'].isin(highest_gdp_countries[0:3])][['Year', 'Entity', 'gdp_per_capita']]
            fig=px.line(
                    Country_highest_gdp, 
                    x='Year',
                    y='gdp_per_capita',
                    color='Entity', 
                    title='Highest 3 GDP per Capita Over Time', 
                    labels={'Year': 'Year', 'gdp_per_capita': 'Highest 3 GDP per Capita ($)'})
            st.plotly_chart(fig, use_container_width=True)




    ####################"Electricity Access"###################################
    with tab2:
        menu = st.radio("Display", ["data for Year 2020",
                                    "Features correlations",
                                    "Graphs",
                                    "Trends in Electricity Access and Renewable Energy Adoption by Entity",
                                    "Summary"], index=0, horizontal=True)
        
        if menu == "data for Year 2020":
            st.subheader("Entities with lowest access to electricity")
            # Filter the data for Year 2020
            lowest_access_2020 = Energy_data[Energy_data['Year'] == 2020]
            lowest_access_2020 = lowest_access_2020.sort_values(by='Access to electricity (% of population)').drop_duplicates(subset='Entity').head(10)
            main_characteristics =["Entity","Year",
                                   "Access to electricity (% of population)",
                                   "gdp_per_capita",
                                   "Land Area(Km2)",
                                   "Population"]
            lowest_access_df=lowest_access_2020[main_characteristics]
            st.dataframe(lowest_access_df)

            st.subheader("Entities with highest access to electricity")
            st.write("Random Samples")
            Highest_access_2020 = Energy_data[Energy_data['Year'] == 2020]
            Highest_access_2020 = Highest_access_2020.sort_values(by='Access to electricity (% of population)').drop_duplicates(subset='Entity').tail(20)
            Highest_access_df=Highest_access_2020[main_characteristics]
            st.dataframe(Highest_access_df)

        if menu == "Features correlations":
            corr1 = Energy_data[['Access to electricity (% of population)',
                                      'gdp_per_capita',
                                      'Land Area(Km2)',
                                      'Population']].corr()
            
            characteristics_fig= px.imshow(
                corr1,
                text_auto=True,
                title="Access to electricity Correlation Heatmap"
            )
            characteristics_fig.update_layout(width=1000, height=600)
            st.plotly_chart(characteristics_fig, use_container_width=True)

        if menu == "Graphs":
            st.subheader("Entities with lowest access to electricity 2020")
            lowest_access_2020 = Energy_data[Energy_data['Year'] == 2020]
            lowest_access_2020 = lowest_access_2020.sort_values(by='Access to electricity (% of population)').drop_duplicates(subset='Entity').head(10)
            main_characteristics =["Entity","Year",
                                   "Access to electricity (% of population)",
                                   "gdp_per_capita",
                                   "Land Area(Km2)",
                                   "Population"]
            lowest_access_df=lowest_access_2020[main_characteristics]
            fig_scatter = px.scatter(lowest_access_df, x='Access to electricity (% of population)',
                         y='gdp_per_capita',
                         title='Access to Electricity vs GDP per Capita',
                        width=600,height=600)
            fig_scatter_l, ax=plt.subplots()
            sns.scatterplot(x='Population',
                            y='gdp_per_capita',
                            data=lowest_access_df,
                            hue='Access to electricity (% of population)',
                           ax=ax)
            plt.title("Lowest Countries access to electricty : Gdp vs Population")
            st.plotly_chart(fig_scatter, use_container_width=True)
            st.pyplot(fig_scatter_l)

            st.subheader("Entities with highest access to electricity 2020")
            st.write("Random Samples")
            Highest_access_2020 = Energy_data[Energy_data['Year'] == 2020]
            Highest_access_2020 = Highest_access_2020.sort_values(by='Access to electricity (% of population)').drop_duplicates(subset='Entity').tail(20)
            Highest_access_df=Highest_access_2020[main_characteristics]
            fig_scatter1 = px.scatter(Highest_access_df, x='Access to electricity (% of population)',
                         y='gdp_per_capita',
                         title='Access to Electricity vs GDP per Capita',
                        width=600,height=600)
            fig_scatter1_h,ax=plt.subplots()
            sns.scatterplot(x='Population',
                            y='gdp_per_capita',
                            data=Highest_access_df,
                            hue='Access to electricity (% of population)',ax=ax)
            plt.title("highest Countries access to electricty : Gdp vs Population")
            st.plotly_chart(fig_scatter1, use_container_width=True)
            st.pyplot(fig_scatter1_h)
        if menu == "Trends in Electricity Access and Renewable Energy Adoption by Entity":
            Afga_Egypt_df = Energy_data[["Entity", "Year", "Access to electricity (% of population)",
                                         "Renewable energy share in the total final energy consumption (%)"]]
    
            # Create a list of unique country names for the dropdown
            country_list = Afga_Egypt_df['Entity'].unique().tolist()
            
            # Add a select box for the user to choose a country
            selected_country = st.selectbox("Select a Country", options=country_list)
            
            # Filter the data based on the selected country
            Afga_df = Afga_Egypt_df[Afga_Egypt_df['Entity'] == selected_country]
            evolved_fig = px.line(Afga_df,
                                  x='Year',
                                  y=['Access to electricity (% of population)',"Renewable energy share in the total final energy consumption (%)"],
                                  labels={'value': 'Percent', 'variable': 'Data'},
                                  title="Evolution of Electricity Access, Renewable Energy over time")
            st.plotly_chart(evolved_fig, use_container_width=True)
            
            

        if menu =="Summary":
            
            st.subheader("Summary of Results")
            st.markdown("### Lowest Entities have Access to Electricity")
            st.markdown("""
            - **Entities with the lowest access to electricity** in 2020 show:
                - Countries in this group tend to have access rates below 30%, indicating significant energy poverty.
                - A positive relationship between GDP per capita and access to electricity: Countries with higher GDP per capita tend to have better electricity access.
                - Population and GDP per capita do not show a clear pattern. Even populous countries can have low GDP and limited electricity access.
                
            """)
            st.markdown("### Highest Entities have Access to Electricity")
            st.markdown("""
            - **Entities with the highest access to electricity** in 2020 show:
                - Near universal access to electricity (>90% of the population), indicating well-developed infrastructure.
                - A positive relationship between GDP per capita and electricity access, although less pronounced than in the lowest-access group (likely due to saturation in electricity access).
                - Populous countries with high GDP tend to have near-complete access to electricity.
            """)

            
####################"Regional Insights"################################           
    with tab3:
        TAB1,TAB2,TAB3=st.tabs(["Renewable Energy Share by Country Over years",
                                    "Geographic Influence on Energy Access,Renewable Adoption,CO2 Emissions",
                                    "GDP vs. Primary Energy Consumption Per Capita"])
        with TAB1:
            
            map_fig = px.choropleth(Energy_data, 
                        locations='Entity', 
                        locationmode='country names', 
                        color='Renewable energy share in the total final energy consumption (%)', 
                        hover_name='Entity', 
                        hover_data=['Year', 'Land Area(Km2)', 'Density','gdp_per_capita'],
                        title='Renewable Energy Share by Country Over Years',
                        animation_frame="Year")
            st.plotly_chart(map_fig, use_container_width=True)
    
        with TAB2:
            Geo_data = Energy_data[['Latitude', 'Longitude', 'Land Area(Km2)', 'Density', 
                         'Access to electricity (% of population)', 
                         'Renewable energy share in the total final energy consumption (%)', 
                         'Value_co2_emissions_kt_by_country']]
            Geo_data = Geo_data.sort_values(by = "Value_co2_emissions_kt_by_country").corr()
            st.subheader("Correlation Analysis")
            st.dataframe(Geo_data)
            st.subheader("Top Emitters")
            fig_Geo = px.scatter_geo(
                Energy_data.drop_duplicates("Entity",keep="last").sort_values(by= "Value_co2_emissions_kt_by_country").tail(10),
                lat='Latitude',
                lon='Longitude',
                size= 'Access to electricity (% of population)', 
                color='Value_co2_emissions_kt_by_country',
                color_continuous_scale='Inferno',  
                hover_name='Entity', 
                hover_data={'Land Area(Km2)','Density'},height=550,width=1100,
                title='CO2 Emissions by Country in 2020')
            st.plotly_chart(fig_Geo, use_container_width=True)
            
        with TAB3:
            fig_Geo1 = px.scatter_geo(
                Energy_data.drop_duplicates("Entity",keep="last").sort_values(by= "gdp_per_capita").tail(10),
                lat='Latitude',
                lon='Longitude',
                color='gdp_per_capita',
                size= 'Primary energy consumption per capita (kWh/person)',
                hover_name='Entity',
                hover_data={'Land Area(Km2)','Density'},height=550,width=1100,
                title='GDP and primary energy consumption per capita')
            st.plotly_chart(fig_Geo1, use_container_width=True)
          

####################"Low Emitters"################################ 
    with tab4:
        st.subheader("entities with top percentage of low-carbon electricity")
        correlation_matrix= Energy_data[["Entity","Year","Low-carbon electricity (% electricity)","gdp_per_capita"]]
        correlation_matrix=correlation_matrix.drop_duplicates("Entity",keep="last").sort_values(by=("Low-carbon electricity (% electricity)"),ascending= False)
        st.dataframe(correlation_matrix.head(10))
        
###############entities have reduced CO2 emissions over time##############################
    with tab5:
        agg_emissions = Energy_data.groupby('Entity').agg(
            emission_2000=('Value_co2_emissions_kt_by_country', 'first'),
            emission_2020=('Value_co2_emissions_kt_by_country', 'last'))

        #calcuting differnce
        agg_emissions['emission_difference'] = agg_emissions['emission_2000'] - agg_emissions['emission_2020']
        # Find entities where last emission is less than the first
        reduced_emissions = agg_emissions[agg_emissions['emission_2020'] < agg_emissions['emission_2000']]
        plot_data=reduced_emissions.sort_values("emission_difference",ascending=False)
        emissions_fig = px.bar(plot_data,
                       x=plot_data.index,
                       y="emission_difference",
                       labels=["Country","emission_difference(2000-2020)"],
                       title='Reduced CO₂ Emission Difference between 2000 and 2020 for Countries',
                       color="emission_difference",
                      height=600)
        st.plotly_chart(emissions_fig, useuse_container_width= False)
        
        
# Conclusion
elif menu == "Conclusion":
    st.write("""
    The analysis reveals significant global progress in access to electricity and clean cooking fuels, though disparities remain, particularly in developing regions such as Sub-Saharan Africa. Renewable energy adoption is positively correlated with GDP per capita, with wealthier nations leading in renewable energy shares due to greater financial capacity and supportive policies. However, outliers in low-GDP regions demonstrate that geographic advantages and innovative policies can also drive renewable energy adoption.
    """)
    
    # Key findings in bullet points
    st.subheader("Key Findings")
    st.markdown("""
    - **Access to Electricity**: Economically underdeveloped regions face the lowest access, while near-universal access is observed in high-GDP countries.
    - **Renewable Energy Adoption**: Geographic factors (e.g., land area, latitude) and economic priorities significantly influence renewable energy shares. Fossil fuels still dominate in many regions, but renewables are growing steadily.
    - **Carbon Emissions**: Countries with higher renewable energy use report lower CO₂ emissions, highlighting the environmental benefits of energy transition.
    - **Financial Flows**: Developing regions with energy access gaps receive the highest financial support for renewable energy development.
    - **Geographic Influences**: Large land areas and favorable latitudes enhance renewable energy potential, while high population density poses challenges.
    """)
    
    # Final summary
    st.subheader("Final Thoughts")
    st.write("""
    The transition to low-carbon energy systems is gaining momentum, particularly in Europe and parts of Asia, driven by technological advancements, cost reductions, and international agreements. However, achieving universal energy access and accelerating the global energy transition will require targeted investments, policy innovations, and efforts to address economic and geographic disparities. The success of renewable energy leaders like Norway and Iceland provides valuable insights for other nations aiming to achieve sustainable energy systems.
    """)
