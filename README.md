## A. Env `artofproblemsolving`

```bash
conda create --name artofproblemsolving python=3.9.12 -y
```

```bash
# Requirements:
requests==2.30.0
selenium==3.141.0
keyboard
mouse
beautifulsoup4
webdriver-manager
pyperclip
pygame
```

## B. Env TensorFlow `aops_TF`:

Documentation:
1. [Install TensorFlow](https://www.tensorflow.org/install/pip#windows-native_1)
2. [Classify Text with BERT](https://www.tensorflow.org/text/tutorials/classify_text_with_bert)

```bash
conda create --name aops_TF python=3.10 -y
conda activate aops_TF

conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
pip install --upgrade pip
pip install "tensorflow<2.11"
# Verify GPU:
# If a list of GPU devices is returned, you've installed TensorFlow successfully.
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

pip install "tf-models-official"
conda install transformers -y
```

## C. Env PyTorch `aops_PT`:

Documentation [Install PyTorch](https://pytorch.org/get-started/locally/)

```bash
conda create --name aops_PT python=3.10 -y
conda activate aops_PT

conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y
# Verify GPU:
# If True, then GPU available
python -c "import torch; print(torch.cuda.is_available())"

conda install transformers -y
```

## D. Env `aops_MATHBERT`:

```bash
conda create --name aops_MATHBERT python=3.10 -y
conda activate aops_MATHBERT
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
pip install --upgrade pip
pip install "tensorflow<2.11"

conda install pytorch torchvision torchaudio cpuonly -c pytorch -y

conda install transformers -y
```
