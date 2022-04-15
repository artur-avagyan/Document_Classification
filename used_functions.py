import pytesseract as pt
from PIL import Image
import os
from tqdm import tqdm
import pandas as pd
import numpy as np
import tqdm
import time
import shutil

def img_2_text(img_path, tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
    pt.pytesseract.tesseract_cmd = tesseract_path
    img_object = Image.open(img_path)
    img_text = pt.image_to_string(img_object)
    return img_text

def save_text(text_from_img, text_path):
    text_file = open(text_path, "w")
    text_file.write(text_from_img)
    text_file.close()

def text_to_csv():
    labels_path = '/text/train_/'
    labels_list = os.listdir(labels_path)

    datas = pd.DataFrame(columns=['text', 'label'])
    datas_test = pd.DataFrame(columns=['text', 'label'])
    # datas_200_val = pd.DataFrame(columns = ['text', 'label'])
    # print(labels_list)

    count_ = 1
    count_train = 0
    count_test = 0

    for label in labels_list:

        start_time = time.time()

        for text_file in os.listdir(labels_path + label):

            text_i = open(labels_path + label + '/' + text_file,
                          encoding='latin-1').read()
            text_i = text_i.replace('\n', ' ')

            if len(text_i) != 0:
                if count_ % 6 != 0:

                    datas = datas.append(
                        {
                            'text': text_i,
                            'label': label,
                        },
                        ignore_index=True
                    )
                    count_ += 1
                    count_train += 1

                else:

                    datas_test = datas_test.append(
                        {
                            'text': text_i,
                            'label': label,
                        },
                        ignore_index=True
                    )
                    count_ += 1
                    count_test += 1

            # if count_train == number_train_val and count_test == number_test:
            #   break
        end_time = time.time()
        run_time_min = int((end_time-start_time) // 60)
        run_time_sec = np.round((end_time-start_time) % 60)
        print(f'{label}\n\ncount_train ----> {count_train}\ncount_test ----> {count_test}\nrun_time ----> {run_time_min} min, {run_time_sec} sec\n')

    datas.to_csv(
        'text_data_all.csv', index=False)
    datas_test.to_csv(
        'text_data_all_test.csv', index=False)

def copy_images_for_image_classification():
    data_dir = ''
    destination_dir = "img_cls/"
    parent_list = os.listdir(os.path.join(data_dir,'img/train/'))

    os.mkdir(os.path.join(destination_dir, 'others'))
    for folder in os.listdir(os.path.join(data_dir,'img/train/'),):
        count = 0
        current_directory = os.path.join(destination_dir, folder)
        if (folder in ['ad', 'file', 'newspaper', 'handwritten']) and (not os.path.exists(current_directory)):
            os.mkdir(current_directory)

    #     print(os.listdir(os.path.join(os.path.join(data_dir,'image_cls'), folder)))
        for image in tqdm(os.listdir(os.path.join(os.path.join(data_dir,'img/train'), folder))):

            len_folder = len(os.listdir(os.path.join('img/train', folder)))

            if folder not in ['ad', 'file', 'newspaper', 'handwritten']:
                if count < 700:
                    image_path = os.path.join(os.path.join(data_dir,'img/train') + '/' + folder, image)
                    shutil.copy(image_path, os.path.join(destination_dir + 'others', image))
                else:
                    break
                count += 1
            else:
                if count < len_folder:
                    image_path = os.path.join(os.path.join(data_dir,'img/train') + '/' + folder, image)
                    shutil.copy(image_path, os.path.join(destination_dir + folder, image))
                else:
                    break
                count += 1
        print(f'{folder} copy is done')