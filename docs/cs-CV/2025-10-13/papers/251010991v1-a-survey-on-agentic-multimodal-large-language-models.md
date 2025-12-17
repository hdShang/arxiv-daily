---
layout: default
title: A Survey on Agentic Multimodal Large Language Models
---

# A Survey on Agentic Multimodal Large Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10991" target="_blank" class="toolbar-btn">arXiv: 2510.10991v1</a>
    <a href="https://arxiv.org/pdf/2510.10991.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10991v1" 
            onclick="toggleFavorite(this, '2510.10991v1', 'A Survey on Agentic Multimodal Large Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Huanjin Yao, Ruifei Zhang, Jiaxing Huang, Jingyi Zhang, Yibo Wang, Bo Fang, Ruolin Zhu, Yongcheng Jing, Shunyu Liu, Guanbin Li, Dacheng Tao

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-13

**🔗 代码/项目**: [GITHUB](https://github.com/HJYao00/Awesome-Agentic-MLLMs)

---

## 💡 一句话要点

**综述Agentic多模态大语言模型，探索自主智能体在动态环境中的应用与发展。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agentic MLLM` `多模态大语言模型` `自主智能体` `环境交互` `工具调用` `推理规划` `综述` `人工智能`

## 📋 核心要点

1. 传统AI智能体静态被动，Agentic MLLM旨在构建更动态、主动和通用的智能体，以应对复杂任务。
2. 论文核心在于构建Agentic MLLM的概念框架，涵盖内部智能、外部工具调用和环境交互三个维度。
3. 论文整理了开源训练框架、数据集，并分析了下游应用和未来方向，旨在促进Agentic MLLM的研究。

## 📝 摘要（中文）

随着革命性的自主智能体系统的兴起，研究领域正经历着从传统的静态、被动和特定领域的AI智能体向更动态、主动和通用化的Agentic AI的重大转变。 鉴于人们对Agentic AI日益增长的兴趣及其迈向AGI的潜力，本文对Agentic多模态大语言模型（Agentic MLLMs）进行了全面的综述。 本文探讨了Agentic MLLMs的新兴范式，阐述了其概念基础，并将其与传统的基于MLLM的智能体区分开来。 我们建立了一个概念框架，该框架沿着三个基本维度组织Agentic MLLM：（i）Agentic内部智能功能作为系统的指挥者，通过推理、反思和记忆实现准确的长期规划；（ii）Agentic外部工具调用，模型主动使用各种外部工具来扩展其解决问题的能力，超越其内在知识；（iii）Agentic环境交互进一步将模型置于虚拟或物理环境中，使其能够采取行动、调整策略并在动态的真实场景中维持目标导向的行为。 为了进一步加速该领域的研究，我们整理了用于开发Agentic MLLM的开源训练框架、训练和评估数据集。 最后，我们回顾了Agentic MLLM的下游应用，并概述了这个快速发展领域的未来研究方向。 为了持续跟踪这个快速发展领域的进展，我们还将积极更新一个公共存储库：https://github.com/HJYao00/Awesome-Agentic-MLLMs。

## 🔬 方法详解

**问题定义**：现有基于MLLM的智能体通常是静态和被动的，缺乏在复杂和动态环境中自主规划和执行任务的能力。它们难以有效地利用外部工具，并且缺乏长期记忆和反思能力，限制了其在现实世界中的应用。

**核心思路**：论文的核心思路是将Agentic能力融入到MLLM中，使其能够像人类一样进行推理、规划、反思和与环境交互。通过赋予MLLM自主性，使其能够主动地利用外部工具，并根据环境反馈调整策略，从而实现更强大的问题解决能力。

**技术框架**：Agentic MLLM的框架主要包含三个核心模块：1) Agentic内部智能：负责推理、规划、记忆和反思，作为系统的指挥者。2) Agentic外部工具调用：允许模型主动调用各种外部工具，扩展其知识和能力。3) Agentic环境交互：使模型能够与虚拟或物理环境交互，采取行动并观察结果。这三个模块协同工作，使Agentic MLLM能够在动态环境中实现目标导向的行为。

**关键创新**：该综述的关键创新在于提出了一个统一的Agentic MLLM概念框架，并从内部智能、外部工具调用和环境交互三个维度对其进行了系统性的分析。此外，论文还整理了相关的资源，包括开源框架、数据集和应用案例，为研究人员提供了宝贵的参考。

**关键设计**：论文本身是一个综述，没有提出具体的模型设计。但是，它强调了Agentic MLLM的关键设计要素，例如如何设计有效的推理和规划机制，如何选择和利用外部工具，以及如何构建能够与环境交互的接口。这些设计要素对于构建具有实际应用价值的Agentic MLLM至关重要。

## 📊 实验亮点

该论文是一篇综述，主要贡献在于对Agentic MLLM领域进行了全面的梳理和总结，并提出了一个统一的概念框架。它整理了大量的相关资源，包括开源框架、数据集和应用案例，为研究人员提供了宝贵的参考。该综述为Agentic MLLM的未来研究方向提供了指导。

## 🎯 应用场景

Agentic MLLM在机器人、自动驾驶、智能助手、游戏AI等领域具有广泛的应用前景。它们可以用于解决复杂的任务，例如自主导航、智能决策、人机协作等。通过不断学习和适应环境，Agentic MLLM有望在未来实现更高级别的自主智能。

## 📄 摘要（原文）

> With the recent emergence of revolutionary autonomous agentic systems, research community is witnessing a significant shift from traditional static, passive, and domain-specific AI agents toward more dynamic, proactive, and generalizable agentic AI. Motivated by the growing interest in agentic AI and its potential trajectory toward AGI, we present a comprehensive survey on Agentic Multimodal Large Language Models (Agentic MLLMs). In this survey, we explore the emerging paradigm of agentic MLLMs, delineating their conceptual foundations and distinguishing characteristics from conventional MLLM-based agents. We establish a conceptual framework that organizes agentic MLLMs along three fundamental dimensions: (i) Agentic internal intelligence functions as the system's commander, enabling accurate long-horizon planning through reasoning, reflection, and memory; (ii) Agentic external tool invocation, whereby models proactively use various external tools to extend their problem-solving capabilities beyond their intrinsic knowledge; and (iii) Agentic environment interaction further situates models within virtual or physical environments, allowing them to take actions, adapt strategies, and sustain goal-directed behavior in dynamic real-world scenarios. To further accelerate research in this area for the community, we compile open-source training frameworks, training and evaluation datasets for developing agentic MLLMs. Finally, we review the downstream applications of agentic MLLMs and outline future research directions for this rapidly evolving field. To continuously track developments in this rapidly evolving field, we will also actively update a public repository at https://github.com/HJYao00/Awesome-Agentic-MLLMs.

