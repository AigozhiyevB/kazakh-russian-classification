import joblib
from .text_prep import char_clean

def kk_ru(y):
    ans = 'казахский' if y == 1 else 'русский'
    return ans

class KazRuClassifier():
    def __init__(self):
        self.model = joblib.load("bin/sklearn_model_first.pkl")

    def predict(self, lst_str):

        '''
        input:  list of strings on kazakh or russian languages
        output: 'kazakh' or 'russian' based on input language
        '''
        inp = [char_clean(a) for a in lst_str]
        output = self.model.predict(inp)
        ans = [kk_ru(a) for a in output]
        return ans


