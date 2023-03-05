import numpy as np
import scipy.stats as st

# makg:JournalArticle
#data = [1000,1000,1000,1000,995,1000,1000,1000,997,1000,1000,996,1000,996,1000,999,997,1000,998,999]

#  makg http://purl.org/spar/fabio/PatentDocument
#data = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,999,1000,1000,1000,1000,1000,1000]

# datos.gob.es dcat:Distribution
#data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# datos.gob.es dcat:Dataset
data = [1000,1000,1000,999,998]



# confidence interval 95% 
print(st.t.interval(alpha = 0.95, df = len(data)-1, loc = np.mean(data), scale = st.sem(data)))




