Installation
------------

Create a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We recommend creating a virtual environment using Python 3.11::

    conda create -n tiscope python=3.11
    conda activate tiscope

Install PyTorch
~~~~~~~~~~~~~~~

Install PyTorch following the `PyTorch installation guide <https://pytorch.org/get-started/locally/>`_.
For example, on a machine with CUDA 12.x::

    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126

Install PyTorch Geometric
~~~~~~~~~~~~~~~~~~~~~~~~~~

Install PyG following the `PyG installation guide <https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html>`_.
Usually::

    pip install torch_geometric

Install dependencies
~~~~~~~~~~~~~~~~~~~~

::

    pip install 'scanpy[leiden]' louvain squidpy ipykernel

Install TISCOPE
~~~~~~~~~~~~~~~

Via PyPI::

    pip install tiscope

Or from GitHub::

    git clone git://github.com/ericli0419/TISCOPE.git
    cd TISCOPE
    pip install -e .
