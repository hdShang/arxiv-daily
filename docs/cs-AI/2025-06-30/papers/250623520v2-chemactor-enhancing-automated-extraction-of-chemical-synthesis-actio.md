---
layout: default
title: "ChemActor: Enhancing Automated Extraction of Chemical Synthesis Actions with LLM-Generated Data"
---

# ChemActor: Enhancing Automated Extraction of Chemical Synthesis Actions with LLM-Generated Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23520" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23520v2</a>
  <a href="https://arxiv.org/pdf/2506.23520.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23520v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23520v2', 'ChemActor: Enhancing Automated Extraction of Chemical Synthesis Actions with LLM-Generated Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Zhang, Ruijie Yu, Jidong Tian, Feng Zhu, Jiapeng Liu, Xiaokang Yang, Yaohui Jin, Yanyan Xu

**分类**: cs.AI

**发布日期**: 2025-06-30 (更新: 2025-07-01)

**🔗 代码/项目**: [GITHUB](https://github.com/Zhanghahah/ChemActor)

---

## 💡 一句话要点

**提出ChemActor以解决化学合成过程自动提取问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `化学合成` `自动提取` `大型语言模型` `数据生成` `机器学习`

## 📋 核心要点

1. 现有方法在化学程序提取中面临语言模糊性和高人力成本的挑战，导致自动化程度低。
2. 论文提出ChemActor，通过微调大型语言模型，利用生成数据框架提升数据质量和数量，从而实现化学动作的自动提取。
3. 实验结果显示，ChemActor在R2D和D2A任务上性能优越，超越基线模型10%，展现了其有效性和先进性。

## 📝 摘要（中文）

随着有机化学中机器人合成的日益关注，从文献中自动提取化学程序变得至关重要。然而，由于化学语言的固有模糊性以及开发可靠计算机辅助提取协议所需的人力标注成本，这一任务仍然具有挑战性。本文提出了ChemActor，一个完全微调的大型语言模型（LLM），作为化学执行器，将非结构化实验程序转换为结构化的动作序列。我们提出了一个基于LLM生成数据的顺序框架，以解决标注数据不足和质量低的问题。该框架集成了一个数据选择模块，根据分布差异选择数据，并利用通用LLM从单一分子输入生成机器可执行的动作。此外，我们引入了一种新颖的多轮LLM循环审查指标，反映模型对化学实验程序的深入理解。大量实验表明，ChemActor在反应到描述（R2D）和描述到动作（D2A）任务上表现出色，超越基线模型10%。

## 🔬 方法详解

**问题定义**：本研究旨在解决从化学文献中自动提取实验程序的困难，现有方法由于化学语言的模糊性和人力标注的高成本，导致提取效果不佳。

**核心思路**：ChemActor通过微调大型语言模型（LLM）来转换非结构化实验程序为结构化动作序列，并引入生成数据框架以提升数据质量和数量，从而克服标注数据不足的问题。

**技术框架**：该框架包括数据选择模块和通用LLM，数据选择模块根据分布差异选择数据，LLM则负责从单一分子输入生成机器可执行的动作。

**关键创新**：最重要的创新在于引入了多轮LLM循环审查指标，能够更好地反映模型对化学实验程序的理解，与现有方法相比，提升了自动提取的准确性和可靠性。

**关键设计**：在模型训练中，采用了特定的损失函数和参数设置，以优化生成数据的质量，并确保模型在不同任务中的泛化能力。具体的网络结构和训练细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，ChemActor在反应到描述（R2D）和描述到动作（D2A）任务上均表现出色，超越基线模型10%，达到了当前最先进的性能。这一成果验证了LLM生成数据在化学合成自动提取中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括化学合成自动化、药物发现和材料科学等。通过提高化学程序的自动提取效率，ChemActor能够加速科学研究进程，降低人力成本，推动智能化实验室的发展。未来，随着模型的进一步优化和应用，可能会在更广泛的科学领域产生深远影响。

## 📄 摘要（原文）

> With the increasing interest in robotic synthesis in the context of organic chemistry, the automated extraction of chemical procedures from literature is critical. However, this task remains challenging due to the inherent ambiguity of chemical language and the high cost of human annotation required for developing reliable computer-aided extraction protocols. Here, we present ChemActor, a fully fine-tuned large language model (LLM), as a chemical executor to convert between unstructured experimental procedures and structured action sequences. We propose a sequential LLM-generated data framework to address the challenges of insufficient and low-quality annotated data. This framework integrates a data selection module that selects data based on distribution divergence, with a general-purpose LLM, to generate machine-executable actions from a single molecule input. Additionally, we introduce a novel multi-round LLMs circle review metric, which reflects the model's advanced understanding of chemical experimental procedures. Extensive experiments on reaction-to-description (R2D) and description-to-action (D2A) tasks demonstrate that ChemActor, augmented by LLM-generated data, achieves state-of-the-art performance, outperforming the baseline model by 10%. The code is available at: https://github.com/Zhanghahah/ChemActor.

