---
layout: default
title: PET Head Motion Estimation Using Supervised Deep Learning with Attention
---

# PET Head Motion Estimation Using Supervised Deep Learning with Attention

**arXiv**: [2510.12758v1](https://arxiv.org/abs/2510.12758) | [PDF](https://arxiv.org/pdf/2510.12758.pdf)

**作者**: Zhuotong Cai, Tianyi Zeng, Jiazhen Zhang, Eléonore V. Lieffrig, Kathryn Fontaine, Chenyu You, Enette Mae Revilla, James S. Duncan, Jingmin Xin, Yihuan Lu, John A. Onofrey

---

## 💡 一句话要点

**提出基于注意力机制的深度学习模型DL-HMC++，用于PET头部运动估计与校正。**

**关键词**: `PET成像` `头部运动校正` `深度学习` `注意力机制` `监督学习` `医学图像分析`

## 📋 核心要点

1. 头部运动导致PET成像伪影和定量误差，影响神经疾病诊断。
2. 使用监督学习和交叉注意力，从3D PET原始数据预测刚性头部运动。
3. 在多种扫描器和示踪剂上验证，性能优于现有方法，接近金标准。

## 📄 摘要（原文）

> Head movement poses a significant challenge in brain positron emission
> tomography (PET) imaging, resulting in image artifacts and tracer uptake
> quantification inaccuracies. Effective head motion estimation and correction
> are crucial for precise quantitative image analysis and accurate diagnosis of
> neurological disorders. Hardware-based motion tracking (HMT) has limited
> applicability in real-world clinical practice. To overcome this limitation, we
> propose a deep-learning head motion correction approach with cross-attention
> (DL-HMC++) to predict rigid head motion from one-second 3D PET raw data.
> DL-HMC++ is trained in a supervised manner by leveraging existing dynamic PET
> scans with gold-standard motion measurements from external HMT. We evaluate
> DL-HMC++ on two PET scanners (HRRT and mCT) and four radiotracers (18F-FDG,
> 18F-FPEB, 11C-UCB-J, and 11C-LSN3172176) to demonstrate the effectiveness and
> generalization of the approach in large cohort PET studies. Quantitative and
> qualitative results demonstrate that DL-HMC++ consistently outperforms
> state-of-the-art data-driven motion estimation methods, producing motion-free
> images with clear delineation of brain structures and reduced motion artifacts
> that are indistinguishable from gold-standard HMT. Brain region of interest
> standard uptake value analysis exhibits average difference ratios between
> DL-HMC++ and gold-standard HMT to be 1.2 plus-minus 0.5% for HRRT and 0.5
> plus-minus 0.2% for mCT. DL-HMC++ demonstrates the potential for data-driven
> PET head motion correction to remove the burden of HMT, making motion
> correction accessible to clinical populations beyond research settings. The
> code is available at https://github.com/maxxxxxxcai/DL-HMC-TMI.

