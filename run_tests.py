import src.modules.model_class as mdc


data = ['салем', 'здравствуйте, меня зовут Макс', 'Мен мектепте болдым', 'Скорая пОмощЬ']

model = mdc.KazRuClassifier()

print(model.predict(data))