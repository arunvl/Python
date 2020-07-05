#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Genetic program


# In[ ]:


import random
import numpy as np
from numpy.random import choice
import pandas as pd
mutationRate = 0.05
totalPopulation = 10000
crossOver = 0.5
target = np.random.rand(8)*8
target =target.astype(np.uint8)
rand_list=[0,1,2,3,4,5,6,7]


# In[ ]:


populationData = []
fitnessData = []
secure_random = random.SystemRandom()
for outloop in range(totalPopulation):
  randomData = []
  fitnessScore = 0
  for inloop in range(len(target)):
    selectedData = secure_random.choice(rand_list)
   # print(selectedData)
    if (selectedData == target[inloop]):
      #print(target[inloop])
      fitnessScore = fitnessScore + 1
    randomData.append(selectedData)
  populationData.append(randomData)
  fitnessData.append(fitnessScore)


# In[ ]:


probabilityDist = []
for outloop in range(totalPopulation):
  probabilityDist.append(fitnessData[outloop]/len(target))


# In[ ]:


probDataFrame = pd.DataFrame({'List':populationData,'FitnessScore':fitnessData,'Probability':probabilityDist})
probDataFrame = probDataFrame.sort_values(['Probability'],ascending=False)
probDataFrame = probDataFrame.reset_index(drop=True)


# In[ ]:


selectedData


# In[ ]:


probDataFrame.head()


# In[ ]:


def maxProb(probabilityDist):
  probabilityList = [f for f in set(probabilityDist)]
  return (probabilityList[len(probabilityList)-2])


# In[ ]:


def getFitnessScore(data):
    fitnessScore = 0
    for inloop in range(len(target)):
      if (data[inloop] == target[inloop]):
        fitnessScore = fitnessScore + 1
    #fitnessScore=8
    return fitnessScore


# In[ ]:


crossOverPoint = int(crossOver*len(target))
generationCount = 1000


# In[ ]:


for loop in range(generationCount):
  draw=[]
  draw.append(probDataFrame[0:1]["List"].values[0])
  draw.append(probDataFrame[1:2]["List"].values[0])
#draw
  print('Fitness Scores of Parents ',getFitnessScore(draw[0]),getFitnessScore(draw[1]))


# In[ ]:


crossOverPoint = int(crossOver*len(target))
generationCount = 10000
for loop in range(generationCount):
  draw=[]
  draw.append(probDataFrame[0:1]["List"].values[0])
  draw.append(probDataFrame[1:2]["List"].values[0])
  #print('Fitness Scores of Parents ',getFitnessScore(draw[0]),getFitnessScore(draw[1]))
  if (getFitnessScore(draw[0])==len(target) | getFitnessScore(draw[1])==len(target)):
    #print(draw[0])
    #print(draw[1])
    break
  child1 = draw[0][0:crossOverPoint]+draw[1][crossOverPoint:]
  child2 = draw[1][0:crossOverPoint]+draw[0][crossOverPoint:]
  child1[random.randint(0,len(target)-1)] = secure_random.choice(rand_list)
  child2[random.randint(0,len(target)-1)] = secure_random.choice(rand_list)
  populationData.append(child1)
  populationData.append(child2)
  fitnessData = []
  totalPopulation = len(populationData)
  for outloop in range(totalPopulation):
    fitnessScore = getFitnessScore(populationData[outloop])
    fitnessData.append(fitnessScore)
    probabilityDist = []
  for outloop in range(totalPopulation):
    probabilityDist.append(fitnessData[outloop]/sum(fitnessData))
  probDataFrame = pd.DataFrame({'List':populationData,'FitnessScore':fitnessData,'Probability':probabilityDist})
  probDataFrame = probDataFrame.sort_values(['Probability'],ascending=False)
  probDataFrame = probDataFrame.reset_index(drop=True)
  if(probDataFrame["FitnessScore"].get()==8):
        print(child1,child2)
        print ('Average Fitness Score ',probDataFrame["FitnessScore"].mean())
  #print('Generation ',loop,' ',' Average Fitness Score ',probDataFrame["FitnessScore"].mean(),' ', ''.join(elem for elem in child1),' ',getFitnessScore(child1),''.join(elem for elem in child2),getFitnessScore(child2))
  #print('Generation ',loop,' ',' Average Fitness Score ',probDataFrame["FitnessScore"].mean())


# In[ ]:




