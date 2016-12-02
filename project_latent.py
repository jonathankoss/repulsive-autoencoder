import matplotlib
import numpy as np
import numpy.linalg
from sklearn.random_projection import GaussianRandomProjection
import matplotlib.pyplot as plt

import vis
import data
import model

# rae, 200 dim hidden space, 200 epoch, bw images,
modelname = "rae"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 64)
batch_size = 200
do_latent_variances = False
color = False

# conv vae, 200 dim hidden space, 200 epoch, color images, xent loss has weight 100
"""
modelname = "vae_conv_xent1"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 64)
batch_size = 200
do_latent_variances = True
color = True
"""

# vae, 200 dim hidden space, 100 epoch, bw images, xent loss has weight 100
"""
modelname = "vae"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 64)
batch_size = 200
do_latent_variances = True
color = False
"""

# simple vae with dense encoder/decoder, 3 dim hidden space
"""
modelname = "vae_var_3"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 60)
batch_size = 1000
do_latent_variances = True
"""

# simple vae with dense encoder/decoder, 100 dim hidden space
"""
modelname = "vae_var_100"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 60)
batch_size = 1000
do_latent_variances = True
"""
# conv vae, 200 dim hidden space, 200 epoch, color images, hidden variables have been sampled
"""
modelname = "vae_conv_dim200"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 60)
batch_size = 200
do_latent_variances = True
color = True
"""

# dense vae, 600 dim hidden space, 200 epoch, color images, hidden variables have been sampled
"""
modelname = "vae_color_dim600"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 64)
batch_size = 200
do_latent_variances = True
color = True
"""

# conv vae, 200 dim hidden space, 30 epoch, color images, hidden variables have been sampled, leaky relu
"""
modelname = "vae_conv_leaky_dim200"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 64)
batch_size = 200
do_latent_variances = True
color = True
"""

# conv vae, 200 dim hidden space, 100 epoch, color images, hidden variables have been sampled, L2 norm after edge detection
"""
modelname = "vae_conv_outline_dim200"
prefix = "/home/zombori/latent/" + modelname
encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder")
encoder_var = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_encoder_var")
generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/" + modelname + "_generator")
shape = (72, 64)
batch_size = 200
do_latent_variances = True
color = True
"""

#encoder = vis.loadModel("/home/csadrian/repulsive-autoencoder/models/disc_3_1000_d2_vae/disc_3_1000_d2_vae_encoder")
#generator = vis.loadModel("/home/csadrian/repulsive-autoencoder/models/disc_3_1000_d2_vae/disc_3_1000_d2_vae_generator")
#shape = (72, 60)
#batch_size = 250
#do_latent_variances = False


#simple vae trained for 300 epoch, latent representation has zero variance
#encoder = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/vae_baseline_300_encoder")
#generator = vis.loadModel("/home/zombori/repulsive-autoencoder/pictures/vae_baseline_300_generator")
# shape = (72, 60)
#batch_size = 1000
#do_latent_variances = False


# encoder = vis.loadModel("/home/csadrian/repulsive-autoencoder/models/disc_3_1000_d2_vae/disc_3_1000_d2_vae_encoder")
# generator = vis.loadModel("/home/csadrian/repulsive-autoencoder/models/disc_3_1000_d2_vae/disc_3_1000_d2_vae_generator")
# batch_size = 250
# do_latent_variances = False

# encoder = vis.loadModel("/home/csadrian/repulsive-autoencoder/models/disc_3_1000_d3_vae/disc_3_1000_d3_vae_encoder")
# generator = vis.loadModel("/home/csadrian/repulsive-autoencoder/models/disc_3_1000_d3_vae/disc_3_1000_d3_vae_generator")
# batch_size = 250
# do_latent_variances = False

#encoder = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_vae_encoder")
#generator = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_vae_generator")
#shape = (72, 64)
#batch_size = 250
#do_latent_variances = False


# modelname = "disc_l50_e300_d2_nvae"
# prefix = "/home/csadrian/repulsive-autoencoder/" + modelname
# encoder = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_nvae_encoder")
# encoder_var = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_nvae_encoder_var")
# generator = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_nvae_generator")
# shape = (72, 60)
# batch_size = 250
# do_latent_variances = True


"""
shape = (72, 60)
modelname = "disc_l50_e300_d2_nvae_cov"
prefix = "/home/csadrian/repulsive-autoencoder/" + modelname
encoder = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_nvae_cov_encoder")
encoder_var = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_nvae_cov_encoder_var")
generator = vis.loadModel("/home/csadrian/repulsive-autoencoder/disc_l50_e300_d2_nvae_cov_generator")
batch_size = 250
do_latent_variances = True
"""

(x_train, x_test) = data.load("celeba", shape=shape, color=color)
latent_train = encoder.predict(x_train, batch_size = batch_size)
latent_test = encoder.predict(x_test, batch_size = batch_size)


if do_latent_variances:
    latent_train_mean = encoder.predict(x_train, batch_size = batch_size)
    latent_test_mean = encoder.predict(x_test, batch_size = batch_size)

    latent_train_logvar = encoder_var.predict(x_train, batch_size = batch_size)
    latent_test_logvar = encoder_var.predict(x_test, batch_size = batch_size)

    latent_train = np.random.normal(size=latent_train_mean.shape) * np.exp(latent_train_logvar/2) + latent_train_mean
    latent_test = np.random.normal(size=latent_test_mean.shape) * np.exp(latent_test_logvar/2) + latent_test_mean

    np.savez(prefix + "_train_latent_mean.npz", latent_train_mean)
    np.savez(prefix + "_train_latent_logvar.npz", latent_train_logvar)
    np.savez(prefix + "_train_latent.npz", latent_train)
    np.savez(prefix + "_test_latent.npz", latent_test)

    mean_variances = np.var(latent_train_mean, axis=0)
    variance_means = np.mean(np.exp(latent_train_logvar), axis=0)
    plt.scatter(mean_variances, variance_means)
    plt.savefig(prefix+"_mvvm.png")
    print "Mean variances"
    print np.histogram(mean_variances)    
    variances = np.var(latent_train, axis=0)
    
    
variances = np.var(latent_train, axis=0)
working_mask = (variances > 0.2)
print "Variances"
print np.sum(working_mask), "/", working_mask.shape
print np.histogram(variances, 100)

n = latent_train.shape[1]

def masked_sampler(batch_size, latent_dim):
    z = np.random.normal(size=(batch_size, latent_dim))
    return z * working_mask

vis.displayRandom(n=20, x_train=x_train, latent_dim=n, sampler=masked_sampler,
        generator=generator, name=prefix + "_masked", batch_size=batch_size)


# projector = GaussianRandomProjection(n_components=2, random_state=81)
# projected_train = projector.fit_transform(latent_train)
# projected_test = projector.fit_transform(latent_test)

projected_train = latent_train[:, [0,1]]
projected_test = latent_test[:, [0,1]]

mymin = np.min((np.min(projected_train), np.min(projected_test)))
mymax = np.max((np.max(projected_train), np.max(projected_test)))
dim = np.max(np.abs((mymin,mymax)))

plt.figure(figsize=(14,6))
ax1 = plt.subplot(121)
ax1.hexbin( projected_train[:, 0], projected_train[:, 1])
plt.xlim(-dim,dim)
plt.ylim(-dim,dim)
ax2 = plt.subplot(122)
ax2.hexbin( projected_test[:, 0], projected_test[:, 1])
plt.xlim(-dim,dim)
plt.ylim(-dim,dim)
plt.savefig(prefix + "_hexbin.png")

corr_train = np.corrcoef(latent_train.T)
corr_test = np.corrcoef(latent_test.T)

plt.figure(figsize=(12,24))
ax1 = plt.subplot(211)
ax1.matshow(np.abs(corr_train), cmap='coolwarm')
ax2 = plt.subplot(212)
ax2.matshow(np.abs(corr_test), cmap='coolwarm')
plt.savefig(prefix + "_corr.png")

cov_train = np.cov(latent_train.T)
eigvals = list(np.linalg.eigvals(cov_train).real)
print "cov_train eigvals = ", sorted(eigvals, reverse=True)


print "CS", cov_train.shape
mean_train = np.mean(latent_train, axis=0)
print "MS", mean_train.shape
cho = np.linalg.cholesky(cov_train)
print "CHOS", cho.shape
N = 100000
z = np.random.normal(0.0, 1.0, (N, n))
sample = cho.dot(z.T).T+mean_train
print sample.shape

corr_learned = np.corrcoef(sample.T)
plt.figure(figsize=(12,24))
ax1 = plt.subplot(211)
ax1.matshow(np.abs(corr_train), cmap='coolwarm')
ax2 = plt.subplot(212)
ax2.matshow(np.abs(corr_learned), cmap='coolwarm')
plt.savefig(prefix + "_corr_learned.png")


# vis.displayRandom(n=20, x_train=x_train, latent_dim=n, sampler=model.spherical_sampler,
#        generator=generator, name=prefix + "_standard", batch_size=batch_size)

def oval_sampler(batch_size, latent_dim):
    z = np.random.normal(size=(batch_size, latent_dim))
    z = cho.dot(z.T).T+mean_train
#    z /= np.linalg.norm(z)
    return z

eigs = np.linalg.eig(cov_train)
eigVal = eigs[0][0]
eigVect = eigs[1][0]
def eigval_sampler(batch_size, latent_dim):
    x = np.linspace(-1.0, 1.0, num=batch_size)
    xs = []
    for i in range(batch_size):
        xi = x[i] * eigVect * np.sqrt(eigVal) + mean_train
        xs.append(xi)
    print xs
    return np.array(xs)

vis.displayRandom(n=20, x_train=x_train, latent_dim=n, sampler=eigval_sampler,
        generator=generator, name=prefix + "_eigval", batch_size=batch_size)
vis.displayRandom(n=20, x_train=x_train, latent_dim=n, sampler=oval_sampler,
        generator=generator, name=prefix + "_oval", batch_size=batch_size)

xxx
do_tsne = True

if do_tsne:
    from sklearn.manifold import TSNE
    import sklearn
    tsne = TSNE(n_components=2, random_state=42, perplexity=100, metric="euclidean")
    n = 5000
    latent_train_sampled = latent_train[np.random.choice(latent_train.shape[0], size=n, replace=False)]
    # print latent_train_sampled[0, :]
    # print latent_train_sampled[:, 0]
    reduced = tsne.fit_transform(latent_train_sampled)

    plt.figure(figsize=(12,12))
    plt.scatter(reduced[:, 0], reduced[:, 1])
    plt.savefig(prefix + "_tsne.png")
