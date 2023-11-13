ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --assume-yes \
    wget \
    ocl-icd-libopencl1

RUN mkdir -p /etc/OpenCL/vendors && \
    echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd
