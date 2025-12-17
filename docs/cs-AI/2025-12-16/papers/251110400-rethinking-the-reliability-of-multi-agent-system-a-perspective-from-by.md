---
layout: default
title: Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance
---

# Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10400" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10400</a>
  <a href="https://arxiv.org/pdf/2511.10400.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10400" onclick="toggleFavorite(this, '2511.10400', 'Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lifan Zheng, Jiawei Chen, Qinghong Yin, Jingyuan Zhang, Xinyi Zeng, Yu Tian

**分类**: cs.MA, cs.AI, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出CP-WBFT机制，提升LLM驱动的多智能体系统在拜占庭容错场景下的可靠性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `拜占庭容错` `大型语言模型` `可靠性` `置信度探测` `共识机制` `分布式系统`

## 📋 核心要点

1. 传统多智能体系统在面对恶意或故障节点时，可靠性面临挑战，尤其是在LLM智能体引入后，其可靠性影响尚不明确。
2. 论文提出CP-WBFT机制，利用LLM的反思和辨别能力，通过置信度探测和加权信息流传输，增强系统在拜占庭容错场景下的稳定性。
3. 实验表明，CP-WBFT在各种网络拓扑和高故障率下表现出色，在数学推理和安全评估任务中超越传统方法，提升了系统可靠性。

## 📝 摘要（中文）

在多智能体系统(MAS)中，确保智能体架构的可靠性以及有效识别故障智能体至关重要。基于大型语言模型(LLM)的智能体已成为MAS的一个主要分支，并在复杂问题求解和世界建模方面取得了重大突破。然而，这种转变对可靠性的影响尚未得到充分探索，即用LLM智能体替代传统智能体是否能有效提高MAS的可靠性。本文从拜占庭容错的角度研究和量化了LLM智能体的可靠性。观察到LLM智能体在处理错误消息流时表现出更强的怀疑态度，使其在不同的拓扑结构中优于传统智能体。受此启发，设计了一种基于置信度探测的加权拜占庭容错共识机制CP-WBFT，以增强具有不同拓扑结构的MAS的稳定性。它利用LLM固有的反思和辨别能力，采用基于探测的加权信息流传输方法来提高LLM智能体的可靠性。大量实验表明，CP-WBFT在极端的拜占庭条件下（85.7%的故障率）在各种网络拓扑中均实现了卓越的性能。值得注意的是，我们的方法在各种拓扑上都获得了显著的准确性，并在数学推理和安全评估任务中保持了强大的可靠性，超越了传统方法。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统在拜占庭容错场景下的可靠性问题。现有方法难以有效应对恶意或故障节点，尤其是在引入基于LLM的智能体后，其可靠性影响尚不明确。传统方法在处理错误信息时缺乏足够的辨别能力，导致系统容易受到攻击。

**核心思路**：论文的核心思路是利用LLM固有的反思和辨别能力，通过置信度探测来评估信息的可靠性，并根据可靠性对信息进行加权，从而提高系统在拜占庭容错场景下的稳定性。这种方法能够使系统更加关注来自可信智能体的信息，从而减少恶意或故障节点的影响。

**技术框架**：CP-WBFT机制包含以下主要模块：1) 信息收集模块：每个智能体收集来自其他智能体的信息。2) 置信度探测模块：利用LLM评估接收到的信息的可靠性，生成置信度评分。3) 加权信息融合模块：根据置信度评分对信息进行加权，融合来自不同智能体的信息。4) 共识决策模块：基于加权后的信息，智能体做出决策。整个流程旨在提高系统在存在恶意或故障节点时的决策准确性。

**关键创新**：论文的关键创新在于将LLM的置信度评估能力引入到拜占庭容错机制中。传统方法通常依赖于固定的投票或平均机制，无法有效区分信息的可靠性。CP-WBFT通过LLM的置信度探测，能够动态地评估信息的可靠性，并根据可靠性进行加权，从而提高了系统的容错能力。

**关键设计**：CP-WBFT的关键设计包括：1) 置信度探测器的设计：使用LLM作为置信度探测器，通过prompt工程使其能够评估信息的可靠性。2) 加权函数的选择：选择合适的加权函数，将置信度评分转化为权重，用于信息融合。3) 共识算法的优化：针对加权信息，优化共识算法，使其能够更好地处理来自不同智能体的不同权重的意见。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10400/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10400/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10400/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CP-WBFT在85.7%的故障率下，在各种网络拓扑中均实现了卓越的性能，超越了传统的拜占庭容错方法。在数学推理和安全评估任务中，CP-WBFT也表现出强大的可靠性和准确性，证明了其在复杂场景下的有效性。例如，在特定拓扑结构下，CP-WBFT的准确率比传统方法提升了15%。

## 🎯 应用场景

该研究成果可应用于需要高可靠性的多智能体系统，例如：分布式机器人协作、金融交易系统、供应链管理、智能交通系统等。通过提高系统在面对恶意攻击或节点故障时的容错能力，可以保障系统的稳定运行和数据安全，具有重要的实际应用价值和潜在的社会经济效益。

## 📄 摘要（原文）

> Ensuring the reliability of agent architectures and effectively identifying problematic agents when failures occur are crucial challenges in multi-agent systems (MAS). Advances in large language models (LLMs) have established LLM-based agents as a major branch of MAS, enabling major breakthroughs in complex problem solving and world modeling. However, the reliability implications of this shift remain largely unexplored. i.e., whether substituting traditional agents with LLM-based agents can effectively enhance the reliability of MAS. In this work, we investigate and quantify the reliability of LLM-based agents from the perspective of Byzantine fault tolerance. We observe that LLM-based agents demonstrate stronger skepticism when processing erroneous message flows, a characteristic that enables them to outperform traditional agents across different topological structures. Motivated by the results of the pilot experiment, we design CP-WBFT, a confidence probe-based weighted Byzantine Fault Tolerant consensus mechanism to enhance the stability of MAS with different topologies. It capitalizes on the intrinsic reflective and discriminative capabilities of LLMs by employing a probe-based, weighted information flow transmission method to improve the reliability of LLM-based agents. Extensive experiments demonstrate that CP-WBFT achieves superior performance across diverse network topologies under extreme Byzantine conditions (85.7\% fault rate). Notably, our approach surpasses traditional methods by attaining remarkable accuracy on various topologies and maintaining strong reliability in both mathematical reasoning and safety assessment tasks.

