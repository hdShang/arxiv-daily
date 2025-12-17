---
layout: default
title: A Matter of Time: Revealing the Structure of Time in Vision-Language Models
---

# A Matter of Time: Revealing the Structure of Time in Vision-Language Models

**arXiv**: [2510.19559v1](https://arxiv.org/abs/2510.19559) | [PDF](https://arxiv.org/pdf/2510.19559.pdf)

**作者**: Nidham Tekaya, Manuela Waldner, Matthias Zeppelzauer

---

## 💡 一句话要点

**提出时间线表示方法以增强视觉语言模型的时间推理能力**

**关键词**: `视觉语言模型` `时间感知` `嵌入空间` `时间线表示` `基准数据集` `时间推理`

## 📋 核心要点

1. 研究视觉语言模型对视觉内容的时间定位能力
2. 发现时间信息在嵌入空间中呈低维非线性流形结构
3. 基于此提出时间线表示方法，在基准测试中表现优于基线

## 📄 摘要（原文）

> Large-scale vision-language models (VLMs) such as CLIP have gained popularity
> for their generalizable and expressive multimodal representations. By
> leveraging large-scale training data with diverse textual metadata, VLMs
> acquire open-vocabulary capabilities, solving tasks beyond their training
> scope. This paper investigates the temporal awareness of VLMs, assessing their
> ability to position visual content in time. We introduce TIME10k, a benchmark
> dataset of over 10,000 images with temporal ground truth, and evaluate the
> time-awareness of 37 VLMs by a novel methodology. Our investigation reveals
> that temporal information is structured along a low-dimensional, non-linear
> manifold in the VLM embedding space. Based on this insight, we propose methods
> to derive an explicit ``timeline'' representation from the embedding space.
> These representations model time and its chronological progression and thereby
> facilitate temporal reasoning tasks. Our timeline approaches achieve
> competitive to superior accuracy compared to a prompt-based baseline while
> being computationally efficient. All code and data are available at
> https://tekayanidham.github.io/timeline-page/.

