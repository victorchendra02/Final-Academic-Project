import pandas as pd
import tensorflow as tf


def load_and_prepare_dataset(path: str, seed: int, batch_size: int, AUTOTUNE=tf.data.AUTOTUNE) -> tuple[tf.data.Dataset]:
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
    val_ds = tf.data.Dataset.from_tensor_slices((val_post_canonical, val_score))
    test_ds = tf.data.Dataset.from_tensor_slices((test_post_canonical, test_score))


    train_ds = train_ds.shuffle(buffer_size=len(df_train), seed=seed).batch(batch_size).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.batch(batch_size).prefetch(buffer_size=AUTOTUNE)
    test_ds = test_ds.batch(batch_size).prefetch(buffer_size=AUTOTUNE)
    
    return train_ds, val_ds, test_ds
