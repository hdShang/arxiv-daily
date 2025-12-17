---
layout: default
title: Unleashing the Power of Vision-Language Models for Long-Tailed Multi-Label Visual Recognition
---

# Unleashing the Power of Vision-Language Models for Long-Tailed Multi-Label Visual Recognition

**arXiv**: [2511.20641v1](https://arxiv.org/abs/2511.20641) | [PDF](https://arxiv.org/pdf/2511.20641.pdf)

**作者**: Wei Tang, Zuo-Zheng Wang, Kun Zhang, Tong Wei, Min-Ling Zhang

---

## 💡 一句话要点

**提出CAPNET以解决长尾多标签视觉识别中的标签相关性与不平衡问题**

**关键词**: `长尾多标签识别` `视觉语言模型` `标签相关性建模` `图卷积网络` `不平衡学习` `参数高效微调`

## 📋 核心要点

1. 核心问题：长尾多标签视觉识别中，类别分布不平衡导致模型偏向头部类别，尾部类别性能差。
2. 方法要点：利用CLIP文本编码器建模标签相关性，结合图卷积网络和可学习软提示优化嵌入。
3. 实验或效果：在VOC-LT等基准测试中，CAPNET显著优于现有方法，验证其有效性。

## 📄 摘要（原文）

> Long-tailed multi-label visual recognition poses a significant challenge, as images typically contain multiple labels with highly imbalanced class distributions, leading to biased models that favor head classes while underperforming on tail classes. Recent efforts have leveraged pre-trained vision-language models, such as CLIP, alongside long-tailed learning techniques to exploit rich visual-textual priors for improved performance. However, existing methods often derive semantic inter-class relationships directly from imbalanced datasets, resulting in unreliable correlations for tail classes due to data scarcity. Moreover, CLIP's zero-shot paradigm is optimized for single-label image-text matching, making it suboptimal for multi-label tasks. To address these issues, we propose the correlation adaptation prompt network (CAPNET), a novel end-to-end framework that explicitly models label correlations from CLIP's textual encoder. The framework incorporates a graph convolutional network for label-aware propagation and learnable soft prompts for refined embeddings. It utilizes a distribution-balanced Focal loss with class-aware re-weighting for optimized training under imbalance. Moreover, it improves generalization through test-time ensembling and realigns visual-textual modalities using parameter-efficient fine-tuning to avert overfitting on tail classes without compromising head class performance. Extensive experiments and ablation studies on benchmarks including VOC-LT, COCO-LT, and NUS-WIDE demonstrate that CAPNET achieves substantial improvements over state-of-the-art methods, validating its effectiveness for real-world long-tailed multi-label visual recognition.

