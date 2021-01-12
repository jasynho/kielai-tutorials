from flair.models.text_classification_model import TARSClassifier
from flair.data import Sentence

# load english model
tars = TARSClassifier.load('tars-base')

# Declare sentences & classes
sentences = ['I really hate fries.', 'I love Hamburgers.','I am so glad you liked it!']
classes = ['happy', 'sad', 'angry']

# Make actual predictions
for elem in sentences:
    sentence=Sentence(elem)
    tars.predict_zero_shot(sentence, classes)
    print(sentence)



