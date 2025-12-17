---
layout: default
title: WWE-UIE: A Wavelet & White Balance Efficient Network for Underwater Image Enhancement
---

# WWE-UIE: A Wavelet & White Balance Efficient Network for Underwater Image Enhancement

**arXiv**: [2511.16321v1](https://arxiv.org/abs/2511.16321) | [PDF](https://arxiv.org/pdf/2511.16321.pdf)

**作者**: Ching-Heng Cheng, Jen-Wei Lee, Chia-Ming Lee, Chih-Chung Hsu

---

## 💡 一句话要点

**提出WWE-UIE网络，结合小波与白平衡先验，高效增强水下图像并实现实时推理。**

**关键词**: `水下图像增强` `小波分解` `白平衡校正` `梯度感知` `高效网络` `实时推理`

## 📋 核心要点

1. 水下图像因波长吸收和散射导致可见性差和颜色失真，现有方法计算成本高。
2. 方法集成自适应白平衡、小波分解和梯度感知模块，提升颜色和结构恢复。
3. 实验显示参数和FLOPs显著减少，在基准数据集上实现竞争性恢复质量。

## 📄 摘要（原文）

> Underwater Image Enhancement (UIE) aims to restore visibility and correct color distortions caused by wavelength-dependent absorption and scattering. Recent hybrid approaches, which couple domain priors with modern deep neural architectures, have achieved strong performance but incur high computational cost, limiting their practicality in real-time scenarios. In this work, we propose WWE-UIE, a compact and efficient enhancement network that integrates three interpretable priors. First, adaptive white balance alleviates the strong wavelength-dependent color attenuation, particularly the dominance of blue-green tones. Second, a wavelet-based enhancement block (WEB) performs multi-band decomposition, enabling the network to capture both global structures and fine textures, which are critical for underwater restoration. Third, a gradient-aware module (SGFB) leverages Sobel operators with learnable gating to explicitly preserve edge structures degraded by scattering. Extensive experiments on benchmark datasets demonstrate that WWE-UIE achieves competitive restoration quality with substantially fewer parameters and FLOPs, enabling real-time inference on resource-limited platforms. Ablation studies and visualizations further validate the contribution of each component. The source code is available at https://github.com/chingheng0808/WWE-UIE.

