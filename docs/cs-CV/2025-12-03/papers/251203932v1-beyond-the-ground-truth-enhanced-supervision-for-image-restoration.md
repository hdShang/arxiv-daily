---
layout: default
title: Beyond the Ground Truth: Enhanced Supervision for Image Restoration
---

# Beyond the Ground Truth: Enhanced Supervision for Image Restoration

**arXiv**: [2512.03932v1](https://arxiv.org/abs/2512.03932) | [PDF](https://arxiv.org/pdf/2512.03932.pdf)

**作者**: Donghun Ryou, Inju Ha, Sanghyeok Chu, Bohyung Han

---

## 💡 一句话要点

**提出增强监督框架，通过自适应频率掩码融合提升真实世界图像恢复的监督质量。**

**关键词**: `图像恢复` `监督增强` `频率域融合` `自适应掩码` `输出细化网络`

## 📋 核心要点

1. 核心问题：真实世界图像恢复受限于数据集ground truth图像质量，影响模型性能。
2. 方法要点：使用条件频率掩码生成器学习自适应掩码，融合原始ground truth与超分辨率变体的频率成分，生成增强监督图像。
3. 实验或效果：增强监督训练轻量输出细化网络，提升恢复图像质量，用户研究验证有效性。

## 📄 摘要（原文）

> Deep learning-based image restoration has achieved significant success. However, when addressing real-world degradations, model performance is limited by the quality of ground-truth images in datasets due to practical constraints in data acquisition. To address this limitation, we propose a novel framework that enhances existing ground truth images to provide higher-quality supervision for real-world restoration. Our framework generates perceptually enhanced ground truth images using super-resolution by incorporating adaptive frequency masks, which are learned by a conditional frequency mask generator. These masks guide the optimal fusion of frequency components from the original ground truth and its super-resolved variants, yielding enhanced ground truth images. This frequency-domain mixup preserves the semantic consistency of the original content while selectively enriching perceptual details, preventing hallucinated artifacts that could compromise fidelity. The enhanced ground truth images are used to train a lightweight output refinement network that can be seamlessly integrated with existing restoration models. Extensive experiments demonstrate that our approach consistently improves the quality of restored images. We further validate the effectiveness of both supervision enhancement and output refinement through user studies. Code is available at https://github.com/dhryougit/Beyond-the-Ground-Truth.

