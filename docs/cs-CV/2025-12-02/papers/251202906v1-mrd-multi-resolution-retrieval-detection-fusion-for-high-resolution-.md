---
layout: default
title: MRD: Multi-resolution Retrieval-Detection Fusion for High-Resolution Image Understanding
---

# MRD: Multi-resolution Retrieval-Detection Fusion for High-Resolution Image Understanding

**arXiv**: [2512.02906v1](https://arxiv.org/abs/2512.02906) | [PDF](https://arxiv.org/pdf/2512.02906.pdf)

**作者**: Fan Yang, Kaihao Zhang

---

## 💡 一句话要点

**提出多分辨率检索-检测融合框架以解决高分辨率图像理解中语义相似性偏差问题**

**关键词**: `高分辨率图像理解` `多模态大语言模型` `语义相似性融合` `开放词汇对象检测` `训练免费框架`

## 📋 核心要点

1. 核心问题：高分辨率图像中目标对象被分割到多个图像块，导致语义相似性计算偏差。
2. 方法要点：结合多分辨率语义融合和开放词汇对象检测，无需训练即可整合不同分辨率下的语义信息。
3. 实验或效果：在高分辨率图像理解基准测试中验证了方法的有效性，提升了目标定位准确性。

## 📄 摘要（原文）

> Understanding high-resolution images remains a significant challenge for multimodal large language models (MLLMs). Recent study address this issue by dividing the image into smaller crops and computing the semantic similarity between each crop and a query using a pretrained retrieval-augmented generation (RAG) model. The most relevant crops are then selected to localize the target object and suppress irrelevant information. However, such crop-based processing can fragment complete objects across multiple crops, thereby disrupting the computation of semantic similarity. In our experiments, we find that image crops of objects with different sizes are better handled at different resolutions. Based on this observation, we propose Multi-resolution Retrieval-Detection (MRD), a training-free framework for high-resolution image understanding. To address the issue of semantic similarity bias caused by objects being split across different image crops, we propose a multi-resolution semantic fusion method, which integrates semantic similarity maps obtained at different resolutions to produce more accurate semantic information and preserve the integrity of target objects. Furthermore, to achieve direct localization of target objects at a global scale, we introduce an open-vocalbulary object detection (OVD) model that identifies object regions using a sliding-window approach.Experiments on high-resolution image understanding benchmarks using different MLLMs demonstrate the effectiveness of our approach.

