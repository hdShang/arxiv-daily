---
layout: default
title: Loomis Painter: Reconstructing the Painting Process
---

# Loomis Painter: Reconstructing the Painting Process

**arXiv**: [2511.17344v1](https://arxiv.org/abs/2511.17344) | [PDF](https://arxiv.org/pdf/2511.17344.pdf)

**作者**: Markus Pobitzer, Chang Liu, Chenyi Zhuang, Teng Long, Bin Ren, Nicu Sebe

---

## 💡 一句话要点

**提出统一框架以解决多媒介绘画过程生成中的一致性问题**

**关键词**: `绘画过程生成` `扩散模型` `风格控制` `跨媒介一致性` `时序连贯性` `数据集构建`

## 📋 核心要点

1. 现有绘画教程视频缺乏交互性，生成模型存在跨媒介和时序不一致问题
2. 采用语义驱动风格控制、跨媒介风格增强和反向绘画训练策略
3. 构建大规模数据集，评估跨媒介一致性、时序连贯性和图像保真度

## 📄 摘要（原文）

> Step-by-step painting tutorials are vital for learning artistic techniques, but existing video resources (e.g., YouTube) lack interactivity and personalization. While recent generative models have advanced artistic image synthesis, they struggle to generalize across media and often show temporal or structural inconsistencies, hindering faithful reproduction of human creative workflows. To address this, we propose a unified framework for multi-media painting process generation with a semantics-driven style control mechanism that embeds multiple media into a diffusion models conditional space and uses cross-medium style augmentation. This enables consistent texture evolution and process transfer across styles. A reverse-painting training strategy further ensures smooth, human-aligned generation. We also build a large-scale dataset of real painting processes and evaluate cross-media consistency, temporal coherence, and final-image fidelity, achieving strong results on LPIPS, DINO, and CLIP metrics. Finally, our Perceptual Distance Profile (PDP) curve quantitatively models the creative sequence, i.e., composition, color blocking, and detail refinement, mirroring human artistic progression.

