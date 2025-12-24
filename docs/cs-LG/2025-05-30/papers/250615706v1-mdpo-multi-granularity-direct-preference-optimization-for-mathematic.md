---
layout: default
title: "MDPO: Multi-Granularity Direct Preference Optimization for Mathematical Reasoning"
---

# MDPO: Multi-Granularity Direct Preference Optimization for Mathematical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15706" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15706v1</a>
  <a href="https://arxiv.org/pdf/2506.15706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15706v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15706v1', 'MDPO: Multi-Granularity Direct Preference Optimization for Mathematical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunze Lin

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出MDPO以解决长链数学推理中的错误输出问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `大型语言模型` `直接偏好优化` `多粒度优化` `机器学习` `推理能力提升` `模型训练`

## 📋 核心要点

1. 现有的直接偏好优化方法在长链数学推理中效果有限，难以有效捕捉偏好数据中的接受与拒绝答案之间的差异。
2. 本文提出的MDPO方法从解决方案、推理和步骤三个粒度优化LLMs的数学推理，统一训练目标以对齐生成指标。
3. 在GSM8K和MATH数据集上，MDPO方法分别提升了1.7%和2.3%的性能，超越了DPO及其变体方法。

## 📝 摘要（中文）

数学推理对大型语言模型（LLMs）提出了重大挑战，因为它要求确保每个推理步骤的正确性。尽管研究者通过监督微调增强了LLMs的数学推理能力，但由于无法抑制错误输出，容易产生幻觉。最近，直接偏好优化（DPO）被广泛采用以对齐人类意图，但在长链数学推理中效果有限。为此，本文提出了多粒度直接偏好优化（MDPO）方法，从解决方案、推理和步骤三个粒度优化LLMs的数学推理能力，并通过实验验证了其有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长链数学推理中生成错误输出的问题。现有的直接偏好优化方法在处理长链数据时，无法有效捕捉偏好数据中接受与拒绝答案的差异，导致推理效果不佳。

**核心思路**：MDPO方法通过从三个粒度（解决方案、推理、步骤）进行优化，提升LLMs的数学推理能力。每个粒度关注不同的推理层面，从而增强模型的整体推理能力。

**技术框架**：MDPO的整体架构包括三个主要模块：Solution2Solution（关注整个长链推理的正确性）、Inference2Inference（专注于步骤间的逻辑推理）和Step2Step（纠正步骤中的计算错误）。这三个模块的训练目标统一，以对齐生成指标。

**关键创新**：MDPO的创新在于其多粒度优化策略，能够在不同层面上提升模型的推理能力。这一方法与传统的DPO方法相比，能够更全面地捕捉推理过程中的细微差异，从而有效抑制错误输出。

**关键设计**：在MDPO中，训练过程中采用了统一的损失函数设计，以确保不同粒度的优化目标能够协同工作。此外，模型的参数设置经过精心调整，以适应不同粒度的推理需求，提升计算能力。

## 📊 实验亮点

实验结果显示，MDPO方法在GSM8K数据集上提升了1.7%，在MATH数据集上提升了2.3%。这些结果均超过了传统DPO及其变体方法，表明MDPO在长链数学推理中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学计算和自动化推理等。通过提升大型语言模型在数学推理方面的能力，MDPO可以为教育工具、智能助手和科研计算提供更准确的支持，未来可能在多个领域产生深远影响。

## 📄 摘要（原文）

> Mathematical reasoning presents a significant challenge for Large Language Models (LLMs) as it requires ensuring the correctness of each reasoning step. Researchers have been strengthening the mathematical reasoning abilities of LLMs through supervised fine-tuning, but due to the inability to suppress incorrect outputs, illusions can easily arise. Recently, Direct Preference Optimization (DPO) has been widely adopted for aligning human intent by using preference data to prevent LLMs from generating incorrect outputs. However, it has shown limited benefits in long-chain mathematical reasoning, mainly because DPO struggles to effectively capture the differences between accepted and rejected answers from preferences in long-chain data. The inconsistency between DPO training and LLMs' generation metrics also affects the effectiveness of suppressing incorrect outputs. We propose the Multi-Granularity Direct Preference Optimization (MDPO) method, optimizing the mathematical reasoning of LLMs at three granularities: Solution2Solution, Inference2Inference, and Step2Step. Solution2Solution focuses on the correctness of entire long-chain reasoning; Inference2Inference concentrates on logical reasoning between steps; Step2Step corrects computational errors in steps, enhancing the computational capabilities of LLMs. Additionally, we unify the training objectives of the three granularities to align with the generation metrics. We conducted experiments on the open-source models Qwen2 and Llama3, achieving improvements of 1.7% and 0.9% on the GSM8K dataset, and 2.3% and 1.2% on the MATH dataset, outperforming DPO and other DPO variant methods. Furthermore, we also provide a pipeline for constructing MDPO training data that is simple and does not require manual annotation costs.

