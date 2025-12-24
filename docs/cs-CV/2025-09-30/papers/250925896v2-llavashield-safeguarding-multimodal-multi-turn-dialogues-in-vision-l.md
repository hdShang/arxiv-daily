---
layout: default
title: "LLaVAShield: Safeguarding Multimodal Multi-Turn Dialogues in Vision-Language Models"
---

# LLaVAShield: Safeguarding Multimodal Multi-Turn Dialogues in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25896" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25896v2</a>
  <a href="https://arxiv.org/pdf/2509.25896.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25896v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25896v2', 'LLaVAShield: Safeguarding Multimodal Multi-Turn Dialogues in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guolei Huang, Qinzhi Peng, Gan Xu, Yuxuan Lu, Yongjun Shen

**分类**: cs.CV

**发布日期**: 2025-09-30 (更新: 2025-10-01)

---

## 💡 一句话要点

**提出LLaVAShield，用于保障视觉-语言模型中多模态多轮对话的安全性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态对话安全` `视觉-语言模型` `红队测试` `蒙特卡洛树搜索` `内容审核` `风险评估`

## 📋 核心要点

1. 现有的单轮或单模态审核方法无法有效应对视觉-语言模型在多轮交互中产生的安全风险。
2. 论文提出LLaVAShield，通过联合检测和评估用户输入和助手响应中的风险来保障多模态多轮对话安全。
3. 实验表明，LLaVAShield在多模态多轮内容审核任务中优于现有基线方法，达到了新的state-of-the-art。

## 📝 摘要（中文）

随着视觉-语言模型(VLMs)进入交互式、多轮使用，出现了单轮或单模态审核遗漏的新安全风险。在多模态多轮(MMT)对话中，恶意意图可以跨轮次和图像传播，而上下文相关的回复可能仍然会推进有害内容。为了应对这一挑战，我们首次系统地定义和研究了MMT对话安全性。在此基础上，我们引入了多模态多轮对话安全(MMDS)数据集。我们进一步开发了一种基于蒙特卡洛树搜索(MCTS)的自动化多模态多轮红队框架，用于为MMDS生成不安全的多模态多轮对话。MMDS包含4,484个带注释的多模态对话样本，具有细粒度的安全评级、策略维度标签以及用户和助手基于证据的理由。利用MMDS，我们提出了LLaVAShield，这是一个强大的工具，可以联合检测和评估用户输入和助手响应中的风险。在全面的实验中，LLaVAShield在MMT内容审核任务和动态策略配置下始终优于强大的基线，建立了新的最先进的结果。我们将公开发布数据集和模型，以支持未来的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型在多模态多轮对话中存在的安全问题。现有方法主要针对单轮或单模态场景，无法有效识别和缓解跨轮次、跨模态传播的恶意意图，以及上下文相关的有害内容。

**核心思路**：论文的核心思路是构建一个能够联合检测和评估用户输入和助手响应风险的系统，即LLaVAShield。通过分析对话历史、图像内容以及上下文信息，更准确地识别潜在的安全风险。

**技术框架**：LLaVAShield的整体框架包含数据收集、模型训练和风险评估三个主要阶段。首先，利用基于蒙特卡洛树搜索(MCTS)的红队框架生成不安全的多模态多轮对话，构建MMDS数据集。然后，基于MMDS数据集训练风险检测模型。最后，利用训练好的模型对用户输入和助手响应进行风险评估，并采取相应的安全措施。

**关键创新**：论文的关键创新在于首次系统地定义和研究了多模态多轮对话安全性问题，并提出了相应的解决方案。此外，基于MCTS的红队框架能够自动生成多样化的不安全对话，有效提升了模型的鲁棒性。MMDS数据集的构建也为后续研究提供了宝贵资源。

**关键设计**：论文使用了细粒度的安全评级和策略维度标签来标注MMDS数据集，以便更准确地评估模型的性能。此外，LLaVAShield的具体模型结构和训练细节（例如损失函数、网络结构等）在论文中未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，LLaVAShield在多模态多轮内容审核任务中显著优于现有基线方法，在MMT内容审核任务和动态策略配置下始终优于强大的基线，建立了新的最先进的结果。具体性能数据和提升幅度在摘要中未给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于各种需要安全保障的视觉-语言对话系统，例如智能客服、教育机器人、医疗诊断助手等。通过有效识别和过滤有害信息，可以提升用户体验，防止恶意攻击，并促进视觉-语言模型在实际场景中的安全应用。

## 📄 摘要（原文）

> As Vision-Language Models (VLMs) move into interactive, multi-turn use, new safety risks arise that single-turn or single-modality moderation misses. In Multimodal Multi-Turn (MMT) dialogues, malicious intent can be spread across turns and images, while context-sensitive replies may still advance harmful content. To address this challenge, we present the first systematic definition and study of MMT dialogue safety. Building on this formulation, we introduce the Multimodal Multi-turn Dialogue Safety (MMDS) dataset. We further develop an automated multimodal multi-turn red-teaming framework based on Monte Carlo Tree Search (MCTS) to generate unsafe multimodal multi-turn dialogues for MMDS. MMDS contains 4,484 annotated multimodal dialogue samples with fine-grained safety ratings, policy dimension labels, and evidence-based rationales for both users and assistants. Leveraging MMDS, we present LLaVAShield, a powerful tool that jointly detects and assesses risk in user inputs and assistant responses. Across comprehensive experiments, LLaVAShield consistently outperforms strong baselines on MMT content moderation tasks and under dynamic policy configurations, establishing new state-of-the-art results. We will publicly release the dataset and model to support future research.

