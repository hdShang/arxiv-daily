---
layout: default
title: "Dual-Head Reasoning Distillation: Improving Classifier Accuracy with Train-Time-Only Reasoning"
---

# Dual-Head Reasoning Distillation: Improving Classifier Accuracy with Train-Time-Only Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21487" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21487v2</a>
  <a href="https://arxiv.org/pdf/2509.21487.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21487v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21487v2', 'Dual-Head Reasoning Distillation: Improving Classifier Accuracy with Train-Time-Only Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jillian Xu, Dylan Zhou, Vinay Shukla, Yang Yang, Junrui Ruan, Shuhuai Lin, Wenfei Zou, Yinxiao Liu, Karthik Lakshmanan

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-25 (更新: 2025-09-29)

**备注**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Efficient Reasoning Workshop

---

## 💡 一句话要点

**提出双头推理蒸馏(DHRD)，在不牺牲推理速度的前提下提升分类器精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `双头推理蒸馏` `Chain-of-Thought` `知识蒸馏` `语言模型` `分类任务`

## 📋 核心要点

1. Chain-of-Thought (CoT) prompting虽然能提高分类精度，但推理过程的生成显著降低了吞吐量。
2. DHRD方法通过引入仅在训练时使用的推理头，并利用教师模型的推理过程进行监督学习，从而提升模型性能。
3. 实验表明，DHRD在SuperGLUE任务上取得了显著的性能提升，同时保持了较高的推理速度。

## 📝 摘要（中文）

本文提出了一种名为双头推理蒸馏(DHRD)的简单训练方法，用于decoder-only语言模型。该方法添加了两个头部：(i)一个在训练和推理期间使用的池化分类头，以及(ii)一个仅在训练期间使用、由教师模型生成的推理过程监督的推理头。训练时，使用标签交叉熵和输入加推理过程序列上的token级语言模型损失的加权和作为损失函数。在七个SuperGLUE任务上，DHRD相对于池化基线产生了0.65-5.47%的相对增益，在蕴含/因果任务上的增益尤为显著。由于在测试时禁用了推理头，因此推理吞吐量与池化分类器相匹配，并且在相同的backbone上，QPS比CoT解码高96-142倍。

## 🔬 方法详解

**问题定义**：论文旨在解决Chain-of-Thought (CoT) prompting在提升分类精度时带来的推理速度下降问题。现有方法，如直接使用CoT进行推理，虽然精度高，但由于需要生成推理过程，导致吞吐量显著降低。而简单的池化分类器虽然速度快，但精度不如CoT。

**核心思路**：论文的核心思路是利用蒸馏学习，在训练阶段引入一个推理头，并使用教师模型的推理过程作为监督信号，从而让学生模型学习到CoT的推理能力。在推理阶段，只使用池化分类头，从而保证推理速度。

**技术框架**：DHRD方法的核心是训练一个带有两个head的decoder-only语言模型。一个head是池化分类头，用于最终的分类任务；另一个head是推理头，仅在训练阶段使用，用于学习教师模型的推理过程。训练过程包括两个损失函数：一个是标准的标签交叉熵损失，用于监督分类头的学习；另一个是token级别的语言模型损失，用于监督推理头的学习，使其能够模仿教师模型的推理过程。

**关键创新**：DHRD的关键创新在于将推理过程的学习与最终的分类任务解耦。通过在训练阶段引入推理头，模型可以学习到CoT的推理能力，而在推理阶段只使用池化分类头，从而避免了推理过程的生成，保证了推理速度。这种train-time-only reasoning的方式，在不牺牲推理速度的前提下，提升了分类精度。

**关键设计**：DHRD的关键设计包括：(1) 使用两个head，一个用于分类，一个用于推理；(2) 使用教师模型的推理过程作为监督信号；(3) 使用标签交叉熵和token级别语言模型损失的加权和作为损失函数；(4) 在推理阶段禁用推理头，只使用池化分类头。损失函数的权重需要根据具体任务进行调整，以平衡分类精度和推理能力。

## 📊 实验亮点

DHRD在七个SuperGLUE任务上取得了显著的性能提升，相对于池化基线，相对增益达到了0.65-5.47%。尤其在蕴含/因果任务上，增益更为显著。更重要的是，DHRD在保持高精度的同时，推理速度与池化分类器相当，并且在相同的backbone上，QPS比CoT解码高96-142倍，显著提升了推理效率。

## 🎯 应用场景

DHRD方法可以应用于各种需要高精度和高效率的分类任务，例如自然语言理解、文本分类、情感分析等。该方法尤其适用于资源受限的场景，例如移动设备或边缘计算环境，在这些场景下，推理速度至关重要。此外，DHRD还可以作为一种通用的模型训练方法，用于提升各种decoder-only语言模型的性能。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) prompting often improves classification accuracy, but it introduces a significant throughput penalty with rationale generation (Wei et al., 2022; Cheng and Van Durme, 2024). To resolve this trade-off, we introduce Dual-Head Reasoning Distillation (DHRD), a simple training method for decoder-only language models (LMs) that adds (i) a pooled classification head used during training and inference and (ii) a reasoning head supervised by teacher rationales used only in training. We train with a loss function that is a weighted sum of label cross-entropy and token-level LM loss over input-plus-rationale sequences. On seven SuperGLUE tasks, DHRD yields relative gains of 0.65-5.47% over pooled baselines, with notably larger gains on entailment/causal tasks. Since we disable the reasoning head at test time, inference throughput matches pooled classifiers and exceeds CoT decoding on the same backbones by 96-142 times in QPS.

