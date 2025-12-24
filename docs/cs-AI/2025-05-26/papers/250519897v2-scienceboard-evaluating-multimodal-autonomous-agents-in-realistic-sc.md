---
layout: default
title: ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows
---

# ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19897" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19897v2</a>
  <a href="https://arxiv.org/pdf/2505.19897.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19897v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19897v2', 'ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiachong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu

**分类**: cs.AI, cs.CL, cs.CV, cs.HC

**发布日期**: 2025-05-26 (更新: 2025-06-27)

**备注**: work in progress

**🔗 代码/项目**: [PROJECT_PAGE](https://qiushisun.github.io/ScienceBoard-Home/)

---

## 💡 一句话要点

**提出ScienceBoard以评估多模态自主智能体在科学工作流中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态智能体` `科学工作流` `大型语言模型` `自动化科研` `任务基准` `跨学科研究` `智能系统`

## 📋 核心要点

1. 现有的LLM基础智能体在复杂科学工作流中表现不佳，成功率仅为15%。
2. ScienceBoard提供了一个动态的多领域环境，允许智能体与专业软件进行自主交互，旨在提升科学研究的效率。
3. 通过对169个真实任务的评估，揭示了现有智能体的不足，并为未来的改进提供了设计原则。

## 📝 摘要（中文）

大型语言模型（LLMs）已超越自然语言处理，推动跨学科研究的发展。本文介绍了ScienceBoard，提供了一个现实的多领域环境，支持自主智能体通过不同接口与专业软件互动，加速复杂的研究任务和实验。此外，构建了一个包含169个高质量、经过严格验证的真实世界任务的基准，涵盖生物化学、天文学和地理信息学等领域。尽管现有智能体在某些方面表现出色，但在复杂工作流中仅实现了15%的成功率，揭示了当前智能体的局限性，并为未来的设计提供了重要见解。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态自主智能体在复杂科学工作流中表现不佳的问题，特别是在任务成功率低的情况下，现有方法未能有效支持科学发现。

**核心思路**：论文提出ScienceBoard，通过创建一个多领域的动态环境，使智能体能够自主与专业软件互动，从而加速科学研究的进程。这样的设计旨在模拟真实的科研工作流，提升智能体的实用性和效率。

**技术框架**：ScienceBoard的整体架构包括两个主要模块：一是动态的多领域环境，二是高质量的任务基准。环境中集成了多种专业软件，智能体通过不同接口进行交互。

**关键创新**：最重要的创新在于创建了一个真实的、动态的科研工作流环境，并结合了严格验证的任务基准。这与现有方法的本质区别在于，现有方法往往缺乏真实场景的模拟和任务的多样性。

**关键设计**：在设计中，任务基准包含169个经过人工策划的高质量任务，涵盖多个科学领域。智能体的评估使用了先进的模型（如GPT-4o、Claude 3.7等），并通过严格的验证流程确保任务的有效性和挑战性。

## 📊 实验亮点

实验结果显示，尽管现有智能体在某些任务上表现出色，但整体成功率仅为15%。这一数据表明，当前的智能体在复杂科学工作流中仍存在显著的局限性，为未来的研究提供了重要的改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究、教育和技术开发等。通过提升智能体在科学工作流中的表现，能够加速科学发现的进程，降低研究人员的工作负担，推动跨学科的合作与创新。未来，ScienceBoard可能成为评估和开发智能体的新标准，促进更高效的科研工具的出现。

## 📄 摘要（原文）

> Large Language Models (LLMs) have extended their impact beyond Natural Language Processing, substantially fostering the development of interdisciplinary research. Recently, various LLM-based agents have been developed to assist scientific discovery progress across multiple aspects and domains. Among these, computer-using agents, capable of interacting with operating systems as humans do, are paving the way to automated scientific problem-solving and addressing routines in researchers' workflows. Recognizing the transformative potential of these agents, we introduce ScienceBoard, which encompasses two complementary contributions: (i) a realistic, multi-domain environment featuring dynamic and visually rich scientific workflows with integrated professional software, where agents can autonomously interact via different interfaces to accelerate complex research tasks and experiments; and (ii) a challenging benchmark of 169 high-quality, rigorously validated real-world tasks curated by humans, spanning scientific-discovery workflows in domains such as biochemistry, astronomy, and geoinformatics. Extensive evaluations of agents with state-of-the-art backbones (e.g., GPT-4o, Claude 3.7, UI-TARS) show that, despite some promising results, they still fall short of reliably assisting scientists in complex workflows, achieving only a 15% overall success rate. In-depth analysis further provides valuable insights for addressing current agent limitations and more effective design principles, paving the way to build more capable agents for scientific discovery. Our code, environment, and benchmark are at https://qiushisun.github.io/ScienceBoard-Home/.

