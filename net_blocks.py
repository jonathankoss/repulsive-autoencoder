from keras.layers import Dense, Reshape, Input, Lambda, Convolution2D, Flatten, merge, Deconvolution2D, Activation, BatchNormalization
from keras.regularizers import l1, l2
from keras.layers.advanced_activations import LeakyReLU

leakyrelu_alpha = 0.2

def dense_block(dims, wd, use_bn, activation):
    layers = []
    for dim in dims:
        layers.append(Dense(dim, kernel_regularizer=l2(wd)))
        if use_bn:
            layers.append(BatchNormalization()) # TODO think about mode (maybe mode=2)
        if activation == "leakyrelu":
            layers.append(LeakyReLU(alpha=leakyrelu_alpha))
        else:
            layers.append(Activation(activation))
    return layers

def conv_block(channels, kernelX, kernelY, wd, use_bn, activation, subsample, border_mode):
    layers = []
    for channel in channels:
        layers.append(Convolution2D(channel, (kernelX, kernelY), strides=subsample, border_mode=border_mode, kernel_regularizer=l2(wd)))
        if use_bn:
            layers.append(BatchNormalization())
        layers.append(Activation(activation))
    return layers
