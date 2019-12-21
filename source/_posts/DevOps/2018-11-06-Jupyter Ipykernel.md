---
layout: post
categories: DevOps
date: 2018-11-06
tag: [] 



---



## Conda

```bash
list all env:

conda info --env

create a simple virtual env:

conda create -n YourEnvName python=3*

delete virtual env

conda env remove -n NAME


```



## Jupyter

```bash
source activate myenv
pip install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

*Installed kernelspec joe_segmentation_36 in /mnt/raid1/home/huangjiancong/.local/share/jupyter/kernels/joe_segmentation_36*



```bash
(joe4_py36) xxx@hpc4:~$ python -m ipykernel install --user --name joe4_py36_kernel --display-name "Joe4_Py36_Kernel"
```

*Installed kernelspec joe4_py36_kernel in /mnt/raid4/home/huangjiancong/.local/share/jupyter/kernels/joe4_py36_kernel*