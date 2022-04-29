from .node import AQPNode

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

class LinearregressionNode(AQPNode):
    
    def __init__(self,id_,output_key,ref_signal_key,draw_options=None, **kwargs):
        super().__init__(self, id_,draw_options=draw_options, **kwargs)
        self.ref_signal_key = ref_signal_key
        self.type_ = 'LinearregressionNode'
    
    def execute(self, result, **kwargs):
        super().execute(result, **kwargs)
        ref_signal = result[self.ref_signal_key]
        print(ref_signal)
        print('Hello World')
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

        def LinearRegTCD(columnchoice):
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
        Linearchoice = LinearRegTCD(columnchoice)
        Y = columnchoice[Linearchoice]
        Y_value = TCDvoip[Y]
        plt_1 = plt.figure(figsize=(6, 6))
        sns.regplot(x=TCDvoip["sampleMOS"], y=Y_value,scatter_kws={"color": "blue"}, line_kws={"color": "red"})
        plt.grid()
        plt.title(Y + ' Linear Regression', fontsize = 16)
        plt.savefig(Y + ' Linear Regression TCDvoip.png')