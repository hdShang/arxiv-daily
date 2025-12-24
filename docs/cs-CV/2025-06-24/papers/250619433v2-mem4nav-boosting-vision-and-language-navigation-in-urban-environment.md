---
layout: default
title: "Mem4Nav: Boosting Vision-and-Language Navigation in Urban Environments with a Hierarchical Spatial-Cognition Long-Short Memory System"
---

# Mem4Nav: Boosting Vision-and-Language Navigation in Urban Environments with a Hierarchical Spatial-Cognition Long-Short Memory System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19433" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19433v2</a>
  <a href="https://arxiv.org/pdf/2506.19433.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19433v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19433v2', 'Mem4Nav: Boosting Vision-and-Language Navigation in Urban Environments with a Hierarchical Spatial-Cognition Long-Short Memory System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lixuan He, Haoyu Dong, Zhenxing Chen, Yangcheng Yu, Jie Feng, Yong Li

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-24 (更新: 2025-10-10)

**备注**: The paper is currently under investigation regarding concerns of potential academic misconduct. While the investigation is ongoing, the authors have voluntarily requested to withdraw the manuscript

**🔗 代码/项目**: [GITHUB](https://github.com/tsinghua-fib-lab/Mem4Nav)

---

## 💡 一句话要点

**提出Mem4Nav以解决城市环境中的视觉-语言导航问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言导航` `长短期记忆` `空间认知` `稀疏八叉树` `语义拓扑图` `多模态融合` `智能体导航`

## 📋 核心要点

1. 现有的视觉-语言导航方法在处理复杂城市环境时，缺乏统一的记忆机制，导致性能受限。
2. 本文提出的Mem4Nav通过层次化的空间认知长短期记忆系统，结合稀疏八叉树和语义拓扑图，增强了导航能力。
3. 在多个基准测试中，Mem4Nav在任务完成率、SPD和nDTW等指标上均取得显著提升，验证了其有效性。

## 📝 摘要（中文）

在大规模城市环境中，视觉-语言导航（VLN）要求具身智能体将语言指令与复杂场景相结合，并在较长时间范围内回忆相关经验。现有的模块化管道虽然提供了解释性，但缺乏统一的记忆，而端到端的（M）LLM智能体在融合视觉和语言方面表现优异，但受到固定上下文窗口和隐式空间推理的限制。本文提出了Mem4Nav，一个层次化空间认知长短期记忆系统，可以增强任何VLN骨干网络。Mem4Nav结合稀疏八叉树进行细粒度体素索引，并利用语义拓扑图实现高层次地标连接，将两者存储在通过可逆Transformer嵌入的可训练记忆标记中。长时记忆（LTM）压缩并保留历史观察，而短时记忆（STM）缓存相对坐标中的最近多模态条目，以实现实时障碍物规避和局部规划。实验结果表明，Mem4Nav在Touchdown和Map2Seq上相较于三种骨干网络（模块化、基于提示的最先进VLN和基于跨步注意力的最先进VLN）在任务完成率上提升了7-13个百分点，且有效减少了SPD，nDTW提升超过10个百分点。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂城市环境中，视觉-语言导航（VLN）智能体如何有效地将语言指令与视觉信息结合的问题。现有方法在记忆管理和空间推理方面存在不足，限制了智能体的表现。

**核心思路**：Mem4Nav的核心思路是通过引入层次化的长短期记忆系统，结合稀疏八叉树和语义拓扑图，来增强智能体的记忆能力和空间认知，从而更好地处理复杂场景中的导航任务。

**技术框架**：Mem4Nav的整体架构包括长时记忆（LTM）和短时记忆（STM）两个主要模块。LTM用于压缩和保留历史观察，而STM则缓存最近的多模态条目，以支持实时决策。系统通过可逆Transformer将信息嵌入可训练的记忆标记中。

**关键创新**：Mem4Nav的创新之处在于其层次化的记忆结构，能够在动态环境中有效地检索和利用历史信息，与传统的固定上下文窗口方法相比，显著提高了智能体的导航能力。

**关键设计**：在设计中，LTM和STM的交互机制至关重要，STM通过动态上下文检索来优化实时决策，而LTM则提供深层历史信息的无损解码，确保了信息的完整性和有效性。

## 📊 实验亮点

在Touchdown和Map2Seq基准测试中，Mem4Nav在任务完成率上提升了7-13个百分点，SPD显著降低，nDTW指标提升超过10个百分点，验证了其在视觉-语言导航中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶车辆和增强现实等场景，能够显著提升这些系统在复杂城市环境中的导航能力。未来，Mem4Nav的设计理念也可能被应用于其他多模态任务，推动智能体在更广泛的应用中实现更高的智能水平。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) in large-scale urban environments requires embodied agents to ground linguistic instructions in complex scenes and recall relevant experiences over extended time horizons. Prior modular pipelines offer interpretability but lack unified memory, while end-to-end (M)LLM agents excel at fusing vision and language yet remain constrained by fixed context windows and implicit spatial reasoning. We introduce \textbf{Mem4Nav}, a hierarchical spatial-cognition long-short memory system that can augment any VLN backbone. Mem4Nav fuses a sparse octree for fine-grained voxel indexing with a semantic topology graph for high-level landmark connectivity, storing both in trainable memory tokens embedded via a reversible Transformer. Long-term memory (LTM) compresses and retains historical observations at both octree and graph nodes, while short-term memory (STM) caches recent multimodal entries in relative coordinates for real-time obstacle avoidance and local planning. At each step, STM retrieval sharply prunes dynamic context, and, when deeper history is needed, LTM tokens are decoded losslessly to reconstruct past embeddings. Evaluated on Touchdown and Map2Seq across three backbones (modular, state-of-the-art VLN with prompt-based LLM, and state-of-the-art VLN with strided-attention MLLM), Mem4Nav yields 7-13 pp gains in Task Completion, sufficient SPD reduction, and >10 pp nDTW improvement. Ablations confirm the indispensability of both the hierarchical map and dual memory modules. Our codes are open-sourced via https://github.com/tsinghua-fib-lab/Mem4Nav.

