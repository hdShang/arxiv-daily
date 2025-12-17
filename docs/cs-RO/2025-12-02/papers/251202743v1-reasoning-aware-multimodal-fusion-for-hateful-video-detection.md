---
layout: default
title: Reasoning-Aware Multimodal Fusion for Hateful Video Detection
---

# Reasoning-Aware Multimodal Fusion for Hateful Video Detection

**arXiv**: [2512.02743v1](https://arxiv.org/abs/2512.02743) | [PDF](https://arxiv.org/pdf/2512.02743.pdf)

**作者**: Shuonan Yang, Tailin Chen, Jiangbei Yue, Guangliang Cheng, Jianbo Jiao, Zeyu Fu

---

## 💡 一句话要点

**提出推理感知多模态融合框架以提升仇恨视频检测性能**

**关键词**: `仇恨视频检测` `多模态融合` `对抗性推理` `语义交叉注意力` `局部全局上下文融合`

## 📋 核心要点

1. 针对在线视频中仇恨言论检测的多模态语义融合与细微理解难题
2. 设计局部全局上下文融合与语义交叉注意力，并引入对抗性推理增强上下文理解
3. 在两个真实数据集上超越现有方法，宏F1提升3%，仇恨类召回率提升7%

## 📄 摘要（原文）

> Hate speech in online videos is posing an increasingly serious threat to digital platforms, especially as video content becomes increasingly multimodal and context-dependent. Existing methods often struggle to effectively fuse the complex semantic relationships between modalities and lack the ability to understand nuanced hateful content. To address these issues, we propose an innovative Reasoning-Aware Multimodal Fusion (RAMF) framework. To tackle the first challenge, we design Local-Global Context Fusion (LGCF) to capture both local salient cues and global temporal structures, and propose Semantic Cross Attention (SCA) to enable fine-grained multimodal semantic interaction. To tackle the second challenge, we introduce adversarial reasoning-a structured three-stage process where a vision-language model generates (i) objective descriptions, (ii) hate-assumed inferences, and (iii) non-hate-assumed inferences-providing complementary semantic perspectives that enrich the model's contextual understanding of nuanced hateful intent. Evaluations on two real-world hateful video datasets demonstrate that our method achieves robust generalisation performance, improving upon state-of-the-art methods by 3% and 7% in Macro-F1 and hate class recall, respectively. We will release the code after the anonymity period ends.

