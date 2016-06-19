import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import Vector_creator as Vc
import pickle
import time


df_object=pd.read_csv('train_dataset.csv',header=0)
#print(df_object.info())
#print("\nHeader:\n",df_object.head(5))
#print("\nTail\n",df_object.tail(5))
training_df=pd.DataFrame(columns=('len of url','no of dots','security sensitive words','no of hyphens in dom',\
'dir_len','no of subdir','domain len','domain token count','path token count','ip present','largest domain_tok_len',\
'avg_dom_token_len','largest path token length','avg path token length','suspicious tld','len_of_file','total dots in file',\
'total delims in file','len_of_argument','no_of_variables','len_of_largest_variable_val',\
'max_no_of_argum_delims'))

print('\n\n===========================================================')
print('Training classifier please wait')
print('===========================================================\n\n')
print('And we go.....3,2,1')
time.sleep(3)
for i in range(len(df_object['URL'])):
	print('-',end='')
	vec=Vc.Construct_Vector(df_object.URL[i])
	training_df.loc[i]=vec
#training_df['URL']=df_object['URL']
training_df['Lable']=df_object.Lable
training_df['URL']=df_object.URL
del(df_object)
	
print('all done feature values for training set obtained')
#print(training_df.info())
#print('\n\n\n',training_df.head(2))
#print(len_URL)	

sns.set_style("darkgrid")
color = sns.color_palette()[2]
"""sns.distplot(training_df[training_df['Lable']==0]['path token count'],color=color)
sns.plt.title('Path Token count Distribution(Benign URLs)')
plt.ylabel('Count')
sns.plt.show()
sns.jointplot(x='no of dots',y='no of hyphens in dom',data=training_df[training_df['Lable']==0])
sns.plt.title('Dots vs Domain Hyphens(Benign URLs)')
sns.jointplot(x='no of dots',y='no of hyphens in dom',data=training_df[training_df['Lable']==1],color=color)
sns.plt.title('Dots vs Domain Hyphens(Malicious URLs)')
sns.plt.show()"""

print('\n\n==========================================================')
print('\nStarting to dump Training Data')
print('==========================================================\n\n')
pickle.dump(training_df,open('Training_Data.pkl','wb'))
print('All Done')

#plt.scatter(training_df[ training_df['Lable']==1 ]['len of url'].values,training_df[ training_df['Lable']==1 ]['domain len'].values,marker='x')
#plt.show()