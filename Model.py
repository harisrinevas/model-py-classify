# import sklearn
# from GlobalConfig import GlobalConfig
import pandas as pd
import  numpy as np

class Model():
    def __init__(self, config):
        self.model_type = ""
        self.data_source_format = ""
        self.eda_location = ""
        self.config = config

    def model_pipeline(self, config, df, imputation=True, imputation_type="mean", one_hot_encoding="None", norm=True):
        """
        :param config: object of GlobalConfig class
        :param df: input data frame
        :param imputation: Boolean, is imputation required
        :param imputation_type: mean, median, frequent are considered
        :param one_hot_encoding: None or all, whether one hot encoding is needed
        :param norm: Boolean , whether the columns to be normalized
        :return: Pandas data frame with required configuration
        """
        logger = config.logger
        logger.info('start model pipeline')

        if isinstance(df, pd.DataFrame):
            logger.info('Valid input')
        else:
            logger.error('Invalid input')

        if imputation and(imputation_type == "mean" or imputation_type == "median"
                                  or imputation_type == "frequent"):
            logger.info('valid imputation')
        else:
            logger.error('invalid imputation')

        if one_hot_encoding == "None" or one_hot_encoding == "All":
            logger.info('valid encoding request')
        else:
            logger.error('invalid encoding request')

        if isinstance(norm, bool):
            logger.info('valid normalizer')
        else:
            logger.error('invalid normalizer')

        return df