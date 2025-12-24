---
layout: default
title: "SharedRep-RLHF: A Shared Representation Approach to RLHF with Diverse Preferences"
---

# SharedRep-RLHF: A Shared Representation Approach to RLHF with Diverse Preferences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03672" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03672v1</a>
  <a href="https://arxiv.org/pdf/2509.03672.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03672v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03672v1', 'SharedRep-RLHF: A Shared Representation Approach to RLHF with Diverse Preferences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arpan Mukherjee, Marcello Bullo, Deniz Gündüz

**分类**: cs.LG, stat.ML

**发布日期**: 2025-09-03

---

## 💡 一句话要点

**提出SharedRep-RLHF，利用共享表征提升RLHF在多偏好场景下的性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `人类反馈` `多偏好` `共享表征` `公平性`

## 📋 核心要点

1. 传统RLHF方法忽略了人群偏好的多样性，易受主导群体影响，导致公平性问题。
2. SharedRep-RLHF通过学习群体间共享的标注特征，而非独立奖励模型，来提升模型性能。
3. 实验表明，SharedRep-RLHF在多种自然语言任务中，相比MaxMin-RLHF，胜率提升高达20%。

## 📝 摘要（中文）

从人类反馈中进行强化学习(RLHF)的统一奖励方法，即训练单一奖励模型来代表所有标注者的偏好，无法捕捉不同子群体之间的意见多样性，从而无意中偏袒了优势群体。目前最先进的MaxMin-RLHF通过学习特定群体的奖励模型，并优化获得最小奖励的群体来解决这个问题，从而促进公平性。然而，我们发现MaxMin-RLHF的一个关键限制是，当最小奖励群体是少数群体时，其性能较差。为了缓解这个缺点，我们引入了一个名为SharedRep-RLHF的新框架。SharedRep-RLHF的核心在于学习和利用不同群体标注中的共享特征，而不是跨群体学习单独的奖励模型。我们首先证明MaxMin-RLHF在学习共享特征方面是次优的，然后量化SharedRep-RLHF的样本复杂度。在各种自然语言任务上的实验表明，与MaxMin-RLHF相比，SharedRep-RLHF的有效性更高，胜率提高了高达20%。

## 🔬 方法详解

**问题定义**：论文旨在解决传统RLHF方法在处理具有多样化偏好的人类反馈时表现不佳的问题。现有方法，如统一奖励RLHF，无法捕捉不同人群的偏好差异，而MaxMin-RLHF在少数群体获得最小奖励时性能下降。这些方法未能有效利用不同群体之间的共享信息，导致次优的奖励模型。

**核心思路**：SharedRep-RLHF的核心思路是学习和利用不同群体标注中的共享特征（shared traits）。通过提取这些共享特征，模型可以更好地泛化到不同的偏好群体，从而提高整体性能和公平性。这种方法避免了为每个群体单独训练奖励模型，减少了对特定群体数据的依赖。

**技术框架**：SharedRep-RLHF框架包含以下主要步骤：1) 数据收集：收集来自不同人群的标注数据。2) 共享表征学习：设计一个模型来学习不同人群标注数据中的共享特征。3) 奖励模型训练：利用学习到的共享表征来训练奖励模型，该模型能够更好地捕捉不同人群的偏好。4) 策略优化：使用训练好的奖励模型来优化策略，从而生成符合人类偏好的内容。

**关键创新**：SharedRep-RLHF的关键创新在于其利用共享表征来建模不同人群的偏好。与MaxMin-RLHF等方法不同，SharedRep-RLHF不依赖于为每个群体单独训练奖励模型，而是通过学习共享特征来实现更好的泛化能力和公平性。此外，论文还从理论上证明了MaxMin-RLHF在学习共享特征方面的次优性，并量化了SharedRep-RLHF的样本复杂度。

**关键设计**：SharedRep-RLHF的具体实现细节取决于具体的任务和数据集。一种可能的设计是使用一个共享编码器来提取不同人群标注数据的特征，然后使用一个或多个特定于人群的解码器来预测奖励。损失函数可以包括一个用于鼓励共享表征学习的正则化项，以及一个用于优化奖励模型性能的项。具体的网络结构和参数设置需要根据实验结果进行调整。

## 📊 实验亮点

实验结果表明，SharedRep-RLHF在多个自然语言任务上优于MaxMin-RLHF。具体而言，SharedRep-RLHF在胜率方面取得了高达20%的提升。这些结果验证了SharedRep-RLHF在处理多偏好场景下的有效性，并表明其能够更好地捕捉不同人群的偏好。

## 🎯 应用场景

SharedRep-RLHF可应用于各种需要考虑多方偏好的场景，例如个性化推荐系统、内容生成、对话系统等。通过学习和利用不同用户群体的共享特征，可以提升用户满意度和公平性，避免算法偏见，并为不同背景的用户提供更优质的服务。

## 📄 摘要（原文）

> Uniform-reward reinforcement learning from human feedback (RLHF), which trains a single reward model to represent the preferences of all annotators, fails to capture the diversity of opinions across sub-populations, inadvertently favoring dominant groups. The state-of-the-art, MaxMin-RLHF, addresses this by learning group-specific reward models, and by optimizing for the group receiving the minimum reward, thereby promoting fairness. However, we identify that a key limitation of MaxMin-RLHF is its poor performance when the minimum-reward group is a minority. To mitigate this drawback, we introduce a novel framework, termed {\em SharedRep-RLHF}. At its core, SharedRep-RLHF learns and leverages {\em shared traits} in annotations among various groups, in contrast to learning separate reward models across groups. We first show that MaxMin-RLHF is provably suboptimal in learning shared traits, and then quantify the sample complexity of SharedRep-RLHF. Experiments across diverse natural language tasks showcase the effectiveness of SharedRep-RLHF compared to MaxMin-RLHF with a gain of up to 20% in win rate.

