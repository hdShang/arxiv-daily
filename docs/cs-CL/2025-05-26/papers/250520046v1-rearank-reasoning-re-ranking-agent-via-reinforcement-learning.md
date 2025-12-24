---
layout: default
title: "REARANK: Reasoning Re-ranking Agent via Reinforcement Learning"
---

# REARANK: Reasoning Re-ranking Agent via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20046" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20046v1</a>
  <a href="https://arxiv.org/pdf/2505.20046.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20046v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20046v1', 'REARANK: Reasoning Re-ranking Agent via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Zhang, Bo Wang, Xipeng Qiu, Siva Reddy, Aishwarya Agrawal

**分类**: cs.IR, cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出REARANK以提升信息检索中的重排序性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息检索` `重排序` `推理机制` `强化学习` `数据增强` `大型语言模型` `可解释性`

## 📋 核心要点

1. 现有的信息检索方法在重排序过程中缺乏有效的推理机制，导致性能不足和可解释性差。
2. REARANK通过引入显式推理步骤，在重排序之前进行逻辑推理，从而提升了模型的性能和可解释性。
3. 实验结果表明，REARANK在多个基准测试中显著超越了基线模型，尤其是在推理密集型任务上表现优异。

## 📝 摘要（中文）

我们提出了REARANK，这是一种基于大型语言模型（LLM）的列表推理重排序代理。REARANK在重排序之前进行显式推理，显著提高了性能和可解释性。通过强化学习和数据增强，REARANK在流行的信息检索基准上取得了显著的改进，且仅需179个标注样本。基于Qwen2.5-7B构建的REARANK-7B在领域内和领域外的基准测试中表现与GPT-4相当，甚至在推理密集的BRIGHT基准上超越了GPT-4。这些结果强调了我们方法的有效性，并展示了强化学习如何增强LLM在重排序中的推理能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决信息检索中重排序的性能不足和可解释性差的问题。现有方法往往缺乏有效的推理机制，导致结果不理想。

**核心思路**：REARANK的核心思路是通过引入显式推理步骤，在重排序之前进行逻辑推理，从而提升模型的性能和可解释性。通过强化学习和数据增强，REARANK能够在较少的标注样本下实现显著的性能提升。

**技术框架**：REARANK的整体架构包括数据预处理、推理模块和重排序模块。首先，模型对输入数据进行预处理，然后通过推理模块进行逻辑推理，最后在重排序模块中生成最终的排序结果。

**关键创新**：REARANK的主要创新在于其显式推理机制和强化学习的结合，这与传统的重排序方法形成了鲜明对比。通过这种设计，REARANK不仅提高了性能，还增强了模型的可解释性。

**关键设计**：在关键设计方面，REARANK采用了Qwen2.5-7B作为基础模型，并通过强化学习优化了推理过程。此外，模型仅需179个标注样本即可实现良好的性能，这在信息检索领域是一个重要的进展。

## 📊 实验亮点

实验结果显示，REARANK在多个信息检索基准上显著超越了基线模型，尤其在推理密集型的BRIGHT基准上表现优于GPT-4。REARANK-7B在领域内和领域外的基准测试中表现与GPT-4相当，证明了其有效性和创新性。

## 🎯 应用场景

REARANK的研究成果在信息检索、推荐系统和自然语言处理等领域具有广泛的应用潜力。通过提升重排序的性能和可解释性，该方法能够帮助用户更好地理解和利用检索结果，进而提高信息获取的效率和准确性。未来，REARANK可能在智能助手和搜索引擎等实际应用中发挥重要作用。

## 📄 摘要（原文）

> We present REARANK, a large language model (LLM)-based listwise reasoning reranking agent. REARANK explicitly reasons before reranking, significantly improving both performance and interpretability. Leveraging reinforcement learning and data augmentation, REARANK achieves substantial improvements over baseline models across popular information retrieval benchmarks, notably requiring only 179 annotated samples. Built on top of Qwen2.5-7B, our REARANK-7B demonstrates performance comparable to GPT-4 on both in-domain and out-of-domain benchmarks and even surpasses GPT-4 on reasoning-intensive BRIGHT benchmarks. These results underscore the effectiveness of our approach and highlight how reinforcement learning can enhance LLM reasoning capabilities in reranking.

