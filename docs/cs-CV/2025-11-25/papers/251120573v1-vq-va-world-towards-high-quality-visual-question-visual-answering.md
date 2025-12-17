---
layout: default
title: VQ-VA World: Towards High-Quality Visual Question-Visual Answering
---

# VQ-VA World: Towards High-Quality Visual Question-Visual Answering

**arXiv**: [2511.20573v1](https://arxiv.org/abs/2511.20573) | [PDF](https://arxiv.org/pdf/2511.20573.pdf)

**作者**: Chenhui Gou, Zilong Chen, Zeyu Wang, Feng Li, Deyao Zhu, Zicheng Duan, Kunchang Li, Chaorui Deng, Hongyi Yuan, Haoqi Fan, Cihang Xie, Jianfei Cai, Hamid Rezatofighi

---

## 💡 一句话要点

**提出VQ-VA World框架以构建高质量视觉问答-视觉回答开源模型**

**关键词**: `视觉问答-视觉回答` `数据构建框架` `开源模型训练` `大规模数据集` `智能基准评估`

## 📋 核心要点

1. 核心问题：视觉问答-视觉回答任务，即根据视觉问题生成图像而非文本，开源模型能力不足。
2. 方法要点：采用数据驱动框架，通过代理管道大规模爬取约180万高质量图文样本用于训练。
3. 实验或效果：训练后模型在IntelligentBench基准上得分53.06，显著超越开源基线并接近专有系统。

## 📄 摘要（原文）

> This paper studies Visual Question-Visual Answering (VQ-VA): generating an image, rather than text, in response to a visual question -- an ability that has recently emerged in proprietary systems such as NanoBanana and GPT-Image. To also bring this capability to open-source models, we introduce VQ-VA World, a data-centric framework built around an agentic pipeline for large-scale, targeted data construction. Leveraging web-scale deployment, this pipeline crawls a massive amount of ~1.8M high-quality, interleaved image-text samples for model training. For evaluation, we further release IntelligentBench, a human-curated benchmark that systematically assesses VQ-VA along the aspects of world knowledge, design knowledge, and reasoning. Training with VQ-VA World data yields strong empirical gains: it helps LightFusion attain 53.06 on IntelligentBench, substantially surpassing the best prior open-source baselines (i.e., 7.78 from vanilla LightFusion; 1.94 from UniWorld-V1), and significantly narrowing the gap toward leading proprietary systems (e.g., 81.67 from NanoBanana; 82.64 from GPT-Image). By releasing the full suite of model weights, datasets, and pipelines, we hope to stimulate future research on VQ-VA.

