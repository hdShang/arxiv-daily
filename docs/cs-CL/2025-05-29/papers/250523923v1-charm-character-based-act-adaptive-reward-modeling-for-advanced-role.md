---
layout: default
title: ChARM: Character-based Act-adaptive Reward Modeling for Advanced Role-Playing Language Agents
---

# ChARM: Character-based Act-adaptive Reward Modeling for Advanced Role-Playing Language Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23923" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23923v1</a>
  <a href="https://arxiv.org/pdf/2505.23923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23923v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23923v1', 'ChARM: Character-based Act-adaptive Reward Modeling for Advanced Role-Playing Language Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feiteng Fang, Ting-En Lin, Yuchuan Wu, Xiong Liu, Xiang Huang, Dingwei Chen, Jing Ye, Haonan Zhang, Liang Zhu, Hamid Alinejad-Rokny, Min Yang, Fei Huang, Yongbin Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-29

**🔗 代码/项目**: [GITHUB](https://github.com/calubkk/ChARM)

---

## 💡 一句话要点

**提出ChARM以解决角色扮演语言代理的奖励建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `角色扮演` `奖励建模` `自适应学习` `对话系统` `机器学习` `数据集构建` `评估基准`

## 📋 核心要点

1. 现有的奖励模型在角色扮演语言代理的可扩展性和适应性方面存在显著不足，难以满足主观对话偏好的需求。
2. ChARM通过引入自适应边际和自我进化机制，提升了学习效率和泛化能力，并利用未标注数据增强训练覆盖。
3. 实验结果表明，ChARM在偏好排名上较传统模型提升了13%，并在多个评估基准上达到了最先进的性能。

## 📝 摘要（中文）

角色扮演语言代理（RPLA）旨在模拟角色以实现真实且引人入胜的人机交互。然而，传统的奖励模型在可扩展性和适应主观对话偏好方面存在困难。我们提出了ChARM，即基于角色的自适应奖励模型，通过两个创新来应对这些挑战：（1）自适应边际显著提高学习效率和泛化能力；（2）自我进化机制利用大规模未标注数据改善训练覆盖。此外，我们引入了RoleplayPref，这是第一个专门针对RPLA的大规模偏好数据集，包含1,108个角色、13个子类别和16,888个双语对话，以及专门的评估基准RoleplayEval。实验结果显示，在偏好排名上相比传统的Bradley-Terry模型提升了13%。此外，将ChARM生成的奖励应用于偏好学习技术（如直接偏好优化）在CharacterEval和RoleplayEval上达到了最先进的结果。

## 🔬 方法详解

**问题定义**：本论文旨在解决角色扮演语言代理（RPLA）中传统奖励模型的可扩展性和适应性不足的问题，特别是在面对主观对话偏好时的挑战。

**核心思路**：ChARM的核心思路是通过引入自适应边际和自我进化机制来提升模型的学习效率和泛化能力，使其能够更好地适应多样化的对话场景。

**技术框架**：ChARM的整体架构包括两个主要模块：自适应边际模块和自我进化机制模块。自适应边际模块负责根据对话上下文动态调整奖励，而自我进化机制则利用大规模未标注数据进行训练覆盖的扩展。

**关键创新**：ChARM的主要创新在于自适应边际的引入和自我进化机制的设计，这与现有方法的静态奖励计算方式形成了本质区别，显著提升了模型的灵活性和适应性。

**关键设计**：在关键设计方面，ChARM采用了特定的损失函数来优化奖励的学习过程，并通过网络结构的调整来实现对多样化对话的适应性。

## 📊 实验亮点

实验结果显示，ChARM在偏好排名上较传统Bradley-Terry模型提升了13%。此外，应用ChARM生成的奖励于偏好学习技术（如直接偏好优化）在CharacterEval和RoleplayEval上达到了最先进的结果，展示了其优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、虚拟助手和教育领域等，能够为用户提供更为个性化和互动性强的体验。通过提升角色扮演语言代理的表现，未来可能在人机交互的多个场景中发挥重要作用。

## 📄 摘要（原文）

> Role-Playing Language Agents (RPLAs) aim to simulate characters for realistic and engaging human-computer interactions. However, traditional reward models often struggle with scalability and adapting to subjective conversational preferences. We propose ChARM, a Character-based Act-adaptive Reward Model, addressing these challenges through two innovations: (1) an act-adaptive margin that significantly enhances learning efficiency and generalizability, and (2) a self-evolution mechanism leveraging large-scale unlabeled data to improve training coverage. Additionally, we introduce RoleplayPref, the first large-scale preference dataset specifically for RPLAs, featuring 1,108 characters, 13 subcategories, and 16,888 bilingual dialogues, alongside RoleplayEval, a dedicated evaluation benchmark. Experimental results show a 13% improvement over the conventional Bradley-Terry model in preference rankings. Furthermore, applying ChARM-generated rewards to preference learning techniques (e.g., direct preference optimization) achieves state-of-the-art results on CharacterEval and RoleplayEval. Code and dataset are available at https://github.com/calubkk/ChARM.

