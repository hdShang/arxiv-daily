---
layout: default
title: HBFormer: A Hybrid-Bridge Transformer for Microtumor and Miniature Organ Segmentation
---

# HBFormer: A Hybrid-Bridge Transformer for Microtumor and Miniature Organ Segmentation

**arXiv**: [2512.03597v1](https://arxiv.org/abs/2512.03597) | [PDF](https://arxiv.org/pdf/2512.03597.pdf)

**作者**: Fuchen Zheng, Xinyi Chen, Weixuan Li, Quanjun Li, Junhua Zhou, Xiaojiao Guo, Xuhang Chen, Chi-Man Pun, Shoujun Zhou

---

## 💡 一句话要点

**提出HBFormer混合桥接Transformer，以解决医学图像中微肿瘤和微型器官分割的局部与全局特征融合问题。**

**关键词**: `医学图像分割` `Transformer架构` `多尺度特征融合` `微肿瘤分割` `注意力机制` `编码器-解码器框架`

## 📋 核心要点

1. 核心问题：现有Vision Transformer的局部注意力机制难以有效融合局部细节与全局上下文，影响微肿瘤和微型器官分割精度。
2. 方法要点：HBFormer结合U形编码器-解码器框架与Swin Transformer骨干，通过多尺度特征融合解码器桥接多尺度特征与全局信息。
3. 实验或效果：在多个医学图像分割数据集上实现最先进结果，验证了其在微肿瘤和微型器官分割中的卓越能力。

## 📄 摘要（原文）

> Medical image segmentation is a cornerstone of modern clinical diagnostics. While Vision Transformers that leverage shifted window-based self-attention have established new benchmarks in this field, they are often hampered by a critical limitation: their localized attention mechanism struggles to effectively fuse local details with global context. This deficiency is particularly detrimental to challenging tasks such as the segmentation of microtumors and miniature organs, where both fine-grained boundary definition and broad contextual understanding are paramount. To address this gap, we propose HBFormer, a novel Hybrid-Bridge Transformer architecture. The 'Hybrid' design of HBFormer synergizes a classic U-shaped encoder-decoder framework with a powerful Swin Transformer backbone for robust hierarchical feature extraction. The core innovation lies in its 'Bridge' mechanism, a sophisticated nexus for multi-scale feature integration. This bridge is architecturally embodied by our novel Multi-Scale Feature Fusion (MFF) decoder. Departing from conventional symmetric designs, the MFF decoder is engineered to fuse multi-scale features from the encoder with global contextual information. It achieves this through a synergistic combination of channel and spatial attention modules, which are constructed from a series of dilated and depth-wise convolutions. These components work in concert to create a powerful feature bridge that explicitly captures long-range dependencies and refines object boundaries with exceptional precision. Comprehensive experiments on challenging medical image segmentation datasets, including multi-organ, liver tumor, and bladder tumor benchmarks, demonstrate that HBFormer achieves state-of-the-art results, showcasing its outstanding capabilities in microtumor and miniature organ segmentation. Code and models are available at: https://github.com/lzeeorno/HBFormer.

