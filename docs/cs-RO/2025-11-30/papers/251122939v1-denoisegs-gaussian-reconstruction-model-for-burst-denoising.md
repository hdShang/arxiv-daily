---
layout: default
title: DenoiseGS: Gaussian Reconstruction Model for Burst Denoising
---

# DenoiseGS: Gaussian Reconstruction Model for Burst Denoising

**arXiv**: [2511.22939v1](https://arxiv.org/abs/2511.22939) | [PDF](https://arxiv.org/pdf/2511.22939.pdf)

**作者**: Yongsen Cheng, Yuanhao Cai, Yulun Zhang

---

## 💡 一句话要点

**提出DenoiseGS框架，利用3D高斯溅射高效处理手持设备拍摄的突发去噪问题。**

**关键词**: `突发去噪` `3D高斯溅射` `高斯自一致性损失` `log加权频率损失` `新视角合成` `高效推理`

## 📋 核心要点

1. 核心问题：突发去噪方法在大运动或高计算成本下表现不佳。
2. 方法要点：引入高斯自一致性损失和log加权频率损失，提升噪声输入下的重建质量。
3. 实验或效果：在突发去噪和噪声条件下的新视角合成中超越现有方法，推理速度提升250倍。

## 📄 摘要（原文）

> Burst denoising methods are crucial for enhancing images captured on handheld devices, but they often struggle with large motion or suffer from prohibitive computational costs. In this paper, we propose DenoiseGS, the first framework to leverage the efficiency of 3D Gaussian Splatting for burst denoising. Our approach addresses two key challenges when applying feedforward Gaussian reconsturction model to noisy inputs: the degradation of Gaussian point clouds and the loss of fine details. To this end, we propose a Gaussian self-consistency (GSC) loss, which regularizes the geometry predicted from noisy inputs with high-quality Gaussian point clouds. These point clouds are generated from clean inputs by the same model that we are training, thereby alleviating potential bias or domain gaps. Additionally, we introduce a log-weighted frequency (LWF) loss to strengthen supervision within the spectral domain, effectively preserving fine-grained details. The LWF loss adaptively weights frequency discrepancies in a logarithmic manner, emphasizing challenging high-frequency details. Extensive experiments demonstrate that DenoiseGS significantly exceeds the state-of-the-art NeRF-based methods on both burst denoising and novel view synthesis under noisy conditions, while achieving \textbf{250$\times$} faster inference speed. Code and models are released at https://github.com/yscheng04/DenoiseGS.

