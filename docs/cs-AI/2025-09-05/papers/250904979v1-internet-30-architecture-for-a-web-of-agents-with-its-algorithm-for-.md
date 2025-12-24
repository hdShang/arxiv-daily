---
layout: default
title: "Internet 3.0: Architecture for a Web-of-Agents with it's Algorithm for Ranking Agents"
---

# Internet 3.0: Architecture for a Web-of-Agents with it's Algorithm for Ranking Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04979" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04979v1</a>
  <a href="https://arxiv.org/pdf/2509.04979.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04979v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04979v1', 'Internet 3.0: Architecture for a Web-of-Agents with it\'s Algorithm for Ranking Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rajesh Tembarai Krishnamachari, Srividya Rajesh

**分类**: cs.AI

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**提出DOVIS协议和AgentRank-UC算法，实现Web of Agents中Agent的动态排名。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agent网络` `Agent排名` `大型语言模型` `隐私保护` `信任机制`

## 📋 核心要点

1. 现有Agent排名方法缺乏全局视角，无法有效利用分散且私有的使用信号，导致排名不准确。
2. 论文提出DOVIS协议和AgentRank-UC算法，通过隐私保护的聚合使用数据和性能指标，实现动态、信任感知的Agent排名。
3. 仿真结果表明，该方法具有良好的收敛性、鲁棒性和抗Sybil攻击能力，验证了其在Agent网络中的可行性。

## 📝 摘要（中文）

人工智能Agent，由具备推理能力的大型语言模型（LLM）驱动，并与工具、数据和网络搜索集成，正准备将互联网转变为一个“Agent网络”：一个机器原生的生态系统，其中自主Agent可以大规模地交互、协作和执行任务。实现这一愿景需要“Agent排名”——不仅根据声明的能力选择Agent，还要根据已证实的、最近的表现选择。与Web 1.0的PageRank不同，Agent交互的全局、透明网络并不存在；使用信号是分散和私有的，使得在没有协调的情况下进行排名变得不可行。我们提出了DOVIS，一个五层操作协议（发现、编排、验证、激励、语义），它能够收集整个生态系统中最小的、保护隐私的使用和性能聚合。在此基础上，我们实现了AgentRank-UC，一种动态的、信任感知的算法，它将“使用”（选择频率）和“能力”（结果质量、成本、安全性、延迟）结合成一个统一的排名。我们展示了仿真结果和关于收敛性、鲁棒性和Sybil抵抗的理论保证，证明了协调协议和性能感知排名在实现可扩展、值得信赖的Agent网络中的可行性。

## 🔬 方法详解

**问题定义**：论文旨在解决Web of Agents中Agent排名的问题。现有方法无法有效利用分散且私有的使用信号，导致排名不准确，缺乏全局视角和信任机制。此外，隐私保护也是一个重要的挑战。

**核心思路**：核心思路是通过设计一个协调协议，在保护隐私的前提下，收集Agent的使用和性能数据，并基于这些数据进行动态排名。AgentRank-UC算法结合了使用频率和能力指标，同时考虑了Agent之间的信任关系，从而实现更准确、更可靠的排名。

**技术框架**：整体框架包含五个层次，即DOVIS协议：1) **Discovery (发现)**：Agent的注册和发现机制；2) **Orchestration (编排)**：任务分配和Agent协作流程；3) **Verification (验证)**：验证Agent执行结果的质量；4) **Incentives (激励)**：激励Agent提供高质量服务；5) **Semantics (语义)**：Agent之间通信的语义标准。AgentRank-UC算法在此基础上，利用收集到的使用和性能数据进行排名。

**关键创新**：关键创新在于DOVIS协议的设计，它能够在保护隐私的前提下，收集Agent的使用和性能数据。AgentRank-UC算法则创新性地结合了使用频率、能力指标和信任关系，实现了动态、信任感知的Agent排名。与传统的PageRank算法不同，AgentRank-UC考虑了Agent的能力和信任度，更适合Agent网络的特点。

**关键设计**：AgentRank-UC算法的关键设计包括：1) 使用频率的计算方法；2) 能力指标的定义和计算方法，例如结果质量、成本、安全性、延迟等；3) 信任关系的建模和更新机制；4) 排名算法的收敛性保证；5) 抗Sybil攻击的机制。具体的参数设置和损失函数等细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

论文通过仿真实验验证了DOVIS协议和AgentRank-UC算法的有效性。实验结果表明，该方法具有良好的收敛性、鲁棒性和抗Sybil攻击能力。具体的性能数据和对比基线在论文中进行了详细描述（未知），证明了该方法在实现可扩展、值得信赖的Agent网络中的可行性。

## 🎯 应用场景

该研究成果可应用于构建可扩展、值得信赖的Agent网络，例如智能客服、自动化流程管理、智能推荐系统等。通过Agent排名，用户可以更容易地找到高质量、可靠的Agent，从而提高任务完成效率和用户满意度。未来，该技术有望推动人工智能在各个领域的广泛应用。

## 📄 摘要（原文）

> AI agents -- powered by reasoning-capable large language models (LLMs) and integrated with tools, data, and web search -- are poised to transform the internet into a \emph{Web of Agents}: a machine-native ecosystem where autonomous agents interact, collaborate, and execute tasks at scale. Realizing this vision requires \emph{Agent Ranking} -- selecting agents not only by declared capabilities but by proven, recent performance. Unlike Web~1.0's PageRank, a global, transparent network of agent interactions does not exist; usage signals are fragmented and private, making ranking infeasible without coordination.
>   We propose \textbf{DOVIS}, a five-layer operational protocol (\emph{Discovery, Orchestration, Verification, Incentives, Semantics}) that enables the collection of minimal, privacy-preserving aggregates of usage and performance across the ecosystem. On this substrate, we implement \textbf{AgentRank-UC}, a dynamic, trust-aware algorithm that combines \emph{usage} (selection frequency) and \emph{competence} (outcome quality, cost, safety, latency) into a unified ranking. We present simulation results and theoretical guarantees on convergence, robustness, and Sybil resistance, demonstrating the viability of coordinated protocols and performance-aware ranking in enabling a scalable, trustworthy Agentic Web.

