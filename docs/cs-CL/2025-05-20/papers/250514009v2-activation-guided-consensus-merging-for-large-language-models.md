---
layout: default
title: Activation-Guided Consensus Merging for Large Language Models
---

# Activation-Guided Consensus Merging for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14009" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14009v2</a>
  <a href="https://arxiv.org/pdf/2505.14009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14009v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14009v2', 'Activation-Guided Consensus Merging for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Yao, Shuqi Liu, Zehua Liu, Qintong Li, Mingyang Liu, Xiongwei Han, Zhijiang Guo, Han Wu, Linqi Song

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-11-14)

---

## 💡 一句话要点

**提出激活引导共识合并以提升大语言模型的效率与稳定性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `模型合并` `激活引导` `互信息` `推理能力` `效率提升` `自然语言处理`

## 📋 核心要点

1. 现有的训练和提示方法在效率和稳定性方面存在显著挑战，无法有效整合不同大语言模型的能力。
2. 本文提出的激活引导共识合并（ACM）框架，通过激活之间的互信息来确定层特定的合并系数，避免了传统方法的局限。
3. 实验结果显示，ACM在Qwen-7B模型中实现了55.3%的响应长度减少，同时推理准确性提高了1.3个百分点，表现优于所有基线方法。

## 📝 摘要（中文）

近年来，研究者越来越关注将系统2的推理能力与系统1的效率相结合。现有的基于训练和提示的方法在效率和稳定性方面面临重大挑战，而模型合并作为一种有前景的策略，可以将不同大语言模型的多样化能力整合为一个统一的模型。然而，传统的模型合并方法往往假设各层的重要性均匀，忽视了神经元组件固有的功能异质性。为了解决这一局限性，本文提出了激活引导共识合并（ACM），这是一种即插即用的合并框架，通过预训练和微调模型激活之间的互信息来确定层特定的合并系数。ACM有效地保留了任务特定的能力，而无需梯度计算或额外训练。大量实验表明，ACM在长短合并任务中始终优于所有基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有模型合并方法在层重要性假设上的不足，尤其是忽视了神经网络各层功能的异质性，导致合并效果不佳。

**核心思路**：提出激活引导共识合并（ACM）框架，通过分析预训练与微调模型激活之间的互信息，动态确定每层的合并系数，从而更有效地整合模型能力。

**技术框架**：ACM框架包括数据预处理、激活提取、互信息计算和层特定合并系数生成等主要模块，形成一个完整的合并流程。

**关键创新**：ACM的核心创新在于其层特定的合并系数计算方法，突破了传统方法的均匀假设，能够更好地保留任务特定能力。

**关键设计**：在设计中，ACM不需要额外的梯度计算或训练，利用互信息作为合并系数的依据，确保了合并过程的高效性和稳定性。具体参数设置和损失函数设计在实验中进行了详细验证。

## 📊 实验亮点

实验结果表明，采用ACM的TIES-Merging在Qwen-7B模型中实现了55.3%的响应长度减少，同时推理准确性提高了1.3个百分点，显著优于所有基线方法，展示了ACM的有效性和优势。

## 🎯 应用场景

该研究的潜在应用场景包括自然语言处理、对话系统和文本生成等领域，能够有效提升大语言模型的性能和响应效率。未来，ACM框架有望在多模态学习和跨领域模型合并中发挥更大作用，推动智能系统的发展。

## 📄 摘要（原文）

> Recent research has increasingly focused on reconciling the reasoning capabilities of System 2 with the efficiency of System 1. While existing training-based and prompt-based approaches face significant challenges in terms of efficiency and stability, model merging emerges as a promising strategy to integrate the diverse capabilities of different Large Language Models (LLMs) into a unified model. However, conventional model merging methods often assume uniform importance across layers, overlooking the functional heterogeneity inherent in neural components. To address this limitation, we propose \textbf{A}ctivation-Guided \textbf{C}onsensus \textbf{M}erging (\textbf{ACM}), a plug-and-play merging framework that determines layer-specific merging coefficients based on mutual information between activations of pre-trained and fine-tuned models. ACM effectively preserves task-specific capabilities without requiring gradient computations or additional training. Extensive experiments on Long-to-Short (L2S) and general merging tasks demonstrate that ACM consistently outperforms all baseline methods. For instance, in the case of Qwen-7B models, TIES-Merging equipped with ACM achieves a \textbf{55.3\%} reduction in response length while simultaneously improving reasoning accuracy by \textbf{1.3} points.

