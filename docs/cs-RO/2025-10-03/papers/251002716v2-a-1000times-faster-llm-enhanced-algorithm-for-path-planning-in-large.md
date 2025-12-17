---
layout: default
title: A $1000\times$ Faster LLM-enhanced Algorithm For Path Planning in Large-scale Grid Maps
---

# A $1000\times$ Faster LLM-enhanced Algorithm For Path Planning in Large-scale Grid Maps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02716" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02716v2</a>
  <a href="https://arxiv.org/pdf/2510.02716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02716v2" onclick="toggleFavorite(this, '2510.02716v2', 'A $1000\times$ Faster LLM-enhanced Algorithm For Path Planning in Large-scale Grid Maps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junlin Zeng, Xin Zhang, Xiang Zhao, Yan Pan

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-03 (更新: 2025-12-01)

---

## 💡 一句话要点

**提出iLLM-A*算法，加速LLM增强的大规模栅格地图路径规划超1000倍**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `路径规划` `栅格地图` `大型语言模型` `A*算法` `增量学习`

## 📋 核心要点

1. 现有A*等算法在大规模栅格地图中路径规划面临搜索时间和内存消耗高的挑战。
2. iLLM-A*通过优化A*算法、增量学习LLM和航路点选择机制，提升路径规划效率。
3. 实验表明，iLLM-A*相比LLM-A*，速度提升超1000倍，内存节省达58.6%，路径更优。

## 📝 摘要（中文）

栅格地图中的路径规划在各种应用中备受关注。现有的A*、Dijkstra及其变体等方法在小规模地图上表现良好，但由于搜索时间和内存消耗高，无法处理大规模地图。最近，大型语言模型（LLM）在路径规划中表现出卓越的性能，但仍然存在空间幻觉和规划性能差的问题。LLM-A*利用LLM生成一系列航路点，然后使用A*算法规划相邻航路点之间的路径，从而构建完整的路径。然而，LLM-A*在大规模地图上仍然面临计算时间过高的问题。为了填补这一空白，我们对LLM-A*进行了深入研究，发现了其瓶颈，导致性能受限。因此，我们设计了一种创新的LLM增强算法，简称iLLM-A*。iLLM-A*包括3个精心设计的机制，包括A*算法的优化、用于LLM生成高质量航路点的增量学习方法，以及为A*选择合适的航路点进行路径规划。最后，在各种栅格地图上的综合评估表明，与LLM-A*相比，iLLM-A* 1)平均速度提高了1000倍以上，在极端情况下速度提高了2349.5倍，2)节省了高达58.6%的内存成本，3)实现了明显更短的路径长度和更低的路径长度标准差。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模栅格地图中，现有路径规划算法（如A*，LLM-A*）计算效率低、内存消耗大的问题。LLM-A*虽然利用LLM生成航路点，但仍存在计算时间瓶颈，限制了其在大规模地图上的应用。

**核心思路**：论文的核心思路是设计一种LLM增强的路径规划算法iLLM-A*，通过优化A*算法、增量学习LLM生成高质量航路点，并选择合适的航路点进行路径规划，从而显著提高路径规划的效率和降低内存消耗。

**技术框架**：iLLM-A*算法主要包含三个阶段：1) A*算法优化：对传统的A*算法进行改进，以适应LLM生成的航路点；2) LLM增量学习：利用增量学习方法训练LLM，使其能够生成更准确、更有效的航路点；3) 航路点选择：设计一种机制，从LLM生成的航路点中选择最合适的航路点，用于A*算法的路径规划。

**关键创新**：iLLM-A*的关键创新在于三个方面：一是A*算法的优化，使其能更好地利用LLM生成的航路点；二是LLM的增量学习方法，提高了LLM生成航路点的质量；三是航路点选择机制，减少了A*算法的搜索空间。与LLM-A*相比，iLLM-A*在LLM和A*的结合上做了更深入的优化。

**关键设计**：关于A*算法的优化，具体优化策略未知。LLM增量学习的具体实现方式未知，可能涉及到特定的损失函数或训练技巧。航路点选择机制的具体算法也未知，可能涉及到一些启发式规则或优化算法。

## 📊 实验亮点

实验结果表明，iLLM-A*算法在速度上相比LLM-A*平均提升超过1000倍，最高提升达2349.5倍。同时，内存消耗降低了高达58.6%，并且路径长度和路径长度标准差均有所降低，表明iLLM-A*不仅提高了效率，还改善了路径质量。

## 🎯 应用场景

该研究成果可广泛应用于机器人导航、自动驾驶、游戏AI、物流规划等领域。通过大幅提升大规模地图的路径规划效率，可以降低计算成本，提高系统响应速度，并为更复杂的任务规划提供支持。未来，该方法有望应用于更复杂的环境和任务中，例如三维空间路径规划、动态环境下的路径规划等。

## 📄 摘要（原文）

> Path planning in grid maps, arising from various applications, has garnered significant attention. Existing methods, such as A*, Dijkstra, and their variants, work well for small-scale maps but fail to address large-scale ones due to high search time and memory consumption. Recently, Large Language Models (LLMs) have shown remarkable performance in path planning but still suffer from spatial illusion and poor planning performance. Among all the works, LLM-A* \cite{meng2024llm} leverages LLM to generate a series of waypoints and then uses A* to plan the paths between the neighboring waypoints. In this way, the complete path is constructed. However, LLM-A* still suffers from high computational time for large-scale maps. To fill this gap, we conducted a deep investigation into LLM-A* and found its bottleneck, resulting in limited performance. Accordingly, we design an innovative LLM-enhanced algorithm, abbr. as iLLM-A*. iLLM-A* includes 3 carefully designed mechanisms, including the optimization of A*, an incremental learning method for LLM to generate high-quality waypoints, and the selection of the appropriate waypoints for A* for path planning. Finally, a comprehensive evaluation on various grid maps shows that, compared with LLM-A*, iLLM-A* \textbf{1) achieves more than $1000\times$ speedup on average, and up to $2349.5\times$ speedup in the extreme case, 2) saves up to $58.6\%$ of the memory cost, 3) achieves both obviously shorter path length and lower path length standard deviation.}

