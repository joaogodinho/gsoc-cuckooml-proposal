from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from os import listdir, makedirs
from os.path import join
import matplotlib.pyplot as plt
import numpy as np


APISTATS_DIR = 'apistats/'
IMAGES_DIR = 'img/'


# Returns a list with the path for all reports
def listReportsPath():
    paths = []
    for f in listdir(APISTATS_DIR):
        paths.append(join(APISTATS_DIR, f))
    return paths


def cluster(apistats, size=5):
    # Turn the calls into a vector
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform((open(f).read() for f in apistats))

    # Clustering with KMeans
    n_clusters = size
    km = KMeans(n_clusters=n_clusters)
    print('Clustering api calls with {} clusters...'.format(n_clusters))
    reduced_data = PCA(n_components=2).fit_transform(X.toarray())
    km.fit(reduced_data)

    # The following code was based in:
    # http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#example-cluster-plot-kmeans-digits-py
    # Calculate the decision boundary

    # Plot the decision boundary. For that, we will assign a color to each
    h = .02
    x_min, x_max = reduced_data[:, 0].min() - 0.1, reduced_data[:, 0].max() + 0.1
    y_min, y_max = reduced_data[:, 1].min() - 0.1, reduced_data[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = km.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)

    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')
    # Plot the data
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=3)
    # Plot the centroids
    centroids = km.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='w', linewidths=2, zorder=10)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.savefig(IMAGES_DIR + 'clustering' + str(size))


def main():
    try:
        makedirs(IMAGES_DIR)
    except:
        # Directory already exists
        pass

    apistats = listReportsPath()
    for i in range(2, 10):
        cluster(apistats, size=i)


if __name__ == '__main__':
    main()
