---
layout: default
title: "Self Generated Wargame AI: Double Layer Agent Task Planning Based on Large Language Model"
---

# Self Generated Wargame AI: Double Layer Agent Task Planning Based on Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01090" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01090v2</a>
  <a href="https://arxiv.org/pdf/2312.01090.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01090v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01090v2', 'Self Generated Wargame AI: Double Layer Agent Task Planning Based on Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Y. Sun, J. Zhao, C. Yu, W. Wang, X. Zhou

**分类**: cs.AI, cs.CL

**发布日期**: 2023-12-02 (更新: 2023-12-18)

---

## 💡 一句话要点

**提出基于大语言模型的双层Agent任务规划，用于智能决策**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `智能决策` `Agent架构` `任务规划` `兵棋推演`

## 📋 核心要点

1. 现有智能决策方法（如强化学习、规则AI）在智能性、可理解性和泛化性方面存在局限性。
2. 提出一种基于大语言模型的双层Agent架构，利用自然语言交互进行任务规划和决策。
3. 实验表明，该方法在兵棋推演中优于传统方法，且智能性与Prompt设计密切相关。

## 📝 摘要（中文）

本文创新性地将大语言模型应用于智能决策领域，构建了一个以大语言模型为核心的Agent架构。在此基础上，进一步提出了双层Agent任务规划方法，通过自然语言交互发布和执行决策指令，并通过兵棋推演模拟环境进行验证。实验结果表明，大语言模型的智能决策能力明显强于常用的强化学习AI和规则AI，并且在智能性、可理解性和泛化性方面均表现更佳。实验还发现，大语言模型的智能程度与Prompt密切相关。这项工作将大语言模型从以往的人机交互扩展到智能决策领域，对智能决策的发展具有重要的参考价值和意义。

## 🔬 方法详解

**问题定义**：现有智能决策方法，如强化学习和规则AI，在复杂环境下的智能性、可理解性和泛化能力方面存在瓶颈。尤其是在需要高度策略性和适应性的兵棋推演等场景中，传统方法难以有效应对。

**核心思路**：将大语言模型置于决策中心，利用其强大的自然语言理解和生成能力，实现更智能、更灵活的决策过程。通过自然语言交互，Agent可以理解任务目标，规划任务步骤，并执行相应的指令。这种方式更接近人类的决策模式，也更易于理解和调试。

**技术框架**：该方法采用双层Agent架构。第一层Agent负责接收高级别的任务目标，并利用大语言模型进行任务分解和规划，生成一系列子任务。第二层Agent负责执行这些子任务，并将执行结果反馈给第一层Agent。整个过程通过自然语言进行交互，实现了任务规划和执行的协同。

**关键创新**：将大语言模型应用于智能决策领域，并提出了双层Agent任务规划方法。与传统的基于规则或强化学习的决策方法相比，该方法具有更强的智能性、可理解性和泛化能力。通过自然语言交互，Agent可以更好地理解任务目标，并根据环境变化进行灵活调整。

**关键设计**：Prompt的设计是关键。不同的Prompt会显著影响大语言模型的决策质量。论文可能探索了不同的Prompt策略，例如，提供详细的任务描述、明确的约束条件、以及相关的背景知识。具体的损失函数和网络结构未知，因为大语言模型本身是预训练的，这里主要关注如何有效地利用它。

## 📊 实验亮点

实验结果表明，基于大语言模型的Agent在兵棋推演中表现显著优于传统的强化学习AI和规则AI。具体性能数据未知，但强调了在智能性、可理解性和泛化性方面的优势。同时，实验还发现Prompt的设计对大语言模型的智能程度有重要影响。

## 🎯 应用场景

该研究成果可应用于军事指挥、智能交通、机器人控制、游戏AI等领域。通过将大语言模型应用于智能决策，可以提高决策效率和质量，实现更智能化的系统。未来，可以进一步探索如何将该方法与其他技术（如强化学习、知识图谱）相结合，以实现更强大的智能决策能力。

## 📄 摘要（原文）

> The large language models represented by ChatGPT have a disruptive impact on the field of artificial intelligence. But it mainly focuses on natural language processing, speech recognition, machine learning and natural language understanding. This paper innovatively applies the large language model to the field of intelligent decision-making, places the large language model in the decision-making center, and constructs an agent architecture with the large language model as the core. Based on this, it further proposes a two-layer agent task planning, issues and executes decision commands through the interaction of natural language, and carries out simulation verification through the wargame simulation environment. Through the game confrontation simulation experiment, it is found that the intelligent decision-making ability of the large language model is significantly stronger than the commonly used reinforcement learning AI and rule AI, and the intelligence, understandability and generalization are all better. And through experiments, it was found that the intelligence of the large language model is closely related to prompt. This work also extends the large language model from previous human-computer interaction to the field of intelligent decision-making, which has important reference value and significance for the development of intelligent decision-making.

