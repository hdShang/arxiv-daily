---
layout: default
title: C2F-Space: Coarse-to-Fine Space Grounding for Spatial Instructions using Vision-Language Models
---

# C2F-Space: Coarse-to-Fine Space Grounding for Spatial Instructions using Vision-Language Models

**arXiv**: [2511.15333v1](https://arxiv.org/abs/2511.15333) | [PDF](https://arxiv.org/pdf/2511.15333.pdf)

**作者**: Nayoung Oh, Dohyun Kim, Junhyeong Bang, Rohan Paul, Daehyung Park

---

## 💡 一句话要点

**提出C2F-Space框架以解决空间指令中复杂推理与细粒度定位问题**

**关键词**: `空间定位` `视觉语言模型` `粗到细框架` `超像素化` `机器人任务`

## 📋 核心要点

1. 核心问题：传统方法难以处理空间指令中的距离、几何和物体关系推理
2. 方法要点：采用粗到细策略，先估计粗略区域再通过超像素化进行局部细化
3. 实验或效果：在新建基准上显著优于五种基线，并验证了模块有效性

## 📄 摘要（原文）

> Space grounding refers to localizing a set of spatial references described in natural language instructions. Traditional methods often fail to account for complex reasoning -- such as distance, geometry, and inter-object relationships -- while vision-language models (VLMs), despite strong reasoning abilities, struggle to produce a fine-grained region of outputs. To overcome these limitations, we propose C2F-Space, a novel coarse-to-fine space-grounding framework that (i) estimates an approximated yet spatially consistent region using a VLM, then (ii) refines the region to align with the local environment through superpixelization. For the coarse estimation, we design a grid-based visual-grounding prompt with a propose-validate strategy, maximizing VLM's spatial understanding and yielding physically and semantically valid canonical region (i.e., ellipses). For the refinement, we locally adapt the region to surrounding environment without over-relaxed to free space. We construct a new space-grounding benchmark and compare C2F-Space with five state-of-the-art baselines using success rate and intersection-over-union. Our C2F-Space significantly outperforms all baselines. Our ablation study confirms the effectiveness of each module in the two-step process and their synergistic effect of the combined framework. We finally demonstrate the applicability of C2F-Space to simulated robotic pick-and-place tasks.

