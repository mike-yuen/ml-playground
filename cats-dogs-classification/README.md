## Cats and Dogs Classification

This is a machine learning project that classifies images of cats and dogs using neural networks. The goal of this project is to train a model that can accurately predict whether an input image contains a cat or a dog.

## Dataset

The dataset for this project consists of 25,000 images of cats and dogs. The images are split into two sets: a training set with 20,000 images and a testing set with 5,000 images. Each image is 64x64 pixels and is in RGB format.

The dataset can be downloaded from Kaggle.

## Installation

To install the required packages, run:

```sh
pip install -r requirements.txt
```

## Usage

To preprocess the data and train the model, run:

```sh
python src/data_preprocessing.py
python src/model_training.py
```

To evaluate the model on the test set, run:

```sh
python src/model_evaluation.py
```

## Results

The trained model achieves an accuracy of 90% on the test set.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was inspired by the [Kaggle Dogs vs. Cats competition](https://www.kaggle.com/c/dogs-vs-cats).
