---
layout: default
title: "OSC: Cognitive Orchestration through Dynamic Knowledge Alignment in Multi-Agent LLM Collaboration"
---

# OSC: Cognitive Orchestration through Dynamic Knowledge Alignment in Multi-Agent LLM Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04876" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04876v1</a>
  <a href="https://arxiv.org/pdf/2509.04876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04876v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04876v1', 'OSC: Cognitive Orchestration through Dynamic Knowledge Alignment in Multi-Agent LLM Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jusheng Zhang, Yijia Fan, Kaitong Cai, Xiaofei Sun, Keze Wang

**分类**: cs.AI

**发布日期**: 2025-09-05

**备注**: Accepted at EMNLP 2025 (Long Paper)

---

## 💡 一句话要点

**提出OSC框架，通过动态知识对齐增强多Agent LLM协作中的认知协同**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多Agent协作` `大型语言模型` `认知协同` `知识对齐` `协作知识模型`

## 📋 核心要点

1. 现有方法在多Agent协作中，缺乏高效的语言交互机制，阻碍了Agent间的深度协作。
2. OSC框架通过协作知识模型（CKM）使Agent能感知协作者的认知状态，并自适应调整通信策略。
3. 实验表明，OSC显著提升了复杂推理和问题解决任务的性能和通信效率，促进了Agent间的认知协同。

## 📝 摘要（中文）

本文介绍了一种知识感知的自适应协作框架OSC（Orchestrating Cognitive Synergy），旨在增强多Agent系统中大型语言模型的认知协同。现有工作主要集中在Agent选择和结果聚合方面，但专家Agent之间进行深度协作的高效语言交互仍然是一个关键瓶颈。OSC通过在选择和聚合之间引入一个关键的中间层来解决这个问题，引入了协作知识模型（CKM），使每个Agent能够动态地感知其协作者的认知状态。通过实时认知差距分析，Agent使用学习到的策略自适应地调整通信行为，包括内容焦点、细节级别和表达风格。在复杂推理和问题解决基准上的实验表明，OSC显著提高了任务性能和通信效率，将“并行工作的个体”转变为“深度协作的认知团队”。该框架不仅优化了多Agent协作，而且为LLM Agent的交互行为提供了新的见解。

## 🔬 方法详解

**问题定义**：现有方法在多Agent LLM协作中，Agent之间的沟通效率低下，无法有效进行深度协作。Agent通常独立工作，缺乏对彼此认知状态的感知，导致信息冗余或缺失，最终影响整体任务完成质量。现有方法主要关注Agent的选择和结果的聚合，忽略了Agent之间高效的语言交互。

**核心思路**：OSC的核心思路是通过引入协作知识模型（CKM），使每个Agent能够动态地感知其协作者的认知状态。基于对协作Agent认知状态的理解，Agent可以自适应地调整其通信行为，包括内容焦点、细节层次和表达方式，从而实现更高效、更精准的协作。

**技术框架**：OSC框架位于Agent选择和结果聚合之间，作为一个中间层。其主要流程包括：1) 每个Agent维护一个CKM，用于追踪和建模其他Agent的认知状态；2) 通过实时认知差距分析，识别Agent之间的知识差异；3) 基于认知差距，Agent使用学习到的策略调整通信行为；4) 调整后的信息传递给其他Agent，促进知识共享和协同。

**关键创新**：OSC的关键创新在于引入了协作知识模型（CKM），使得Agent能够动态感知协作者的认知状态，并基于此进行自适应的通信调整。这与现有方法中Agent独立工作或简单信息交换的方式有本质区别，实现了更深层次的认知协同。

**关键设计**：CKM的具体实现方式未知，但可以推测可能使用了某种形式的知识图谱或向量表示来编码Agent的认知状态。通信策略的调整可能涉及到强化学习或策略梯度等方法，以学习最优的通信行为。具体的损失函数和网络结构等技术细节在论文中未明确说明。

## 📊 实验亮点

实验结果表明，OSC框架在复杂推理和问题解决基准上显著提高了任务性能和通信效率。具体提升幅度未知，但论文强调OSC能够将“并行工作的个体”转变为“深度协作的认知团队”，表明其在提升协作效率方面具有显著优势。

## 🎯 应用场景

OSC框架可应用于各种需要多Agent协作的复杂任务，例如：协同知识库构建、分布式问题求解、智能客服团队等。该研究有助于提升多Agent系统的整体效率和智能化水平，促进人机协作和人工智能的更广泛应用。未来，该框架还可扩展到机器人协作、自动驾驶等领域。

## 📄 摘要（原文）

> This paper introduces OSC (Orchestrating Cognitive Synergy), a knowledge-aware adaptive collaboration framework designed to enhance cognitive synergy in multi-agent systems with large language models. While prior work has advanced agent selection and result aggregation, efficient linguistic interactions for deep collaboration among expert agents remain a critical bottleneck. OSC addresses this gap as a pivotal intermediate layer between selection and aggregation, introducing Collaborator Knowledge Models (CKM) to enable each agent to dynamically perceive its collaborators' cognitive states. Through real-time cognitive gap analysis, agents adaptively adjust communication behaviors, including content focus, detail level, and expression style, using learned strategies. Experiments on complex reasoning and problem-solving benchmarks demonstrate that OSC significantly improves task performance and communication efficiency, transforming "parallel-working individuals'' into a "deeply collaborative cognitive team.'' This framework not only optimizes multi-agent collaboration but also offers new insights into LLM agent interaction behaviors.

