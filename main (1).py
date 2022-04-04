import pandas as pd
import logging

logging.basicConfig(filename="bmi.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class Data:
    df = pd.DataFrame()  ####an empty dataframe has been created
    #final = pd.DataFrame()

    def __init__(self, args):  ###args can take multiple inputs
        self.args = args
        logging.info(f"an object has been created fo this class ")
        df = self._insert_data()

    def _insert_data(self):  ###user cannot access this func as it is protected
        """ method to insert data in the dataframe """
        logging.info("data insertion started")
        try:

            Data.df = pd.concat([Data.df, pd.DataFrame(self.args)], ignore_index=True)

            Data.df['Bmi'] = Data.df['WeightKg'] / ((Data.df['HeightCm'] * (.01)) ** 2)
            bmi_cat = []
            health_risk = []
            for i in Data.df['Bmi']:
                if i <= 18.4:
                    bmi_cat.append("Underweight")
                    health_risk.append('Malnutrition risk')
                elif i >= 18.5 and i <= 24.9:
                    bmi_cat.append('Normal weight')
                    health_risk.append('Low risk ')
                elif i >= 25 and i <= 29.9:
                    bmi_cat.append('Overweight')
                    health_risk.append('Enhanced risk')
                elif i >= 30 and i <= 34.9:
                    bmi_cat.append('Moderately obese')
                    health_risk.append('Medium risk')
                elif i >= 35 and i <= 35.9:
                    bmi_cat.append('severely obese')
                    health_risk.append('High risk')
                else:
                    bmi_cat.append('Very severely obese')
                    health_risk.append('Very High risk ')

            Data.df['Bmi category'] = bmi_cat
            Data.df['Health Risk'] = health_risk
        except Exception as e:
            logging.error(f'error in insertion of data as {e}')
            print("error in inserting data")
            pass
        return Data.df

    ### functions users can use to see data,overweight persons and  to clear data
    def see_data(self):
        return Data.df

    def check_cat_in_col(self):
        counts_cat = self.df['Bmi category'].value_counts()
        return f"the total overweight person are {counts_cat['Overweight']}"

    def clear_data(self):
        del [Data.df]


