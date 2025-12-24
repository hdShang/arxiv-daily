---
layout: default
title: Truth or Twist? Optimal Model Selection for Reliable Label Flipping Evaluation in LLM-based Counterfactuals
---

# Truth or Twist? Optimal Model Selection for Reliable Label Flipping Evaluation in LLM-based Counterfactuals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13972" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13972v3</a>
  <a href="https://arxiv.org/pdf/2505.13972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13972v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13972v3', 'Truth or Twist? Optimal Model Selection for Reliable Label Flipping Evaluation in LLM-based Counterfactuals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianli Wang, Van Bach Nguyen, Nils Feldhus, Luis Felipe Villa-Arenas, Christin Seifert, Sebastian Möller, Vera Schmitt

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-08-27)

**备注**: Accepted at INLG 2025, camera-ready version

---

## 💡 一句话要点

**提出优化模型选择方法以提高LLM反事实评估的可靠性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `反事实生成` `标签翻转` `模型选择` `大型语言模型` `数据增强` `评估方法`

## 📋 核心要点

1. 现有方法在评估反事实生成的有效性时，判别模型的选择导致结果不一致，影响了模型的性能和鲁棒性。
2. 本文提出通过定义生成器与判别模型之间的关系，探索最优判别模型选择，以提高标签翻转评估的可靠性。
3. 实验结果显示，独立且未微调的判别模型在评估标签翻转时表现最佳，但与用户研究结果之间仍存在较大差距。

## 📝 摘要（中文）

反事实示例被广泛用于通过反事实数据增强（CDA）提升大型语言模型（LLMs）的性能和鲁棒性。然而，用于评估标签翻转的判别模型选择导致结果不一致。本文定义了生成器与判别模型之间的四种关系，并通过大量实验表明，独立且未微调的判别模型提供了最可靠的标签翻转评估。尽管如此，最有效判别模型与用户研究结果之间仍存在显著差距，表明CDA的完全自动化流程可能不足，需要人工干预。

## 🔬 方法详解

**问题定义**：本文旨在解决在反事实数据增强（CDA）中，判别模型选择导致的标签翻转评估不一致性问题。现有方法未能有效识别最优判别模型，影响了反事实示例的有效性评估。

**核心思路**：通过定义生成器与判别模型之间的四种关系，探索不同关系对标签翻转评估的影响，提出选择独立且未微调的判别模型作为最佳方案。

**技术框架**：研究包括两个最先进的LLM方法、三个数据集、四个生成器模型和15个判别模型的广泛实验，结合90人的用户研究，形成完整的评估框架。

**关键创新**：最重要的创新在于明确了生成器与判别模型之间的关系对评估结果的影响，提出了独立关系的判别模型在评估中的优越性。

**关键设计**：在实验中，选择了多种判别模型并进行了系统的对比，关注模型的独立性和微调状态，以确保评估结果的可靠性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文。

## 📊 实验亮点

实验结果表明，独立且未微调的判别模型在标签翻转评估中表现最佳，显著提高了评估的可靠性。尽管如此，最有效的判别模型与用户研究结果之间仍存在较大差距，提示未来研究需关注人工干预的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的反事实生成、模型评估和数据增强等。通过优化判别模型的选择，可以提升大型语言模型在实际应用中的性能和鲁棒性，推动智能对话系统、文本生成等技术的发展。

## 📄 摘要（原文）

> Counterfactual examples are widely employed to enhance the performance and robustness of large language models (LLMs) through counterfactual data augmentation (CDA). However, the selection of the judge model used to evaluate label flipping, the primary metric for assessing the validity of generated counterfactuals for CDA, yields inconsistent results. To decipher this, we define four types of relationships between the counterfactual generator and judge models: being the same model, belonging to the same model family, being independent models, and having an distillation relationship. Through extensive experiments involving two state-of-the-art LLM-based methods, three datasets, four generator models, and 15 judge models, complemented by a user study (n = 90), we demonstrate that judge models with an independent, non-fine-tuned relationship to the generator model provide the most reliable label flipping evaluations. Relationships between the generator and judge models, which are closely aligned with the user study for CDA, result in better model performance and robustness. Nevertheless, we find that the gap between the most effective judge models and the results obtained from the user study remains considerably large. This suggests that a fully automated pipeline for CDA may be inadequate and requires human intervention.

