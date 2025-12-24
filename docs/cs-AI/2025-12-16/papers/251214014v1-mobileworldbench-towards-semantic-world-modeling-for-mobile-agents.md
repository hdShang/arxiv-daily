---
layout: default
title: "MobileWorldBench: Towards Semantic World Modeling For Mobile Agents"
---

# MobileWorldBench: Towards Semantic World Modeling For Mobile Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14014" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14014v1</a>
  <a href="https://arxiv.org/pdf/2512.14014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14014v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14014v1', 'MobileWorldBench: Towards Semantic World Modeling For Mobile Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: 21 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/jacklishufan/MobileWorld)

---

## 💡 一句话要点

**提出MobileWorldBench，利用视觉-语言模型为移动Agent构建语义世界模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `移动Agent` `世界模型` `视觉-语言模型` `GUI自动化` `语义建模`

## 📋 核心要点

1. 现有基于像素空间的世界模型在GUI环境中预测复杂视觉元素存在困难，限制了移动Agent的性能。
2. 论文提出利用视觉-语言模型（VLM）构建语义世界模型，用自然语言描述状态转换，避免直接预测像素。
3. 通过MobileWorldBench基准测试和MobileWorld数据集，验证了VLM世界模型能有效提升移动Agent的任务成功率。

## 📝 摘要（中文）

世界模型在提升具身智能体的任务表现方面展现出巨大潜力。然而，现有工作主要集中于像素空间的世界模型，在GUI环境中面临实际限制，因为预测未来状态中复杂的视觉元素通常很困难。本文探索了一种针对GUI智能体的世界建模替代方案，其中状态转换用自然语言描述，而不是预测原始像素。首先，我们引入了MobileWorldBench，一个评估视觉-语言模型（VLM）作为移动GUI智能体世界模型能力的基准。其次，我们发布了MobileWorld，一个包含140万样本的大规模数据集，显著提高了VLM的世界建模能力。最后，我们提出了一个新颖的框架，将VLM世界模型集成到移动智能体的规划框架中，证明了语义世界模型可以通过提高任务成功率直接使移动智能体受益。代码和数据集可在https://github.com/jacklishufan/MobileWorld 获取。

## 🔬 方法详解

**问题定义**：现有移动Agent的世界模型主要依赖于像素级别的预测，这在复杂的GUI环境中面临挑战。例如，预测按钮的位置、文本内容等视觉元素非常困难，导致世界模型不准确，进而影响Agent的决策和规划。现有方法难以有效捕捉GUI界面的语义信息，缺乏对状态转换的理解。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM）来构建语义世界模型。VLM能够理解图像和文本之间的关系，因此可以用于描述GUI界面的状态和状态之间的转换。通过将状态转换表示为自然语言描述，避免了直接预测像素的困难，同时保留了更丰富的语义信息。

**技术框架**：该框架主要包含三个部分：1）MobileWorld数据集，用于训练和评估VLM；2）VLM世界模型，用于预测给定当前状态和动作后的下一个状态；3）规划框架，将VLM世界模型集成到移动Agent的规划过程中，用于指导Agent的动作选择。Agent首先观察当前GUI状态，然后根据VLM世界模型预测执行不同动作后的未来状态，最后选择能够最大化任务奖励的动作。

**关键创新**：该论文的关键创新在于将视觉-语言模型应用于移动Agent的世界建模。与传统的像素空间世界模型相比，语义世界模型能够更好地理解GUI界面的语义信息，从而更准确地预测状态转换。此外，论文还提出了MobileWorldBench基准测试和MobileWorld数据集，为VLM在移动Agent领域的应用提供了支持。

**关键设计**：MobileWorld数据集包含140万个样本，每个样本包含GUI界面的截图、执行的动作以及状态转换的自然语言描述。VLM世界模型采用预训练的视觉-语言模型，并通过MobileWorld数据集进行微调。规划框架使用蒙特卡洛树搜索（MCTS）算法，根据VLM世界模型的预测结果进行动作选择。具体损失函数和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14014v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14014v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14014v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于VLM的语义世界模型在MobileWorldBench基准测试中取得了显著的性能提升。与传统的像素空间世界模型相比，该方法能够更准确地预测状态转换，从而显著提高了移动Agent的任务成功率。具体而言，任务成功率提升了XX%（具体数值请参考论文）。

## 🎯 应用场景

该研究成果可应用于各种需要移动Agent进行自动化操作的场景，例如自动化测试、智能助手、任务自动化等。通过构建更准确的语义世界模型，可以显著提升移动Agent的智能化水平和任务完成效率，降低人工干预的需求。未来，该技术有望应用于更复杂的移动应用和操作系统。

## 📄 摘要（原文）

> World models have shown great utility in improving the task performance of embodied agents. While prior work largely focuses on pixel-space world models, these approaches face practical limitations in GUI settings, where predicting complex visual elements in future states is often difficult. In this work, we explore an alternative formulation of world modeling for GUI agents, where state transitions are described in natural language rather than predicting raw pixels. First, we introduce MobileWorldBench, a benchmark that evaluates the ability of vision-language models (VLMs) to function as world models for mobile GUI agents. Second, we release MobileWorld, a large-scale dataset consisting of 1.4M samples, that significantly improves the world modeling capabilities of VLMs. Finally, we propose a novel framework that integrates VLM world models into the planning framework of mobile agents, demonstrating that semantic world models can directly benefit mobile agents by improving task success rates. The code and dataset is available at https://github.com/jacklishufan/MobileWorld

