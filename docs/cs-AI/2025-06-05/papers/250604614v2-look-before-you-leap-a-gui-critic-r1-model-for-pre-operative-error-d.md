---
layout: default
title: "Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation"
---

# Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04614" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04614v2</a>
  <a href="https://arxiv.org/pdf/2506.04614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04614v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04614v2', 'Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyang Wanyan, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Jiabo Ye, Yutong Kou, Ming Yan, Fei Huang, Xiaoshan Yang, Weiming Dong, Changsheng Xu

**分类**: cs.AI

**发布日期**: 2025-06-05 (更新: 2025-11-17)

---

## 💡 一句话要点

**提出GUI-Critic-R1模型以解决GUI自动化中的预操作错误诊断问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图形用户界面` `自动化` `多模态大语言模型` `错误诊断` `预操作评估` `策略优化` `数据收集`

## 📋 核心要点

1. 现有的GUI自动化方法在实时交互环境中决策错误容忍度低，容易导致不可逆的错误。
2. 本文提出了一种预操作评估机制，通过推理潜在结果和动作的正确性，提供有效的反馈。
3. 实验结果表明，GUI-Critic-R1在评估准确性和操作效率上显著优于现有的多模态大语言模型。

## 📝 摘要（中文）

近年来，多模态大语言模型（MLLMs）在多模态推理任务中得到了广泛应用，包括图形用户界面（GUI）自动化。与一般的离线多模态任务不同，GUI自动化是在在线交互环境中执行的，要求基于环境的实时状态进行逐步决策。每一步的决策错误容忍度较低，任何错误可能会累积导致不可逆的结果，如删除或支付。为了解决这些问题，本文引入了一种预操作评估机制，通过推理潜在结果和动作的正确性，在实际执行前提供有效反馈。具体而言，我们提出了一种基于建议的梯度相对策略优化（S-GRPO）策略，构建了预操作评估模型GUI-Critic-R1，结合新颖的建议奖励以增强模型反馈的可靠性。此外，我们开发了一种基于推理引导的数据收集管道，创建了GUI-Critic-Train和GUI-Critic-Test，填补了现有GUI评估数据的空白。静态实验结果显示，GUI-Critic-R1在移动和网页领域的评估准确性上显著优于当前的MLLMs。

## 🔬 方法详解

**问题定义**：本文旨在解决GUI自动化中的预操作错误诊断问题，现有方法在实时决策中容易出现错误，导致不可逆的后果。

**核心思路**：论文提出了一种预操作评估机制，通过推理潜在结果和动作的正确性，提前提供反馈，以降低决策错误的风险。

**技术框架**：整体架构包括预操作评估模型GUI-Critic-R1，采用建议感知的梯度相对策略优化（S-GRPO）策略，并结合推理引导的数据收集管道，生成训练和测试数据集。

**关键创新**：最重要的创新点在于引入了建议奖励机制，增强了模型反馈的可靠性，与现有方法相比，提供了更为准确的评估。

**关键设计**：在模型设计中，采用了特定的损失函数和网络结构，确保模型能够有效地学习和推理，并在动态评估中表现出色。

## 📊 实验亮点

实验结果显示，GUI-Critic-R1在静态测试中相比现有多模态大语言模型的评估准确性显著提高，动态评估中成功率和操作效率也得到了明显改善，具体提升幅度未明确给出。

## 🎯 应用场景

该研究的潜在应用领域包括软件测试、用户界面设计和自动化操作等。通过提高GUI自动化的准确性和效率，能够显著降低用户操作错误的风险，提升用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In recent years, Multimodal Large Language Models (MLLMs) have been extensively utilized for multimodal reasoning tasks, including Graphical User Interface (GUI) automation. Unlike general offline multimodal tasks, GUI automation is executed in online interactive environments, necessitating step-by-step decision-making based on real-time status of the environment. This task has a lower tolerance for decision-making errors at each step, as any mistakes may cumulatively disrupt the process and potentially lead to irreversible outcomes like deletions or payments. To address these issues, we introduce a pre-operative critic mechanism that provides effective feedback prior to the actual execution, by reasoning about the potential outcome and correctness of actions. Specifically, we propose a Suggestion-aware Gradient Relative Policy Optimization (S-GRPO) strategy to construct our pre-operative critic model GUI-Critic-R1, incorporating a novel suggestion reward to enhance the reliability of the model's feedback. Furthermore, we develop a reasoning-bootstrapping based data collection pipeline to create a GUI-Critic-Train and a GUI-Critic-Test, filling existing gaps in GUI critic data. Static experiments on the GUI-Critic-Test across both mobile and web domains reveal that our GUI-Critic-R1 offers significant advantages in critic accuracy compared to current MLLMs. Dynamic evaluation on GUI automation benchmark further highlights the effectiveness and superiority of our model, as evidenced by improved success rates and operational efficiency.

