pip3 install -r requirements.txt
cd sounder
pip3 install --upgrade scipy
pip3 install --upgrade numpy
pip3 install --upgrade pybind11
pip3 install numpy==2.1
cd sounder
export CFLAGS=-I/usr/local/lib/python3.10/dist-packages/numpy/_core/include/