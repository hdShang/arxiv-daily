---
layout: default
title: T^2Agent A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search
---

# T^2Agent A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19768" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19768v2</a>
  <a href="https://arxiv.org/pdf/2505.19768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19768v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19768v2', 'T^2Agent A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xing Cui, Yueying Zou, Zekun Li, Peipei Li, Xinyuan Xu, Xuannan Liu, Huaibo Huang

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-11-17)

**备注**: accepted by AAAI 2026 (Oral)

---

## 💡 一句话要点

**提出T^2Agent以解决多模态虚假信息检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚假信息检测` `多模态融合` `蒙特卡洛树搜索` `动态推理` `工具包设计` `自适应验证`

## 📋 核心要点

1. 现有的虚假信息检测方法主要依赖静态流程和有限工具，难以应对多样化和复杂的伪造源。
2. 本文提出的T^2Agent结合了可扩展工具包与蒙特卡洛树搜索，能够动态收集证据并进行多源验证。
3. 实验结果显示，T^2Agent在多源虚假信息基准测试中表现优异，超越了现有的检测基线。

## 📝 摘要（中文）

现实世界中的多模态虚假信息通常源于多种伪造方式，需动态推理和自适应验证。然而，现有方法主要依赖静态流程和有限的工具使用，限制了其处理复杂性和多样性的能力。为此，本文提出了一种新颖的虚假信息检测代理T^2Agent，结合了可扩展工具包和蒙特卡洛树搜索（MCTS）。该工具包包含网络搜索、伪造检测和一致性分析等模块化工具，使用标准化模板描述，便于无缝集成和未来扩展。为避免同时使用所有工具的低效，提出了一种贪婪搜索选择器，以识别与任务相关的子集，作为MCTS的动态证据收集和多源验证的动作空间。实验结果表明，T^2Agent在复杂的多源虚假信息基准测试中，始终优于现有基线，展示了其作为无训练检测器的强大潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态虚假信息检测中的复杂性和多样性问题。现有方法因依赖静态流程和有限工具，无法有效处理来自不同伪造源的信息。

**核心思路**：T^2Agent通过引入可扩展的工具包和蒙特卡洛树搜索（MCTS），实现动态推理和自适应验证，提升了虚假信息检测的灵活性和准确性。

**技术框架**：整体架构包括一个模块化工具包，包含网络搜索、伪造检测和一致性分析等工具。通过贪婪搜索选择器，识别与任务相关的工具子集，作为MCTS的动作空间，进行动态证据收集。

**关键创新**：T^2Agent的核心创新在于将传统MCTS扩展为多源验证，能够将任务分解为针对不同伪造源的协调子任务，显著提升了检测的有效性。

**关键设计**：设计中采用了双重奖励机制，包括推理轨迹得分和置信度得分，以平衡对不同伪造源的探索与对可靠证据的利用。

## 📊 实验亮点

实验结果表明，T^2Agent在复杂的多源虚假信息基准测试中，表现出色，始终优于现有基线，具体提升幅度达到XX%（具体数据未知），验证了其作为无训练检测器的强大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、新闻真实性验证和在线广告监测等。通过提高虚假信息检测的准确性和灵活性，T^2Agent能够有效帮助用户识别和应对虚假信息，具有重要的社会价值和实际影响。

## 📄 摘要（原文）

> Real-world multimodal misinformation often arises from mixed forgery sources, requiring dynamic reasoning and adaptive verification. However, existing methods mainly rely on static pipelines and limited tool usage, limiting their ability to handle such complexity and diversity. To address this challenge, we propose \method, a novel misinformation detection agent that incorporates an extensible toolkit with Monte Carlo Tree Search (MCTS). The toolkit consists of modular tools such as web search, forgery detection, and consistency analysis. Each tool is described using standardized templates, enabling seamless integration and future expansion. To avoid inefficiency from using all tools simultaneously, a greedy search-based selector is proposed to identify a task-relevant subset. This subset then serves as the action space for MCTS to dynamically collect evidence and perform multi-source verification. To better align MCTS with the multi-source nature of misinformation detection, \method~ extends traditional MCTS with multi-source verification, which decomposes the task into coordinated subtasks targeting different forgery sources. A dual reward mechanism containing a reasoning trajectory score and a confidence score is further proposed to encourage a balance between exploration across mixed forgery sources and exploitation for more reliable evidence. We conduct ablation studies to confirm the effectiveness of the tree search mechanism and tool usage. Extensive experiments further show that \method~ consistently outperforms existing baselines on challenging mixed-source multimodal misinformation benchmarks, demonstrating its strong potential as a training-free detector.

