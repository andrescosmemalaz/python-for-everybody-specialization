
# coding: utf-8

# # Practice notebook for confidence intervals using NHANES data
# 
# This notebook will give you the opportunity to practice working with confidence intervals using the NHANES data.
# 
# You can enter your code into the cells that say "enter your code here", and you can type responses to the questions into the cells that say "Type Markdown and Latex".
# 
# Note that most of the code that you will need to write below is very similar to code that appears in the case study notebook.  You will need to edit code from that notebook in small ways to adapt it to the prompts below.
# 
# To get started, we will use the same module imports and read the data in the same way as we did in the case study:

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_confint

da = pd.read_csv("nhanes_2015_2016.csv")


# ## Question 1
# 
# Restrict the sample to women between 35 and 50, then use the marital status variable [DMDMARTL](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDMARTL) to partition this sample into two groups - women who are currently married, and women who are not currently married.  Within each of these groups, calculate the proportion of women who have completed college.  Calculate 95% confidence intervals for each of these proportions.

# In[4]:


# enter your code here
da_female_35_50=da[(da['RIAGENDR']==2)&(da['RIDAGEYR']>=35)&(da['RIDAGEYR']<=50)]
da_female_35_50.reset_index(inplace=True, drop=True)


# In[5]:


da_female_35_50_married=da_female_35_50[da_female_35_50['DMDMARTL']==1]
da_female_35_50_not_married=da_female_35_50[da_female_35_50['DMDMARTL'].isin([2,3,4,5,6])]
da_female_35_50_married.reset_index(inplace=True, drop=True)
da_female_35_50_not_married.reset_index(inplace=True, drop=True)


# In[6]:


proportion_married=sum(da_female_35_50_married['DMDEDUC2']==5)/len(da_female_35_50_married)


# In[7]:


proportion_married


# In[8]:


se_married=proportion_married*(1-proportion_married)


# In[9]:


se_married


# In[11]:


n_married=len(da_female_35_50_married['DMDEDUC2'])


# In[12]:


n_married


# In[13]:


print('Lower Boundary: ', proportion_married-1.96*np.sqrt((se_married/n_married)))
print('Upper Boundary: ', proportion_married+1.96*np.sqrt((se_married/n_married)))


# In[14]:


ci_low, ci_upp = proportion_confint(162, 449, alpha=0.05, method='normal')


# In[15]:


ci_low, ci_upp


# In[16]:


ci_upp-ci_low


# In[17]:


proportion_not_married=sum(da_female_35_50_not_married['DMDEDUC2']==5)/len(da_female_35_50_not_married)


# In[18]:


proportion_not_married


# In[19]:


se_not_married=proportion_not_married*(1-proportion_not_married)


# In[20]:


se_not_married


# In[21]:


n_not_married=len(da_female_35_50_not_married['DMDEDUC2'])


# In[22]:


n_not_married


# In[23]:


print('Lower Boundary: ', proportion_not_married-1.96*np.sqrt((se_not_married/n_not_married)))
print('Upper Boundary: ', proportion_not_married+1.96*np.sqrt((se_not_married/n_not_married)))


# In[24]:


ci_low, ci_upp = proportion_confint(72, 338, alpha=0.05, method='normal')


# In[25]:


ci_low, ci_upp


# In[26]:


ci_upp-ci_low


# __Q1a.__ Identify which of the two confidence intervals is wider, and explain why this is the case. 

# __Q1b.__ Write 1-2 sentences summarizing these findings for an audience that does not know what a confidence interval is (the goal here is to report the substance of what you learned about how marital status and educational attainment are related, not to teach a person what a confidence interval is).

# ## Question 2
# 
# Construct a 95% confidence interval for the proportion of smokers who are female. Construct a 95% confidence interval for the proportion of smokers who are male. Construct a 95% confidence interval for the **difference** between those two gender proportions.

# In[28]:


# enter your code here
da_smokers=da[da['SMQ020']==1]
da_smokers.reset_index(inplace=True, drop=True)
smokers_gender=da_smokers['RIAGENDR']
smokers_gender=smokers_gender[~smokers_gender.isna()]
smokers_gender.reset_index(inplace=True, drop=True)
n_smokers=len(smokers_gender)
n_smokers
n_smokers_gender_male=sum(smokers_gender==1)
n_smokers_gender_male
n_smokers_gender_female=sum(smokers_gender==2)
n_smokers_gender_female
proportion_smokers_gender_male=(n_smokers_gender_male/n_smokers)
proportion_smokers_gender_male
proportion_smokers_gender_female=(n_smokers_gender_female/n_smokers)
proportion_smokers_gender_female


# In[29]:


se_smokers_gender_male=np.sqrt((proportion_smokers_gender_male*(1-proportion_smokers_gender_male))/n_smokers_gender_male)
se_smokers_gender_male


# In[30]:


se_smokers_gender_female=np.sqrt((proportion_smokers_gender_female*(1-proportion_smokers_gender_female))/n_smokers_gender_female)
se_smokers_gender_female


# In[31]:


print('Lower Boundary Male: ', proportion_smokers_gender_male-1.96*se_smokers_gender_male)
print('Upper Boundary Male: ', proportion_smokers_gender_male+1.96*se_smokers_gender_male)


# In[32]:


ci_low, ci_upp = proportion_confint(n_smokers_gender_male, n_smokers, alpha=0.05, method='normal')
ci_low, ci_upp


# In[33]:


0.6347544952210894-0.5838742240544604


# In[34]:


ci_low, ci_upp = proportion_confint(n_smokers_gender_female, n_smokers, alpha=0.05, method='normal')
ci_low, ci_upp


# In[35]:


print('Lower Boundary Female: ', proportion_smokers_gender_female-1.96*se_smokers_gender_female)
print('Upper Boundary Female: ', proportion_smokers_gender_female+1.96*se_smokers_gender_female)


# In[36]:


0.4224563125599452-0.35891496816450497


# In[37]:


proportion_smokers_gender_diff=proportion_smokers_gender_male-proportion_smokers_gender_female
proportion_smokers_gender_diff


# In[38]:



se_proportion_smokers_diff=np.sqrt((se_smokers_gender_male**2)+(se_smokers_gender_female**2))


# In[39]:


print('Lower Boundary Gender Difference: ', proportion_smokers_gender_diff-1.96*se_proportion_smokers_diff)
print('Upper Boundary Gender Difference: ', proportion_smokers_gender_diff+1.96*se_proportion_smokers_diff)


# In[40]:


0.2593297771290309-0.17792766142206878


# __Q2a.__ Why might it be relevant to report the separate gender proportions **and** the difference between the gender proportions?

# __Q2b.__ How does the **width** of the confidence interval for the difference between the gender proportions compare to the widths of the confidence intervals for the separate gender proportions?

# ## Question 3
# 
# Construct a 95% interval for height ([BMXHT](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXHT)) in centimeters.  Then convert height from centimeters to inches by dividing by 2.54, and construct a 95% confidence interval for height in inches.  Finally, convert the endpoints (the lower and upper confidence limits) of the confidence interval from inches to back to centimeters   

# In[42]:


# enter your code here
height_values_cm=da['BMXHT']


# In[43]:


height_values_cm=height_values_cm[~height_values_cm.isna()]
height_values_cm.reset_index(inplace=True, drop=True)


# In[44]:


np.mean(height_values_cm)


# In[45]:


height_values_inches=height_values_cm/2.54


# In[46]:


height_values_inches=height_values_inches[~height_values_inches.isna()]
height_values_inches.reset_index(inplace=True, drop=True)


# In[47]:


np.mean(height_values_inches)


# In[48]:


n_height_values_inches=len(height_values_inches)
n_height_values_inches


# In[49]:


std_height_values_inches=np.std(height_values_inches)
std_height_values_inches


# In[50]:


print('Lower Boundary Inches: ', np.mean(height_values_inches)-1.96*(std_height_values_inches/np.sqrt(n_height_values_inches)))
print('Upper Boundary Inches: ', np.mean(height_values_inches)+1.96*(std_height_values_inches/np.sqrt(n_height_values_inches)))


# In[51]:


sm.stats.DescrStatsW(height_values_inches).tconfint_mean()


# In[52]:


print('Lower Boundary cm: ', (np.mean(height_values_inches)-1.96*(std_height_values_inches/np.sqrt(n_height_values_inches)))*2.54)
print('Upper Boundary cm: ', (np.mean(height_values_inches)+1.96*(std_height_values_inches/np.sqrt(n_height_values_inches)))*2.54)


# __Q3a.__ Describe how the confidence interval constructed in centimeters relates to the confidence interval constructed in inches.

# ## Question 4
# 
# Partition the sample based on 10-year age bands, i.e. the resulting groups will consist of people with ages from 18-28, 29-38, etc. Construct 95% confidence intervals for the difference between the mean BMI for females and for males within each age band.

# In[53]:


# enter your code here

for val in [[18, 28], [29, 38], [39, 48], [49, 58], [59, 68], [69, 78], [79, 88]]:
    da_year_band=da[(da['RIDAGEYR']>=val[0])&(da['RIDAGEYR']<=val[1])]
    da_year_band.reset_index(inplace=True, drop=True)
    
    bmi_males=da_year_band[da_year_band['RIAGENDR']==1]['BMXBMI']
    bmi_females=da_year_band[da_year_band['RIAGENDR']==2]['BMXBMI']
    
    bmi_males=bmi_males[~bmi_males.isna()]
    bmi_males.reset_index(inplace=True, drop=True)
    bmi_females=bmi_females[~bmi_females.isna()]
    bmi_females.reset_index(inplace=True, drop=True)
    
    print("Std Males: ", np.std(bmi_males))
    print("Std Females: ", np.std(bmi_females))
    print("Variance Ratio: ", (np.std(bmi_males)**2)/(np.std(bmi_females)**2))
    print("_________________________________________________________")


# In[55]:


for val in [[18, 28], [29, 38], [39, 48], [49, 58], [59, 68], [69, 78], [79, 88]]:
    da_year_band=da[(da['RIDAGEYR']>=val[0])&(da['RIDAGEYR']<=val[1])]
    da_year_band.reset_index(inplace=True, drop=True)
    
    bmi_males=da_year_band[da_year_band['RIAGENDR']==1]['BMXBMI']
    bmi_females=da_year_band[da_year_band['RIAGENDR']==2]['BMXBMI']
    
    bmi_males=bmi_males[~bmi_males.isna()]
    bmi_males.reset_index(inplace=True, drop=True)
    bmi_females=bmi_females[~bmi_females.isna()]
    bmi_females.reset_index(inplace=True, drop=True)
    
    bmi_males_temp=sm.stats.DescrStatsW(bmi_males)
    bmi_females_temp=sm.stats.DescrStatsW(bmi_females)
    
    cm = sm.stats.CompareMeans(bmi_males_temp, bmi_females_temp)
    lower, upper=cm.tconfint_diff(usevar='pooled')
    print(val)
    print("pooled: ", lower, ",", upper)
    print("pooled diff: ", abs(upper)-abs(lower))
    print('--------------------------------------------------------------------------')


# __Q4a.__ How do the widths of these confidence intervals differ?  Provide an explanation for any substantial diferences in the confidence interval widths that you see.

# ## Question 5
# 
# Construct a 95% confidence interval for the first and second systolic blood pressure measures, and for the difference between the first and second systolic blood pressure measurements within a subject.

# In[56]:


# enter code here
first_sbp=da['BPXSY1']
second_sbp=da['BPXSY2']
sbp_diff=first_sbp-second_sbp

first_sbp=first_sbp[~first_sbp.isna()]
first_sbp.reset_index(inplace=True, drop=True)
second_sbp=second_sbp[~second_sbp.isna()]
second_sbp.reset_index(inplace=True, drop=True)
sbp_diff=sbp_diff[~sbp_diff.isna()]
sbp_diff.reset_index(inplace=True, drop=True)


# In[57]:


lower, upper=sm.stats.DescrStatsW(first_sbp).tconfint_mean()
print(lower, ",", upper)
print(abs(upper)-abs(lower))


# In[58]:


lower, upper=sm.stats.DescrStatsW(second_sbp).tconfint_mean()
print(lower, ",", upper)
print(abs(upper)-abs(lower))


# In[59]:


lower, upper=sm.stats.DescrStatsW(sbp_diff).tconfint_mean()
print(lower, ",", upper)
print(abs(upper)-abs(lower))


# __Q5a.__ Based on these confidence intervals, would you say that a difference of zero between the population mean values of the first and second systolic blood pressure measures is consistent with the data?

# __Q5b.__ Discuss how the width of the confidence interval for the within-subject difference compares to the widths of the confidence intervals for the first and second measures.

# ## Question 6
# 
# Construct a 95% confidence interval for the mean difference between the average age of a smoker, and the average age of a non-smoker.

# In[60]:


# insert your code here

smokers_age=da[da['SMQ020']==1]['RIDAGEYR']
smokers_age=smokers_age[~smokers_age.isna()]
smokers_age.reset_index(inplace=True, drop=True)
non_smokers_age=da[da['SMQ020']!=1]['RIDAGEYR']
non_smokers_age=non_smokers_age[~non_smokers_age.isna()]
non_smokers_age.reset_index(inplace=True, drop=True)


# In[61]:


smokers_age_temp=sm.stats.DescrStatsW(smokers_age)
non_smokers_age_temp=sm.stats.DescrStatsW(non_smokers_age)

cm = sm.stats.CompareMeans(smokers_age_temp, non_smokers_age_temp)
lower, upper=cm.tconfint_diff(usevar='pooled')
print("pooled: ", lower, ",", upper)


# __Q6a.__ Use graphical and numerical techniques to compare the variation in the ages of smokers to the variation in the ages of non-smokers.  

# In[62]:


# insert your code here
smokers_age.describe()


# In[63]:


non_smokers_age.describe()


# In[64]:


sns.boxplot(smokers_age)


# In[65]:


sns.boxplot(non_smokers_age)


# In[ ]:


get_ipython().set_next_input('__Q6b.__ Does it appear that uncertainty about the mean age of smokers, or uncertainty about the mean age of non-smokers contributed more to the uncertainty for the mean difference that we are focusing on here');get_ipython().run_line_magic('pinfo', 'here')

