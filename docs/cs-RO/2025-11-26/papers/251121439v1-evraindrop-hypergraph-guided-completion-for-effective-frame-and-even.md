---
layout: default
title: EvRainDrop: HyperGraph-guided Completion for Effective Frame and Event Stream Aggregation
---

# EvRainDrop: HyperGraph-guided Completion for Effective Frame and Event Stream Aggregation

**arXiv**: [2511.21439v1](https://arxiv.org/abs/2511.21439) | [PDF](https://arxiv.org/pdf/2511.21439.pdf)

**作者**: Futian Wang, Fan Zhang, Xiao Wang, Mengqi Wang, Dexing Huang, Jin Tang

---

## 💡 一句话要点

**提出超图引导的事件流补全机制，解决事件相机空间稀疏导致的欠采样问题。**

**关键词**: `事件相机` `超图学习` `多模态融合` `事件流补全` `自注意力机制`

## 📋 核心要点

1. 核心问题：事件相机输出空间稀疏事件流，现有方法难以处理欠采样。
2. 方法要点：使用超图连接事件令牌，通过消息传递补全稀疏事件。
3. 实验或效果：在单标签和多标签事件分类任务中验证有效性。

## 📄 摘要（原文）

> Event cameras produce asynchronous event streams that are spatially sparse yet temporally dense. Mainstream event representation learning algorithms typically use event frames, voxels, or tensors as input. Although these approaches have achieved notable progress, they struggle to address the undersampling problem caused by spatial sparsity. In this paper, we propose a novel hypergraph-guided spatio-temporal event stream completion mechanism, which connects event tokens across different times and spatial locations via hypergraphs and leverages contextual information message passing to complete these sparse events. The proposed method can flexibly incorporate RGB tokens as nodes in the hypergraph within this completion framework, enabling multi-modal hypergraph-based information completion. Subsequently, we aggregate hypergraph node information across different time steps through self-attention, enabling effective learning and fusion of multi-modal features. Extensive experiments on both single- and multi-label event classification tasks fully validated the effectiveness of our proposed framework. The source code of this paper will be released on https://github.com/Event-AHU/EvRainDrop.

