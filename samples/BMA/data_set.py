import os

# Root directory of the project
ROOT_DIR = os.path.abspath("../")
ROOT_IM = ROOT_DIR


class DataSet():
    # Directory of images to run detection on
    IMAGE_DIR = os.path.join("Training")

    # the specific directory of the type
    im_dir = IMAGE_DIR + '/im'
    mask_dir = IMAGE_DIR + '/mask'
    skl_dir = IMAGE_DIR + '/skl'

    # creates a list of all the files in the directory
    im_files = os.listdir(im_dir)
    mask_files = os.listdir(mask_dir)
    skl_files = os.listdir(skl_dir)

    # constants for the number of files we want for training (80%), development(10%), and testing(10%)
    # based on the total number of files for each shape.
    num_training = [784, 1016, 700, 660, 759, 2364, 452,
                    1871, 95, 923, 892, 71, 74, 30428,
                    1084, 303, 89]

    num_devel = [98, 127, 87, 82, 94, 295, 56, 233, 11,
                 115, 111, 8, 9, 3803, 135, 37, 11]

    num_val = num_devel  # (they are the same - 10%)

    # List of all the shapes contained in
    shape_names = os.listdir(IMAGE_DIR + '/im/')

    def training(self, type, shape=None):
        """
        Returns the training set for the given type (image, mask, skeleton) and the given shape
        (horse, motorcycle, sheep, etc)
        If shape is None, return the entire training set in a dict() with the shape as keys.
        """
        if type == 'image':
            directory = DataSet.im_dir
            file_list = DataSet.im_files
        elif type == 'mask':
            directory = DataSet.mask_dir
            file_list = DataSet.mask_files
        elif type == 'skeleton':
            directory = DataSet.skl_dir
            file_list = DataSet.skl_files
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)

        if shape is None:
            training = {}
            for i, item in enumerate(file_list):
                training[item] = os.listdir(directory + '/' + item + '/.')
            return sorted(training)
        else:
            if shape not in DataSet.shape_names:
                raise ValueError("shape should be contained in %s, not %s" % (DataSet.shape_names, shape))
            else:
                index = DataSet.shape_names.index(shape)
            training = os.listdir(directory + '/' + shape + '/.')
            return sorted(training)

    def development(self, type, shape=None):
        """
        Returns the development set for the given type (image, mask, skeleton) and the given shape
        (horse, motorcycle, sheep, etc)
        If shape is None, return the entire development set in a dict() with the shape as keys.
        """
        if type == 'image':
            directory = DataSet.im_dir
            file_list = DataSet.im_files
        elif type == 'mask':
            directory = DataSet.mask_dir
            file_list = DataSet.mask_files
        elif type == 'skeleton':
            directory = DataSet.skl_dir
            file_list = DataSet.skl_files
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)

        if shape is None:
            development = {}
            for i, item in enumerate(file_list):
                development[item] = os.listdir(directory + '/' + item + '/.')[
                                   DataSet.num_training[i]: DataSet.num_training[i] + DataSet.num_devel[i]]
            return development
        else:
            if shape not in DataSet.shape_names:
                raise ValueError("shape should be contained in %s, not %s" % (DataSet.shape_names, shape))
            else:
                index = DataSet.shape_names.index(shape)
            development = os.listdir(directory + '/' + shape + '/.')[DataSet.num_training[index]:
                                                                   DataSet.num_training[index]
                                                                   + DataSet.num_devel[index]]
            return development

    def validation(self, type, shape=None):
        """
        Returns the development set for the given type (image, mask, skeleton) and the given shape
        (horse, motorcycle, sheep, etc)
        If shape is None, return the entire development set in a dict() with the shape as keys.
        """
        if type == 'image':
            directory = DataSet.im_dir
            file_list = DataSet.im_files
        elif type == 'mask':
            directory = DataSet.mask_dir
            file_list = DataSet.mask_files
        elif type == 'skeleton':
            directory = DataSet.skl_dir
            file_list = DataSet.skl_files
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)

        if shape is None:
            validation = {}
            for i, item in enumerate(file_list):

                validation[item] = os.listdir(directory + '/' + item + '/.')[DataSet.num_devel[i]
                                                                           + DataSet.num_training[i]:
                                                                           DataSet.num_devel[i]
                                                                           + DataSet.num_training[i]
                                                                           + DataSet.num_val[i]]
            return validation
        else:
            if shape not in DataSet.shape_names:
                raise ValueError("shape should be contained in %s, not %s" % (DataSet.shape_names, shape))
            else:
                index = DataSet.shape_names.index(shape)
            validation = os.listdir(directory + '/' + shape + '/.')[DataSet.num_devel[index]
                                                                       + DataSet.num_training[index]:
                                                                       DataSet.num_devel[index]
                                                                       + DataSet.num_training[index]
                                                                       + DataSet.num_val[index]]
            return validation

    def path(self, type, shape):
        """
        Returns the path of the file.  Type is image, mask, or skeleton.
        Shape is type of picture (motorcycle, elephant, etc.)
        """

        if type is 'image':
            return DataSet.im_dir + '/' + shape + '/'
        elif type is 'mask':
            return DataSet.mask_dir + '/' + shape + '/'
        elif type is 'skeleton':
            return DataSet.skl_dir + '/' + shape + '/'
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)


