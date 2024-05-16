## A. Env `artofproblemsolving`

```bash
conda create --name artofproblemsolving python=3.9.12 anaconda -y
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

## B. Env TensorFlow `aops_tenflow`:

Documentation:
1. [Install TensorFlow](https://www.tensorflow.org/install/pip#windows-native_1)
2. [Classify Text with BERT](https://www.tensorflow.org/text/tutorials/classify_text_with_bert)

```bash
conda create --name aops_tenflow python=3.9.12 anaconda -y
conda activate aops_tenflow

conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
python -m pip install "tensorflow<2.11"
# Verify GPU:
# If a list of GPU devices is returned, you've installed TensorFlow successfully.
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

pip install -U "tensorflow-text"
pip install tf-models-official
conda install transformers==4.24.0 -y
```

## C. Env PyTorch `aops_pytorch`:

Documentation [Install PyTorch](https://pytorch.org/get-started/locally/)

```bash
conda create --name aops_pytorch python=3.9.12 anaconda -y
conda activate aops_pytorch

conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y
# Verify GPU:
# If True, then GPU available
python -c "import torch; print(torch.cuda.is_available())"

conda install transformers==4.24.0 -y
```

## D. Env `aops_mathbert`:

```bash
conda create --name aops_mathbert python=3.9.12 anaconda -y
conda activate aops_mathbert

conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
pip install --upgrade pip
pip install "tensorflow<2.11"
pip install tf-models-official

conda install pytorch torchvision torchaudio cpuonly -c pytorch -y

conda install transformers==4.24.0 -y
```
