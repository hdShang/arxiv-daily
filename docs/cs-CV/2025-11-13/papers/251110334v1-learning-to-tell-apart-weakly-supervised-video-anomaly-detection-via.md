---
layout: default
title: Learning to Tell Apart: Weakly Supervised Video Anomaly Detection via Disentangled Semantic Alignment
---

# Learning to Tell Apart: Weakly Supervised Video Anomaly Detection via Disentangled Semantic Alignment

**arXiv**: [2511.10334v1](https://arxiv.org/abs/2511.10334) | [PDF](https://arxiv.org/pdf/2511.10334.pdf)

**作者**: Wenti Yin, Huaxin Zhang, Xiang Wang, Yuqing Lu, Yicheng Zhang, Bingquan Gong, Jialong Zuo, Li Yu, Changxin Gao, Nong Sang

---

## 💡 一句话要点

**提出DSANet以解决弱监督视频异常检测中的类别混淆问题**

**关键词**: `弱监督视频异常检测` `语义对齐` `对比学习` `多模态基础模型` `特征解耦`

## 📋 核心要点

1. 核心问题：现有方法易忽略正常模式多样性，导致细粒度分类效果不佳
2. 方法要点：通过粗粒度正常原型建模和细粒度对比语义对齐分离异常与正常特征
3. 实验或效果：在XD-Violence和UCF-Crime基准上超越现有最优方法

## 📄 摘要（原文）

> Recent advancements in weakly-supervised video anomaly detection have achieved remarkable performance by applying the multiple instance learning paradigm based on multimodal foundation models such as CLIP to highlight anomalous instances and classify categories. However, their objectives may tend to detect the most salient response segments, while neglecting to mine diverse normal patterns separated from anomalies, and are prone to category confusion due to similar appearance, leading to unsatisfactory fine-grained classification results. Therefore, we propose a novel Disentangled Semantic Alignment Network (DSANet) to explicitly separate abnormal and normal features from coarse-grained and fine-grained aspects, enhancing the distinguishability. Specifically, at the coarse-grained level, we introduce a self-guided normality modeling branch that reconstructs input video features under the guidance of learned normal prototypes, encouraging the model to exploit normality cues inherent in the video, thereby improving the temporal separation of normal patterns and anomalous events. At the fine-grained level, we present a decoupled contrastive semantic alignment mechanism, which first temporally decomposes each video into event-centric and background-centric components using frame-level anomaly scores and then applies visual-language contrastive learning to enhance class-discriminative representations. Comprehensive experiments on two standard benchmarks, namely XD-Violence and UCF-Crime, demonstrate that DSANet outperforms existing state-of-the-art methods.

