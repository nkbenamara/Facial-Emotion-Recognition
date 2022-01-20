# Facial-Emotion-Recognition

This repository contains the code and our FER models published in [1]. The tables below show the obtained performances with our models (single and ensembles) on the FER2013 database (test subset).

## Single models

| Model | A | B | C | D | 
| :---: | :---: | :---: | :---: | :---: | 
| Accuracy | 68.68% | 67.48% | 68.15% | 68.15% |

## Ensemble models

| Model | AB | AC | AD | BC | BD | CD | ABC | ABD | BCD | CAD | ABCD |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| Accuracy | 70.47% | 70.97% | 71.11% | 70.58% | 69.60% | 70.08% | **72.47%** | 71.08% | 71.50% | 71.66% | 72.14% | 

The FER 2013 database is available from the following Kaggle link ([Click](https://www.kaggle.com/deadskull7/fer2013))

If you use our models, please cite our paper:

[1] Benamara N.K. et al. (2019) Real-Time Emotional Recognition for Sociable Robotics Based on Deep Neural Networks Ensemble. In: Ferrández Vicente J., Álvarez-Sánchez J., de la Paz López F., Toledo Moreo J., Adeli H. (eds) Understanding the Brain Function and Emotions. IWINAC 2019. Lecture Notes in Computer Science, vol 11486. Springer, Cham. https://doi.org/10.1007/978-3-030-19591-5_18
