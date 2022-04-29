import pandas as pd
import re
from scipy.stats import pearsonr

from .node import AQPNode

class PearsonNode(AQPNode):
    
    def __init__(self, id_: str, df_key: str, x_data_key: str, 
                 y_data_keys: list, titles: list, y_labels: list, **kwargs):
        super().__init__(id_)
        TCDvoip = pd.read_csv("C:\\Users\\Jack Crowley\\AQP\\results\\TCDVoipData.csv")
        FullData = pd.read_csv("C:\\Users\\Jack Crowley\\AQP\\results\\GenSpeechData.csv")
        Data = FullData.drop("Unnamed: 0",1)
        count = 0
        count2 = 0
        New_Column_List2 = []
        for items in Data["Test_Wave"]:
            string = Data.at[count,'Test_Wave']
            change = string[53:-4:1]
            line = re.sub('[!@#$/9]', '', change)
            count +=1
            New_Column_List2.append(line)

        New_Column_List3 = []
        for items in Data["Test_Wave"]:
            string = Data.at[count2,'Test_Wave']
            change = string[41:48:1]
            line = re.sub('[!@#$/t]', '', change)
            count2 +=1
            New_Column_List3.append(line)

        Data['Type']= New_Column_List2
        Data['Directory']= New_Column_List3   

        columnchoice = (Data.columns.values.tolist())
        columnchoice = [e for e in columnchoice if e not in ('Ref_Wave', 'Test_Wave', 'MOS', 'Type', 'Directory')]
        columnchoice
        def PearsonTCD(columnchoice):
            print("Please choose:")
            for idx, element in enumerate(columnchoice):
                print("{}) {}".format(idx+1,element))
            i = input("Enter number: ")
            try:
                if 0 < int(i) <= 3:
                    return int(i)-1
            except:
                pass
            return None
        data1 = TCDvoip['sampleMOS']
        Pearsonchoice = PearsonTCD(columnchoice)
        columnname = columnchoice[Pearsonchoice]
        data2 = TCDvoip[columnname]
        # calculate Pearson's correlation
        corr, _ = pearsonr(data1, data2)
        print('Pearsons correlation for '+ columnname + ': %.3f' % corr)
    