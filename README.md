# Document Classification
Final Project for Sourcemind AI/ML Specialist couse

The dataset for this project is a subset of RVL-CDIP, and whola dataset can be found here: \
  https://www.cs.cmu.edu/~aharley/rvl-cdip/

![dataset_images_2](https://user-images.githubusercontent.com/58246780/163474682-2f1f6ce6-3695-40c7-a402-874d50afb81b.jpg)
![dataset_images_3](https://user-images.githubusercontent.com/58246780/163474687-c1a9e7e7-af34-49dd-a614-2518389f8fc7.jpg)

**Task**: Create a image classification model to distinguish 13 document classes.

**Dataset**
There are ~85k images with 13 labelled classes and they have uniform distribution:
- ad
- cv
- email
- file
- handwritten
- invoice
- letter
- memorandum
- newspaper
- publication
- report
- specification
- survey

Diring analysis images, we found that there as 3 classes (***ad, file and handwritten***), which would be easily for image classification and others are easily for text classification. According to that, our model architecture is:
![presentation](https://user-images.githubusercontent.com/58246780/163481671-85bb1951-770c-4921-b021-53d5d586be85.png)


In the fisrt part of our model we used pretrained **VGG 16** and changed last layer to fit for 4 label image classification. Loss function is CrossEntropy, and optimizer is Adam. After 20 epochs we have ***88.7%*** accuracy on **train data** and ***88.1%*** on **validation data**
![accuracy train val](https://user-images.githubusercontent.com/58246780/163477709-fb9a53de-03cf-4648-99a0-25d34310e956.png)
\
\
If our image classifiction predict `others`, so image would go to second part of our model and there will be extract text from that image, and finally that text would be go to last part of model: **text classificion**. Text are extracted from image with ***pytesseract*** package. For text classification we used some text pre-processing, and after that 3 models: **Naive Bayes**, **Logistic Regression** and **FastText**. For each model we use both **CountVectorizer** and **TF-IDF**. Best result on validation data are gotten with ***FastText with 5 chargram*** with 98.6% accuracy on train data and 85.5% on validation data. Accuracy results from each models on validation data are represented on this chart:
![download](https://user-images.githubusercontent.com/58246780/163480172-749ed268-dfb2-4a32-b50c-d7fb99e3dd69.png)

After good results during bot image and text classifications we tested our model in all documents with 13 labels. We chose 1000 random images from each 13 label, and testing our model. Accuracy was 88.7%, and it's great for this dataset. This chart shows ***confution matrix*** for testing dataset\
![all_data](https://user-images.githubusercontent.com/58246780/163481340-49f198bc-b766-4aa8-b269-f3ee917dac9f.png)

<h4 align="left">Artur Avagyan</h4>
    <ul>
    <li>Responsible Actuary in Armenia Insurance</li>
    <li>Student from YSU (Data Science for Business Master's Degree Program)</li>
    <li>E-mail:   avagyan.artur97@gmail.com</li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/artur-avagyan-0a16311b3">Artur Avagyan</a></li>
    <li>GitHub:   <a href="https://github.com/artur-avagyan">Artur Avagyan</a></li>
    </ul>

<h4 align="left">Nune Tadevosyan</h4>
    <ul>
    <li>R&D engineer at Instigate Semiconductor</li>
    <li>Student from YSU (Information and Applied Matematics)</li>
    <li>E-mail:   nune.tadevosyan.011@gmail.com</li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/nune-tadevosyan-9806a8207/">Nune Tadevosyan</a></li>
    <li>GitHub:   <a href="https://github.com/NuneTadevosyan">Nune Tadevosyan</a></li>
    </ul>

<h4 align="left">Supervised by Arsen Yeghiazaryan</h4>
    <ul>
    <li>Machine Learning Team Lead at Webb Fontaine</li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/arsen-yeghiazaryan-9abb4721//">Arsen Yeghiazaryan</a></li>
    </ul>
<h3 align="center">Sourcemind AI/ML Specialist couse</h3>
