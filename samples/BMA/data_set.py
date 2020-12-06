import os

# Root directory of the project
ROOT_DIR = os.path.abspath("../")
ROOT_IM = ROOT_DIR


class DataSet():
    # Directory of images to run detection on
    IMAGE_DIR = ROOT_IM + "/BMA"

    # the specific directory of the type
    im_dir = '/im'
    mask_dir = '/mask'
    skl_dir = '/skl'

    # creates a list of all the files in the directory
    #im_files = os.listdir(im_dir)
    #mask_files = os.listdir(mask_dir)
    #skl_files = os.listdir(skl_dir)

    # constants for the number of files we want for training (80%), development(10%), and testing(10%)
    # based on the total number of files for each shape.
    # num_training = [784, 1016, 700, 660, 759, 2364, 452,
    #                1871, 95, 923, 892, 71, 74, 30428,
    #                1084, 303, 89]

    # num_devel = [98, 127, 87, 82, 94, 295, 56, 233, 11,
    #             115, 111, 8, 9, 3803, 135, 37, 11]

    # num_val = num_devel  # (they are the same - 10%)

    # List of all the shapes contained in
    shape_names = sorted(os.listdir(IMAGE_DIR + '/Training' + im_dir))

    def training(self, type, shape=None):
        """
        Returns the training set for the given type (image, mask, skeleton) and the given shape
        (horse, motorcycle, sheep, etc)
        If shape is None, return the entire training set in a dict() with the shape as keys.
        """
        if type == 'image':
            directory = DataSet.IMAGE_DIR + '/Training' + DataSet.im_dir
            # file_list = DataSet.im_files
        elif type == 'mask':
            directory = DataSet.IMAGE_DIR + '/Training' + DataSet.mask_dir
            # file_list = DataSet.mask_files
        elif type == 'skeleton':
            directory = DataSet.IMAGE_DIR + '/Training' + DataSet.skl_dir
            # file_list = DataSet.skl_files
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)

        if shape is None:
            training = {}
            
            for item in DataSet.shape_names:
                ph = sorted(os.listdir(directory + '/' + item + '/.'))
                item_list = []
                j = 0 
                for image in ph:
                     # if statements for leveling dataset to account for blobby/skinny shapes. 
                    if (item == "cat" or item == "dog" or item == "sheep") and j == 800:
                        #print("breaking for " + str(item))
                        break
                    if item == "person" and j == 2400:
                        #print("breaking for " + str(item))
                        break
                    if image.endswith('.jpg') or image.endswith('.png'):
                        j += 1
                        item_list.append(image) 
                training[item] = sorted(item_list)
            return training
            
        else:
            training = []
            if shape not in DataSet.shape_names:
                raise ValueError("shape should be contained in %s, not %s" % (DataSet.shape_names, shape))
            else:
                index = DataSet.shape_names.index(shape)
            ph = os.listdir(directory + '/' + shape + '/.')
            for image in ph:
                if image.endswith('.jpg') or image.endswith('.png'):
                    training.append(image)
            
            return sorted(training)
            

    def development(self, type, shape=None):
        """
        Returns the development set for the given type (image, mask, skeleton) and the given shape
        (horse, motorcycle, sheep, etc)
        If shape is None, return the entire development set in a dict() with the shape as keys.
        """
        if type == 'image':
            directory = DataSet.IMAGE_DIR + '/Development' + DataSet.im_dir
            # file_list = DataSet.im_files
        elif type == 'mask':
            directory = DataSet.IMAGE_DIR + '/Development' + DataSet.mask_dir
            # file_list = DataSet.mask_files
        elif type == 'skeleton':
            directory = DataSet.IMAGE_DIR + '/Development' + DataSet.skl_dir
            # file_list = DataSet.skl_files
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)

        if shape is None:
            development = {}
            
            for item in DataSet.shape_names:
                ph = sorted(os.listdir(directory + '/' + item + '/.'))
                item_list = []
                j = 0
                for image in ph:
                    # if statements for leveling dataset to account for blobby/skinny shapes. 
                    if (item == "cat" or item == "dog" or item == "sheep") and j == 100:
                        #print("breaking for " + str(item))
                        break
                    if item == "person" and j == 300:
                        #print("breaking for " + str(item))
                        break
                    if image.endswith('.jpg') or image.endswith('.png'):
                        j += 1
                        item_list.append(image) 
                development[item] = sorted(item_list)
            return development
        
        else:
            if shape not in DataSet.shape_names:
                raise ValueError("shape should be contained in %s, not %s" % (DataSet.shape_names, shape))
            
            development = os.listdir(directory + '/' + shape + '/.')
            return development

    def validation(self, type, shape=None):
        """
        Returns the development set for the given type (image, mask, skeleton) and the given shape
        (horse, motorcycle, sheep, etc)
        If shape is None, return the entire development set in a dict() with the shape as keys.
        """
        if type == 'image':
            directory = DataSet.IMAGE_DIR + '/Validation' + DataSet.im_dir
            # file_list = DataSet.im_files
        elif type == 'mask':
            directory = DataSet.IMAGE_DIR + '/Validation' + DataSet.mask_dir
            # file_list = DataSet.mask_files
        elif type == 'skeleton':
            directory = DataSet.IMAGE_DIR + '/Validation' + DataSet.skl_dir
            # file_list = DataSet.skl_files
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)

        if shape is None:
            validation = {}
            
            for item in DataSet.shape_names:
                ph = sorted(os.listdir(directory + '/' + item + '/.'))
                item_list = []
                j = 0
                for image in ph:
                    # if statements for leveling dataset to account for blobby/skinny shapes. 
                    if (item == "cat" or item == "dog" or item == "sheep") and j == 100:
                        #print("breaking for " + str(item))
                        break
                    if item == "person" and j == 300:
                        #print("breaking for " + str(item))
                        break
                    if image.endswith('.jpg') or image.endswith('.png'):
                        j += 1
                        item_list.append(image) 
                validation[item] = sorted(item_list)
            return validation
        else:
            if shape not in DataSet.shape_names:
                raise ValueError("shape should be contained in %s, not %s" % (DataSet.shape_names, shape))
            else:
                index = DataSet.shape_names.index(shape)
            validation = os.listdir(directory + '/' + shape + '/.')
            return validation

    def path(self, type, shape, sub):
        """
        Returns the path of the file.  Type is image, mask, or skeleton.
        Shape is type of picture (motorcycle, elephant, etc.)
        """
        if type is 'image':
            return DataSet.IMAGE_DIR + '/' + sub + DataSet.im_dir + '/' + shape + '/'
        elif type is 'mask':
            return DataSet.IMAGE_DIR + '/' + sub + DataSet.mask_dir + '/' + shape + '/'
        elif type is 'skeleton':
            return DataSet.IMAGE_DIR + '/' + sub + DataSet.skl_dir + '/' + shape + '/'
        else:
            raise ValueError("type should be 'image', 'mask', or 'skeleton'. Not %s" % type)


