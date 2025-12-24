---
layout: default
title: "JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation"
---

# JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22548" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22548v1</a>
  <a href="https://arxiv.org/pdf/2509.22548.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22548v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22548v1', 'JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuang Zeng, Dekang Qi, Xinyuan Chang, Feng Xiong, Shichao Xie, Xiaolong Wu, Shiyi Liang, Mu Xu, Xing Wei

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-26

**备注**: Project page: https://miv-xjtu.github.io/JanusVLN.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://miv-xjtu.github.io/JanusVLN.github.io/)

---

## 💡 一句话要点

**JanusVLN：利用双重隐式记忆解耦语义与空间信息，提升视觉语言导航性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `隐式记忆` `多模态学习` `空间推理` `机器人导航`

## 📋 核心要点

1. 现有VLN方法依赖显式语义记忆，导致空间信息损失、计算冗余和内存膨胀，影响导航效率。
2. JanusVLN提出双重隐式神经记忆，分别建模空间几何和视觉语义信息，实现紧凑高效的记忆存储。
3. 实验结果表明，JanusVLN在VLN任务上取得了SOTA性能，成功率显著优于现有方法。

## 📝 摘要（中文）

视觉语言导航（VLN）要求智能体在未知的环境中，根据自然语言指令和连续视频流进行导航。最近VLN的进展得益于多模态大型语言模型强大的语义理解能力。然而，这些方法通常依赖于显式的语义记忆，例如构建文本认知地图或存储历史视觉帧。这种类型的方法存在空间信息丢失、计算冗余和内存膨胀的问题，阻碍了高效导航。受到人类导航中隐式场景表征的启发，类似于左脑的语义理解和右脑的空间认知，我们提出了JanusVLN，一种新颖的VLN框架，其特点是双重隐式神经记忆，将空间几何记忆和视觉语义记忆建模为独立的、紧凑的、固定大小的神经表征。该框架首先扩展了MLLM，使其包含来自空间几何编码器的3D先验知识，从而增强了仅基于RGB输入的模型的空间推理能力。然后，将来自空间几何和视觉语义编码器的历史键值缓存构建为双重隐式记忆。通过仅保留初始和滑动窗口中token的KV，避免了冗余计算，实现了高效的增量更新。大量实验表明，JanusVLN优于20多种最新的方法，实现了SOTA性能。例如，与使用多种数据类型作为输入的方法相比，成功率提高了10.5-35.5%，与使用更多RGB训练数据的方法相比，成功率提高了3.6-10.8%。这表明所提出的双重隐式神经记忆作为一种新的范例，为未来的VLN研究探索了有希望的新方向。

## 🔬 方法详解

**问题定义**：视觉语言导航（VLN）任务旨在让智能体根据自然语言指令在未知环境中导航。现有方法，特别是基于多模态大语言模型的方法，通常依赖于显式的语义记忆，例如构建文本认知地图或存储历史视觉帧。这些方法的痛点在于空间信息的丢失，计算冗余以及内存占用过大，限制了导航的效率和可扩展性。

**核心思路**：JanusVLN的核心思路是模仿人类大脑在导航过程中的信息处理方式，将语义理解和空间认知解耦。借鉴人类左脑负责语义理解，右脑负责空间认知的概念，论文提出了双重隐式神经记忆，分别用于存储视觉语义信息和空间几何信息。通过隐式表征，可以避免显式记忆带来的冗余和信息损失。

**技术框架**：JanusVLN的整体框架包含以下几个主要模块：1）空间几何编码器：用于提取场景的3D先验知识，增强模型的空间推理能力。2）视觉语义编码器：用于提取视觉场景的语义信息。3）双重隐式记忆：分别存储空间几何和视觉语义编码器的历史键值缓存，并进行增量更新。4）多模态大语言模型（MLLM）：融合来自双重隐式记忆的信息，生成导航决策。整体流程是，首先利用空间几何编码器和视觉语义编码器提取特征，然后构建双重隐式记忆，最后利用MLLM进行决策。

**关键创新**：JanusVLN最重要的技术创新点在于提出了双重隐式神经记忆。与现有方法依赖显式记忆不同，JanusVLN将空间几何和视觉语义信息编码为紧凑的隐式表征，避免了冗余计算和信息损失。此外，通过仅保留初始和滑动窗口中token的KV，实现了高效的增量更新。

**关键设计**：在空间几何编码器中，使用了3D先验知识来增强模型的空间推理能力。在双重隐式记忆中，采用了键值缓存机制，并仅保留初始和滑动窗口中的token，以减少计算量。损失函数方面，可能采用了交叉熵损失或类似的损失函数来优化导航决策。

## 📊 实验亮点

JanusVLN在VLN任务上取得了显著的性能提升，超越了20多种最新的方法，实现了SOTA性能。与使用多种数据类型作为输入的方法相比，成功率提高了10.5-35.5%，与使用更多RGB训练数据的方法相比，成功率提高了3.6-10.8%。这些结果表明，JanusVLN提出的双重隐式神经记忆是一种有效的VLN解决方案。

## 🎯 应用场景

JanusVLN的研究成果可应用于机器人导航、自动驾驶、虚拟现实等领域。该方法能够提升智能体在复杂环境中的导航能力，使其能够更好地理解自然语言指令，并做出更准确的决策。未来，该技术有望应用于智能家居、物流配送、安防巡逻等场景，提高工作效率和生活质量。

## 📄 摘要（原文）

> Vision-and-Language Navigation requires an embodied agent to navigate through unseen environments, guided by natural language instructions and a continuous video stream. Recent advances in VLN have been driven by the powerful semantic understanding of Multimodal Large Language Models. However, these methods typically rely on explicit semantic memory, such as building textual cognitive maps or storing historical visual frames. This type of method suffers from spatial information loss, computational redundancy, and memory bloat, which impede efficient navigation. Inspired by the implicit scene representation in human navigation, analogous to the left brain's semantic understanding and the right brain's spatial cognition, we propose JanusVLN, a novel VLN framework featuring a dual implicit neural memory that models spatial-geometric and visual-semantic memory as separate, compact, and fixed-size neural representations. This framework first extends the MLLM to incorporate 3D prior knowledge from the spatial-geometric encoder, thereby enhancing the spatial reasoning capabilities of models based solely on RGB input. Then, the historical key-value caches from the spatial-geometric and visual-semantic encoders are constructed into a dual implicit memory. By retaining only the KVs of tokens in the initial and sliding window, redundant computation is avoided, enabling efficient incremental updates. Extensive experiments demonstrate that JanusVLN outperforms over 20 recent methods to achieve SOTA performance. For example, the success rate improves by 10.5-35.5 compared to methods using multiple data types as input and by 3.6-10.8 compared to methods using more RGB training data. This indicates that the proposed dual implicit neural memory, as a novel paradigm, explores promising new directions for future VLN research. Ours project page: https://miv-xjtu.github.io/JanusVLN.github.io/.

