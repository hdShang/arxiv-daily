---
layout: default
title: Layer-wise Noise Guided Selective Wavelet Reconstruction for Robust Medical Image Segmentation
---

# Layer-wise Noise Guided Selective Wavelet Reconstruction for Robust Medical Image Segmentation

**arXiv**: [2511.16162v1](https://arxiv.org/abs/2511.16162) | [PDF](https://arxiv.org/pdf/2511.16162.pdf)

**作者**: Yuting Lu, Ziliang Wang, Weixin Xu, Wei Zhang, Yongqiang Zhao, Yang Yu, Xiaohong Zhang

---

## 💡 一句话要点

**提出层间噪声引导选择性小波重建以增强医学图像分割的鲁棒性**

**关键词**: `医学图像分割` `鲁棒性增强` `小波重建` `频率适应` `对抗训练` `噪声注入`

## 📋 核心要点

1. 医学图像分割模型在分布偏移和扰动下稳定性不足，主流对抗训练存在精度-鲁棒性权衡和高成本问题
2. 方法在训练中注入层间噪声学习频率偏置先验，通过选择性小波重建抑制噪声敏感频带并增强结构特征
3. 实验在CT和超声数据集上，结合或不结合对抗训练均提升干净指标并显著降低强攻击下的性能下降

## 📄 摘要（原文）

> Clinical deployment requires segmentation models to stay stable under distribution shifts and perturbations. The mainstream solution is adversarial training (AT) to improve robustness; however, AT often brings a clean--robustness trade-off and high training/tuning cost, which limits scalability and maintainability in medical imaging. We propose \emph{Layer-wise Noise-Guided Selective Wavelet Reconstruction (LNG-SWR)}. During training, we inject small, zero-mean noise at multiple layers to learn a frequency-bias prior that steers representations away from noise-sensitive directions. We then apply prior-guided selective wavelet reconstruction on the input/feature branch to achieve frequency adaptation: suppress noise-sensitive bands, enhance directional structures and shape cues, and stabilize boundary responses while maintaining spectral consistency. The framework is backbone-agnostic and adds low additional inference overhead. It can serve as a plug-in enhancement to AT and also improves robustness without AT. On CT and ultrasound datasets, under a unified protocol with PGD-$L_{\infty}/L_{2}$ and SSAH, LNG-SWR delivers consistent gains on clean Dice/IoU and significantly reduces the performance drop under strong attacks; combining LNG-SWR with AT yields additive gains. When combined with adversarial training, robustness improves further without sacrificing clean accuracy, indicating an engineering-friendly and scalable path to robust segmentation. These results indicate that LNG-SWR provides a simple, effective, and engineering-friendly path to robust medical image segmentation in both adversarial and standard training regimes.

