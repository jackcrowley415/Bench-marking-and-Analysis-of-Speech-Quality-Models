import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

from .node import AQPNode

class BarchartperconditionNode(AQPNode):
    
    def __init__(self, id_: str, df_key: str, x_data_key: str, 
                 y_data_keys: list, titles: list, y_labels: list, **kwargs):
        super().__init__(id_)
        self.df_key = df_key
        self.x_data_key = x_data_key
        self.y_data_keys = y_data_keys
        self.titles = titles
        self.y_labels = y_labels
        self.type_ = "BarchartperconditionNode"
        
    def execute(self, result, **kwargs):
        super().execute(result, **kwargs)
        super().execute(result, **kwargs)
        ref_signal = result[self.ref_signal_key]
        TCDvoip = pd.read_csv("C:\\Users\\Jack Crowley\\AQP\\results\\TCDVoipData.csv")
        x = TCDvoip['Degradation'].to_list()
        deglist = []
        for i in x:
            if i not in deglist:
                deglist.append(i)
        del deglist[2]

        ECHO_df = TCDvoip[TCDvoip['Degradation'] == 'ECHO']
        CHOP_df = TCDvoip[TCDvoip['Degradation'] == 'CHOP']
        CLIP_df = TCDvoip[TCDvoip['Degradation'] == 'CLIP']
        COMPSPKR_df = TCDvoip[TCDvoip['Degradation'] == 'COMPSPKR']
        NOISE_df = TCDvoip[TCDvoip['Degradation'] == 'NOISE']

        ConditionECHO_df = ECHO_df.drop_duplicates(subset=['Condition'])
        ConditionCHOP_df = CHOP_df.drop_duplicates(subset=['Condition'])
        ConditionCLIP_df = CLIP_df.drop_duplicates(subset=['Condition'])
        ConditionCOMPSPKR_df = COMPSPKR_df.drop_duplicates(subset=['Condition'])
        ConditionNOISE_df = NOISE_df.drop_duplicates(subset=['Condition'])
        list_of_Condition_df = [ConditionECHO_df,ConditionCHOP_df,ConditionCLIP_df,ConditionCOMPSPKR_df,ConditionNOISE_df]

        count = 0
        namelist = ['ECHO','CHOP','CLIP','COMPSPKR','NOISE']
        for i in list_of_Condition_df:
            objects = i['Condition']
            y_pos = np.arange(len(objects))
            performance = i['conditionMOS']
            errorbar = i['sampleSTD']
            plt.figure(figsize=(10, 6))
            plt.bar(y_pos, performance, align='center', alpha=0.5,width =.8,color = 'slateblue')
            plt.errorbar(y_pos, performance, yerr = errorbar,fmt='o',ecolor = 'gray',color='black')
            plt.xticks(y_pos, objects)
            plt.xlabel('Condition',fontsize = 15)
            plt.ylabel('Average MOS',fontsize = 15)
            plt.title(namelist[count] +' per Condition Average MOS',fontsize = 18)
            plt.savefig(namelist[count] + ' Linear Regression.png')
            count += 1
    
    