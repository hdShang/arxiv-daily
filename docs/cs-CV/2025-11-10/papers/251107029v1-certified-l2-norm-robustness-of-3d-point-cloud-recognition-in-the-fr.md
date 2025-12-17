---
layout: default
title: Certified L2-Norm Robustness of 3D Point Cloud Recognition in the Frequency Domain
---

# Certified L2-Norm Robustness of 3D Point Cloud Recognition in the Frequency Domain

**arXiv**: [2511.07029v1](https://arxiv.org/abs/2511.07029) | [PDF](https://arxiv.org/pdf/2511.07029.pdf)

**作者**: Liang Zhou, Qiming Wang, Tianze Chen

---

## 💡 一句话要点

**提出FreqCert框架以解决3D点云识别在安全关键应用中的对抗扰动问题**

**关键词**: `3D点云识别` `频域鲁棒性` `图傅里叶变换` `认证防御` `L2范数扰动`

## 📋 核心要点

1. 3D点云分类易受结构化对抗扰动和几何破坏影响，现有认证防御忽略全局几何失真
2. FreqCert在频域分析鲁棒性，使用图傅里叶变换和谱相似性子采样结合多数投票
3. 在ModelNet40和ScanObjectNN数据集上，FreqCert实现更高认证精度和实证精度

## 📄 摘要（原文）

> 3D point cloud classification is a fundamental task in safety-critical
> applications such as autonomous driving, robotics, and augmented reality.
> However, recent studies reveal that point cloud classifiers are vulnerable to
> structured adversarial perturbations and geometric corruptions, posing risks to
> their deployment in safety-critical scenarios. Existing certified defenses
> limit point-wise perturbations but overlook subtle geometric distortions that
> preserve individual points yet alter the overall structure, potentially leading
> to misclassification. In this work, we propose FreqCert, a novel certification
> framework that departs from conventional spatial domain defenses by shifting
> robustness analysis to the frequency domain, enabling structured certification
> against global L2-bounded perturbations. FreqCert first transforms the input
> point cloud via the graph Fourier transform (GFT), then applies structured
> frequency-aware subsampling to generate multiple sub-point clouds. Each
> sub-cloud is independently classified by a standard model, and the final
> prediction is obtained through majority voting, where sub-clouds are
> constructed based on spectral similarity rather than spatial proximity, making
> the partitioning more stable under L2 perturbations and better aligned with the
> object's intrinsic structure. We derive a closed-form lower bound on the
> certified L2 robustness radius and prove its tightness under minimal and
> interpretable assumptions, establishing a theoretical foundation for frequency
> domain certification. Extensive experiments on the ModelNet40 and ScanObjectNN
> datasets demonstrate that FreqCert consistently achieves higher certified
> accuracy and empirical accuracy under strong perturbations. Our results suggest
> that spectral representations provide an effective pathway toward certifiable
> robustness in 3D point cloud recognition.

