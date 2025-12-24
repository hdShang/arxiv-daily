---
layout: default
title: "CityNavAgent: Aerial Vision-and-Language Navigation with Hierarchical Semantic Planning and Global Memory"
---

# CityNavAgent: Aerial Vision-and-Language Navigation with Hierarchical Semantic Planning and Global Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05622" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05622v1</a>
  <a href="https://arxiv.org/pdf/2505.05622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05622v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05622v1', 'CityNavAgent: Aerial Vision-and-Language Navigation with Hierarchical Semantic Planning and Global Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weichen Zhang, Chen Gao, Shiquan Yu, Ruiying Peng, Baining Zhao, Qian Zhang, Jinqiang Cui, Xinlei Chen, Yong Li

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-08

**🔗 代码/项目**: [GITHUB](https://github.com/VinceOuti/CityNavAgent)

---

## 💡 一句话要点

**提出CityNavAgent以解决城市空中视觉语言导航问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `无人机导航` `分层语义规划` `全局记忆模块` `大型语言模型` `城市环境` `具身人工智能`

## 📋 核心要点

1. 现有的地面视觉语言导航方法在空中环境中面临挑战，特别是在缺乏导航图和行动空间扩展的问题上。
2. 本文提出了CityNavAgent，通过分层语义规划模块将长时间任务分解为多个子目标，从而简化导航过程。
3. 实验结果显示，CityNavAgent在城市空中导航任务中表现优异，显著提升了导航效率和准确性。

## 📝 摘要（中文）

城市空中视觉语言导航（VLN）要求无人机理解自然语言指令并在复杂的城市环境中导航，是一个重要的具身人工智能挑战。现有的地面VLN代理在室内和室外环境中取得了显著成果，但在空中VLN中，由于缺乏预定义的导航图和长时间探索中行动空间的指数扩展，面临困难。本文提出了CityNavAgent，一个大型语言模型（LLM）驱动的代理，显著降低了城市空中VLN的导航复杂性。我们设计了一个分层语义规划模块（HSPM），将长时间任务分解为不同语义层次的子目标。通过实现不同能力的子目标，代理逐步达到目标。此外，开发了一个全局记忆模块，将历史轨迹存储到拓扑图中，以简化已访问目标的导航。大量基准实验表明，我们的方法在性能上达到了最先进水平，并取得了显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决城市空中视觉语言导航中的复杂性问题，现有方法在缺乏导航图和长时间探索中面临行动空间指数扩展的挑战。

**核心思路**：提出CityNavAgent，通过分层语义规划模块（HSPM）将长时间任务分解为多个子目标，使得代理可以逐步实现目标，降低导航复杂性。

**技术框架**：CityNavAgent的整体架构包括分层语义规划模块和全局记忆模块。HSPM负责将任务分解为不同语义层次的子目标，而全局记忆模块则存储历史轨迹以简化导航。

**关键创新**：最重要的创新在于引入了分层语义规划模块和全局记忆模块，使得代理能够在复杂的城市环境中高效导航，与现有方法相比，显著降低了导航复杂性。

**关键设计**：在设计中，HSPM的子目标设置基于不同的语义层次，确保代理能够逐步实现目标；全局记忆模块则通过拓扑图的方式存储历史轨迹，优化了已访问目标的导航效率。

## 📊 实验亮点

实验结果表明，CityNavAgent在城市空中导航任务中达到了最先进的性能，相较于基线方法，导航效率提升了显著的XX%（具体数据待补充），并在多个基准测试中表现优异。

## 🎯 应用场景

该研究的潜在应用领域包括城市无人机配送、搜索与救援任务以及智能城市管理等。通过提高无人机在复杂环境中的导航能力，CityNavAgent能够在实际应用中提供更高效的解决方案，推动无人机技术的广泛应用。

## 📄 摘要（原文）

> Aerial vision-and-language navigation (VLN), requiring drones to interpret natural language instructions and navigate complex urban environments, emerges as a critical embodied AI challenge that bridges human-robot interaction, 3D spatial reasoning, and real-world deployment. Although existing ground VLN agents achieved notable results in indoor and outdoor settings, they struggle in aerial VLN due to the absence of predefined navigation graphs and the exponentially expanding action space in long-horizon exploration. In this work, we propose \textbf{CityNavAgent}, a large language model (LLM)-empowered agent that significantly reduces the navigation complexity for urban aerial VLN. Specifically, we design a hierarchical semantic planning module (HSPM) that decomposes the long-horizon task into sub-goals with different semantic levels. The agent reaches the target progressively by achieving sub-goals with different capacities of the LLM. Additionally, a global memory module storing historical trajectories into a topological graph is developed to simplify navigation for visited targets. Extensive benchmark experiments show that our method achieves state-of-the-art performance with significant improvement. Further experiments demonstrate the effectiveness of different modules of CityNavAgent for aerial VLN in continuous city environments. The code is available at \href{https://github.com/VinceOuti/CityNavAgent}{link}.

