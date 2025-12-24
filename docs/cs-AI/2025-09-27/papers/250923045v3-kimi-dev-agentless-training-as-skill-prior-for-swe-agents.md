---
layout: default
title: "Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents"
---

# Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23045" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23045v3</a>
  <a href="https://arxiv.org/pdf/2509.23045.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23045v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23045v3', 'Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zonghan Yang, Shengjie Wang, Kelin Fu, Wenyang He, Weimin Xiong, Yibo Liu, Yibo Miao, Bofei Gao, Yejie Wang, Yingwei Ma, Yanhao Li, Yue Liu, Zhenxing Hu, Kaitai Zhang, Shuyi Wang, Huarong Chen, Flood Sung, Yang Liu, Yang Gao, Zhilin Yang, Tianyu Liu

**分类**: cs.AI, cs.CL, cs.SE

**发布日期**: 2025-09-27 (更新: 2025-12-08)

**备注**: 68 pages. GitHub repo at https://github.com/MoonshotAI/Kimi-Dev

---

## 💡 一句话要点

**Kimi-Dev：基于无Agent训练的技能先验提升软件工程Agent性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `软件工程Agent` `无Agent训练` `技能先验` `代码生成` `语言模型`

## 📋 核心要点

1. 现有SWE-Agent框架和无Agent方法各有优劣，如何结合二者优势是关键挑战。
2. 论文提出通过无Agent训练学习技能先验，再迁移到SWE-Agent，提升其性能。
3. Kimi-Dev在SWE-bench Verified上达到60.4%，SFT后SWE-Agent pass@1达到48.6%。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地应用于软件工程（SWE）领域，SWE-bench是关键的基准测试。现有的解决方案分为多轮交互的SWE-Agent框架和单轮可验证步骤的基于工作流的无Agent方法。本文认为这两种范式并非互斥：推理密集的无Agent训练可以诱导技能先验，包括定位、代码编辑和自我反思，从而实现高效且有效的SWE-Agent适应。本文首先整理了无Agent训练方案，并提出了Kimi-Dev，一个开源的SWE LLM，在SWE-bench Verified上实现了60.4%的性能，是工作流方法中的最佳结果。通过在5k个公开可用的轨迹上进行额外的SFT适应，Kimi-Dev驱动SWE-Agent达到48.6%的pass@1，与Claude 3.5 Sonnet（241022版本）的性能相当。这些结果表明，来自无Agent训练的结构化技能先验可以弥合工作流和Agent框架之间的差距，从而实现可迁移的编码Agent。

## 🔬 方法详解

**问题定义**：现有软件工程Agent方法主要分为两类：基于多轮交互的Agent框架和基于单轮工作流的Agentless方法。Agent框架虽然具备更强的交互能力，但训练和推理成本较高。Agentless方法虽然效率高，但缺乏复杂的推理和规划能力。如何结合两者的优势，提升软件工程Agent的性能是一个关键问题。

**核心思路**：论文的核心思路是利用Agentless方法进行预训练，学习软件工程相关的技能先验（如代码定位、编辑和自我反思），然后将这些先验知识迁移到Agent框架中，从而提升Agent的性能和效率。这种方法类似于预训练+微调的范式，但更侧重于技能的迁移。

**技术框架**：整体框架包含两个主要阶段：1) 无Agent训练阶段：使用大规模的软件工程数据集，训练一个基于工作流的语言模型（Kimi-Dev），使其具备基本的代码生成和编辑能力。2) Agent适应阶段：使用少量Agent交互数据，对Kimi-Dev进行微调，使其适应Agent框架的交互模式。

**关键创新**：论文的关键创新在于提出了“技能先验”的概念，并证明了通过Agentless训练可以有效地学习这些先验知识。与传统的端到端Agent训练相比，这种方法可以更有效地利用大规模的无标注数据，并提升Agent的泛化能力。

**关键设计**：Kimi-Dev采用了标准的Transformer架构，并使用了大规模的代码数据集进行训练。在Agent适应阶段，使用了SFT（Supervised Fine-Tuning）方法，利用5k个公开可用的Agent交互轨迹进行微调。具体的损失函数和优化器选择与标准的语言模型训练方法类似。

## 📊 实验亮点

Kimi-Dev在SWE-bench Verified上取得了60.4%的成绩，是目前workflow方法中的最佳结果。经过SFT适应后，Kimi-Dev驱动的SWE-Agent在pass@1指标上达到了48.6%，与Claude 3.5 Sonnet (241022版本)的性能相当，证明了无Agent训练的技能先验可以有效提升Agent的性能。

## 🎯 应用场景

该研究成果可应用于自动化代码生成、代码修复、软件测试等领域。通过提升软件工程Agent的性能，可以显著提高软件开发的效率和质量，降低开发成本。未来，该方法有望应用于更复杂的软件工程任务，例如软件架构设计和需求分析。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly applied to software engineering (SWE), with SWE-bench as a key benchmark. Solutions are split into SWE-Agent frameworks with multi-turn interactions and workflow-based Agentless methods with single-turn verifiable steps. We argue these paradigms are not mutually exclusive: reasoning-intensive Agentless training induces skill priors, including localization, code edit, and self-reflection that enable efficient and effective SWE-Agent adaptation. In this work, we first curate the Agentless training recipe and present Kimi-Dev, an open-source SWE LLM achieving 60.4\% on SWE-bench Verified, the best among workflow approaches. With additional SFT adaptation on 5k publicly-available trajectories, Kimi-Dev powers SWE-Agents to 48.6\% pass@1, on par with that of Claude 3.5 Sonnet (241022 version). These results show that structured skill priors from Agentless training can bridge workflow and agentic frameworks for transferable coding agents.

