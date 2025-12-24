---
layout: default
title: Agent Context Protocols Enhance Collective Inference
---

# Agent Context Protocols Enhance Collective Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14569" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14569v1</a>
  <a href="https://arxiv.org/pdf/2505.14569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14569v1', 'Agent Context Protocols Enhance Collective Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Devansh Bhardwaj, Arjun Beniwal, Shreyas Chaudhari, Ashwin Kalyan, Tanmay Rajpurohit, Karthik R. Narasimhan, Ameet Deshpande, Vishvak Murahari

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出Agent上下文协议以增强多智能体集体推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `集体推理` `结构化协议` `智能体通信` `容错能力` `标准化消息架构` `执行蓝图`

## 📋 核心要点

1. 现有的多智能体系统通常依赖模糊的自然语言进行协调，限制了复杂交互和领域特定智能体的互操作性。
2. 本文提出Agent上下文协议（ACPs），通过结构化的协议改善智能体之间的通信和协作，提升集体推理能力。
3. 基于ACPs的系统在长时间网页辅助任务中达到了28.3%的准确率，超越了现有商业AI系统的表现。

## 📝 摘要（中文）

随着AI智能体在编码、推理和多模态理解等复杂任务中的能力不断提升，构建通用系统需要超越单个智能体，转向集体推理的范式。现有的协调方式通常依赖模糊的自然语言，限制了复杂交互并妨碍了与特定领域智能体的互操作性。为此，本文提出了Agent上下文协议（ACPs），这是一种领域和智能体无关的结构化协议家族，旨在改善智能体之间的通信、协调和错误处理。通过结合持久执行蓝图和标准化消息架构，ACPs实现了稳健且容错的多智能体集体推理，实验结果显示，基于ACPs的通用系统在AssistantBench上达到了28.3%的准确率，超越了商业AI系统。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体系统中因依赖模糊自然语言而导致的协调不精确和互操作性不足的问题。现有方法在复杂任务中表现不佳，难以实现高效的集体推理。

**核心思路**：论文提出的Agent上下文协议（ACPs）通过结构化的通信协议，结合持久执行蓝图和标准化消息架构，旨在提升智能体之间的协作效率和容错能力。这样的设计使得多智能体系统能够更好地处理复杂任务。

**技术框架**：ACPs的整体架构包括两个主要模块：持久执行蓝图和标准化消息架构。持久执行蓝图用于存储智能体的中间输出，形成明确的依赖图；标准化消息架构则确保智能体之间的通信高效且一致。

**关键创新**：ACPs的核心创新在于其结构化的协议设计，使得智能体能够在复杂任务中进行高效的集体推理。这一设计与传统的自然语言协调方式形成了鲜明对比，显著提升了系统的性能和可靠性。

**关键设计**：ACPs的设计中，持久执行蓝图的构建依赖于明确的依赖关系图，而标准化消息架构则采用了统一的消息格式，确保信息传递的准确性和一致性。

## 📊 实验亮点

实验结果表明，基于ACPs的通用系统在AssistantBench上达到了28.3%的准确率，显著超越了现有商业AI系统的表现，展示了其在长时间网页辅助和多模态技术报告生成中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括多智能体协作系统、智能客服、自动化技术支持等。通过提升智能体之间的协作能力，ACPs能够在复杂任务中实现更高效的集体推理，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> AI agents have become increasingly adept at complex tasks such as coding, reasoning, and multimodal understanding. However, building generalist systems requires moving beyond individual agents to collective inference -- a paradigm where multi-agent systems with diverse, task-specialized agents complement one another through structured communication and collaboration. Today, coordination is usually handled with imprecise, ad-hoc natural language, which limits complex interaction and hinders interoperability with domain-specific agents. We introduce Agent context protocols (ACPs): a domain- and agent-agnostic family of structured protocols for agent-agent communication, coordination, and error handling. ACPs combine (i) persistent execution blueprints -- explicit dependency graphs that store intermediate agent outputs -- with (ii) standardized message schemas, enabling robust and fault-tolerant multi-agent collective inference. ACP-powered generalist systems reach state-of-the-art performance: 28.3 % accuracy on AssistantBench for long-horizon web assistance and best-in-class multimodal technical reports, outperforming commercial AI systems in human evaluation. ACPs are highly modular and extensible, allowing practitioners to build top-tier generalist agents quickly.

