---
layout: default
title: "OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models"
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

**OS-Oracle：跨平台GUI评论模型的综合框架，提升计算机使用代理的决策能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `GUI评论模型` `跨平台` `计算机使用代理` `两阶段训练` `数据合成` `强化学习` `基准测试`

## 📋 核心要点

1. 现有计算机使用代理在GUI操作中面临步级决策可靠性问题，长时程任务中易累积错误。
2. 提出OS-Oracle框架，通过合成数据、两阶段训练和基准测试，提升评论模型性能。
3. OS-Oracle-7B在跨平台GUI评论任务中达到SOTA，并能有效提升现有GUI代理的性能。

## 📝 摘要（中文）

随着VLM驱动的计算机使用代理(CUA)在图形用户界面(GUI)导航和操作方面能力日益增强，可靠的步级决策已成为实际部署的关键瓶颈。在长时程工作流程中，错误会迅速累积，不可逆的操作可能导致意想不到的后果，因此需要评估每次操作的评论模型。然而，缺乏多样化、高质量的GUI反馈数据和用于计算机使用中步级评估的公共评论基准阻碍了评论模型的有效性。为了弥合这些差距，我们引入了OS-Oracle，它做出了三个核心贡献：(1)用于合成跨平台GUI评论数据的可扩展数据管道；(2)结合监督微调(SFT)和一致性保持的群体相对策略优化(CP-GRPO)的两阶段训练范式；(3)OS-Critic Bench，一个用于评估移动、Web和桌面平台评论模型性能的整体基准。利用该框架，我们整理了一个包含31万个评论样本的高质量数据集。由此产生的评论模型OS-Oracle-7B在OS-Critic Bench上实现了开源VLM中最先进的性能，并在移动领域超越了专有模型。此外，当作为预评论模型时，OS-Oracle-7B提高了原生GUI代理（如UI-TARS-1.5-7B）在OSWorld和AndroidWorld环境中的性能。代码已在https://github.com/numbmelon/OS-Oracle上开源。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机使用代理（CUAs）在图形用户界面（GUI）交互中，由于缺乏可靠的步级决策能力而导致的性能瓶颈问题。现有方法在长时程任务中容易累积错误，并且缺乏高质量的GUI反馈数据和公共评论基准，难以有效评估和提升决策能力。

**核心思路**：论文的核心思路是构建一个综合的框架，包括数据合成管道、训练范式和评估基准，从而提升评论模型在GUI交互中的决策能力。通过大规模合成高质量的GUI反馈数据，并采用两阶段训练方法，训练出一个能够准确评估每一步操作的评论模型。

**技术框架**：OS-Oracle框架包含三个主要组成部分：(1) 可扩展的数据管道，用于合成跨平台GUI评论数据；(2) 两阶段训练范式，包括监督微调（SFT）和一致性保持的群体相对策略优化（CP-GRPO）；(3) OS-Critic Bench，一个用于评估评论模型在移动、Web和桌面平台性能的基准。整体流程是先通过数据管道生成训练数据，然后使用两阶段训练方法训练评论模型，最后使用OS-Critic Bench评估模型性能。

**关键创新**：论文的关键创新在于提出了一个完整的框架，解决了GUI评论模型训练和评估中的数据稀缺和基准缺失问题。具体包括：(1) 设计了一个可扩展的数据管道，能够合成多样化、高质量的GUI反馈数据；(2) 提出了一个两阶段训练范式，结合了监督学习和强化学习的优点，提升了模型的泛化能力和鲁棒性；(3) 构建了一个全面的评估基准，能够客观地评估评论模型在不同平台和任务上的性能。

**关键设计**：在数据合成方面，论文设计了能够模拟用户交互行为的规则和策略，从而生成真实的GUI反馈数据。在两阶段训练中，SFT阶段使用监督学习方法，使模型学习基本的评论知识；CP-GRPO阶段使用强化学习方法，通过群体策略优化，提升模型的一致性和鲁棒性。损失函数的设计也考虑了不同平台和任务的特点，从而更好地优化模型性能。具体参数设置和网络结构细节在论文中有更详细的描述。

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

OS-Oracle-7B在OS-Critic Bench上实现了开源VLM中最先进的性能，并在移动领域超越了专有模型。此外，当作为预评论模型时，OS-Oracle-7B提高了原生GUI代理（如UI-TARS-1.5-7B）在OSWorld和AndroidWorld环境中的性能。这些结果表明，OS-Oracle框架能够有效提升评论模型的性能，并改善计算机使用代理的决策能力。

## 🎯 应用场景

该研究成果可广泛应用于各种需要人机交互的场景，例如智能助手、自动化测试、机器人流程自动化（RPA）等。通过提升计算机使用代理的决策能力，可以减少人为干预，提高工作效率，并降低错误率。未来，该技术有望应用于更复杂的任务，例如医疗诊断、金融分析等。

## 📄 摘要（原文）

> With VLM-powered computer-using agents (CUAs) becoming increasingly capable at graphical user interface (GUI) navigation and manipulation, reliable step-level decision-making has emerged as a key bottleneck for real-world deployment. In long-horizon workflows, errors accumulate quickly and irreversible actions can cause unintended consequences, motivating critic models that assess each action before execution. While critic models offer a promising solution, their effectiveness is hindered by the lack of diverse, high-quality GUI feedback data and public critic benchmarks for step-level evaluation in computer use. To bridge these gaps, we introduce OS-Oracle that makes three core contributions: (1) a scalable data pipeline for synthesizing cross-platform GUI critic data; (2) a two-stage training paradigm combining supervised fine-tuning (SFT) and consistency-preserving group relative policy optimization (CP-GRPO); (3) OS-Critic Bench, a holistic benchmark for evaluating critic model performance across Mobile, Web, and Desktop platforms. Leveraging this framework, we curate a high-quality dataset containing 310k critic samples. The resulting critic model, OS-Oracle-7B, achieves state-of-the-art performance among open-source VLMs on OS-Critic Bench, and surpasses proprietary models on the mobile domain. Furthermore, when serving as a pre-critic, OS-Oracle-7B improves the performance of native GUI agents such as UI-TARS-1.5-7B in OSWorld and AndroidWorld environments. The code is open-sourced at https://github.com/numbmelon/OS-Oracle.

