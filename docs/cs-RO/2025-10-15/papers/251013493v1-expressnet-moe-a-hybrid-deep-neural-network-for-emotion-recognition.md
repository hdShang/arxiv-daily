---
layout: default
title: ExpressNet-MoE: A Hybrid Deep Neural Network for Emotion Recognition
---

# ExpressNet-MoE: A Hybrid Deep Neural Network for Emotion Recognition

**arXiv**: [2510.13493v1](https://arxiv.org/abs/2510.13493) | [PDF](https://arxiv.org/pdf/2510.13493.pdf)

**作者**: Deeptimaan Banerjee, Prateek Gothwal, Ashis Kumer Biswas

---

## 💡 一句话要点

**提出ExpressNet-MoE混合深度学习模型以解决面部情感识别中的泛化与适应性问题**

**关键词**: `面部情感识别` `混合深度学习` `CNN` `MoE框架` `多尺度特征提取` `自适应模型`

## 📋 核心要点

1. 面部情感识别在真实场景中面临头部姿态、遮挡和光照变化等挑战
2. 模型结合CNN与MoE框架，动态选择专家网络，实现多尺度特征提取
3. 在多个数据集上评估，准确率优于现有方法，如AffectNet达74.77%

## 📄 摘要（原文）

> In many domains, including online education, healthcare, security, and
> human-computer interaction, facial emotion recognition (FER) is essential.
> Real-world FER is still difficult despite its significance because of some
> factors such as variable head positions, occlusions, illumination shifts, and
> demographic diversity. Engagement detection, which is essential for
> applications like virtual learning and customer services, is frequently
> challenging due to FER limitations by many current models. In this article, we
> propose ExpressNet-MoE, a novel hybrid deep learning model that blends both
> Convolution Neural Networks (CNNs) and Mixture of Experts (MoE) framework, to
> overcome the difficulties. Our model dynamically chooses the most pertinent
> expert networks, thus it aids in the generalization and providing flexibility
> to model across a wide variety of datasets. Our model improves on the accuracy
> of emotion recognition by utilizing multi-scale feature extraction to collect
> both global and local facial features. ExpressNet-MoE includes numerous
> CNN-based feature extractors, a MoE module for adaptive feature selection, and
> finally a residual network backbone for deep feature learning. To demonstrate
> efficacy of our proposed model we evaluated on several datasets, and compared
> with current state-of-the-art methods. Our model achieves accuracies of 74.77%
> on AffectNet (v7), 72.55% on AffectNet (v8), 84.29% on RAF-DB, and 64.66% on
> FER-2013. The results show how adaptive our model is and how it may be used to
> develop end-to-end emotion recognition systems in practical settings.
> Reproducible codes and results are made publicly accessible at
> https://github.com/DeeptimaanB/ExpressNet-MoE.

