---
layout: default
title: D-GAP: Improving Out-of-Domain Robustness via Dataset-Agnostic and Gradient-Guided Augmentation in Amplitude and Pixel Spaces
---

# D-GAP: Improving Out-of-Domain Robustness via Dataset-Agnostic and Gradient-Guided Augmentation in Amplitude and Pixel Spaces

**arXiv**: [2511.11286v1](https://arxiv.org/abs/2511.11286) | [PDF](https://arxiv.org/pdf/2511.11286.pdf)

**作者**: Ruoqi Wang, Haitao Wang, Shaojie Guo, Qiong Luo

---

## 💡 一句话要点

**提出D-GAP方法，通过频率和像素空间增强提升模型在域外场景的鲁棒性**

**关键词**: `域外鲁棒性` `频率空间增强` `像素空间混合` `梯度引导增强` `数据集无关增强`

## 📋 核心要点

1. 核心问题：模型在域外场景中因学习偏向特定频率组件而性能下降
2. 方法要点：基于任务梯度计算频率敏感图，自适应插值振幅并混合像素细节
3. 实验或效果：在真实世界和基准数据集上平均提升OOD性能5.3%和1.8%

## 📄 摘要（原文）

> Out-of-domain (OOD) robustness is challenging to achieve in real-world computer vision applications, where shifts in image background, style, and acquisition instruments always degrade model performance. Generic augmentations show inconsistent gains under such shifts, whereas dataset-specific augmentations require expert knowledge and prior analysis. Moreover, prior studies show that neural networks adapt poorly to domain shifts because they exhibit a learning bias to domain-specific frequency components. Perturbing frequency values can mitigate such bias but overlooks pixel-level details, leading to suboptimal performance. To address these problems, we propose D-GAP (Dataset-agnostic and Gradient-guided augmentation in Amplitude and Pixel spaces), improving OOD robustness by introducing targeted augmentation in both the amplitude space (frequency space) and pixel space. Unlike conventional handcrafted augmentations, D-GAP computes sensitivity maps in the frequency space from task gradients, which reflect how strongly the model responds to different frequency components, and uses the maps to adaptively interpolate amplitudes between source and target samples. This way, D-GAP reduces the learning bias in frequency space, while a complementary pixel-space blending procedure restores fine spatial details. Extensive experiments on four real-world datasets and three domain-adaptation benchmarks show that D-GAP consistently outperforms both generic and dataset-specific augmentations, improving average OOD performance by +5.3% on real-world datasets and +1.8% on benchmark datasets.

