---
layout: default
title: iRadioDiff: Physics-Informed Diffusion Model for Indoor Radio Map Construction and Localization
---

# iRadioDiff: Physics-Informed Diffusion Model for Indoor Radio Map Construction and Localization

**arXiv**: [2511.20015v1](https://arxiv.org/abs/2511.20015) | [PDF](https://arxiv.org/pdf/2511.20015.pdf)

**作者**: Xiucheng Wang, Tingwei Yuan, Yang Cao, Nan Cheng, Ruijin Sun, Weihua Zhuang

---

## 💡 一句话要点

**提出iRadioDiff扩散模型以解决室内无线电地图构建与定位问题**

**关键词**: `室内无线电地图` `扩散模型` `物理信息学习` `多路径建模` `信号强度定位`

## 📋 核心要点

1. 核心问题：室内无线电地图构建受限于电磁求解器延迟和学习方法对稀疏测量或均匀材料的依赖。
2. 方法要点：基于扩散模型，结合物理先验和多路径关键信息，实现无采样生成。
3. 实验或效果：在室内无线电地图构建和定位中达到先进性能，并具有跨布局泛化能力。

## 📄 摘要（原文）

> Radio maps (RMs) serve as environment-aware electromagnetic (EM) representations that connect scenario geometry and material properties to the spatial distribution of signal strength, enabling localization without costly in-situ measurements. However, constructing high-fidelity indoor RMs remains challenging due to the prohibitive latency of EM solvers and the limitations of learning-based methods, which often rely on sparse measurements or assumptions of homogeneous material, which are misaligned with the heterogeneous and multipath-rich nature of indoor environments. To overcome these challenges, we propose iRadioDiff, a sampling-free diffusion-based framework for indoor RM construction. iRadioDiff is conditioned on access point (AP) positions, and physics-informed prompt encoded by material reflection and transmission coefficients. It further incorporates multipath-critical priors, including diffraction points, strong transmission boundaries, and line-of-sight (LoS) contours, to guide the generative process via conditional channels and boundary-weighted objectives. This design enables accurate modeling of nonstationary field discontinuities and efficient construction of physically consistent RMs. Experiments demonstrate that iRadioDiff achieves state-of-the-art performance in indoor RM construction and received signal strength based indoor localization, which offers effective generalization across layouts and material configurations. Code is available at https://github.com/UNIC-Lab/iRadioDiff.

