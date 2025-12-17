---
layout: default
title: VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference
---

# VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference

**arXiv**: [2511.16449v1](https://arxiv.org/abs/2511.16449) | [PDF](https://arxiv.org/pdf/2511.16449.pdf)

**作者**: Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, Bo Zhao

---

## 💡 一句话要点

**提出VLA-Pruner以解决视觉-语言-动作模型推理效率低的问题**

**关键词**: `视觉-语言-动作模型` `令牌剪枝` `双级重要性` `机器人操作` `推理加速`

## 📋 核心要点

1. 核心问题：现有视觉-语言模型剪枝方法忽略VLA模型的双系统特性，导致动作生成信息丢失。
2. 方法要点：采用双级重要性标准，结合语义级和动作级注意力，自适应保留关键视觉令牌。
3. 实验或效果：在多种VLA架构和机器人任务中实现最优性能，提升推理效率。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment. Token pruning (keeping salient visual tokens and dropping redundant ones) has emerged as an effective approach for accelerating Vision-Language Models (VLMs), offering a solution for efficient VLA. However, these VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution. Consequently, these methods bias token retention toward semantic cues, discard critical information for action generation, and significantly degrade VLA performance. To bridge this gap, we propose VLA-Pruner, a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation. Specifically, VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance. Based on this criterion, VLA-Pruner proposes a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens for both semantic understanding and action execution under given compute budget. Experiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks.

