import rasterio
import numpy as np
import matplotlib.pyplot as plt


def read_elevation_raster(file_path='elevation.tiff'):
    """
    Read elevation raster data from a GeoTIFF file.

    Parameters:
    file_path (str): Path to the raster file

    Returns:
    tuple: (data, transform, crs, bounds)
    """
    try:
        with rasterio.open(file_path) as src:
            # Read the raster data
            data = src.read(1)  # Read the first band

            # Get metadata
            transform = src.transform
            crs = src.crs
            bounds = src.bounds

            print("Raster loaded successfully!")
            print(f"Shape: {data.shape}")
            print(f"Data type: {data.dtype}")
            print(f"Coordinate Reference System: {crs}")
            print(f"Bounds: {bounds}")
            print(f"Transform: {transform}")
            print(f"Min elevation: {np.nanmin(data):.2f}")
            print(f"Max elevation: {np.nanmax(data):.2f}")
            print(f"Mean elevation: {np.nanmean(data):.2f}")

            return data, transform, crs, bounds

    except Exception as e:
        print(f"Error reading raster file: {e}")
        return None, None, None, None


def plot_elevation(data, nx, ny):
    """
    Plot the elevation data.

    Parameters:
    data (numpy.ndarray): Elevation data
    title (str): Plot title
    """
    plt.figure(figsize=(10, 8))
    plt.imshow(data, cmap='terrain')
    plt.contour(data, cmap='terrain')

    x, y = np.meshgrid(np.arange(data.shape[0]), np.arange(data.shape[1]))
    downsample = 50
    plt.colorbar(label='Elevation')
    plt.title("Elevation Data")
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.show()


# Read the elevation raster
data, transform, crs, bounds = read_elevation_raster()
x, y = np.meshgrid(np.arange(data.shape[0]), np.arange(data.shape[1]))
nx, ny = np.gradient(data)
dx, dy = np.gradient(data)
laplacian = (
    np.gradient(np.gradient(data, axis=0), axis=0) +
    np.gradient(np.gradient(data, axis=1), axis=1))


plt.close(1)
fig = plt.figure(1)
ax = fig.add_subplot(111, aspect='equal')
# img = ax.imshow(data, cmap='terrain')
# ctr = ax.contour(data, np.arange(-100, 700, 100), colors='black')
downsample = 1
bounds = (1, -1)
q_ones = ax.quiver(x[bounds[0]:bounds[1]:downsample, bounds[0]:bounds[1]:downsample], y[bounds[0]:bounds[1]:downsample, bounds[0]:bounds[1]:downsample], dx[bounds[0]:bounds[1]:downsample, bounds[0]:bounds[1]:downsample], dy[bounds[0]:bounds[1]:downsample, bounds[0]:bounds[1]:downsample], width=0.001, headwidth=0.01)
plt.colorbar(img, ax=ax)
fig.show()
