---
layout: default
title: "Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization"
---

# Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13993" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13993v1</a>
  <a href="https://arxiv.org/pdf/2508.13993.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13993v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13993v1', 'Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaohua Duan, Xinze Li, Zhenghao Liu, Xiaoyuan Yi, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-19

**🔗 代码/项目**: [GITHUB](https://github.com/NEUIR/LongMab-PO)

---

## 💡 一句话要点

**提出LongMab-PO以解决长上下文LLM偏好优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文建模` `多臂赌博机` `偏好优化` `大型语言模型` `数据多样性` `自然语言处理` `推理任务`

## 📋 核心要点

1. 现有方法在长上下文建模中面临生成数据多样性低和事实不一致性的问题，限制了模型的有效性。
2. 本文提出LongMab-PO框架，通过多臂赌博机策略选择信息量最大的上下文片段，优化LLM的响应生成。
3. 实验结果显示，LongMab-PO在长上下文推理基准上显著提升了偏好数据对的多样性和质量，达到了最先进的性能。

## 📝 摘要（中文）

长上下文建模对于长上下文问答、摘要和复杂推理任务至关重要。近期研究通过合成数据微调大型语言模型（LLMs）以增强其长上下文能力，但效果常因生成数据的低多样性和事实不一致性而受限。为解决这些挑战，本文提出了LongMab-PO框架，利用多臂赌博机（MAB）策略从长上下文中识别最具信息量的片段，以采样高质量和多样化的响应，并构建直接偏好优化（DPO）训练的数据对。实验结果表明，LongMab-PO显著提高了偏好数据对的多样性和质量，在长上下文推理基准上达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决长上下文建模中生成数据多样性不足和事实不一致性的问题。现有方法在微调大型语言模型时，往往依赖于合成数据，导致生成的响应质量不高。

**核心思路**：LongMab-PO框架的核心思想是将上下文片段视为多臂赌博机的臂，通过预期奖励分数选择最具信息量的片段进行响应生成，从而提高生成数据的质量和多样性。

**技术框架**：该框架包括两个主要模块：一是多臂赌博机策略，用于选择上下文片段；二是直接偏好优化（DPO），用于进一步优化生成的响应。整个流程是通过迭代更新奖励分数来实现的。

**关键创新**：LongMab-PO的创新在于将上下文片段视为多臂赌博机的臂，并通过奖励反馈机制动态调整选择策略，这一设计使得模型能够更有效地聚焦于相关上下文。

**关键设计**：在参数设置上，奖励分数的计算基于生成响应的质量反馈，损失函数采用DPO方法进行优化，确保生成的响应在多样性和准确性上达到最佳平衡。整体网络结构设计上，结合了上下文选择和响应生成的模块化设计。

## 📊 实验亮点

实验结果表明，LongMab-PO在长上下文推理基准上显著提高了偏好数据对的多样性和质量，具体性能提升幅度达到XX%，超越了当前的最先进基线，展示了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括长上下文问答系统、智能摘要生成和复杂推理任务等。通过优化长上下文的处理能力，LongMab-PO能够提升各类自然语言处理任务的性能，具有广泛的实际价值和深远的影响。未来，随着长上下文模型的不断发展，该方法有望在更多实际应用中得到推广。

## 📄 摘要（原文）

> Long-context modeling is critical for a wide range of real-world tasks, including long-context question answering, summarization, and complex reasoning tasks. Recent studies have explored fine-tuning Large Language Models (LLMs) with synthetic data to enhance their long-context capabilities. However, the effectiveness of such approaches is often limited by the low diversity and factual inconsistencies in the generated data. To address these challenges, we propose LongMab-PO, a novel framework that leverages a Multi-Armed Bandit (MAB) rollout strategy to identify the most informative chunks from the given long context for sampling high-quality and diverse responses and constructing preference data pairs for Direct Preference Optimization (DPO) training. Specifically, we treat context chunks as arms of MAB, select chunks based on their expected reward scores to input into LLMs to generate responses, and iteratively update these scores based on reward feedback. This exploration and exploitation process enables the model to focus on the most relevant context segments, thereby generating and collecting high-quality and diverse responses. Finally, we collect these generated responses from the rollout process and apply the DPO method to further optimize the LLM. Experimental results show that LongMab-PO significantly improves the diversity and quality of preference data pairs, achieving state-of-the-art performance on long-context reasoning benchmarks. All code and data will be released on https://github.com/NEUIR/LongMab-PO.

