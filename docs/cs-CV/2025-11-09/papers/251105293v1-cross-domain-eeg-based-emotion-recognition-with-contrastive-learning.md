---
layout: default
title: Cross-domain EEG-based Emotion Recognition with Contrastive Learning
---

# Cross-domain EEG-based Emotion Recognition with Contrastive Learning

**arXiv**: [2511.05293v1](https://arxiv.org/abs/2511.05293) | [PDF](https://arxiv.org/pdf/2511.05293.pdf)

**作者**: Rui Yan, Yibo Li, Han Ding, Fei Wang

---

## 💡 一句话要点

**提出EmotionCLIP框架，通过EEG-文本匹配解决跨域脑电情绪识别问题**

**关键词**: `脑电情绪识别` `跨域学习` `对比学习` `多模态匹配` `Transformer网络`

## 📋 核心要点

1. 核心问题：脑电情绪识别面临特征利用不足和跨域泛化挑战
2. 方法要点：使用SST-LegoViT骨干网络提取空间、频谱和时间特征
3. 实验效果：在SEED和SEED-IV数据集上实现高跨域准确率，优于现有模型

## 📄 摘要（原文）

> Electroencephalogram (EEG)-based emotion recognition is vital for affective
> computing but faces challenges in feature utilization and cross-domain
> generalization. This work introduces EmotionCLIP, which reformulates
> recognition as an EEG-text matching task within the CLIP framework. A tailored
> backbone, SST-LegoViT, captures spatial, spectral, and temporal features using
> multi-scale convolution and Transformer modules. Experiments on SEED and
> SEED-IV datasets show superior cross-subject accuracies of 88.69% and 73.50%,
> and cross-time accuracies of 88.46% and 77.54%, outperforming existing models.
> Results demonstrate the effectiveness of multimodal contrastive learning for
> robust EEG emotion recognition.

