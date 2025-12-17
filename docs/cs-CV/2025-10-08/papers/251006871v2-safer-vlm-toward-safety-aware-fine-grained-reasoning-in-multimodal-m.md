---
layout: default
title: SaFeR-VLM: Toward Safety-aware Fine-grained Reasoning in Multimodal Models
---

# SaFeR-VLM: Toward Safety-aware Fine-grained Reasoning in Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06871" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06871v2</a>
  <a href="https://arxiv.org/pdf/2510.06871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06871v2" onclick="toggleFavorite(this, '2510.06871v2', 'SaFeR-VLM: Toward Safety-aware Fine-grained Reasoning in Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huahui Yi, Kun Wang, Qiankun Li, Miao Yu, Liang Lin, Gongli Xi, Hao Wu, Xuming Hu, Kang Li, Yang Liu

**分类**: cs.LG, cs.CV

**发布日期**: 2025-10-08 (更新: 2025-10-09)

**🔗 代码/项目**: [GITHUB](https://github.com/HarveyYi/SaFeR-VLM)

---

## 💡 一句话要点

**SaFeR-VLM：面向安全的多模态模型细粒度推理框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `安全性` `强化学习` `安全对齐` `大型语言模型`

## 📋 核心要点

1. 现有MLRMs在安全性方面存在不足，容易受到对抗性攻击，且缺乏对推理过程的约束。
2. SaFeR-VLM通过安全对齐的强化学习，将安全性嵌入多模态推理，主动驱动安全推理。
3. SaFeR-VLM在安全性和helpfulness上超越了同等规模和更大规模的模型，且代码已开源。

## 📝 摘要（中文）

多模态大型推理模型(MLRMs)在跨模态推理方面表现出色，但常常在对抗性或不安全提示下放大安全风险，我们称之为“推理税”。现有的防御措施主要在输出层面起作用，没有约束推理过程，使模型暴露于隐性风险。本文提出了SaFeR-VLM，一个安全对齐的强化学习框架，将安全性直接嵌入到多模态推理中。该框架集成了四个组成部分：(I) QI-Safe-10K，一个强调安全关键和推理敏感案例的精选数据集；(II) 安全感知rollout，其中不安全的生成经历反思和纠正，而不是被丢弃；(III) 结构化奖励建模，具有多维加权标准和对幻觉和矛盾的显式惩罚；(IV) GRPO优化，它强化安全和纠正的轨迹。这种统一的设计将安全性从被动保障转变为推理的主动驱动力，从而实现可扩展和可泛化的安全感知推理。SaFeR-VLM进一步展示了对显性和隐性风险的鲁棒性，支持超越表面过滤的动态和可解释的安全决策。SaFeR-VLM-3B在六个基准测试中，安全性和有用性的平均性能分别达到70.13和78.97，超过了同等规模和大于10倍规模的模型，如Skywork-R1V3-38B、Qwen2.5VL-72B和GLM4.5V-106B。值得注意的是，SaFeR-VLM-7B受益于其规模的增加，在安全指标上分别超过GPT-5-mini和Gemini-2.5-Flash 6.47和16.76个点，并且在helpfulness性能上没有任何下降。我们的代码可在https://github.com/HarveyYi/SaFeR-VLM获得。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型推理模型（MLRMs）在面对对抗性或不安全提示时，容易产生不安全输出的问题，即所谓的“推理税”。现有方法主要集中在输出层面的过滤，缺乏对模型推理过程的约束，导致模型容易受到隐性风险的影响。

**核心思路**：论文的核心思路是将安全性融入到模型的推理过程中，而不是仅仅在输出层面进行过滤。通过强化学习，使模型在推理过程中能够识别并纠正不安全的行为，从而提高模型的整体安全性。

**技术框架**：SaFeR-VLM框架包含四个主要组成部分：1) QI-Safe-10K数据集，用于训练和评估模型的安全性；2) 安全感知rollout，允许模型在生成不安全内容后进行反思和纠正，而不是直接丢弃；3) 结构化奖励建模，使用多维加权标准，并对幻觉和矛盾进行显式惩罚；4) GRPO优化，强化安全和纠正后的轨迹，鼓励模型生成安全的内容。

**关键创新**：SaFeR-VLM的关键创新在于将安全性从被动的防御转变为主动的驱动力。通过安全感知rollout和结构化奖励建模，模型能够在推理过程中学习安全策略，从而提高模型的整体安全性。此外，GRPO优化进一步强化了模型的安全行为。

**关键设计**：QI-Safe-10K数据集包含安全关键和推理敏感的案例，用于训练模型的安全意识。安全感知rollout允许模型在生成不安全内容后进行反思和纠正，而不是直接丢弃。结构化奖励建模使用多维加权标准，并对幻觉和矛盾进行显式惩罚，以提高模型的准确性和可靠性。GRPO优化使用Proximal Policy Optimization (PPO) 的变体，强化安全和纠正后的轨迹。

## 📊 实验亮点

SaFeR-VLM-3B在安全性和helpfulness上超越了同等规模和大于10倍规模的模型，如Skywork-R1V3-38B、Qwen2.5VL-72B和GLM4.5V-106B。SaFeR-VLM-7B在安全指标上分别超过GPT-5-mini和Gemini-2.5-Flash 6.47和16.76个点，且helpfulness性能没有下降。

## 🎯 应用场景

SaFeR-VLM可应用于各种需要安全保障的多模态应用场景，例如自动驾驶、医疗诊断、金融风控等。通过提高模型在复杂推理过程中的安全性，可以降低潜在风险，提升用户信任度，并促进多模态人工智能技术的广泛应用。

## 📄 摘要（原文）

> Multimodal Large Reasoning Models (MLRMs) demonstrate impressive cross-modal reasoning but often amplify safety risks under adversarial or unsafe prompts, a phenomenon we call the \textit{Reasoning Tax}. Existing defenses mainly act at the output level and do not constrain the reasoning process, leaving models exposed to implicit risks. In this paper, we propose SaFeR-VLM, a safety-aligned reinforcement learning framework that embeds safety directly into multimodal reasoning. The framework integrates four components: (I) QI-Safe-10K, a curated dataset emphasizing safety-critical and reasoning-sensitive cases; (II) safety-aware rollout, where unsafe generations undergo reflection and correction instead of being discarded; (III) structured reward modeling with multi-dimensional weighted criteria and explicit penalties for hallucinations and contradictions; and (IV) GRPO optimization, which reinforces both safe and corrected trajectories. This unified design shifts safety from a passive safeguard to an active driver of reasoning, enabling scalable and generalizable safety-aware reasoning. SaFeR-VLM further demonstrates robustness against both explicit and implicit risks, supporting dynamic and interpretable safety decisions beyond surface-level filtering. SaFeR-VLM-3B achieves average performance $70.13$ and $78.97$ on safety and helpfulness across six benchmarks, surpassing both same-scale and $>10\times$ larger models such as Skywork-R1V3-38B, Qwen2.5VL-72B, and GLM4.5V-106B. Remarkably, SaFeR-VLM-7B benefits from its increased scale to surpass GPT-5-mini and Gemini-2.5-Flash by \num{6.47} and \num{16.76} points respectively on safety metrics, achieving this improvement without any degradation in helpfulness performance. Our codes are available at https://github.com/HarveyYi/SaFeR-VLM.

