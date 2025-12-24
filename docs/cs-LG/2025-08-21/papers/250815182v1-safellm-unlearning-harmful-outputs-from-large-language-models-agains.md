---
layout: default
title: "SafeLLM: Unlearning Harmful Outputs from Large Language Models against Jailbreak Attacks"
---

# SafeLLM: Unlearning Harmful Outputs from Large Language Models against Jailbreak Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15182" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15182v1</a>
  <a href="https://arxiv.org/pdf/2508.15182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15182v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15182v1', 'SafeLLM: Unlearning Harmful Outputs from Large Language Models against Jailbreak Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangman Li, Xiaodong Wu, Qi Li, Jianbing Ni, Rongxing Lu

**分类**: cs.LG

**发布日期**: 2025-08-21

---

## 💡 一句话要点

**提出SafeLLM以解决大型语言模型的监狱突破攻击问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `去学习` `安全性` `监狱突破攻击` `内容过滤` `深度学习` `模型优化`

## 📋 核心要点

1. 现有方法在应对监狱突破攻击时，无法有效去除有害知识，导致模型生成不安全内容。
2. SafeLLM通过去学习机制，结合动态检测和优化策略，有效去除有害知识，确保模型安全性。
3. 实验结果显示，SafeLLM在多个监狱突破基准上显著降低攻击成功率，同时保持高性能，优于传统防御方法。

## 📝 摘要（中文）

监狱突破攻击通过设计对抗性提示，绕过大型语言模型（LLMs）的对齐机制，导致模型生成有害、受限或偏见的内容，严重威胁其安全性。本文提出了SafeLLM，一个基于去学习的防御框架，旨在去除LLMs中的有害知识，同时保持语言流畅性和一般能力。SafeLLM采用三阶段流程：动态不安全输出检测、基于前馈网络激活的有害内容追踪，以及约束优化以抑制不安全行为而不降低模型整体质量。通过识别和中和负责有害生成路径的前馈网络子结构，SafeLLM实现了有针对性的不可逆遗忘。大量实验表明，SafeLLM显著降低了攻击成功率，同时保持高通用性能。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何有效去除大型语言模型中的有害知识，以防止监狱突破攻击。现有方法如监督微调和直接偏好优化在安全性和控制精度上存在不足，无法满足实际需求。

**核心思路**：SafeLLM的核心思路是通过去学习机制，动态检测和抑制有害输出，同时保持模型的语言流畅性和一般能力。这种设计旨在实现对有害知识的精准控制和不可逆遗忘。

**技术框架**：SafeLLM的整体架构包括三个主要阶段：第一阶段是动态不安全输出检测，结合外部分类器与模型内部评估；第二阶段是通过前馈网络激活追踪有害内容；第三阶段是约束优化，抑制不安全行为。

**关键创新**：SafeLLM的关键创新在于实现了针对性和不可逆的遗忘，通过识别和中和前馈网络中负责有害生成的子结构，显著提升了模型的安全性和控制能力。

**关键设计**：在设计中，SafeLLM采用了混合检测方法，结合了多种损失函数和网络结构，以确保在去除有害知识的同时，保持模型的整体性能和流畅性。

## 📊 实验亮点

实验结果表明，SafeLLM在多个监狱突破基准上显著降低了攻击成功率，具体表现为相比于标准防御方法，攻击成功率降低了XX%（具体数据未知），同时保持了高通用性能，展示了其在安全性和性能上的优越性。

## 🎯 应用场景

SafeLLM的研究成果具有广泛的应用潜力，尤其在需要确保内容安全的领域，如社交媒体、在线客服和教育等。通过有效去除有害知识，SafeLLM能够提升大型语言模型在实际应用中的安全性和可靠性，促进其在敏感场景中的应用。未来，该方法可能会引领更多去学习技术在AI安全领域的研究与应用。

## 📄 摘要（原文）

> Jailbreak attacks pose a serious threat to the safety of Large Language Models (LLMs) by crafting adversarial prompts that bypass alignment mechanisms, causing the models to produce harmful, restricted, or biased content. In this paper, we propose SafeLLM, a novel unlearning-based defense framework that unlearn the harmful knowledge from LLMs while preserving linguistic fluency and general capabilities. SafeLLM employs a three-stage pipeline: (1) dynamic unsafe output detection using a hybrid approach that integrates external classifiers with model-internal evaluations; (2) token-level harmful content tracing through feedforward network (FFN) activations to localize harmful knowledge; and (3) constrained optimization to suppress unsafe behavior without degrading overall model quality. SafeLLM achieves targeted and irreversible forgetting by identifying and neutralizing FFN substructures responsible for harmful generation pathways. Extensive experiments on prominent LLMs (Vicuna, LLaMA, and GPT-J) across multiple jailbreak benchmarks show that SafeLLM substantially reduces attack success rates while maintaining high general-purpose performance. Compared to standard defense methods such as supervised fine-tuning and direct preference optimization, SafeLLM offers stronger safety guarantees, more precise control over harmful behavior, and greater robustness to unseen attacks. Moreover, SafeLLM maintains the general performance after the harmful knowledge unlearned. These results highlight unlearning as a promising direction for scalable and effective LLM safety.

