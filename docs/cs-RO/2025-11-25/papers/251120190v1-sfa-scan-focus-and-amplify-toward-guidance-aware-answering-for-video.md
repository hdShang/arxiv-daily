---
layout: default
title: SFA: Scan, Focus, and Amplify toward Guidance-aware Answering for Video TextVQA
---

# SFA: Scan, Focus, and Amplify toward Guidance-aware Answering for Video TextVQA

**arXiv**: [2511.20190v1](https://arxiv.org/abs/2511.20190) | [PDF](https://arxiv.org/pdf/2511.20190.pdf)

**作者**: Haibin He, Qihuang Zhong, Juhua Liu, Bo Du, Peng Wang, Jing Zhang

---

## 💡 一句话要点

**提出SFA框架以解决视频文本视觉问答中的文本感知与引导问题**

**关键词**: `视频文本视觉问答` `无训练框架` `注意力引导` `文本感知` `时空整合`

## 📋 核心要点

1. 核心问题：视频中文本尺度、方向、清晰度变化大，需整合时空语义并过滤冗余信息。
2. 方法要点：采用无训练框架，通过扫描、聚焦、放大关键区域引导Video-LLM注意力。
3. 实验或效果：在多个公开数据集上实现新SOTA，超越先前方法，验证有效性和泛化性。

## 📄 摘要（原文）

> Video text-based visual question answering (Video TextVQA) task aims to answer questions about videos by leveraging the visual text appearing within the videos. This task poses significant challenges, requiring models to accurately perceive and comprehend scene text that varies in scale, orientation, and clarity across frames, while effectively integrating temporal and semantic context to generate precise answers. Moreover, the model must identify question-relevant textual cues and filter out redundant or irrelevant information to ensure answering is guided by the most relevant and informative cues. To address these challenges, we propose SFA, a training-free framework and the first Video-LLM-based method tailored for Video TextVQA, motivated by the human process of answering questions. By adaptively scanning video frames, selectively focusing on key regions, and directly amplifying them, SFA effectively guides the Video-LLM's attention toward essential cues, enabling it to generate more accurate answers. SFA achieves new state-of-the-art results across several public Video TextVQA datasets and surpasses previous methods by a substantial margin, demonstrating its effectiveness and generalizability.

