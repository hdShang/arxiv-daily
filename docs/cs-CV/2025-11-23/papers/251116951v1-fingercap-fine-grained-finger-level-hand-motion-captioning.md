---
layout: default
title: FingerCap: Fine-grained Finger-level Hand Motion Captioning
---

# FingerCap: Fine-grained Finger-level Hand Motion Captioning

**arXiv**: [2511.16951v1](https://arxiv.org/abs/2511.16951) | [PDF](https://arxiv.org/pdf/2511.16951.pdf)

**作者**: Xin Shen, Rui Zhu, Lei Shen, Xinyu Wang, Kaihao Zhang, Tianqing Zhu, Shuchen Wu, Chenxi Miao, Weikang Li, Yang Li, Deguo Xia, Jizhou Huang, Xin Yu

---

## 💡 一句话要点

**提出FiGOP方法以解决视频多模态大模型在细粒度手指运动理解中的时间稀疏性问题**

**关键词**: `手指运动描述` `视频多模态大模型` `时间稀疏性` `手部关键点` `运动嵌入` `细粒度理解`

## 📋 核心要点

1. 核心问题：视频多模态大模型因RGB采样稀疏，难以捕捉手指细微高频动态。
2. 方法要点：引入FiGOP，将RGB关键帧与后续手部关键点配对，编码运动嵌入。
3. 实验或效果：在FingerCap-40K数据集上，FiGOP增强模型在HandJudge评估中表现更优。

## 📄 摘要（原文）

> Understanding fine-grained human hand motion is fundamental to visual perception, embodied intelligence, and multimodal communication. In this work, we propose Fine-grained Finger-level Hand Motion Captioning (FingerCap), which aims to generate textual descriptions that capture detailed finger-level semantics of hand actions. To support this task, we curate FingerCap-40K, a large-scale corpus of 40K paired hand-motion videos and captions spanning two complementary sources: concise instruction-style finger motions and diverse, naturalistic hand-object interactions. To enable effective evaluation, we employ HandJudge, a LLM-based rubric that measures finger-level correctness and motion completeness. Temporal sparsity remains a fundamental bottleneck for current Video-MLLMs, since sparse RGB sampling is insufficient to capture the subtle, high-frequency dynamics underlying fine finger motions. As a simple and compute-friendly remedy, we introduce FiGOP (Finger Group-of-Pictures), which pairs each RGB keyframe with subsequent hand keypoints until the next keyframe. A lightweight temporal encoder converts the keypoints into motion embeddings and integrates them with RGB features. FiGOP adapts the classic GOP concept to finger motion, recovering fine temporal cues without increasing RGB density. Experiments on FingerCap-40K show that strong open- and closed-source Video-MLLMs still struggle with finger-level reasoning, while our FiGOP-augmented model yield consistent gains under HandJudge and human studies.

