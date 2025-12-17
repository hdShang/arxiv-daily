---
layout: default
title: ViDiC: Video Difference Captioning
---

# ViDiC: Video Difference Captioning

**arXiv**: [2512.03405v1](https://arxiv.org/abs/2512.03405) | [PDF](https://arxiv.org/pdf/2512.03405.pdf)

**作者**: Jiangtao Wu, Shihao Li, Zhaozhou Bian, Yuanxing Zhang, Jialu Chen, Runzhe Wen, An Ping, Yiwen He, Jiakai Wang, Jiaheng Liu

---

## 💡 一句话要点

**提出ViDiC任务与数据集以评估多模态大模型在视频对差异描述中的能力**

**关键词**: `视频差异描述` `多模态大语言模型` `比较推理` `视频理解` `数据集构建`

## 📋 核心要点

1. 核心问题：现有图像差异描述方法无法捕捉视频中的运动连续性和事件演化
2. 方法要点：构建ViDiC-1K数据集，包含1000个视频对和4000多项比较标注，覆盖七类变化
3. 实验或效果：测试19个多模态模型，发现其在比较描述和差异感知方面存在显著性能差距

## 📄 摘要（原文）

> Understanding visual differences between dynamic scenes requires the comparative perception of compositional, spatial, and temporal changes--a capability that remains underexplored in existing vision-language systems. While prior work on Image Difference Captioning (IDC) has enabled models to describe semantic changes between static images, these approaches fail to capture motion continuity, event evolution, or editing consistency over time. We introduce the ViDiC (Video Difference Captioning) task and its corresponding ViDiC-1K dataset, designed to evaluate the ability of Multimodal Large Language Models (MLLMs) to provide fine-grained descriptions of similarities and differences between video pairs. ViDiC-1K comprises 1,000 curated video pairs annotated with over 4,000 comparative checklist items, covering seven categories: subject, style, background, cinematography, motion, location, and playback techniques. To ensure reliable evaluation, we propose a dual-checklist framework that measures the accuracy of similarity and difference separately, based on the LLM-as-a-Judge protocol. Experiments on nineteen representative multimodal models reveal a significant performance gap in their comparative description and difference perception abilities. We hope ViDiC-1K can be a challenging benchmark that lays a solid foundation for advancing video understanding, edit awareness, and comparative reasoning in multimodal intelligence.

