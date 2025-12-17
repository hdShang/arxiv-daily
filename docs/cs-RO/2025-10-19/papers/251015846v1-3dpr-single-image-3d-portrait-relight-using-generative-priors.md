---
layout: default
title: 3DPR: Single Image 3D Portrait Relight using Generative Priors
---

# 3DPR: Single Image 3D Portrait Relight using Generative Priors

**arXiv**: [2510.15846v1](https://arxiv.org/abs/2510.15846) | [PDF](https://arxiv.org/pdf/2510.15846.pdf)

**作者**: Pramod Rao, Abhimitra Meka, Xilong Zhou, Gereon Fox, Mallikarjun B R, Fangneng Zhan, Tim Weyrich, Bernd Bickel, Hanspeter Pfister, Wojciech Matusik, Thabo Beeler, Mohamed Elgharib, Marc Habermann, Christian Theobalt

---

## 💡 一句话要点

**提出3DPR方法，利用生成先验从单张肖像图像实现高质量3D重光照**

**关键词**: `3D肖像重光照` `生成先验` `光阶段数据集` `反射网络` `图像嵌入` `环境重光照`

## 📋 核心要点

1. 核心问题：单张肖像图像重光照是欠约束问题，传统方法受限于几何、材质和光照分解的假设
2. 方法要点：结合生成头部模型的几何先验和光阶段数据训练的反射网络，合成高保真OLAT图像
3. 实验或效果：在身份保持和光照效果（如镜面反射、自阴影）上优于先前方法，支持物理准确环境重光照

## 📄 摘要（原文）

> Rendering novel, relit views of a human head, given a monocular portrait
> image as input, is an inherently underconstrained problem. The traditional
> graphics solution is to explicitly decompose the input image into geometry,
> material and lighting via differentiable rendering; but this is constrained by
> the multiple assumptions and approximations of the underlying models and
> parameterizations of these scene components. We propose 3DPR, an image-based
> relighting model that leverages generative priors learnt from multi-view
> One-Light-at-A-Time (OLAT) images captured in a light stage. We introduce a new
> diverse and large-scale multi-view 4K OLAT dataset of 139 subjects to learn a
> high-quality prior over the distribution of high-frequency face reflectance. We
> leverage the latent space of a pre-trained generative head model that provides
> a rich prior over face geometry learnt from in-the-wild image datasets. The
> input portrait is first embedded in the latent manifold of such a model through
> an encoder-based inversion process. Then a novel triplane-based reflectance
> network trained on our lightstage data is used to synthesize high-fidelity OLAT
> images to enable image-based relighting. Our reflectance network operates in
> the latent space of the generative head model, crucially enabling a relatively
> small number of lightstage images to train the reflectance model. Combining the
> generated OLATs according to a given HDRI environment maps yields physically
> accurate environmental relighting results. Through quantitative and qualitative
> evaluations, we demonstrate that 3DPR outperforms previous methods,
> particularly in preserving identity and in capturing lighting effects such as
> specularities, self-shadows, and subsurface scattering. Project Page:
> https://vcai.mpi-inf.mpg.de/projects/3dpr/

