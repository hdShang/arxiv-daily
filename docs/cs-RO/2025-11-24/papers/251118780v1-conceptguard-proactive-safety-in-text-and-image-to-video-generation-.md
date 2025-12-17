---
layout: default
title: ConceptGuard: Proactive Safety in Text-and-Image-to-Video Generation through Multimodal Risk Detection
---

# ConceptGuard: Proactive Safety in Text-and-Image-to-Video Generation through Multimodal Risk Detection

**arXiv**: [2511.18780v1](https://arxiv.org/abs/2511.18780) | [PDF](https://arxiv.org/pdf/2511.18780.pdf)

**作者**: Ruize Ma, Minghong Cai, Yilei Jiang, Jiaming Han, Yi Feng, Yingshui Tan, Xiaoyong Zhu, Bo Zhang, Bo Zheng, Xiangyu Yue

---

## 💡 一句话要点

**提出ConceptGuard框架以主动检测和缓解多模态视频生成中的安全风险**

**关键词**: `多模态视频生成` `安全风险检测` `对比学习` `语义抑制` `基准数据集` `主动安全框架`

## 📋 核心要点

1. 核心问题：多模态视频生成中文本和图像交互可能产生有害内容，现有方法难以主动应对。
2. 方法要点：采用对比检测模块识别潜在风险，并通过语义抑制机制干预生成过程。
3. 实验或效果：在ConceptRisk和T2VSafetyBench-TI2V基准上实现最优风险检测和安全生成效果。

## 📄 摘要（原文）

> Recent progress in video generative models has enabled the creation of high-quality videos from multimodal prompts that combine text and images. While these systems offer enhanced controllability, they also introduce new safety risks, as harmful content can emerge from individual modalities or their interaction. Existing safety methods are often text-only, require prior knowledge of the risk category, or operate as post-generation auditors, struggling to proactively mitigate such compositional, multimodal risks. To address this challenge, we present ConceptGuard, a unified safeguard framework for proactively detecting and mitigating unsafe semantics in multimodal video generation. ConceptGuard operates in two stages: First, a contrastive detection module identifies latent safety risks by projecting fused image-text inputs into a structured concept space; Second, a semantic suppression mechanism steers the generative process away from unsafe concepts by intervening in the prompt's multimodal conditioning. To support the development and rigorous evaluation of this framework, we introduce two novel benchmarks: ConceptRisk, a large-scale dataset for training on multimodal risks, and T2VSafetyBench-TI2V, the first benchmark adapted from T2VSafetyBench for the Text-and-Image-to-Video (TI2V) safety setting. Comprehensive experiments on both benchmarks show that ConceptGuard consistently outperforms existing baselines, achieving state-of-the-art results in both risk detection and safe video generation.

