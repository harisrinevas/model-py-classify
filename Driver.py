from GlobalConfig import GlobalConfig
from Model import Model

def get_config():
    config = GlobalConfig()
    config.log_file = 'log_file.txt'
    logger = config.get_logger()
    return config, logger


if __name__ == '__main__':
    config, logger = get_config()
    try:
        logger.info('config set')
        logger.info('Clear log file')
        try:
            open('log_file.txt','w').close()
        except:
            logger.error('log file not cleared')
    except:
        logger.error('Exception caught')

    Model = Model(config)
    df = Model.model_pipeline(config, df="True", norm=False, imputation_type="frequent", one_hot_encoding="dummy")