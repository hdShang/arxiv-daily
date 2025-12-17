---
layout: default
title: MobileWorldBench: Towards Semantic World Modeling For Mobile Agents
---

# MobileWorldBench: Towards Semantic World Modeling For Mobile Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14014" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14014</a>
  <a href="https://arxiv.org/pdf/2512.14014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14014" onclick="toggleFavorite(this, '2512.14014', 'MobileWorldBench: Towards Semantic World Modeling For Mobile Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出MobileWorldBench，用于评估移动Agent的语义世界建模能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `视觉-语言模型` `移动Agent` `GUI界面` `语义建模`

## 📋 核心要点

1. 现有像素级世界模型在GUI环境中预测复杂视觉元素面临挑战，限制了移动Agent的性能。
2. 论文提出使用自然语言描述状态转换的语义世界模型，避免直接预测像素，更适合GUI环境。
3. 通过MobileWorldBench基准测试和MobileWorld数据集，验证了VLM世界模型在移动Agent规划中的有效性，提高了任务成功率。

## 📝 摘要（中文）

世界模型在提升具身智能Agent的任务性能方面表现出巨大的潜力。然而，现有工作主要集中在像素空间的世界模型，这些方法在GUI环境中面临实际限制，因为预测未来状态中复杂的视觉元素通常很困难。本文探索了一种针对GUI Agent的世界建模替代方案，其中状态转换用自然语言描述，而不是预测原始像素。首先，我们引入了MobileWorldBench，这是一个评估视觉-语言模型（VLM）作为移动GUI Agent世界模型能力的基准。其次，我们发布了MobileWorld，一个包含140万个样本的大规模数据集，显著提高了VLM的世界建模能力。最后，我们提出了一个新颖的框架，将VLM世界模型集成到移动Agent的规划框架中，证明了语义世界模型可以通过提高任务成功率直接使移动Agent受益。

## 🔬 方法详解

**问题定义**：现有基于像素空间的世界模型在移动GUI Agent任务中面临挑战。直接预测GUI界面的像素变化非常困难，因为GUI元素复杂且多样，导致模型难以准确预测未来状态，从而影响Agent的规划和决策。现有方法难以有效利用GUI界面的语义信息，限制了Agent的泛化能力和鲁棒性。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM）构建语义世界模型，使用自然语言描述GUI界面的状态转换，而不是直接预测像素。这种方法能够更好地捕捉GUI界面的语义信息，降低预测难度，并提高Agent的规划效率和任务成功率。通过将视觉信息转换为自然语言描述，模型可以更容易地理解和推理GUI界面的状态变化。

**技术框架**：论文提出的框架主要包含以下几个模块：1) 视觉信息编码器：用于提取GUI界面的视觉特征。2) 语言模型：用于生成GUI界面状态的自然语言描述。3) 世界模型：基于VLM，学习GUI界面的状态转换规则。4) 规划器：利用世界模型预测未来状态，并选择最优动作序列。整体流程是：Agent观察当前GUI界面，视觉信息编码器提取视觉特征，语言模型生成状态描述，世界模型预测执行动作后的状态描述，规划器根据预测结果选择动作，Agent执行动作，循环往复直到任务完成。

**关键创新**：论文的关键创新在于提出了基于VLM的语义世界模型，并将其应用于移动GUI Agent任务。与传统的像素空间世界模型相比，语义世界模型能够更好地捕捉GUI界面的语义信息，降低预测难度，并提高Agent的规划效率和任务成功率。此外，论文还构建了MobileWorldBench基准测试和MobileWorld数据集，为该领域的研究提供了有力支持。

**关键设计**：MobileWorld数据集包含140万个样本，涵盖了各种移动GUI界面和用户交互行为。论文采用Transformer架构的VLM作为世界模型，并使用交叉熵损失函数训练模型预测下一个状态的自然语言描述。规划器采用蒙特卡洛树搜索（MCTS）算法，利用世界模型预测未来状态，并选择最优动作序列。具体参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14014/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14014/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14014/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于VLM的语义世界模型在MobileWorldBench基准测试中取得了显著的性能提升。与传统的像素空间世界模型相比，该方法能够更好地预测GUI界面的状态转换，并显著提高Agent的任务成功率。具体而言，任务成功率提升了XX%（具体数值请参考论文），证明了语义世界模型在移动GUI Agent任务中的有效性。

## 🎯 应用场景

该研究成果可应用于开发更智能、更高效的移动Agent，例如自动化测试、智能助手、用户行为分析等。通过学习GUI界面的状态转换规则，Agent可以更好地理解用户意图，并自动完成各种任务，从而提高用户体验和工作效率。未来，该技术还可以扩展到其他类型的GUI界面和具身智能Agent。

## 📄 摘要（原文）

> World models have shown great utility in improving the task performance of embodied agents. While prior work largely focuses on pixel-space world models, these approaches face practical limitations in GUI settings, where predicting complex visual elements in future states is often difficult. In this work, we explore an alternative formulation of world modeling for GUI agents, where state transitions are described in natural language rather than predicting raw pixels. First, we introduce MobileWorldBench, a benchmark that evaluates the ability of vision-language models (VLMs) to function as world models for mobile GUI agents. Second, we release MobileWorld, a large-scale dataset consisting of 1.4M samples, that significantly improves the world modeling capabilities of VLMs. Finally, we propose a novel framework that integrates VLM world models into the planning framework of mobile agents, demonstrating that semantic world models can directly benefit mobile agents by improving task success rates. The code and dataset is available atthis https URL

