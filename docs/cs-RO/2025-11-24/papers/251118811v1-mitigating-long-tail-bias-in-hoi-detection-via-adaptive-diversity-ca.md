---
layout: default
title: Mitigating Long-Tail Bias in HOI Detection via Adaptive Diversity Cache
---

# Mitigating Long-Tail Bias in HOI Detection via Adaptive Diversity Cache

**arXiv**: [2511.18811v1](https://arxiv.org/abs/2511.18811) | [PDF](https://arxiv.org/pdf/2511.18811.pdf)

**作者**: Yuqiu Jiang, Xiaozhen Qiao, Tianyu Mei, Haojian Huang, Yifan Chen, Ye Zheng, Zhe Sun

---

## 💡 一句话要点

**提出自适应多样性缓存以缓解HOI检测中的长尾偏差**

**关键词**: `人-物交互检测` `长尾分布` `自适应缓存` `训练无关方法` `特征多样性`

## 📋 核心要点

1. HOI检测中长尾场景下稀有交互样本不足，导致模型偏差
2. ADC模块无需训练，构建类特定缓存并采用频率感知适应策略
3. 在HICO-DET和V-COCO数据集上，稀有类别mAP提升达8.57%

## 📄 摘要（原文）

> Human-Object Interaction (HOI) detection is a fundamental task in computer vision, empowering machines to comprehend human-object relationships in diverse real-world scenarios. Recent advances in VLMs have significantly improved HOI detection by leveraging rich cross-modal representations. However, most existing VLM-based approaches rely heavily on additional training or prompt tuning, resulting in substantial computational overhead and limited scalability, particularly in long-tailed scenarios where rare interactions are severely underrepresented. In this paper, we propose the Adaptive Diversity Cache (ADC) module, a novel training-free and plug-and-play mechanism designed to mitigate long-tail bias in HOI detection. ADC constructs class-specific caches that accumulate high-confidence and diverse feature representations during inference. The method incorporates frequency-aware cache adaptation that favors rare categories and is designed to enable robust prediction calibration without requiring additional training or fine-tuning. Extensive experiments on HICO-DET and V-COCO datasets show that ADC consistently improves existing HOI detectors, achieving up to +8.57\% mAP gain on rare categories and +4.39\% on the full dataset, demonstrating its effectiveness in mitigating long-tail bias while preserving overall performance.

