---
layout: default
title: Multi-modal Deepfake Detection and Localization with FPN-Transformer
---

# Multi-modal Deepfake Detection and Localization with FPN-Transformer

**arXiv**: [2511.08031v1](https://arxiv.org/abs/2511.08031) | [PDF](https://arxiv.org/pdf/2511.08031.pdf)

**作者**: Chende Zheng, Ruiqi Suo, Zhoulin Ji, Jingyi Deng, Fangbin Yi, Chenhao Lin, Chao Shen

---

## 💡 一句话要点

**提出基于FPN-Transformer的多模态深度伪造检测与定位框架，以应对跨模态伪造威胁。**

**关键词**: `多模态深度伪造检测` `特征金字塔-Transformer` `跨模态定位` `自监督特征提取` `时间边界回归`

## 📋 核心要点

1. 核心问题：单模态方法难以利用跨模态关联并精确定位伪造片段，限制了对精细伪造的检测。
2. 方法要点：使用WavLM和CLIP提取特征，构建多尺度特征金字塔，通过双分支预测头实现检测与定位。
3. 实验或效果：在IJCAI'25 DDL-AV基准测试中得分0.7535，验证了方法的有效性。

## 📄 摘要（原文）

> The rapid advancement of generative adversarial networks (GANs) and diffusion models has enabled the creation of highly realistic deepfake content, posing significant threats to digital trust across audio-visual domains. While unimodal detection methods have shown progress in identifying synthetic media, their inability to leverage cross-modal correlations and precisely localize forged segments limits their practicality against sophisticated, fine-grained manipulations. To address this, we introduce a multi-modal deepfake detection and localization framework based on a Feature Pyramid-Transformer (FPN-Transformer), addressing critical gaps in cross-modal generalization and temporal boundary regression. The proposed approach utilizes pre-trained self-supervised models (WavLM for audio, CLIP for video) to extract hierarchical temporal features. A multi-scale feature pyramid is constructed through R-TLM blocks with localized attention mechanisms, enabling joint analysis of cross-context temporal dependencies. The dual-branch prediction head simultaneously predicts forgery probabilities and refines temporal offsets of manipulated segments, achieving frame-level localization precision. We evaluate our approach on the test set of the IJCAI'25 DDL-AV benchmark, showing a good performance with a final score of 0.7535 for cross-modal deepfake detection and localization in challenging environments. Experimental results confirm the effectiveness of our approach and provide a novel way for generalized deepfake detection. Our code is available at https://github.com/Zig-HS/MM-DDL

