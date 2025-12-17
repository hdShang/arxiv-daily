---
layout: default
title: A Lightweight 3D-CNN for Event-Based Human Action Recognition with Privacy-Preserving Potential
---

# A Lightweight 3D-CNN for Event-Based Human Action Recognition with Privacy-Preserving Potential

**arXiv**: [2511.03665v1](https://arxiv.org/abs/2511.03665) | [PDF](https://arxiv.org/pdf/2511.03665.pdf)

**作者**: Mehdi Sefidgar Dilmaghani, Francis Fowley, Peter Corcoran

---

## 💡 一句话要点

**提出轻量3D-CNN用于事件相机的人类动作识别，兼顾隐私保护与边缘部署。**

**关键词**: `事件相机` `人类动作识别` `3D卷积神经网络` `隐私保护` `边缘计算` `焦点损失`

## 📋 核心要点

1. 核心问题：传统相机在人类监测中易泄露隐私，事件相机仅记录像素变化以保护隐私。
2. 方法要点：设计轻量3D-CNN建模时空动态，采用焦点损失与数据增强应对类别不平衡。
3. 实验或效果：在复合数据集上F1分数0.9415，准确率94.17%，优于基准模型达3%。

## 📄 摘要（原文）

> This paper presents a lightweight three-dimensional convolutional neural
> network (3DCNN) for human activity recognition (HAR) using event-based vision
> data. Privacy preservation is a key challenge in human monitoring systems, as
> conventional frame-based cameras capture identifiable personal information. In
> contrast, event cameras record only changes in pixel intensity, providing an
> inherently privacy-preserving sensing modality. The proposed network
> effectively models both spatial and temporal dynamics while maintaining a
> compact design suitable for edge deployment. To address class imbalance and
> enhance generalization, focal loss with class reweighting and targeted data
> augmentation strategies are employed. The model is trained and evaluated on a
> composite dataset derived from the Toyota Smart Home and ETRI datasets.
> Experimental results demonstrate an F1-score of 0.9415 and an overall accuracy
> of 94.17%, outperforming benchmark 3D-CNN architectures such as C3D, ResNet3D,
> and MC3_18 by up to 3%. These results highlight the potential of event-based
> deep learning for developing accurate, efficient, and privacy-aware human
> action recognition systems suitable for real-world edge applications.

