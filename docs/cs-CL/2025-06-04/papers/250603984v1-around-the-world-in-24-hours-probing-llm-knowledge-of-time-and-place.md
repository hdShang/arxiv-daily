---
layout: default
title: "Around the World in 24 Hours: Probing LLM Knowledge of Time and Place"
---

# Around the World in 24 Hours: Probing LLM Knowledge of Time and Place

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03984" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03984v1</a>
  <a href="https://arxiv.org/pdf/2506.03984.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03984v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03984v1', 'Around the World in 24 Hours: Probing LLM Knowledge of Time and Place')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Carolin Holtermann, Paul Röttger, Anne Lauscher

**分类**: cs.CL

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出GeoTemp数据集以评估语言模型的时间与空间推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `时间推理` `空间推理` `GeoTemp数据集` `推理能力评估` `提示构造` `模型性能`

## 📋 核心要点

1. 现有研究主要孤立测试语言模型在时间或空间推理方面的能力，缺乏对二者联合推理的深入分析。
2. 本文提出GeoTemp数据集，旨在全面评估语言模型在时间和空间联合推理中的表现，填补该领域的研究空白。
3. 实验结果表明，模型在时间推理任务中表现良好，但在需要结合时间和空间信息的任务中性能受限，提示构造对结果影响显著。

## 📝 摘要（中文）

理解时间和空间对于我们认识世界至关重要。然而，语言模型在这一领域的能力尚未得到充分探索。本文首次评估了语言模型在时间和空间联合推理方面的能力。为此，我们创建了GeoTemp数据集，涵盖289个城市、217个国家和37个时区，共320,000个提示。通过GeoTemp，我们评估了三种不同模型家族的八个开放聊天模型在不同时间和地理知识组合下的表现。结果显示，大多数模型在仅涉及时间知识的推理任务中表现良好，且随着模型规模的增大，整体性能有所提升。然而，在需要连接时间和地理信息的任务中，性能仍然受到限制。我们发现，低模型困惑度的地名表现显著提高，提示的构造对性能影响显著，直接注入地理知识可提升性能，而链式思维提示在简单任务中反而降低了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决语言模型在时间和空间联合推理能力评估的不足，现有方法多为孤立测试，缺乏全面性和实用性。

**核心思路**：通过创建GeoTemp数据集，涵盖丰富的地理和时间信息，评估语言模型在复杂推理任务中的表现，探索模型在不同知识组合下的能力。

**技术框架**：研究首先构建GeoTemp数据集，然后对八个开放聊天模型进行评估，分析其在不同时间和地理知识组合下的推理能力，最后总结模型表现与提示构造的关系。

**关键创新**：GeoTemp数据集的创建是本研究的核心创新，首次系统性地评估语言模型在时间与空间联合推理中的能力，揭示了模型性能与地名困惑度的关系。

**关键设计**：在实验中，采用了不同的提示构造策略，发现直接注入地理知识能提升模型性能，而链式思维提示在简单任务中反而降低了性能，提示设计的细节对结果有显著影响。

## 📊 实验亮点

实验结果显示，大多数模型在仅涉及时间知识的推理任务中表现良好，整体性能随着模型规模的增大而提升。然而，在需要连接时间和地理信息的任务中，模型性能仍受限，提示构造的影响显著，直接注入地理知识可提升性能，而链式思维提示在简单任务中降低了性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动问答系统和地理信息系统等，能够帮助提升这些系统在复杂场景下的推理能力。未来，随着数据集的进一步扩展和模型的优化，可能会推动更广泛的应用，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Reasoning over time and space is essential for understanding our world. However, the abilities of language models in this area are largely unexplored as previous work has tested their abilities for logical reasoning in terms of time and space in isolation or only in simple or artificial environments. In this paper, we present the first evaluation of the ability of language models to jointly reason over time and space. To enable our analysis, we create GeoTemp, a dataset of 320k prompts covering 289 cities in 217 countries and 37 time zones. Using GeoTemp, we evaluate eight open chat models of three different model families for different combinations of temporal and geographic knowledge. We find that most models perform well on reasoning tasks involving only temporal knowledge and that overall performance improves with scale. However, performance remains constrained in tasks that require connecting temporal and geographical information. We do not find clear correlations of performance with specific geographic regions. Instead, we find a significant performance increase for location names with low model perplexity, suggesting their repeated occurrence during model training. We further demonstrate that their performance is heavily influenced by prompt formulation - a direct injection of geographical knowledge leads to performance gains, whereas, surprisingly, techniques like chain-of-thought prompting decrease performance on simpler tasks.

