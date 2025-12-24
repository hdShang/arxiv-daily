---
layout: default
title: "Less Data, More Security: Advancing Cybersecurity LLMs Specialization via Resource-Efficient Domain-Adaptive Continuous Pre-training with Minimal Tokens"
---

# Less Data, More Security: Advancing Cybersecurity LLMs Specialization via Resource-Efficient Domain-Adaptive Continuous Pre-training with Minimal Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02964" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02964v1</a>
  <a href="https://arxiv.org/pdf/2507.02964.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02964v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02964v1', 'Less Data, More Security: Advancing Cybersecurity LLMs Specialization via Resource-Efficient Domain-Adaptive Continuous Pre-training with Minimal Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Salahuddin Salahuddin, Ahmed Hussain, Jussi Löppönen, Toni Jutila, Panos Papadimitratos

**分类**: cs.CL, cs.AI, cs.CR, cs.LG

**发布日期**: 2025-06-30

**备注**: 15 Pages and 10 Figures

---

## 💡 一句话要点

**通过资源高效的领域自适应预训练提升网络安全LLM专业化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络安全` `大型语言模型` `领域自适应` `连续预训练` `模型微调` `数据效率` `性能提升`

## 📋 核心要点

1. 现有的通用大型语言模型在网络安全分析中缺乏专业知识，导致效果不佳。
2. 本文提出领域自适应连续预训练（DAP）方法，通过调整预训练模型以增强网络安全理解，同时保持语言能力。
3. 实验结果显示，Llama-3.3-70B-Ins-DAP模型在多个基准测试中表现优异，准确率显著高于其他专业模型。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在自然语言处理方面表现出色，但通用模型在网络安全分析中缺乏专业领域知识。本文探讨了领域自适应连续预训练（DAP）作为增强预训练LLM网络安全理解的方法，同时保持通用语言能力。我们系统地调整了三种解码器架构，使用了来自标准、学术文献等多种来源的1.26亿字网络安全语料库。通过约束训练参数和分布式FSDP训练，我们在领域专业化与知识保留之间取得了平衡。评估结果表明，Llama-3.3-70B-Ins-DAP模型在CTI-MCQ、CyberMetric和SecEval三个网络安全基准上均实现了显著提升，分别达到了0.718、0.933和0.864的准确率，超越了包括Llama-Primus-Base在内的专业模型。值得注意的是，使用显著更小的数据集（1.188亿对比2.77亿tokens）实现了竞争性表现，证明了高效领域专业化的可行性。

## 🔬 方法详解

**问题定义**：本文旨在解决通用大型语言模型在网络安全领域缺乏专业知识的问题。现有方法通常依赖于庞大的数据集，导致资源浪费和训练效率低下。

**核心思路**：论文提出领域自适应连续预训练（DAP）作为解决方案，通过使用针对性的网络安全语料库进行微调，增强模型在特定领域的理解能力，同时保持其通用语言处理能力。

**技术框架**：整体架构包括三个主要阶段：首先是数据准备，构建126百万字的网络安全语料库；其次是模型微调，采用约束训练参数和分布式FSDP训练；最后是模型评估，通过CTI-MCQ、CyberMetric和SecEval等基准测试验证模型性能。

**关键创新**：最重要的技术创新在于通过领域自适应预训练实现了在较小数据集上的有效专业化，挑战了对大型数据集的传统依赖。

**关键设计**：在训练过程中，采用了分布式FSDP训练策略，并对训练参数进行了严格约束，以确保在保持知识的同时实现领域专业化。

## 📊 实验亮点

实验结果显示，Llama-3.3-70B-Ins-DAP模型在CTI-MCQ、CyberMetric和SecEval基准测试中分别达到了0.718、0.933和0.864的准确率，超越了包括Llama-Primus-Base在内的多个专业模型，且使用的数据集显著小于传统方法，显示出高效的领域专业化能力。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全威胁分析、漏洞评估和安全文档编写。通过提升LLM在网络安全领域的专业能力，可以为安全专家提供更有效的辅助工具，增强整体网络安全防护能力。

## 📄 摘要（原文）

> While Large Language Models (LLMs) demonstrate exceptional natural language capabilities, general-purpose models lack specialized domain knowledge for effective cybersecurity analysis. In this work, we investigate Domain-Adaptive Continuous Pretraining (DAP) as a methodology for enhancing cybersecurity understanding in pretrained LLMs while preserving general language capabilities. We systematically adapted three decoder-based architectures -- Llama-3.1-8B, DeepSeek-R1-Distill-Qwen-14B, and Llama-3.3-70B-Instruct -- using a curated 126-million-word cybersecurity corpus from standards, academic literature, and various other sources. Our approach employed constrained training parameters and distributed FSDP training to balance domain specialization with knowledge preservation. Evaluation across three cybersecurity benchmarks, namely, CTI-MCQ, CyberMetric, and SecEval, demonstrates consistent improvements post-adaptation. The Llama-3.3-70B-Ins-DAP model achieved state-of-the-art accuracies of 0.718, 0.933, and 0.864, respectively, outperforming specialized models, including Llama-Primus-Base. Notably, competitive performance was achieved using substantially smaller datasets (118.8 million versus 2.77 billion tokens), demonstrating efficient domain specialization viability. We establish that targeted continuous pretraining enables effective cybersecurity domain adaptation with computational feasibility, providing foundations for specialized AI assistants in threat analysis, vulnerability assessment, and security documentation while challenging prevailing assumptions about data requirements for LLM specialization.

