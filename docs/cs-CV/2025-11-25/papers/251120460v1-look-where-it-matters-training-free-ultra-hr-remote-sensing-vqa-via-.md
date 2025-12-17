---
layout: default
title: Look Where It Matters: Training-Free Ultra-HR Remote Sensing VQA via Adaptive Zoom Search
---

# Look Where It Matters: Training-Free Ultra-HR Remote Sensing VQA via Adaptive Zoom Search

**arXiv**: [2511.20460v1](https://arxiv.org/abs/2511.20460) | [PDF](https://arxiv.org/pdf/2511.20460.pdf)

**作者**: Yunqi Zhou, Chengjie Jiang, Chun Yuan, Jing Li

---

## 💡 一句话要点

**提出ZoomSearch以解决超高分遥感VQA中细节丢失与效率低下的问题**

**关键词**: `遥感视觉问答` `超高分图像处理` `自适应缩放搜索` `布局感知重组` `训练免费方法` `推理效率优化`

## 📋 核心要点

1. 超高分遥感图像全图编码导致内存和token不足，缩放预处理丢失关键细节
2. 采用自适应多分支缩放搜索和布局感知补丁重组，无需训练即可定位并整合相关区域
3. 在LRS-VQA和MME-RealWorld-RS基准上，集成LLaVA-ov实现SOTA精度和更高推理效率

## 📄 摘要（原文）

> With advances in satellite constellations, sensor technologies, and imaging pipelines, ultra-high-resolution (Ultra-HR) remote sensing imagery is becoming increasingly widespread. However, current remote sensing foundation models are ill-suited to such inputs: full-image encoding exhausts token and memory budgets, while resize-based preprocessing loses fine-grained and answer-critical details. In this context, guiding the model look where it matters before prediction becomes crucial. Therefore, we present ZoomSearch, a training-free, plug-and-play pipeline that decouples 'where to look' from 'how to answer' for Ultra-HR Remote Sensing Visual Question Answering (RS-VQA). ZoomSearch combines Adaptive Multi-Branch Zoom Search, which performs a hierarchical search over image patches to localize query-relevant regions, with Layout-Aware Patch Reassembly, which reorganizes the selected patches into a compact, layout-faithful canvas. We conduct comprehensive experiments on Ultra-HR RS-VQA benchmarks MME-RealWorld-RS and LRS-VQA, comparing against (i) strong general foundation models, (ii) remote sensing foundation models, (iii) Ultra-HR RS-VQA methods, and (iv) plug-and-play search-based VQA methods. When integrated with LLaVA-ov, ZoomSearch attains state-of-the-art accuracy across diverse tasks, improving the LLaVA-ov baseline by 26.3% on LRS-VQA and 114.8\% on MME-RealWorld-RS. Meanwhile, it achieves much higher inference efficiency, outperforming prior search-based methods by 20%~44% in speed.

