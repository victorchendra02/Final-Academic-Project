import pandas as pd
import numpy as np
import tensorflow as tf


def load_and_prepare_dataset(path: str, batch_size: int, AUTOTUNE=tf.data.AUTOTUNE) -> tuple[tf.data.Dataset]:
    df_train = pd.read_csv(f"{path}train.csv")
    df_test = pd.read_csv(f"{path}test.csv")
    df_val = pd.read_csv(f"{path}val.csv")
    
    train_post_canonical = df_train['post_canonical'].values
    train_score = df_train['score'].values
    
    test_post_canonical = df_test['post_canonical'].values
    test_score = df_test['score'].values
    
    val_post_canonical = df_val['post_canonical'].values
    val_score = df_val['score'].values
    
    train_ds = tf.data.Dataset.from_tensor_slices((train_post_canonical, train_score))
    test_ds = tf.data.Dataset.from_tensor_slices((test_post_canonical, test_score))
    val_ds = tf.data.Dataset.from_tensor_slices((val_post_canonical, val_score))

    train_ds = train_ds.batch(batch_size).prefetch(buffer_size=AUTOTUNE)
    test_ds = test_ds.batch(batch_size).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.batch(batch_size).prefetch(buffer_size=AUTOTUNE)
    
    train_list = return_list_of_batched_tf_dataset(train_ds)
    test_list = return_list_of_batched_tf_dataset(test_ds)
    val_list = return_list_of_batched_tf_dataset(val_ds)

    r = {
        'train': train_list,
        'test': test_list,
        'val': val_list,
    }
    
    return train_ds, test_ds, val_ds, r

def mse_tf(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred)).numpy()

def rmse_tf(y_true, y_pred):
    return tf.sqrt(mse_tf(y_true, y_pred)).numpy()

def mae_tf(y_true, y_pred):
    return tf.reduce_mean(tf.abs(y_true - y_pred)).numpy()

def r2_score_tf(y_true, y_pred):
    mean_true = tf.reduce_mean(y_true)
    total_error = tf.reduce_sum(tf.square(y_true - mean_true))
    unexplained_error = tf.reduce_sum(tf.square(y_true - y_pred))
    r_squared = 1 - (unexplained_error / total_error)
    return r_squared.numpy()

def return_list_of_batched_tf_dataset(ds):
    X = []
    y = []
    for text_, score_ in ds:
        text_, score_ = list(text_.numpy()), list(score_.numpy())
        X += text_
        y += score_
    
    return {'X': np.array(X), 'y': np.array(y)}

def calculate_descriptive_statistics(array) -> dict:
    mean = np.mean(array)
    variance = np.var(array)
    std = np.std(array)
    min_ = np.min(array)
    max_ = np.max(array)
    
    return {
        'mean': mean,
        'variance': variance,
        'std': std,
        'min': min_,
        'max': max_,
    }