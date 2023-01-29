# Breast Cancer Ultrasound Image Classifier by 🅱🅻🅰🆀
![doc3](https://user-images.githubusercontent.com/100685852/215300772-aea04a41-592f-4be4-ae23-2200656c7b2b.png)

Benign cancer, and Malignant cancer; the treatment options and outcomes for the two types of cancer are very different. Benign cancers are not typically life-threatening
and can often be treated with surgery alone. Malignant cancers, on the other hand, can be life-threatening and may require a combination of treatments such as surgery, 
chemotherapy, and radiation therapy. Accurately determining the type of cancer a person has is crucial for developing an effective treatment plan and improving the chances
of a successful outcome.
Here, I have trained a model that classifies patients according to the cancer that they have; benign, or malignant. With over 9000 ultrasound images of breast cancer; both
malignant and benign, the model was trained on pretrained neural networks, and deployed to dockerhub. 

You can find the dataset above in 'train.csv' and 'val.csv'.

## How to access the model:
The fastest way for you to run this model is to simply get the docker image blaqadonis1993/cancer_model and run it locally.

## Download the image:
It is quite light; not up to 300MB.
```docker pull blaqadonis1993/cancer_model```
## Start the service:
```docker run -it --rm -p 9696:9696 blaqadonis1993/cancer_model:latest```
In the terminal, run: ```python predict_test.py```

If all goes well, you should have results similar to the ones in the screenshots below:

![doc2](https://user-images.githubusercontent.com/100685852/215300903-8144483d-3989-44a8-b281-b18bb006153e.PNG)


![doc](https://user-images.githubusercontent.com/100685852/215300878-690f1994-b2a6-45c9-b70c-b900e1d9aab9.PNG)
