---
layout: default
title: "OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows"
---

# OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09124" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09124v1</a>
  <a href="https://arxiv.org/pdf/2508.09124.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09124v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09124v1', 'OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weixuan Wang, Dongge Han, Daniel Madrigal Diaz, Jin Xu, Victor Rühle, Saravan Rajmohan

**分类**: cs.CL

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出OdysseyBench以解决长时间复杂办公应用工作流程评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间工作流程` `大型语言模型` `办公应用` `基准评估` `多步骤推理` `自动化生成` `复杂任务`

## 📋 核心要点

1. 现有基准主要关注原子任务，无法捕捉复杂工作流程中的长期上下文依赖和多交互协调。
2. 论文提出OdysseyBench基准，涵盖真实和合成的复杂任务，评估LLM代理在长时间工作流程中的表现。
3. 实验结果显示，OdysseyBench在评估LLM代理能力方面优于现有的原子任务基准，提供了更准确的评估。

## 📝 摘要（中文）

自主代理 powered by 大型语言模型（LLMs）在需要复杂、长时间工作流程的现实应用中越来越多地被部署。然而，现有基准主要集中在自包含和独立的原子任务上，未能捕捉现实场景中所需的长期上下文依赖和多交互协调。为了解决这一问题，我们提出了OdysseyBench，这是一个全面的基准，用于评估LLM代理在包括Word、Excel、PDF、电子邮件和日历等多种办公应用中的长时间工作流程。我们的基准包括两个互补的分支：OdysseyBench+和OdysseyBench-Neo，涵盖了300个真实用例任务和302个新合成的复杂任务。每个任务要求代理从长时间交互历史中识别关键信息，并在各种应用中进行多步推理。我们还提出了HomerAgents，一个多代理框架，通过系统的环境探索、任务生成和对话合成，自动生成长时间工作流程基准。我们的广泛评估表明，OdysseyBench有效挑战了最先进的LLM代理，提供了更准确的能力评估。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有基准无法有效评估LLM代理在复杂长时间工作流程中的表现这一问题。现有方法主要集中在原子任务上，缺乏对长期上下文和多交互的考量。

**核心思路**：论文的核心思路是通过引入OdysseyBench基准，设计出能够涵盖多种办公应用的复杂任务，进而评估LLM代理在长时间工作流程中的能力。这样的设计能够更好地模拟现实场景中的工作流程。

**技术框架**：OdysseyBench由两个主要部分组成：OdysseyBench+和OdysseyBench-Neo，分别包含真实用例和新合成的复杂任务。同时，HomerAgents框架用于自动生成长时间工作流程基准，包含环境探索、任务生成和对话合成等模块。

**关键创新**：最重要的技术创新点在于OdysseyBench的设计，使其能够有效评估LLM代理在复杂场景中的表现，填补了现有基准的空白。与传统原子任务基准相比，OdysseyBench更关注长期上下文和多步骤推理。

**关键设计**：在任务生成过程中，采用了系统化的环境探索方法，确保生成的任务具有代表性和挑战性。同时，设计了多步骤推理机制，以支持代理在不同应用之间的协调与信息提取。

## 📊 实验亮点

实验结果表明，OdysseyBench在评估LLM代理方面显著优于现有的原子任务基准，提供了更准确的能力评估。具体而言，OdysseyBench能够有效挑战最先进的LLM代理，提升了评估的准确性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括办公自动化、智能助手和企业级软件等。通过提供一个全面的评估基准，OdysseyBench将推动LLM代理在实际生产力场景中的发展与应用，提升工作效率和用户体验。未来，随着更多复杂任务的引入，OdysseyBench有望成为评估LLM代理能力的重要标准。

## 📄 摘要（原文）

> Autonomous agents powered by large language models (LLMs) are increasingly deployed in real-world applications requiring complex, long-horizon workflows. However, existing benchmarks predominantly focus on atomic tasks that are self-contained and independent, failing to capture the long-term contextual dependencies and multi-interaction coordination required in realistic scenarios. To address this gap, we introduce OdysseyBench, a comprehensive benchmark for evaluating LLM agents on long-horizon workflows across diverse office applications including Word, Excel, PDF, Email, and Calendar. Our benchmark comprises two complementary splits: OdysseyBench+ with 300 tasks derived from real-world use cases, and OdysseyBench-Neo with 302 newly synthesized complex tasks. Each task requires agent to identify essential information from long-horizon interaction histories and perform multi-step reasoning across various applications. To enable scalable benchmark creation, we propose HomerAgents, a multi-agent framework that automates the generation of long-horizon workflow benchmarks through systematic environment exploration, task generation, and dialogue synthesis. Our extensive evaluation demonstrates that OdysseyBench effectively challenges state-of-the-art LLM agents, providing more accurate assessment of their capabilities in complex, real-world contexts compared to existing atomic task benchmarks. We believe that OdysseyBench will serve as a valuable resource for advancing the development and evaluation of LLM agents in real-world productivity scenarios. In addition, we release OdysseyBench and HomerAgents to foster research along this line.

