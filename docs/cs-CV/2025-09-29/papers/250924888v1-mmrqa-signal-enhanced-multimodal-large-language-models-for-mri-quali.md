---
layout: default
title: "MMRQA: Signal-Enhanced Multimodal Large Language Models for MRI Quality Assessment"
---

# MMRQA: Signal-Enhanced Multimodal Large Language Models for MRI Quality Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24888" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24888v1</a>
  <a href="https://arxiv.org/pdf/2509.24888.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24888v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24888v1', 'MMRQA: Signal-Enhanced Multimodal Large Language Models for MRI Quality Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fankai Jia, Daisong Gan, Zhe Zhang, Zhaochi Wen, Chenchen Dan, Dong Liang, Haifeng Wang

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出MMRQA框架，融合信号处理与多模态大语言模型，用于MRI质量评估。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `MRI质量评估` `多模态大语言模型` `信号处理` `MRQy` `LLaVA-OneVision`

## 📋 核心要点

1. 传统MRI质量评估方法在定量分析和语义理解之间存在权衡，难以兼顾准确性和可解释性。
2. MMRQA框架融合信号处理与多模态大语言模型，提取定量指标并进行语义推理，实现更全面的质量评估。
3. 实验表明，MMRQA在多个MRI数据集上取得了SOTA性能，并具有良好的零样本泛化能力。

## 📝 摘要（中文）

磁共振成像(MRI)质量评估对于临床决策至关重要，但由于数据稀缺和协议多变而充满挑战。传统方法面临根本性的权衡：基于信号的方法（如MRIQC）提供定量指标，但缺乏语义理解；深度学习方法实现高精度，但牺牲了可解释性。为了解决这些局限性，我们引入了多模态MRI质量评估(MMRQA)框架，率先将多模态大语言模型(MLLM)与采集感知的信号处理相结合。MMRQA结合了三个关键创新：通过MRQy增强的模拟伪影进行稳健的指标提取，使用Qwen将指标结构化转换为问答对，以及通过LLaVA-OneVision的低秩适应(LoRA)进行参数高效的融合。在MR-ART、FastMRI和MyConnectome基准上的评估表明，MMRQA实现了最先进的性能，并具有强大的零样本泛化能力，并通过全面的消融研究得到了验证。通过桥接定量分析与语义推理，我们的框架生成了临床可解释的输出，从而增强了动态医疗环境中的质量控制。

## 🔬 方法详解

**问题定义**：MRI质量评估对于临床诊断至关重要，但现有方法存在局限性。基于信号的方法（如MRIQC）虽然能提供定量指标，但缺乏对图像语义的理解。深度学习方法虽然精度高，但可解释性差，难以应用于临床实践。因此，需要一种既能准确评估MRI质量，又能提供可解释结果的方法。

**核心思路**：MMRQA的核心思路是将MRI图像的定量信号特征与多模态大语言模型的语义理解能力相结合。通过信号处理提取MRI图像的定量指标，然后利用大语言模型对这些指标进行语义推理，最终生成可解释的质量评估报告。这种方法既能保证评估的准确性，又能提供临床医生易于理解的解释。

**技术框架**：MMRQA框架主要包含三个模块：1) 基于MRQy的指标提取模块，用于提取MRI图像的定量指标，并使用模拟伪影进行增强；2) 基于Qwen的问答对生成模块，用于将提取的指标结构化为问答对，以便输入到大语言模型中；3) 基于LLaVA-OneVision和LoRA的参数高效融合模块，用于将图像信息和问答对信息融合，并利用LoRA进行参数高效的微调。

**关键创新**：MMRQA的关键创新在于将信号处理与多模态大语言模型相结合，实现了MRI质量评估的定量分析和语义推理。此外，使用Qwen将指标结构化为问答对，以及使用LoRA进行参数高效的微调，也是重要的技术创新。

**关键设计**：在指标提取模块中，使用了MRQy工具包，并结合模拟伪影进行数据增强，提高了指标提取的鲁棒性。在问答对生成模块中，使用了Qwen大语言模型，并设计了特定的prompt模板，以保证生成的问答对的质量。在参数高效融合模块中，使用了LLaVA-OneVision模型，并利用LoRA技术对模型进行微调，降低了计算成本。

## 📊 实验亮点

MMRQA在MR-ART、FastMRI和MyConnectome等多个MRI数据集上取得了SOTA性能，尤其在零样本泛化能力方面表现出色。消融实验表明，各个模块都对性能提升有贡献，验证了框架的有效性。相较于传统方法，MMRQA能够提供更准确、更可解释的MRI质量评估结果。

## 🎯 应用场景

MMRQA可应用于临床MRI质量控制流程，辅助医生快速准确地评估MRI图像质量，减少因图像质量问题导致的误诊和漏诊。此外，该框架还可用于MRI设备性能监控和优化，以及MRI图像数据清洗和预处理等领域，具有广阔的应用前景。

## 📄 摘要（原文）

> Magnetic resonance imaging (MRI) quality assessment is crucial for clinical decision-making, yet remains challenging due to data scarcity and protocol variability. Traditional approaches face fundamental trade-offs: signal-based methods like MRIQC provide quantitative metrics but lack semantic understanding, while deep learning approaches achieve high accuracy but sacrifice interpretability. To address these limitations, we introduce the Multimodal MRI Quality Assessment (MMRQA) framework, pioneering the integration of multimodal large language models (MLLMs) with acquisition-aware signal processing. MMRQA combines three key innovations: robust metric extraction via MRQy augmented with simulated artifacts, structured transformation of metrics into question-answer pairs using Qwen, and parameter-efficient fusion through Low-Rank Adaptation (LoRA) of LLaVA-OneVision. Evaluated on MR-ART, FastMRI, and MyConnectome benchmarks, MMRQA achieves state-of-the-art performance with strong zero-shot generalization, as validated by comprehensive ablation studies. By bridging quantitative analysis with semantic reasoning, our framework generates clinically interpretable outputs that enhance quality control in dynamic medical settings.

