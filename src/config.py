common_params = {
    'image_size': 64,
    'batch_size': 16,
    'output_size': 7,
    'num_steps': 450000,
    'boxes_per_cell': 2,
    'num_classes': 2,
    'object_scale': 1.0,
    'noobject_scale': 0.5,
    'class_scale': 1.0,
    'coord_scale': 5.0,
}

dataset_params = {
    'train_file': '../data/train.txt',
    'test_file': '../data/test.txt'
}

path_params = {
    'checkpoints': '../checkpoints/'
}

class_names = (
    'person','mask'
)
