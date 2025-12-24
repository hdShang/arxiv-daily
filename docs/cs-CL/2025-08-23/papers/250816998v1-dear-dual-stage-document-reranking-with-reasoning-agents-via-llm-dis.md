---
layout: default
title: "DeAR: Dual-Stage Document Reranking with Reasoning Agents via LLM Distillation"
---

# DeAR: Dual-Stage Document Reranking with Reasoning Agents via LLM Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16998" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16998v1</a>
  <a href="https://arxiv.org/pdf/2508.16998.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16998v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16998v1', 'DeAR: Dual-Stage Document Reranking with Reasoning Agents via LLM Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdelrahman Abdallah, Jamshid Mozafari, Bhawna Piryani, Adam Jatowt

**分类**: cs.CL, cs.IR

**发布日期**: 2025-08-23

**备注**: Accept at EMNLP Findings 2025

**🔗 代码/项目**: [GITHUB](https://github.com/DataScienceUIBK/DeAR-Reranking)

---

## 💡 一句话要点

**提出DeAR以解决文档重排序中的推理与评分平衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档重排序` `推理模型` `知识蒸馏` `自然语言处理` `信息检索`

## 📋 核心要点

1. 现有文档重排序方法在细粒度相关性评分与整体分析之间难以取得平衡，影响了重排序的准确性。
2. 本文提出的DeAR框架通过双阶段方法，分别处理令牌级相关性和列表推理，提升了模型的准确性和可解释性。
3. 在多个数据集上，DeAR在nDCG@5和nDCG@10等指标上超越了现有的开源基线，展现出优越的性能。

## 📝 摘要（中文）

大型语言模型（LLMs）通过对候选集进行全局推理，改变了列表文档重排序的方式。然而，单一模型往往难以在细粒度相关性评分和整体跨文档分析之间取得平衡。为此，本文提出了DeAR（深度代理排名），一个开源框架，采用双阶段方法解耦这两项任务，从而实现更高的准确性和可解释性。在第一阶段，我们从一个冻结的13B LLaMA教师模型中提炼出令牌级相关性信号，生成一个紧凑的3B或8B学生模型，确保稳健的逐点评分。在第二阶段，我们附加了第二个LoRA适配器，并在20K个GPT-4o生成的思维链排列上进行微调，使得能够进行带自然语言解释的列表推理。经过在多个数据集上的评估，DeAR在准确性上超越了开源基线。

## 🔬 方法详解

**问题定义**：本文旨在解决文档重排序中，现有方法在细粒度相关性评分与整体跨文档分析之间的平衡问题。单一模型往往无法同时兼顾这两方面，导致重排序效果不佳。

**核心思路**：DeAR框架采用双阶段方法，第一阶段提取令牌级相关性信号，第二阶段进行列表推理。通过这种设计，模型能够在保持高准确性的同时，提供可解释的推理过程。

**技术框架**：DeAR的整体架构分为两个主要阶段：第一阶段使用一个冻结的13B LLaMA教师模型进行知识蒸馏，生成一个紧凑的学生模型；第二阶段则在此基础上，附加LoRA适配器，并在生成的思维链上进行微调。

**关键创新**：DeAR的创新之处在于其双阶段的设计，使得模型能够分别优化细粒度评分和整体推理，显著提升了重排序的准确性和可解释性。

**关键设计**：在第一阶段，采用交叉熵、RankNet和KL散度损失的混合损失函数进行蒸馏；在第二阶段，使用20K个GPT-4o生成的思维链进行微调，确保模型能够进行有效的列表推理。

## 📊 实验亮点

在TREC-DL19/20和NovelEval-2306等多个数据集上，DeAR在nDCG@5上超越开源基线5.1个百分点，并在NovelEval上达到90.97的nDCG@10，超越GPT-4 3.09个百分点。此外，DeAR在开放域问答中表现出色，Natural Questions的Top-1准确率达到54.29，优于MonoT5、UPR和RankGPT等基线。

## 🎯 应用场景

DeAR框架在文档重排序领域具有广泛的应用潜力，尤其是在信息检索、问答系统和推荐系统等场景中。其高准确性和可解释性使得用户能够更好地理解模型的决策过程，提升用户体验。未来，DeAR还可以扩展到其他需要复杂推理的任务中，推动相关领域的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have transformed listwise document reranking by enabling global reasoning over candidate sets, yet single models often struggle to balance fine-grained relevance scoring with holistic cross-document analysis. We propose \textbf{De}ep\textbf{A}gent\textbf{R}ank (\textbf{\DeAR}), an open-source framework that decouples these tasks through a dual-stage approach, achieving superior accuracy and interpretability. In \emph{Stage 1}, we distill token-level relevance signals from a frozen 13B LLaMA teacher into a compact \{3, 8\}B student model using a hybrid of cross-entropy, RankNet, and KL divergence losses, ensuring robust pointwise scoring. In \emph{Stage 2}, we attach a second LoRA adapter and fine-tune on 20K GPT-4o-generated chain-of-thought permutations, enabling listwise reasoning with natural-language justifications. Evaluated on TREC-DL19/20, eight BEIR datasets, and NovelEval-2306, \DeAR surpasses open-source baselines by +5.1 nDCG@5 on DL20 and achieves 90.97 nDCG@10 on NovelEval, outperforming GPT-4 by +3.09. Without fine-tuning on Wikipedia, DeAR also excels in open-domain QA, achieving 54.29 Top-1 accuracy on Natural Questions, surpassing baselines like MonoT5, UPR, and RankGPT. Ablations confirm that dual-loss distillation ensures stable calibration, making \DeAR a highly effective and interpretable solution for modern reranking systems.\footnote{Dataset and code available at https://github.com/DataScienceUIBK/DeAR-Reranking.}.

