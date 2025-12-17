---
layout: default
title: Beyond the Pipeline: Analyzing Key Factors in End-to-End Deep Learning for Historical Writer Identification
---

# Beyond the Pipeline: Analyzing Key Factors in End-to-End Deep Learning for Historical Writer Identification

**arXiv**: [2510.18671v1](https://arxiv.org/abs/2510.18671) | [PDF](https://arxiv.org/pdf/2510.18671.pdf)

**作者**: Hanif Rasyidi, Moshiur Farazi

---

## 💡 一句话要点

**分析端到端深度学习在历史笔迹识别中的关键因素，识别出简化设计的高性能配置**

**关键词**: `历史笔迹识别` `端到端深度学习` `零样本泛化` `特征提取` `文档图像处理`

## 📋 核心要点

1. 核心问题：历史笔迹识别因风格多样、文档退化及样本稀少而困难，端到端模型在零样本场景泛化差
2. 方法要点：探索预处理、骨干架构和后处理组合，包括文本分割、补丁采样和特征聚合
3. 实验或效果：多数配置性能不佳，但发现一种简化端到端设置与顶尖系统效果相当

## 📄 摘要（原文）

> This paper investigates various factors that influence the performance of
> end-to-end deep learning approaches for historical writer identification (HWI),
> a task that remains challenging due to the diversity of handwriting styles,
> document degradation, and the limited number of labelled samples per writer.
> These conditions often make accurate recognition difficult, even for human
> experts. Traditional HWI methods typically rely on handcrafted image processing
> and clustering techniques, which tend to perform well on small and carefully
> curated datasets. In contrast, end-to-end pipelines aim to automate the process
> by learning features directly from document images. However, our experiments
> show that many of these models struggle to generalise in more realistic,
> document-level settings, especially under zero-shot scenarios where writers in
> the test set are not present in the training data. We explore different
> combinations of pre-processing methods, backbone architectures, and
> post-processing strategies, including text segmentation, patch sampling, and
> feature aggregation. The results suggest that most configurations perform
> poorly due to weak capture of low-level visual features, inconsistent patch
> representations, and high sensitivity to content noise. Still, we identify one
> end-to-end setup that achieves results comparable to the top-performing system,
> despite using a simpler design. These findings point to key challenges in
> building robust end-to-end systems and offer insight into design choices that
> improve performance in historical document writer identification.

