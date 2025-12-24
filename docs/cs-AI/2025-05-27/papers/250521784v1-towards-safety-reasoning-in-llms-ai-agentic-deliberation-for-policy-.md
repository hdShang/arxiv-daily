---
layout: default
title: Towards Safety Reasoning in LLMs: AI-agentic Deliberation for Policy-embedded CoT Data Creation
---

# Towards Safety Reasoning in LLMs: AI-agentic Deliberation for Policy-embedded CoT Data Creation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21784" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21784v1</a>
  <a href="https://arxiv.org/pdf/2505.21784.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21784v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21784v1', 'Towards Safety Reasoning in LLMs: AI-agentic Deliberation for Policy-embedded CoT Data Creation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tharindu Kumarage, Ninareh Mehrabi, Anil Ramakrishna, Xinyan Zhao, Richard Zemel, Kai-Wei Chang, Aram Galstyan, Rahul Gupta, Charith Peris

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-27

**备注**: Accepted to ACL 2025 (Findings)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/AmazonScience)

---

## 💡 一句话要点

**提出AIDSAFE以解决LLMs安全推理中的数据生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全推理` `多智能体协商` `链式思维` `数据生成` `开放源代码LLMs` `政策遵循` `推理质量`

## 📋 核心要点

1. 现有的安全推理方法在生成响应时面临过度拒绝和越狱漏洞等问题，难以保证推理的准确性。
2. 本文提出AIDSAFE，通过多智能体协商迭代扩展安全政策的推理，确保生成高质量的CoT数据集。
3. 实验结果显示，AIDSAFE生成的CoT在政策遵循和推理质量上优于现有方法，显著提升了LLMs的安全性和鲁棒性。

## 📝 摘要（中文）

安全推理是一个新兴范式，LLMs在生成响应前需对安全政策进行推理，以减轻现有安全措施的局限性，如过度拒绝和越狱漏洞。然而，创建高质量的政策嵌入链式思维（CoT）数据集的资源密集型过程使得这一范式的实施面临挑战。为此，本文提出了AIDSAFE：一种利用多智能体协商的迭代推理方法，旨在扩展安全政策的推理。AIDSAFE中的数据精炼阶段确保输出高质量，消除重复和误导性思维。实验表明，基于AIDSAFE生成的CoT在政策遵循和推理质量上表现优越，显著提升了开放源代码LLMs的安全性和越狱鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决在生成响应时，LLMs对安全政策推理的不足，尤其是在创建高质量的政策嵌入CoT数据集时面临的资源消耗和推理准确性问题。

**核心思路**：AIDSAFE通过多智能体的协商机制，迭代地扩展对安全政策的推理，确保生成的CoT数据集不仅高质量且符合安全要求。

**技术框架**：AIDSAFE的整体架构包括两个主要阶段：第一阶段是多智能体协商生成初步的CoT，第二阶段是数据精炼，去除冗余和误导性思维，确保输出的高质量。

**关键创新**：AIDSAFE的创新在于其多智能体协商机制和数据精炼阶段的结合，这与现有方法的单一生成过程形成了显著区别。

**关键设计**：在AIDSAFE中，采用了特定的参数设置和损失函数，以优化CoT的生成质量，同时确保推理过程中的一致性和准确性。

## 📊 实验亮点

实验结果表明，基于AIDSAFE生成的CoT在政策遵循和推理质量上显著优于基线方法，具体表现为政策遵循率提升了XX%，推理准确性提高了YY%。这些结果表明，AIDSAFE在安全推理领域具有重要的应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括安全敏感的对话系统、自动化决策支持和智能代理等。通过提升LLMs的安全性和鲁棒性，AIDSAFE能够在实际应用中有效降低安全风险，增强用户信任，推动智能系统的广泛应用。

## 📄 摘要（原文）

> Safety reasoning is a recent paradigm where LLMs reason over safety policies before generating responses, thereby mitigating limitations in existing safety measures such as over-refusal and jailbreak vulnerabilities. However, implementing this paradigm is challenging due to the resource-intensive process of creating high-quality policy-embedded chain-of-thought (CoT) datasets while ensuring reasoning remains accurate and free from hallucinations or policy conflicts. To tackle this, we propose AIDSAFE: Agentic Iterative Deliberation for Safety Reasoning, a novel data generation recipe that leverages multi-agent deliberation to iteratively expand reasoning on safety policies. A data refiner stage in AIDSAFE ensures high-quality outputs by eliminating repetitive, redundant, and deceptive thoughts. AIDSAFE-generated CoTs provide a strong foundation for supervised fine-tuning (SFT)-based safety training. Additionally, to address the need of preference data in alignment stages, such as DPO training, we introduce a supplemental recipe that uses belief augmentation to create distinct selected and rejected CoT samples. Our evaluations demonstrate that AIDSAFE-generated CoTs achieve superior policy adherence and reasoning quality. Consequently, we show that fine-tuning open-source LLMs on these CoTs can significantly improve safety generalization and jailbreak robustness while maintaining acceptable utility and over-refusal accuracy. AIDSAFE-generated CoT datasets can be found here: https://huggingface.co/datasets/AmazonScience/AIDSAFE

