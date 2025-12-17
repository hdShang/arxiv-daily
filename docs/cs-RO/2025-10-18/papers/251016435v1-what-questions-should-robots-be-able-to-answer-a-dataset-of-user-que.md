---
layout: default
title: What Questions Should Robots Be Able to Answer? A Dataset of User Questions for Explainable Robotics
---

# What Questions Should Robots Be Able to Answer? A Dataset of User Questions for Explainable Robotics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16435" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16435v1</a>
  <a href="https://arxiv.org/pdf/2510.16435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16435v1" onclick="toggleFavorite(this, '2510.16435v1', 'What Questions Should Robots Be Able to Answer? A Dataset of User Questions for Explainable Robotics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lennart Wachowiak, Andrew Coles, Gerard Canal, Oya Celiktutan

**分类**: cs.RO, cs.CL, cs.HC

**发布日期**: 2025-10-18

---

## 💡 一句话要点

**构建面向可解释机器人的用户问题数据集，助力提升人机交互能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `可解释机器人` `用户问题数据集` `问答系统` `家庭机器人`

## 📋 核心要点

1. 现有可解释机器人研究主要集中在“为什么”的问题上，缺乏对用户多样化问题的全面理解。
2. 论文通过收集和整理用户针对家庭机器人提出的各类问题，构建了一个包含丰富问题类型的数据集。
3. 该数据集揭示了用户对机器人问题的关注点，并区分了新手和专家用户的问题差异，为机器人设计提供了参考。

## 📝 摘要（中文）

本文提出了一个包含1893个用户问题的家庭机器人数据集，这些问题由100名参与者提出，并被组织成12个类别和70个子类别。与现有可解释机器人研究主要关注“为什么”的问题不同，该数据集涵盖了从简单的执行细节到假设场景中机器人行为的各种问题，为机器人专家提供了宝贵的洞察力，了解机器人需要回答哪些问题。数据集通过展示机器人执行各种家庭任务的15个视频和7个文本刺激，并要求参与者提出他们想问机器人的问题来收集。最终数据集中，最常见的类别是关于任务执行细节（22.5%）、机器人能力（12.7%）和性能评估（11.3%）的问题。尽管关于机器人如何处理潜在困难场景和确保正确行为的问题频率较低，但用户认为它们对于机器人来说最重要。此外，机器人新手和经验丰富的用户提出的问题有所不同。新手更倾向于询问简单的事实，例如机器人做了什么或环境的当前状态。该数据集为识别机器人需要记录和暴露给对话界面的信息、基准测试问答模块以及设计符合用户期望的解释策略奠定了有价值的基础。

## 🔬 方法详解

**问题定义**：现有可解释机器人研究主要关注机器人行为的“为什么”解释，忽略了用户在实际交互中可能提出的各种问题，例如任务执行细节、机器人能力、潜在风险处理等。缺乏全面的用户问题数据集限制了机器人问答模块的开发和评估，以及解释策略的设计。

**核心思路**：论文的核心思路是通过用户调研，收集真实场景下用户针对家庭机器人提出的问题，并对这些问题进行分类和分析，从而构建一个全面的用户问题数据集。该数据集可以帮助机器人研究人员更好地理解用户需求，并开发更有效的问答系统和解释策略。

**技术框架**：论文采用众包的方式收集用户问题。首先，创建一系列视频和文本刺激，展示机器人执行各种家庭任务的场景。然后，通过Prolific平台招募参与者，并要求他们针对每个场景提出他们想问机器人的问题。最后，对收集到的问题进行清洗、分类和标注，构建最终的数据集。数据集包含12个类别和70个子类别的问题。

**关键创新**：该论文的关键创新在于构建了一个包含多样化用户问题的数据集，这些问题涵盖了从简单的执行细节到假设场景中机器人行为的各种情况。与现有研究主要关注“为什么”的问题不同，该数据集更全面地反映了用户对机器人问题的关注点。此外，论文还分析了新手和专家用户的问题差异，为个性化机器人设计提供了参考。

**关键设计**：论文的关键设计包括：(1) 使用视频和文本刺激来模拟真实场景，激发用户提出更自然的问题；(2) 对收集到的问题进行细致的分类和标注，方便研究人员使用；(3) 分析新手和专家用户的问题差异，为个性化机器人设计提供依据。

## 📊 实验亮点

实验结果表明，用户最常提出的问题是关于任务执行细节（22.5%）、机器人能力（12.7%）和性能评估（11.3%）。尽管关于机器人如何处理潜在困难场景的问题频率较低，但用户认为这些问题对于机器人来说最重要。此外，新手用户更倾向于询问简单的事实，而专家用户更倾向于询问更深入的问题。这些发现为机器人设计提供了有价值的参考。

## 🎯 应用场景

该研究成果可应用于家庭服务机器人、智能助手等领域，提升机器人的人机交互能力和用户体验。该数据集可用于训练和评估机器人的问答系统，设计更符合用户期望的解释策略，并为机器人提供更个性化的服务。未来，该数据集可以扩展到其他机器人应用场景，例如工业机器人、医疗机器人等。

## 📄 摘要（原文）

> With the growing use of large language models and conversational interfaces in human-robot interaction, robots' ability to answer user questions is more important than ever. We therefore introduce a dataset of 1,893 user questions for household robots, collected from 100 participants and organized into 12 categories and 70 subcategories. Most work in explainable robotics focuses on why-questions. In contrast, our dataset provides a wide variety of questions, from questions about simple execution details to questions about how the robot would act in hypothetical scenarios -- thus giving roboticists valuable insights into what questions their robot needs to be able to answer. To collect the dataset, we created 15 video stimuli and 7 text stimuli, depicting robots performing varied household tasks. We then asked participants on Prolific what questions they would want to ask the robot in each portrayed situation. In the final dataset, the most frequent categories are questions about task execution details (22.5%), the robot's capabilities (12.7%), and performance assessments (11.3%). Although questions about how robots would handle potentially difficult scenarios and ensure correct behavior are less frequent, users rank them as the most important for robots to be able to answer. Moreover, we find that users who identify as novices in robotics ask different questions than more experienced users. Novices are more likely to inquire about simple facts, such as what the robot did or the current state of the environment. As robots enter environments shared with humans and language becomes central to giving instructions and interaction, this dataset provides a valuable foundation for (i) identifying the information robots need to log and expose to conversational interfaces, (ii) benchmarking question-answering modules, and (iii) designing explanation strategies that align with user expectations.

