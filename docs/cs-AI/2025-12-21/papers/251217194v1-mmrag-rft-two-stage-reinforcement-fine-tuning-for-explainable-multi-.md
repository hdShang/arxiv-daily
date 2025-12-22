---
layout: default
title: MMRAG-RFT: Two-stage Reinforcement Fine-tuning for Explainable Multi-modal Retrieval-augmented Generation
---

# MMRAG-RFT: Two-stage Reinforcement Fine-tuning for Explainable Multi-modal Retrieval-augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17194" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17194v1</a>
  <a href="https://arxiv.org/pdf/2512.17194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17194v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17194v1', 'MMRAG-RFT: Two-stage Reinforcement Fine-tuning for Explainable Multi-modal Retrieval-augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengwei Zhao, Jingwen Yao, Sitong Wei, Linhai Xu, Yuying Liu, Dong Zhang, Zhiqiang Tian, Shaoyi Du

**分类**: cs.AI

**发布日期**: 2025-12-19

**备注**: This paper was accepted to AAAI2026

---

## 💡 一句话要点

**提出MMRAG-RFT，通过两阶段强化学习提升多模态检索增强生成的可解释性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索增强生成` `强化学习` `可解释性` `多模态大语言模型` `两阶段微调`

## 📋 核心要点

1. 现有MMRAG方法缺乏对检索和生成过程的推理逻辑的解释，导致结果可解释性不足。
2. 提出MMRAG-RFT框架，通过两阶段强化学习微调，提升多模态大语言模型在检索和生成过程中的推理能力。
3. 在WebQA和MultimodalQA数据集上取得了SOTA结果，并通过消融实验验证了框架的有效性。

## 📝 摘要（中文）

多模态检索增强生成(MMRAG)通过整合外部多模态知识来实现高度可信的生成，在复杂的多模态场景中表现出令人印象深刻的性能。然而，现有的MMRAG方法未能阐明检索和响应生成背后的推理逻辑，这限制了结果的可解释性。为了解决这个问题，我们提出将强化学习引入多模态检索增强生成，通过两阶段强化微调框架增强多模态大型语言模型的推理能力，从而实现可解释的多模态检索增强生成。具体来说，在第一阶段，采用基于规则的强化微调来执行多模态文档的粗粒度逐点排序，有效地过滤掉那些显著不相关的文档。在第二阶段，利用基于推理的强化微调来联合优化细粒度的列表式排序和答案生成，引导多模态大型语言模型在MMRAG过程中输出可解释的推理逻辑。我们的方法在WebQA和MultimodalQA这两个多模态检索增强生成的基准数据集上取得了最先进的结果，并通过全面的消融实验验证了其有效性。

## 🔬 方法详解

**问题定义**：现有的多模态检索增强生成（MMRAG）方法在生成答案时，缺乏对检索到的多模态文档进行有效排序和推理的能力，导致生成结果缺乏可解释性。用户难以理解模型为何选择特定的文档以及如何利用这些文档生成最终答案。现有方法未能明确地建模检索和生成之间的推理过程，导致模型在复杂场景下的表现受到限制。

**核心思路**：论文的核心思路是通过引入强化学习，显式地建模多模态文档的排序和答案生成过程，从而提升MMRAG的可解释性。具体而言，通过两阶段的强化微调，首先进行粗粒度的文档过滤，然后进行细粒度的排序和答案生成，引导模型学习可解释的推理逻辑。

**技术框架**：MMRAG-RFT框架包含两个主要阶段：1) 基于规则的强化微调（Rule-based Reinforcement Fine-tuning）：对多模态文档进行粗粒度的逐点排序，过滤掉不相关的文档。2) 基于推理的强化微调（Reasoning-based Reinforcement Fine-tuning）：联合优化细粒度的列表式排序和答案生成，引导模型输出可解释的推理逻辑。这两个阶段都利用强化学习来优化模型的行为，使其更符合人类的推理习惯。

**关键创新**：该方法最重要的创新点在于将强化学习引入到MMRAG框架中，并设计了两阶段的强化微调策略。与传统的监督学习方法不同，强化学习能够更好地建模序列决策过程，从而优化检索和生成之间的交互。此外，两阶段的微调策略能够有效地平衡效率和效果，先进行粗粒度过滤，再进行细粒度优化。

**关键设计**：在第一阶段，使用基于规则的奖励函数来指导模型的学习，例如，如果检索到的文档与问题相关，则给予正向奖励，否则给予负向奖励。在第二阶段，使用基于推理的奖励函数，鼓励模型生成包含推理逻辑的答案。具体的奖励函数设计需要根据具体的任务和数据集进行调整。此外，论文还可能涉及一些关于网络结构、损失函数和训练策略的细节，但具体内容未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17194v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17194v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MMRAG-RFT在WebQA和MultimodalQA两个基准数据集上取得了state-of-the-art的结果。具体的性能提升数据未知，但摘要中明确指出通过全面的消融实验验证了其有效性。这表明该方法在提升多模态检索增强生成的可解释性和准确性方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于需要高度可信和可解释性的多模态问答系统、智能客服、教育辅导等领域。通过提供清晰的推理逻辑，可以增强用户对AI系统决策的信任感，并促进人机协作。未来，该方法有望扩展到更复杂的多模态任务中，例如多模态对话生成、多模态内容创作等。

## 📄 摘要（原文）

> Multi-modal Retrieval-Augmented Generation (MMRAG) enables highly credible generation by integrating external multi-modal knowledge, thus demonstrating impressive performance in complex multi-modal scenarios. However, existing MMRAG methods fail to clarify the reasoning logic behind retrieval and response generation, which limits the explainability of the results. To address this gap, we propose to introduce reinforcement learning into multi-modal retrieval-augmented generation, enhancing the reasoning capabilities of multi-modal large language models through a two-stage reinforcement fine-tuning framework to achieve explainable multi-modal retrieval-augmented generation. Specifically, in the first stage, rule-based reinforcement fine-tuning is employed to perform coarse-grained point-wise ranking of multi-modal documents, effectively filtering out those that are significantly irrelevant. In the second stage, reasoning-based reinforcement fine-tuning is utilized to jointly optimize fine-grained list-wise ranking and answer generation, guiding multi-modal large language models to output explainable reasoning logic in the MMRAG process. Our method achieves state-of-the-art results on WebQA and MultimodalQA, two benchmark datasets for multi-modal retrieval-augmented generation, and its effectiveness is validated through comprehensive ablation experiments.

