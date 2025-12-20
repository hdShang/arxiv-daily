---
layout: default
title: OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
---

# OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16295" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16295v1</a>
  <a href="https://arxiv.org/pdf/2512.16295.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16295v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16295v1', 'OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyu Wu, Jingjing Xie, Zehao Li, Bowen Yang, Qiushi Sun, Zhaoyang Liu, Zhoumianze Liu, Yu Qiao, Xiangyu Yue, Zun Wang, Zichen Ding

**分类**: cs.AI

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/numbmelon/OS-Oracle)

---

## 💡 一句话要点

**OS-Oracle：构建跨平台GUI评论模型的综合框架，提升计算机使用代理的决策能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `GUI评论模型` `计算机使用代理` `跨平台` `数据合成` `两阶段训练` `强化学习` `VLM`

## 📋 核心要点

1. 现有的计算机使用代理在长流程任务中容易累积错误，缺乏有效的步进式决策机制，导致实际应用受限。
2. OS-Oracle通过构建可扩展的数据管道、设计两阶段训练范式，并提供全面的评估基准，来解决GUI评论模型的不足。
3. 实验结果表明，OS-Oracle-7B在跨平台GUI评论任务中取得了领先的性能，并能有效提升现有GUI代理的性能。

## 📝 摘要（中文）

随着VLM驱动的计算机使用代理(CUA)在图形用户界面(GUI)导航和操作方面能力日益增强，可靠的步进式决策已成为实际部署的关键瓶颈。在长流程任务中，错误会迅速累积，不可逆操作可能导致意外后果，因此需要评估每次操作的评论模型。然而，缺乏多样化、高质量的GUI反馈数据和用于计算机使用中步进式评估的公共评论基准阻碍了评论模型的有效性。为了弥补这些差距，我们引入了OS-Oracle，它做出了三个核心贡献：(1)用于合成跨平台GUI评论数据的可扩展数据管道；(2)结合监督微调(SFT)和一致性保持组相对策略优化(CP-GRPO)的两阶段训练范式；(3)OS-Critic Bench，一个用于评估移动、Web和桌面平台评论模型性能的整体基准。利用该框架，我们整理了一个包含310k评论样本的高质量数据集。由此产生的评论模型OS-Oracle-7B在OS-Critic Bench上实现了最先进的开源VLM性能，并在移动领域超越了专有模型。此外，当作为预评论模型时，OS-Oracle-7B提高了原生GUI代理（如UI-TARS-1.5-7B）在OSWorld和AndroidWorld环境中的性能。代码已在https://github.com/numbmelon/OS-Oracle开源。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机使用代理（CUA）在GUI环境中的步进式决策问题。现有方法在长流程任务中容易出错，缺乏有效的反馈机制来评估每一步操作的合理性。此外，缺乏高质量的GUI反馈数据和公共评论基准也限制了评论模型的发展。

**核心思路**：论文的核心思路是构建一个高质量的GUI评论模型，该模型能够评估CUA在GUI环境中的每一步操作，并提供反馈以指导CUA做出更合理的决策。通过大规模数据合成、有效的训练范式和全面的评估基准，提升评论模型的性能和泛化能力。

**技术框架**：OS-Oracle框架包含三个主要组成部分：(1) 可扩展的数据管道，用于合成跨平台GUI评论数据；(2) 两阶段训练范式，包括监督微调(SFT)和一致性保持组相对策略优化(CP-GRPO)；(3) OS-Critic Bench，用于评估评论模型性能的基准。数据管道负责生成多样化的GUI交互数据，训练范式用于优化评论模型的性能，基准用于评估模型的泛化能力。

**关键创新**：论文的关键创新在于：(1) 提出了一个可扩展的数据管道，能够合成大规模、高质量的跨平台GUI评论数据，解决了数据稀缺的问题；(2) 设计了一种两阶段训练范式，结合了监督学习和强化学习的优点，提升了评论模型的性能和鲁棒性；(3) 构建了一个全面的评估基准，能够评估评论模型在不同平台和任务上的性能。

**关键设计**：在数据管道方面，论文采用了多种数据增强技术，以增加数据的多样性。在训练范式方面，CP-GRPO损失函数旨在保持策略的一致性，避免模型过度拟合。在OS-Critic Bench中，论文选择了多个具有代表性的GUI任务，并设计了合理的评估指标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16295v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16295v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16295v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

OS-Oracle-7B在OS-Critic Bench上取得了最先进的开源VLM性能，并在移动领域超越了专有模型。作为预评论模型时，OS-Oracle-7B显著提高了UI-TARS-1.5-7B在OSWorld和AndroidWorld环境中的性能。具体而言，在某些任务上，性能提升超过10%。

## 🎯 应用场景

该研究成果可应用于各种需要计算机使用代理的场景，例如自动化测试、智能助手、机器人流程自动化(RPA)等。通过提升CUA的决策能力，可以减少人工干预，提高工作效率，并降低错误率。未来，该技术有望应用于更复杂的GUI环境，例如游戏、虚拟现实等。

## 📄 摘要（原文）

> With VLM-powered computer-using agents (CUAs) becoming increasingly capable at graphical user interface (GUI) navigation and manipulation, reliable step-level decision-making has emerged as a key bottleneck for real-world deployment. In long-horizon workflows, errors accumulate quickly and irreversible actions can cause unintended consequences, motivating critic models that assess each action before execution. While critic models offer a promising solution, their effectiveness is hindered by the lack of diverse, high-quality GUI feedback data and public critic benchmarks for step-level evaluation in computer use. To bridge these gaps, we introduce OS-Oracle that makes three core contributions: (1) a scalable data pipeline for synthesizing cross-platform GUI critic data; (2) a two-stage training paradigm combining supervised fine-tuning (SFT) and consistency-preserving group relative policy optimization (CP-GRPO); (3) OS-Critic Bench, a holistic benchmark for evaluating critic model performance across Mobile, Web, and Desktop platforms. Leveraging this framework, we curate a high-quality dataset containing 310k critic samples. The resulting critic model, OS-Oracle-7B, achieves state-of-the-art performance among open-source VLMs on OS-Critic Bench, and surpasses proprietary models on the mobile domain. Furthermore, when serving as a pre-critic, OS-Oracle-7B improves the performance of native GUI agents such as UI-TARS-1.5-7B in OSWorld and AndroidWorld environments. The code is open-sourced at https://github.com/numbmelon/OS-Oracle.

