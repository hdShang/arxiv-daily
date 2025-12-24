---
layout: default
title: "Xolver: Multi-Agent Reasoning with Holistic Experience Learning Just Like an Olympiad Team"
---

# Xolver: Multi-Agent Reasoning with Holistic Experience Learning Just Like an Olympiad Team

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14234" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14234v1</a>
  <a href="https://arxiv.org/pdf/2506.14234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14234v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14234v1', 'Xolver: Multi-Agent Reasoning with Holistic Experience Learning Just Like an Olympiad Team')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Tanzib Hosain, Salman Rahman, Md Kishor Morol, Md Rizwan Parvez

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-17

**🔗 代码/项目**: [PROJECT_PAGE](https://kagnlp.github.io/xolver.github.io/)

---

## 💡 一句话要点

**提出Xolver框架以解决大型语言模型的经验整合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体推理` `经验整合` `大型语言模型` `推理框架` `教育应用` `编程竞赛` `智能体学习`

## 📋 核心要点

1. 现有大型语言模型在推理时通常孤立处理问题，缺乏经验知识的积累与整合，导致推理能力有限。
2. Xolver框架通过整合多种经验模式，提供持久的经验记忆，使得语言模型能够在推理时借鉴过去的经验和策略。
3. 实验结果显示，Xolver在多个基准测试中超越了专门的推理智能体，尤其在GSM8K和Math-500等任务中表现优异。

## 📝 摘要（中文）

尽管在复杂推理方面取得了显著进展，现有的大型语言模型（LLMs）通常孤立地处理每个问题，未能积累或整合经验知识。与此相对，专家问题解决者如奥林匹克或编程竞赛团队利用丰富的经验，吸收教练的指导、从过去的问题中发展直觉、利用工具和库的知识、根据同伴的经验调整策略、通过反复试验不断完善推理，并在竞赛中学习相关问题。我们提出了Xolver，一个无训练的多智能体推理框架，为黑箱LLM提供持久、不断发展的整体经验记忆。Xolver整合了多种经验模式，包括外部和自我检索、工具使用、协作互动、智能体驱动的评估和迭代优化。通过在推理时学习相关策略、代码片段和抽象推理模式，Xolver避免了从头生成解决方案，标志着从孤立推理向经验感知语言智能体的转变。

## 🔬 方法详解

**问题定义**：论文旨在解决现有大型语言模型在推理过程中缺乏经验整合的问题。现有方法通常将每个问题视为独立尝试，无法利用过去的经验进行优化。

**核心思路**：Xolver的核心思路是通过构建一个持久的、不断发展的经验记忆，允许语言模型在推理时整合多种经验，从而提高推理的准确性和效率。

**技术框架**：Xolver的整体架构包括多个模块：外部和自我检索模块、工具使用模块、协作互动模块、智能体驱动的评估模块以及迭代优化模块。这些模块共同作用，形成一个经验感知的推理系统。

**关键创新**：Xolver的主要创新在于其无训练的多智能体推理框架，能够在推理时动态整合经验，而不是依赖于静态的训练数据。这一设计使得模型能够更灵活地应对复杂问题。

**关键设计**：Xolver在参数设置上采用了轻量级的骨干网络（如QWQ-32B），并通过优化损失函数和网络结构，确保在推理时能够有效地整合和利用经验知识。

## 📊 实验亮点

在多个基准测试中，Xolver表现出色，尤其在GSM8K上达到了98.1%的准确率，在Math-500上达到了99.8%。与其他高级模型相比，Xolver在轻量级骨干网络下仍能超越Qwen3-235B、Gemini 2.5 Pro等模型，展示了其在推理能力上的显著提升。

## 🎯 应用场景

Xolver框架的潜在应用领域包括教育、编程竞赛、复杂问题解决等场景。通过整合经验，Xolver能够帮助学生和专业人员更高效地解决问题，提升学习和工作效率。未来，该框架可能推动智能体在更广泛领域的应用，成为通用智能体发展的重要一步。

## 📄 摘要（原文）

> Despite impressive progress on complex reasoning, current large language models (LLMs) typically operate in isolation - treating each problem as an independent attempt, without accumulating or integrating experiential knowledge. In contrast, expert problem solvers - such as Olympiad or programming contest teams - leverage a rich tapestry of experiences: absorbing mentorship from coaches, developing intuition from past problems, leveraging knowledge of tool usage and library functionality, adapting strategies based on the expertise and experiences of peers, continuously refining their reasoning through trial and error, and learning from other related problems even during competition. We introduce Xolver, a training-free multi-agent reasoning framework that equips a black-box LLM with a persistent, evolving memory of holistic experience. Xolver integrates diverse experience modalities, including external and self-retrieval, tool use, collaborative interactions, agent-driven evaluation, and iterative refinement. By learning from relevant strategies, code fragments, and abstract reasoning patterns at inference time, Xolver avoids generating solutions from scratch - marking a transition from isolated inference toward experience-aware language agents. Built on both open-weight and proprietary models, Xolver consistently outperforms specialized reasoning agents. Even with lightweight backbones (e.g., QWQ-32B), it often surpasses advanced models including Qwen3-235B, Gemini 2.5 Pro, o3, and o4-mini-high. With o3-mini-high, it achieves new best results on GSM8K (98.1%), AIME'24 (94.4%), AIME'25 (93.7%), Math-500 (99.8%), and LiveCodeBench-V5 (91.6%) - highlighting holistic experience learning as a key step toward generalist agents capable of expert-level reasoning. Code and data are available at https://kagnlp.github.io/xolver.github.io/.

