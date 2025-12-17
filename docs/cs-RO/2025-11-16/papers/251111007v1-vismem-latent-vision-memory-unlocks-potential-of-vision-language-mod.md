---
layout: default
title: VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models
---

# VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models

**arXiv**: [2511.11007v1](https://arxiv.org/abs/2511.11007) | [PDF](https://arxiv.org/pdf/2511.11007.pdf)

**作者**: Xinlei Yu, Chengming Xu, Guibin Zhang, Zhangquan Chen, Yudong Zhang, Yongbo He, Peng-Tao Jiang, Jiangning Zhang, Xiaobin Hu, Shuicheng Yan

---

## 💡 一句话要点

**提出VisMem框架以解决视觉语言模型在复杂任务中的视觉处理瓶颈问题**

**关键词**: `视觉语言模型` `潜在记忆` `视觉处理瓶颈` `认知对齐` `性能提升`

## 📋 核心要点

1. 核心问题：视觉语言模型在长序列生成中易丢失视觉证据和上下文经验
2. 方法要点：引入短时和长时潜在视觉记忆模块，模拟人类认知记忆机制
3. 实验或效果：在多个基准测试中平均性能提升11.8%，优于现有方法

## 📄 摘要（原文）

> Despite the remarkable success of Vision-Language Models (VLMs), their performance on a range of complex visual tasks is often hindered by a "visual processing bottleneck": a propensity to lose grounding in visual evidence and exhibit a deficit in contextualized visual experience during prolonged generation. Drawing inspiration from human cognitive memory theory, which distinguishes short-term visually-dominant memory and long-term semantically-dominant memory, we propose VisMem, a cognitively-aligned framework that equips VLMs with dynamic latent vision memories, a short-term module for fine-grained perceptual retention and a long-term module for abstract semantic consolidation. These memories are seamlessly invoked during inference, allowing VLMs to maintain both perceptual fidelity and semantic consistency across thinking and generation. Extensive experiments across diverse visual benchmarks for understanding, reasoning, and generation reveal that VisMem delivers a significant average performance boost of 11.8% relative to the vanilla model and outperforms all counterparts, establishing a new paradigm for latent-space memory enhancement. The code will be available: https://github.com/YU-deep/VisMem.git.

