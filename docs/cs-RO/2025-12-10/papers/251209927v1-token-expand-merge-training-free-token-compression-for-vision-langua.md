---
layout: default
title: Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models
---

# Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models

**arXiv**: [2512.09927v1](https://arxiv.org/abs/2512.09927) | [PDF](https://arxiv.org/pdf/2512.09927.pdf)

**作者**: Yifan Ye, Jiaqi Ma, Jun Cen, Zhihe Lu

---

## 💡 一句话要点

**提出TEAM-VLA训练无关的令牌压缩框架，以加速视觉-语言-动作模型推理并保持性能。**

**关键词**: `视觉-语言-动作模型` `令牌压缩` `训练无关优化` `推理加速` `机器人感知控制`

## 📋 核心要点

1. 核心问题：大规模VLA模型在实时部署中面临高计算成本和延迟挑战。
2. 方法要点：通过动态令牌扩展和动作感知合并，在单次前向传播中压缩令牌。
3. 实验或效果：在LIBERO基准上提升推理速度，同时维持或超越原始模型任务成功率。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models pretrained on large-scale multimodal datasets have emerged as powerful foundations for robotic perception and control. However, their massive scale, often billions of parameters, poses significant challenges for real-time deployment, as inference becomes computationally expensive and latency-sensitive in dynamic environments. To address this, we propose Token Expand-and-Merge-VLA (TEAM-VLA), a training-free token compression framework that accelerates VLA inference while preserving task performance. TEAM-VLA introduces a dynamic token expansion mechanism that identifies and samples additional informative tokens in the spatial vicinity of attention-highlighted regions, enhancing contextual completeness. These expanded tokens are then selectively merged in deeper layers under action-aware guidance, effectively reducing redundancy while maintaining semantic coherence. By coupling expansion and merging within a single feed-forward pass, TEAM-VLA achieves a balanced trade-off between efficiency and effectiveness, without any retraining or parameter updates. Extensive experiments on LIBERO benchmark demonstrate that TEAM-VLA consistently improves inference speed while maintaining or even surpassing the task success rate of full VLA models. The code is public available on \href{https://github.com/Jasper-aaa/TEAM-VLA}{https://github.com/Jasper-aaa/TEAM-VLA}

