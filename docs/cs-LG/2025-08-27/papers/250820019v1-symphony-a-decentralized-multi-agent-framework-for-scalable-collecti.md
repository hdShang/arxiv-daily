---
layout: default
title: "Symphony: A Decentralized Multi-Agent Framework for Scalable Collective Intelligence"
---

# Symphony: A Decentralized Multi-Agent Framework for Scalable Collective Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20019" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20019v1</a>
  <a href="https://arxiv.org/pdf/2508.20019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20019v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20019v1', 'Symphony: A Decentralized Multi-Agent Framework for Scalable Collective Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ji Wang, Kashing Chen, Xinyuan Song, Ke Zhang, Lynn Ai, Eric Yang, Bill Shi

**分类**: cs.LG, cs.AI, cs.CL, cs.MA

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出Symphony以解决集中式多代理系统的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `去中心化` `多代理系统` `大型语言模型` `动态任务分配` `链式思维` `隐私保护` `可扩展性`

## 📋 核心要点

1. 现有的集中式多代理系统在部署成本和适应性方面存在显著不足，限制了其应用范围。
2. Symphony通过去中心化的设计，利用轻量级LLM在消费级GPU上实现高效协调，提升了系统的灵活性和可扩展性。
3. 实验结果表明，Symphony在推理基准测试中显著超越了现有方法，准确性提升明显，且在不同模型中表现出良好的鲁棒性。

## 📝 摘要（中文）

现有的基于大型语言模型（LLM）的代理框架大多依赖于集中式协调，这导致了高昂的部署成本、僵化的通信拓扑和有限的适应性。为了解决这些挑战，本文提出了Symphony，一个去中心化的多代理系统，使轻量级LLM能够在消费级GPU上进行协调。Symphony引入了三个关键机制：去中心化的能力记录账本、动态任务分配的信标选择协议，以及基于链式思维的加权结果投票。这一设计形成了一个节省隐私、可扩展且容错的低开销协调机制。实验证明，Symphony在推理基准测试中超越了现有基线，取得了显著的准确性提升，并在不同能力模型中表现出鲁棒性。

## 🔬 方法详解

**问题定义**：现有的集中式多代理系统在资源利用和适应性方面存在瓶颈，导致高成本和低效率。

**核心思路**：Symphony通过去中心化的机制，允许轻量级LLM在消费级硬件上进行高效的协作，从而降低了系统的复杂性和成本。

**技术框架**：Symphony的架构包括三个主要模块：去中心化的能力记录账本、信标选择协议用于动态任务分配，以及基于链式思维的加权结果投票机制。

**关键创新**：Symphony的核心创新在于去中心化的设计理念，打破了传统集中式系统的局限，使得多个代理能够独立而高效地协作。

**关键设计**：在设计中，Symphony采用了去中心化账本来记录代理的能力，信标选择协议动态分配任务，并通过加权投票机制提高结果的准确性和可靠性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在推理基准测试中，Symphony的性能显著优于现有基线，准确性提升幅度达到XX%（具体数据未知），并且在不同能力模型中展现出良好的鲁棒性，证明了其设计的有效性和适用性。

## 🎯 应用场景

Symphony的去中心化多代理框架具有广泛的应用潜力，尤其适用于需要高效协调和灵活适应的场景，如智能家居、自动驾驶和分布式计算等领域。其设计理念能够推动多代理系统在资源受限环境中的应用，提升系统的整体性能和可扩展性。

## 📄 摘要（原文）

> Most existing Large Language Model (LLM)-based agent frameworks rely on centralized orchestration, incurring high deployment costs, rigid communication topologies, and limited adaptability. To address these challenges, we introduce Symphony, a decentralized multi-agent system which enables lightweight LLMs on consumer-grade GPUs to coordinate. Symphony introduces three key mechanisms: (1) a decentralized ledger that records capabilities, (2) a Beacon-selection protocol for dynamic task allocation, and (3) weighted result voting based on CoTs. This design forms a privacy-saving, scalable, and fault-tolerant orchestration with low overhead. Empirically, Symphony outperforms existing baselines on reasoning benchmarks, achieving substantial accuracy gains and demonstrating robustness across models of varying capacities.

