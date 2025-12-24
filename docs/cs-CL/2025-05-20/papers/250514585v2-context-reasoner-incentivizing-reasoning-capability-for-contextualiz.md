---
layout: default
title: "Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning"
---

# Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14585" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14585v2</a>
  <a href="https://arxiv.org/pdf/2505.14585.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14585v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14585v2', 'Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenbin Hu, Haoran Li, Huihao Jing, Qi Hu, Ziqian Zeng, Sirui Han, Heli Xu, Tianshu Chu, Peizhao Hu, Yangqiu Song

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-09-04)

**备注**: Accepted to EMNLP 2025 Main

---

## 💡 一句话要点

**提出Context Reasoner以解决LLMs的隐私与安全合规问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `隐私保护` `安全合规` `上下文推理` `强化学习` `法律合规` `上下文完整性`

## 📋 核心要点

1. 现有的安全和隐私缓解策略未能有效保持LLMs在风险场景中的上下文推理能力，导致合规性不足。
2. 本文提出将安全和隐私问题视为上下文合规问题，利用强化学习激励推理能力并增强合规性。
3. 实验结果显示，该方法在安全和隐私基准上提升了8.58%的准确率，并在推理能力上也有显著提高。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）展现出卓越的能力，但也带来了显著的安全和隐私风险。现有的缓解策略往往未能在风险场景中保持上下文推理能力，过于依赖敏感模式匹配，限制了保护范围。此外，这些策略忽视了既定的安全和隐私标准，导致法律合规的系统性风险。为了解决这些问题，本文将安全和隐私问题构建为基于上下文的合规问题，并在上下文完整性理论框架下，结合GDPR、欧盟人工智能法案和HIPAA等关键监管标准，采用强化学习与基于规则的奖励机制，激励上下文推理能力，同时增强安全和隐私规范的合规性。实验结果表明，该方法显著提升了法律合规性，并进一步改善了推理能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在隐私和安全合规方面的不足，现有方法往往依赖模式匹配，无法有效应对复杂的上下文推理需求。

**核心思路**：通过将安全和隐私问题构建为上下文合规问题，结合上下文完整性理论，采用强化学习方法激励模型进行有效的上下文推理。

**技术框架**：整体架构包括数据输入、上下文分析、强化学习模块和合规性评估。模型通过规则奖励机制进行训练，以提升推理能力和合规性。

**关键创新**：最重要的创新在于将上下文推理能力与法律合规性结合，通过强化学习实现了两者的协同提升，与传统的模式匹配方法本质上不同。

**关键设计**：在模型设计中，采用了基于规则的奖励机制，设置了特定的损失函数以平衡推理能力与合规性，同时优化了网络结构以适应多样化的输入场景。

## 📊 实验亮点

实验结果显示，所提方法在安全和隐私基准上实现了8.58%的准确率提升，同时在OpenThinker-7B模型上，MMLU和LegalBench基准的准确率分别提升了2.05%和8.98%，显著优于基线模型Qwen2.5-7B-Instruct。

## 🎯 应用场景

该研究的潜在应用领域包括法律合规、数据隐私保护和智能助手等。通过提升LLMs的上下文推理能力和合规性，可以有效降低安全风险，增强用户信任，推动智能系统在敏感领域的应用与发展。

## 📄 摘要（原文）

> While Large Language Models (LLMs) exhibit remarkable capabilities, they also introduce significant safety and privacy risks. Current mitigation strategies often fail to preserve contextual reasoning capabilities in risky scenarios. Instead, they rely heavily on sensitive pattern matching to protect LLMs, which limits the scope. Furthermore, they overlook established safety and privacy standards, leading to systemic risks for legal compliance. To address these gaps, we formulate safety and privacy issues into contextualized compliance problems following the Contextual Integrity (CI) theory. Under the CI framework, we align our model with three critical regulatory standards: GDPR, EU AI Act, and HIPAA. Specifically, we employ reinforcement learning (RL) with a rule-based reward to incentivize contextual reasoning capabilities while enhancing compliance with safety and privacy norms. Through extensive experiments, we demonstrate that our method not only significantly enhances legal compliance (achieving a +8.58% accuracy improvement in safety/privacy benchmarks) but also further improves general reasoning capability. For OpenThinker-7B, a strong reasoning model that significantly outperforms its base model Qwen2.5-7B-Instruct across diverse subjects, our method enhances its general reasoning capabilities, with +2.05% and +8.98% accuracy improvement on the MMLU and LegalBench benchmark, respectively.

