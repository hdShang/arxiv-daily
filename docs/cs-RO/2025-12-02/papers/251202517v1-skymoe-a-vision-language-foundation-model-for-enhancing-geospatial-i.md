---
layout: default
title: SkyMoE: A Vision-Language Foundation Model for Enhancing Geospatial Interpretation with Mixture of Experts
---

# SkyMoE: A Vision-Language Foundation Model for Enhancing Geospatial Interpretation with Mixture of Experts

**arXiv**: [2512.02517v1](https://arxiv.org/abs/2512.02517) | [PDF](https://arxiv.org/pdf/2512.02517.pdf)

**作者**: Jiaqi Liu, Ronghao Fu, Lang Sun, Haoran Liu, Xiao Yang, Weipeng Zhang, Xu Na, Zhuoran Duan, Bo Yang

---

## 💡 一句话要点

**提出SkyMoE模型，通过专家混合架构增强遥感多任务多粒度视觉语言理解**

**关键词**: `遥感视觉语言模型` `专家混合架构` `多粒度理解` `自适应路由` `上下文解耦增强` `多任务基准`

## 📋 核心要点

1. 问题：通用视觉语言模型在遥感任务中表现不佳，难以平衡局部细节与全局上下文理解
2. 方法：采用自适应路由器和上下文解耦增强策略，实现任务和粒度感知的专家分配
3. 效果：在21个公开数据集上达到先进性能，验证了模型在复杂场景下的适应性和可扩展性

## 📄 摘要（原文）

> The emergence of large vision-language models (VLMs) has significantly enhanced the efficiency and flexibility of geospatial interpretation. However, general-purpose VLMs remain suboptimal for remote sensing (RS) tasks. Existing geospatial VLMs typically adopt a unified modeling strategy and struggle to differentiate between task types and interpretation granularities, limiting their ability to balance local detail perception and global contextual understanding. In this paper, we present SkyMoE, a Mixture-of-Experts (MoE) vision-language model tailored for multimodal, multi-task RS interpretation. SkyMoE employs an adaptive router that generates task- and granularity-aware routing instructions, enabling specialized large language model experts to handle diverse sub-tasks. To further promote expert decoupling and granularity sensitivity, we introduce a context-disentangled augmentation strategy that creates contrastive pairs between local and global features, guiding experts toward level-specific representation learning. We also construct MGRS-Bench, a comprehensive benchmark covering multiple RS interpretation tasks and granularity levels, to evaluate generalization in complex scenarios. Extensive experiments on 21 public datasets demonstrate that SkyMoE achieves state-of-the-art performance across tasks, validating its adaptability, scalability, and superior multi-granularity understanding in remote sensing.

