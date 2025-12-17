---
layout: default
title: SAM-Fed: SAM-Guided Federated Semi-Supervised Learning for Medical Image Segmentation
---

# SAM-Fed: SAM-Guided Federated Semi-Supervised Learning for Medical Image Segmentation

**arXiv**: [2511.14302v1](https://arxiv.org/abs/2511.14302) | [PDF](https://arxiv.org/pdf/2511.14302.pdf)

**作者**: Sahar Nasirihaghighi, Negin Ghamsarian, Yiping Li, Marcel Breeuwer, Raphael Sznitman, Klaus Schoeffmann

---

## 💡 一句话要点

**提出SAM-Fed框架，利用分割基础模型指导轻量客户端，解决医学图像分割中联邦半监督学习的伪标签不可靠问题。**

**关键词**: `医学图像分割` `联邦半监督学习` `知识蒸馏` `分割基础模型` `伪标签优化` `异构客户端`

## 📋 核心要点

1. 核心问题：医学图像分割中数据隐私和标注成本高，联邦半监督学习面临伪标签不可靠和客户端资源受限挑战。
2. 方法要点：结合双重知识蒸馏和自适应一致性机制，利用高容量分割模型指导轻量客户端训练。
3. 实验或效果：在皮肤病变和息肉分割实验中，SAM-Fed在异构和同构设置下优于现有联邦半监督学习方法。

## 📄 摘要（原文）

> Medical image segmentation is clinically important, yet data privacy and the cost of expert annotation limit the availability of labeled data. Federated semi-supervised learning (FSSL) offers a solution but faces two challenges: pseudo-label reliability depends on the strength of local models, and client devices often require compact or heterogeneous architectures due to limited computational resources. These constraints reduce the quality and stability of pseudo-labels, while large models, though more accurate, cannot be trained or used for routine inference on client devices. We propose SAM-Fed, a federated semi-supervised framework that leverages a high-capacity segmentation foundation model to guide lightweight clients during training. SAM-Fed combines dual knowledge distillation with an adaptive agreement mechanism to refine pixel-level supervision. Experiments on skin lesion and polyp segmentation across homogeneous and heterogeneous settings show that SAM-Fed consistently outperforms state-of-the-art FSSL methods.

